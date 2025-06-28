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
                    if "Bid Award" in card.find_element(By.CLASS_NAME, 'text-success').text  or "Financial Evaluation" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        main_window = driver.current_window_handle

                        try: 
                            view_bid_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='View BID Results']")))
                            view_bid_button.click()
                            
                            
                        except: 
                            view_bid_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='View RA Results']")))
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
                        
                        time.sleep(2)

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
        
        max_threads = 6
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


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = '''
        SELECT * 
        FROM tender_data 
        WHERE end_date < CAST(GETDATE() AS DATE);
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
GEM/2025/B/6225418
GEM/2025/B/6213179
GEM/2025/B/6217852
GEM/2025/B/6215962
GEM/2025/B/6228270
GEM/2025/B/6252877
GEM/2025/B/6250104
GEM/2025/B/6253688
GEM/2025/B/6063031
GEM/2025/B/6134461
GEM/2025/B/6195682
GEM/2025/B/6092335
GEM/2025/B/6235260
GEM/2025/B/6045899
GEM/2025/B/6215870
GEM/2025/B/6195992
GEM/2025/B/6165580
GEM/2025/B/6170503
GEM/2025/B/6213471
GEM/2025/B/6235441
GEM/2025/B/6196275
GEM/2025/B/6161075
GEM/2025/B/6216737
GEM/2025/B/6089982
GEM/2025/B/6208981
GEM/2025/B/6047337
GEM/2025/B/6182308
GEM/2025/B/6199336
GEM/2025/B/6081614
GEM/2025/B/6208429
GEM/2025/B/6224215
GEM/2025/B/6187835
GEM/2025/B/6195010
GEM/2025/B/6187021
GEM/2025/B/6224014
GEM/2025/B/6213807
GEM/2025/B/6195037
GEM/2025/B/6214839
GEM/2025/B/6180521
GEM/2025/B/6215224
GEM/2025/B/6217903
GEM/2025/B/6230827
GEM/2025/B/6154979
GEM/2025/B/6243340
GEM/2025/B/6258533
GEM/2025/B/6156206
GEM/2025/B/6178029
GEM/2025/B/6086045
GEM/2025/B/6207230
GEM/2025/B/6143682
GEM/2025/B/6081899
GEM/2025/B/6220758
GEM/2025/B/6186024
GEM/2025/B/6230162
GEM/2025/B/6204757
GEM/2025/B/6096210
GEM/2025/B/6177881
GEM/2025/B/6230109
GEM/2025/B/6207401
GEM/2025/B/6252427
GEM/2025/B/6233426
GEM/2025/B/6211989
GEM/2025/B/6260454
GEM/2025/B/6234175
GEM/2025/B/6206265
GEM/2025/B/6192305
GEM/2025/B/6198646
GEM/2025/B/6213598
GEM/2025/B/6228781
GEM/2025/B/6145701
GEM/2025/B/6145481
GEM/2025/B/6143053
GEM/2025/B/6246424
GEM/2025/B/6176933
GEM/2025/B/6148769
GEM/2025/B/6263378
GEM/2025/B/6236919
GEM/2025/B/6161362
GEM/2025/B/6213614
GEM/2025/B/6263918
GEM/2025/B/6261886
GEM/2025/B/6185852
GEM/2025/B/6247798
GEM/2025/B/6257250
GEM/2025/B/6176129
GEM/2025/B/6169761
GEM/2025/B/6203495
GEM/2025/B/6263844
GEM/2025/B/6081988
GEM/2025/B/6248139
GEM/2025/B/6220109
GEM/2025/B/6154887
GEM/2025/B/6177743
GEM/2025/B/6182123
GEM/2025/B/6174724
GEM/2025/B/6203731
GEM/2025/B/6210912
GEM/2025/B/6266639
GEM/2025/B/6269024
GEM/2025/B/6267452
GEM/2025/B/6228331
GEM/2025/B/6259134
GEM/2025/B/5877167
GEM/2025/B/6261987
GEM/2025/B/6190649
GEM/2025/B/6221111
GEM/2025/B/6234476
GEM/2025/B/6135483
GEM/2025/B/6214778
GEM/2025/B/6267833
GEM/2025/B/6103350
GEM/2025/B/6003270
GEM/2025/B/6228450
GEM/2025/B/6218751
GEM/2025/B/6256588
GEM/2025/B/6202754
GEM/2025/B/6188386
GEM/2025/B/6238728
GEM/2025/B/6259135
GEM/2025/B/6239940
GEM/2025/B/6270615
GEM/2025/B/6101170
GEM/2025/B/6214999
GEM/2025/B/6198055
GEM/2025/B/6279022
GEM/2024/B/5767378
GEM/2025/B/6232980
GEM/2025/B/6104317
GEM/2025/B/6143048
GEM/2025/B/6165438
GEM/2025/B/6156632
GEM/2025/B/6243867
GEM/2025/B/6286757
GEM/2025/B/6196447
GEM/2025/B/6108613
GEM/2025/B/6239274
GEM/2025/B/6292078
GEM/2025/B/6297724
GEM/2025/B/6251357
GEM/2025/B/6081681
GEM/2025/B/6259436
GEM/2025/B/6245998
GEM/2025/B/6266162
GEM/2025/B/6265175
GEM/2025/B/6180219
GEM/2025/B/6293503
GEM/2025/B/6292825
GEM/2025/B/6234868
GEM/2025/B/6298586
GEM/2025/B/6147842
GEM/2025/B/6224962
GEM/2025/B/6165146
GEM/2025/B/6289260
GEM/2025/B/6307638
GEM/2025/B/6305555
GEM/2025/B/6191472
GEM/2025/B/6314827
GEM/2025/B/6262094
GEM/2025/B/6278514
GEM/2025/B/6278280
GEM/2025/B/6311744
GEM/2025/B/6284536
GEM/2025/B/6272390
GEM/2025/B/6324216
GEM/2025/B/6281706
GEM/2025/B/6327065
GEM/2025/B/6214313
GEM/2025/B/6276600
GEM/2025/B/6250408
GEM/2025/B/6255287
GEM/2025/B/6283495
GEM/2025/B/6282768
GEM/2025/B/6286880
GEM/2025/B/6272189
GEM/2025/B/6323346
GEM/2025/B/6278885
GEM/2025/B/6313857
GEM/2025/B/6321204
GEM/2025/B/6285434
GEM/2025/B/6277966
GEM/2025/B/6197439
GEM/2025/B/6262779
GEM/2022/B/2655453
GEM/2023/B/3847509
GEM/2024/B/5671817
GEM/2024/B/5012301
GEM/2024/B/4899014
GEM/2025/B/6290224
GEM/2025/B/6111068
GEM/2025/B/6306358
GEM/2025/B/6302279
GEM/2025/B/6288146

"""

tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)

split_arrays = split_into_parts(tender_ids, 5)


Main(split_arrays)

# 17579