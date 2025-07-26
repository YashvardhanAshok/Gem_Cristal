from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
import json
from selenium.common.exceptions import TimeoutException
from datetime import datetime as ds
from time import sleep
from datetime import date
today = date.today()
from selenium.common.exceptions import NoSuchElementException
import pyodbc
import pyodbc
import pandas as pd

def sql_udate(status, L_Placeholder, tender_id_to_update):
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        # Serialize list into JSON string
        L_Placeholder_str = json.dumps(L_Placeholder)

        update_query = """
            UPDATE tender_data
            SET status = ?, L_Placeholder = ?
            WHERE tender_id = ?
        """

        cursor.execute(update_query, status, L_Placeholder_str, tender_id_to_update)
        conn.commit()
        print(f"Updated tender_id {tender_id_to_update} successfully.")
        cursor.close()
        conn.close()
    except:
        return print(f"faild:{tender_id_to_update}")    

def gem_funtion(elements_list):
    driver = webdriver.Edge()
    driver.get('https://bidplus.gem.gov.in/all-bids')
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "bidrastatus")))
    checkbox.click()
    sleep(2)
    
    def update_c_sql(gem_ids):
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        
        cursor = conn.cursor()
        update_query = """UPDATE tender_data SET Cancel = ? WHERE tender_id = ?"""
        
        for gem_id in gem_ids:
            cursor.execute(update_query, "Cancel in close T", gem_id)
            conn.commit()
            print(f"{gem_id}: Cancel")
            
        cursor.close()
        conn.close()
    Cancel_ids = []
    for element in elements_list:
        time.sleep(1)
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchBid')))
        search.clear()
        search.send_keys(element)
        search.send_keys(Keys.RETURN)
        
       

        c = False
        try:
            alerts = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.alert.alert-danger')))
            for alert in alerts:
                print()
                try:
                    if alert.text == "No data found":
                        Cancel_ids.append(element) 
                        c = True
                except: pass
        except: pass  
        if c: continue 

        try:
            card_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
            if card_elements:
                pass
            else:
                continue
            for card in card_elements:
                if element == card.find_element(By.CLASS_NAME, 'bid_no_hover').text:
                    if "Technical Evaluation" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        sql_udate("Technical Evaluation", None, element)
                        break

                    if "Bid Award" in card.find_element(By.CLASS_NAME, 'text-success').text  or "Financial Evaluation" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        main_window = driver.current_window_handle
                        click = False
                        for x in ["View RA Results","View BID Results"]:
                            try:
                                wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{x}']"))).click()
                                click = True
                                break
                            except: pass
                            
                        if not click: continue  
                        driver.set_page_load_timeout(15)  
                        try:
                            wait.until(EC.new_window_is_opened)
                            all_windows = driver.window_handles
                            new_window = [w for w in all_windows if w != main_window][0]
                            driver.switch_to.window(new_window)
                            driver.get(driver.current_url)  
                            
                        except TimeoutException:
                            print("Page load exceeded 30 seconds. Reloading...")
                            driver.execute_script("window.stop();")  
                            driver.get(driver.current_url)   
                        
                        def click_on_evaluation(evaluation_texts):
                            for text in evaluation_texts:
                                xpath = f"//h4[@class='panel-title']/a[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text}')]"
                                try:
                                    link = WebDriverWait(driver, 1).until(
                                        EC.element_to_be_clickable((By.XPATH, xpath))
                                    )
                                    driver.execute_script("arguments[0].scrollIntoView(true);", link)
                                    driver.execute_script("arguments[0].click();", link)
                                    print(f"✅ Clicked element with text containing: {text}")
                                    return True
                                except TimeoutException:
                                    pass
                                    print(f"❌ Timeout for text: {text}")
                            return False
                        evaluation_texts = ['financial evaluation', 'ra evaluation']
                        clicked = click_on_evaluation(evaluation_texts)
                        try:
                            if clicked:
                                try:
                                    table_element = WebDriverWait(driver, 10).until(
                                        EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'List of Sellers Qualified Financially')]/following::table[1]"))
                                    )    
                                except NoSuchElementException:
                                    try:
                                        elements = driver.find_elements(By.CLASS_NAME, "technical_eligible")
                                        if len(elements) == 1:
                                            table_element = elements[0]
                                        else:
                                            print("Could not do")
                                            table_element = None  
                                    except:
                                        
                                        print(f"Timeout: Table not loaded for Tender ID: {element}")
                                if table_element is not None: pass
                                else:
                                    print(f"Table not found for Tender ID: {element}")
                                    driver.close()
                                    driver.switch_to.window(main_window)
                                    continue
                                
                                rows = table_element.find_elements(By.XPATH, ".//tbody/tr")
                                table_data = []
                                for row in rows:
                                    cells = row.find_elements(By.TAG_NAME, "td")
                                    row_data = [cell.text.strip() for cell in cells]
                                    table_data.append(row_data)

                                new_arr = []
                                for arr in table_data:
                                    price_str = arr[3].replace('`', '').strip()  
                                    new_arr.append([arr[1], price_str])

                                sql_udate("Bid Award", new_arr, element)
                            else: sql_udate("Financial Evaluation", None, element)
                        except: traceback.print_exc() 
                            
                        driver.close()
                        driver.switch_to.window(main_window)

        except Exception:
            print(f"error in gem id:{element}")
            traceback.print_exc() 

    driver.quit()
    update_c_sql(Cancel_ids)
    
import threading
def Main(tender_ids,max_threads):
    try:
        threads = []
        item_list = split_into_parts(tender_ids, max_threads)
        
        for elements in item_list: 
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                
                time.sleep(0.5)

            t = threading.Thread(target=gem_funtion, args=(elements,))
            t.start()
            threads.append(t)
                
    except: traceback.print_exc() 

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = '''
    SELECT * 
    FROM tender_data 
    WHERE end_date < CAST(GETDATE() AS DATE) AND organisation='ASSAM RIFLES'
'''
        
df = pd.read_sql(query, conn)

filtered_df = df[
    (
        (df['status'].isnull()) |
        (df['status'] == 'null') |
        (df['status'] == '')
    ) &
    ((df['L_Placeholder'] != 'NULL') | (df['L_Placeholder'] != 'null') | df['L_Placeholder'] != '')
]

# for know 
tender_ids = filtered_df['tender_id'].tolist()

total_entries = len(tender_ids)
print(f"Total entries where live is 'no': {total_entries}")

def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

raw_text = """  
GEM/2025/B/6185022

"""

tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)

Main(tender_ids,6)


