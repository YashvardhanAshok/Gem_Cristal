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
    for element in elements_list:
        time.sleep(1)
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchBid')))
        search.clear()
        search.send_keys(element)
        search.send_keys(Keys.RETURN)
        
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
                    if "Bid Award" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        main_window = driver.current_window_handle

                        view_bid_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='View BID Results']")))
                        view_bid_button.click()

                        wait.until(EC.new_window_is_opened)
                        all_windows = driver.window_handles
                        new_window = [w for w in all_windows if w != main_window][0]
                        driver.switch_to.window(new_window)
                        time.sleep(5)

                        evaluation_texts = ['financial evaluation', 'ra evaluation', "evaluation"]
                        clicked = False
                            

                        for text in evaluation_texts:
                            xpath = f"//h4[@class='panel-title']/a[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text}')]"

                            try:
                                link = WebDriverWait(driver, 1).until(
                                    EC.element_to_be_clickable((By.XPATH, xpath))
                                )
                                driver.execute_script("arguments[0].scrollIntoView(true);", link)
                                driver.execute_script("arguments[0].click();", link)
                                print(f"✅ Clicked element with text containing: {text}")
                                clicked = True
                                break
                            except TimeoutException:
                                print(f"❌ Timeout for text: {text}")

                        if not clicked:
                            print("❌ No matching evaluation link found.")
                        
                        time.sleep(5)

                        try:
                            table_element = driver.find_element(By.XPATH, "//label[contains(text(), 'List of Sellers Qualified Financially')]/following::table[1]")
                        except NoSuchElementException:
                            elements = driver.find_elements(By.CLASS_NAME, "technical_eligible")
                            if len(elements) == 1:
                                table_element = elements[0]
                            else:
                                print("Could not do")
                                table_element = None  
                        
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
                        print(f"done:{element}")
                        driver.close()
                        driver.switch_to.window(main_window)

        except Exception as e:
            print(f"error in gem id:{element}")
            traceback.print_exc() 

    driver.quit()

    
import threading
def Main(item_list):
    try:
        
        threads = []
        
        max_threads = 5
        for elements in item_list: 
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                
                time.sleep(0.5)

            t = threading.Thread(target=gem_funtion, args=(elements,))
            t.start()
            threads.append(t)
                
    except:
        traceback.print_exc() 

import pyodbc
import pandas as pd
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM tender_data"
df = pd.read_sql(query, conn)

filtered_df = df[
    (df['Live'].str.lower() == 'no') & 
    (df['L_Placeholder'].isnull() | (df['L_Placeholder'] == 'null'))
]

id_array = filtered_df['tender_id'].tolist()

total_entries = len(id_array)
print(f"Total entries where live is 'no': {total_entries}")

def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

split_arrays = split_into_parts(id_array, 5)
Main( split_arrays)

