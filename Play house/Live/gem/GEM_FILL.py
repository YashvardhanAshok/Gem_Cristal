import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
import pandas as pd
import json
import os
from datetime import date
from datetime import datetime as ds
import pyodbc
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import traceback
import time
import json
from datetime import datetime as ds
from time import sleep

from datetime import date
import pyodbc
import pyodbc
import pandas as pd

today = date.today()
from time import sleep
import requests
import pdfplumber
import re
from lib.gem_card import gem_find

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

total_gem_ids_q = "SELECT * FROM tender_data"
total_gem_ids_df = pd.read_sql(total_gem_ids_q, conn)
conn.close()
all_gem_ids = total_gem_ids_df['tender_id'].tolist()
from selenium.webdriver.chrome.options import Options
db_lock = threading.Lock()

def sql(extracted_data):
    try:
        
        with db_lock:  
            conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=localhost\\SQLEXPRESS;"
                "DATABASE=gem_tenders;"
                "Trusted_Connection=yes;"
            )
            cursor = conn.cursor()

            for tender_data in extracted_data:
                try:
                    if tender_data == []:continue
                    try:
                        if tender_data["TENDER ID"] in [False, '', None]:
                            continue
                    except: pass
                    

                    cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (str(tender_data["TENDER ID"])))
                    exists = cursor.fetchone()[0]

                    try: end_date = datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date()
                    except:
                        print(f"Invalid END DATE for tender {str(tender_data["TENDER ID"])}: {tender_data.get('END DATE')}")
                        end_date = None

                    end_time = str(tender_data.get("END Time", ""))
                    date_of_search_str = tender_data.get("DATE OF SEARCH", "")
                    try:
                        extended = datetime.strptime(date_of_search_str, "%d-%b-%Y").strftime("%Y-%m-%d")
                    except:
                        print(f"Invalid DATE OF SEARCH for tender {str(tender_data["TENDER ID"])}: {date_of_search_str}")
                        extended = ""



                    if exists:
                        update_sql = """
                            UPDATE tender_data
                            SET
                                date_of_search = ?, 
                                element_put = ?, 
                                item_description = ?, 
                                qty = ?,
                                start_date = ?, 
                                end_date = ?, 
                                end_time = ?, 
                                day_left_formula = ?,
                                emd_amount = ?, 
                                tender_value = ?, 
                                item_category = ?,
                                consignee_reporting = ?, 
                                address = ?, 
                                MSE = ?,
                                ministry = ?, 
                                department = ?, 
                                branch = ?, 
                                link_href = ?, 
                                file_path = ?,
                                matches = ?, 
                                matched_products = ?, 
                                organisation = ?
                            WHERE tender_id = ?
                        """
                        cursor.execute(update_sql, (
                        datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                        str(tender_data.get("elementPut", "")),
                        str(tender_data.get("ITEM DESCRIPTION", "")),
                        int(tender_data.get("QTY", 0)),
                        datetime.strptime(tender_data["START DATE"], "%d-%b-%Y").date(),
                        end_date,
                        end_time,
                        str(tender_data.get("DAY LEFT", "")),
                        float(tender_data.get("EMD AMOUNT") or 0),
                        float(tender_data.get("TENDER VALUE") or 0),
                        str(tender_data.get("ITEM CATEGORY", "")),
                        json.dumps(tender_data.get("Consignee Reporting", [])),
                        json.dumps(tender_data.get("ADDRESS", [])),
                        str(tender_data.get("MSE", "")),
                        str(tender_data.get("MINISTRY", "")),
                        str(tender_data.get("DEPARTMENT", "")),
                        str(tender_data.get("BRANCH", "")),
                        str(tender_data.get("link", "")),
                        str(tender_data.get("file_path", "")),
                        int(tender_data.get("matches", False)),
                        json.dumps(tender_data.get("matched_products", [])),
                        str(tender_data.get("ORGANISATION", "")),
                        str(tender_data["TENDER ID"])))
                        print(f"Tender ID {str(tender_data["TENDER ID"])} exists.")
                        conn.commit()
                        continue

                    insert_sql = """
                    INSERT INTO tender_data (
                        date_of_search, tender_id, element_put, item_description, qty,
                        start_date, end_date, end_time, day_left_formula,
                        emd_amount, tender_value, item_category,
                        consignee_reporting, address, MSE,
                        ministry, department, branch, link_href, file_path,
                        matches, matched_products, organisation
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """

                    values = (
                        datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                        str(tender_data["TENDER ID"]),
                        str(tender_data.get("elementPut", "")),
                        str(tender_data.get("ITEM DESCRIPTION", "")),
                        int(tender_data.get("QTY", 0)),
                        datetime.strptime(tender_data["START DATE"], "%d-%b-%Y").date(),
                        end_date,
                        end_time,
                        str(tender_data.get("DAY LEFT", "")),
                        float(tender_data.get("EMD AMOUNT") or 0),
                        float(tender_data.get("TENDER VALUE") or 0),
                        str(tender_data.get("ITEM CATEGORY", "")),
                        json.dumps(tender_data.get("Consignee Reporting", [])),
                        json.dumps(tender_data.get("ADDRESS", [])),
                        str(tender_data.get("MSE", "")),
                        str(tender_data.get("MINISTRY", "")),
                        str(tender_data.get("DEPARTMENT", "")),
                        str(tender_data.get("BRANCH", "")),
                        str(tender_data.get("link", "")),
                        str(tender_data.get("file_path", "")),
                        int(tender_data.get("matches", False)),
                        json.dumps(tender_data.get("matched_products", [])),
                        
                        
                        str(tender_data.get("ORGANISATION", "")),
                    )

                    cursor.execute(insert_sql, values)
                    conn.commit()
                    print(f"Tender ID {str(tender_data["TENDER ID"])} inserted successfully.")

                
                except:pass

            cursor.close()
            conn.close()
        
    except: pass

def convert_date_format(date_str):
    date_obj = ds.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%b-%Y")

    
def gem_funtion(elements_list):
    tenders = []
    try:
        options = Options()
        prefs = {
            "download.default_directory": os.path.join(os.getcwd(), "download_pdf"),
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        }
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Edge(options=options)
        
        
        driver.get('https://bidplus.gem.gov.in/all-bids')
        wait = WebDriverWait(driver, 30)
        # close tender_ids
        checkbox = wait.until(EC.element_to_be_clickable((By.ID, "bidrastatus")))
        checkbox.click()
        sleep(2)
        for element in elements_list:
            time.sleep(1)
            search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'searchBid')))
            search.clear()
            search.send_keys(element)
            search.send_keys(Keys.RETURN)
            
            try:
                try:
                    card_elements = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
                except: continue 
                
                if card_elements: pass
                else:continue
                
                for card in card_elements:
                    if element == card.find_element(By.CLASS_NAME, 'bid_no_hover').text:
                        a = gem_find(driver,card_elements , card, gem_ids=[], org_name=[], ministry_name=[],close_tender_id_list=[],gem_ids_copy=[])
                        tenders.append(a)
                        break

            except Exception as e:
                print(f"error in gem id:{element}")
                traceback.print_exc() 
        driver.quit()
    except: pass
    # print(tenders)
    sql(tenders)
    
import threading

def Main(item_list):
    try:
        threads = []
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

query  = "SELECT * FROM tender_data WHERE id >= 24258 AND start_date is null ;"
df = pd.read_sql(query, conn)

tender_ids = df['tender_id'].tolist()

total_entries = len(tender_ids)
print(f"Total entries where live is 'no': {total_entries}")

def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

raw_text = """  
GEM/2025/B/6414351
GEM/2025/B/6456641
GEM/2025/B/6403646
GEM/2025/B/6402590
GEM/2025/B/6398808
GEM/2025/B/6385846
GEM/2025/B/6361796
GEM/2025/B/6382886
GEM/2025/B/6337823
GEM/2025/B/6121135
GEM/2025/B/6206597
GEM/2025/B/6138648
GEM/2025/B/6132335
GEM/2025/B/6159094

GEM/2025/B/6056067
GEM/2025/B/5981206
GEM/2025/B/5961998
GEM/2024/B/5613644
GEM/2025/B/5903599
GEM/2025/B/5833198
GEM/2025/B/5800971
GEM/2025/B/5787058
GEM/2025/B/5790404
GEM/2025/B/5787747
GEM/2025/B/5785600
GEM/2025/B/5788510
GEM/2025/B/5787247
GEM/2025/B/5780166
GEM/2024/B/5686382
GEM/2024/B/5686382
GEM/2024/B/5683332
GEM/2024/B/5731576
GEM/2024/B/5661144
GEM/2024/B/5586096
GEM/2024/B/5571472
GEM/2024/B/5684030

"""

tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)

max_threads = 6

split_arrays = split_into_parts(tender_ids, max_threads)
print(split_arrays)
Main(split_arrays)


