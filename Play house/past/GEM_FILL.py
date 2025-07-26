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

def gem_find(driver,card_elements , card):
    global all_gem_ids
    # scroll
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
    sleep(0.01)
    try:
        bid_title = card.find_element(By.CLASS_NAME, 'bid_no_hover')
        link_href = bid_title.get_attribute("href")
        start_date = card.find_element(By.CLASS_NAME, 'start_date').text
        end_date = card.find_element(By.CLASS_NAME, 'end_date').text
        
        closing_date_parts = end_date.split(" ")
        end_date = convert_date_format(closing_date_parts[0])
        end_date_time = closing_date_parts[1] + " " + closing_date_parts[2]

        try:
            bid_id_no = link_href.split('/')[-1]
            download_path = f'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-{bid_id_no}.pdf'

            if os.path.exists(download_path): 
                print(f"have file for: {bid_id_no}")
                try:
                    if bid_title.text in all_gem_ids:
                        all_gem_ids.append(bid_title.text)
                        print(f"alrady in db:{bid_title.text}")
                        # return 
                except: pass
            
            else:
                try:
                    driver.execute_script("window.open(arguments[0]);", link_href)
                    download_dir = os.path.join(os.getcwd(), 'download_pdf')
                    os.makedirs(download_dir, exist_ok=True)
                    latest_file = max(
                        [os.path.join(download_dir, f) for f in os.listdir(download_dir)],
                        key=os.path.getctime,
                    )
                    download_path = latest_file
                    download_path = f"C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-{bid_id_no}.pdf"
                    
                except requests.exceptions.RequestException as e:
                    return
                sleep(1.1)
        except: pass

        opening_date_parts = start_date.split(" ")
        start_date = convert_date_format(opening_date_parts[0])
        
        try:
            quantity_element = card.find_element(By.XPATH, ".//div[contains(@class, 'col-md-4')]//div[contains(text(), 'Quantity')]")
            quantity_text = quantity_element.text.strip()
            if "Quantity:" in quantity_text:
                quantity = quantity_text.split("Quantity:")[-1].strip()
            else: quantity = 0

        except:
            quantity = 0

        try:
            item_element = driver.find_element(By.XPATH, "//strong[text()='Items:']/parent::div")
            from_card_discription = item_element.text.replace("Items:", "").strip()
        except:
            titles = []
            try:
                for card_element in card_elements:
                    text = card_element.text
                    if text.startswith(bid_title.text):
                        from_card_discription = titles.append(text)
            except: pass
        
        print(f"New tender:{bid_title.text} and started at: {start_date}")
        

        try:

            
            
            if os.path.exists(download_path):
                try:
                    with pdfplumber.open(download_path) as pdf:
                        emd_amount = None
                        epbg_percentage = None 
                        Tender_value = None 
                        MSE_value = None
                        Beneficiary = ['NA']
                        Address_list = []
                        Consignee_Reporting_list = []
                        Not_Beneficiary_Found = True
                        Item_Category=''
                        found_mse = False

                        for page in pdf.pages:
                            try:
                                tables = page.extract_tables()
                                for table in tables:
                                    if not found_mse:
                                        for row_num, row in enumerate(table):
                                            if not row or all(cell is None or cell.strip() == '' for cell in row):
                                                continue
                                            for i, cell in enumerate(row):
                                                if cell:
                                                    norm_cell = re.sub(r'\W+', '', cell.lower())
                                                    if "reservedformse" in norm_cell:
                                                        if i + 1 < len(row) and row[i + 1]:
                                                            value = row[i + 1].strip()
                                                        else:
                                                            value = next((c.strip() for c in row if c and "reservedformse" not in c.lower()), "No")
                                                        MSE_value = "Yes" if "yes" in value.lower() else value
                                                        found_mse = True
                                                        break
                                            if found_mse:
                                                break

                 
                                    if (MSE_value or "").lower() == "yes":
                                        print("MSE_value is yes",bid_title.text)
                                    
                                    
                                    if not table or len(table) < 2: continue

                                    for row in table[1:]:
                                        if len(row) >= 2:
                                            key, value = row[0], row[1]
                                                 
                                            try: 
                                                if "Total Quantity" in key and value: Total_Quantity = value
                                            except: pass
                                            
                                            try: 
                                                if "Organisation Name" in key and value: Organisation = value.upper()
                                            except: pass
                                            
                                            try: 
                                                if "Department Name" in key and value: Department_Name = value.upper()
                                            except: pass
                                            
                                            try: 
                                                if "Ministry/State Name" in key and value: Ministry_Name = value.upper()
                                            except: pass
                                            
                                            try: 
                                                if "Item Category" in key and value: Item_Category = value
                                            except: pass
                                            
                                            try:
                                                if key and "EMD Amount" in key and value:
                                                    try:
                                                        emd_amount = float(re.sub(r'[^\d.]', '', value))
                                                        Tender_value = emd_amount * 50
                                                    except: pass
                                            except: pass
                                            
                                            try:
                                                if key and "Estimated Bid Value" in key and value: Tender_value = value
                                            except: pass
                                            
                                            try:
                                                if "ePBG Percentage" in key: epbg_percentage = value
                                            except: pass
                                            
                                            
                                    headers = [cell.strip() if cell else "" for cell in table[0]]
                                    if (any("Consignee" in h for h in headers)):
                                        try:
                                            data = dict(zip(headers, row))
                                            address = data.get(next((h for h in headers if "Address" in h), ""), "")
                                            consignee = data.get(next((h for h in headers if "Consignee" in h), ""), "")
                                            try: consignee = consignee.replace("*", "").strip()
                                            except: pass
                                            if consignee and consignee not in Consignee_Reporting_list:
                                                Consignee_Reporting_list.append(consignee)

                                            address = data.get(next((h for h in headers if "Address" in h), ""), "")
                                            try: address = address.replace("*", "").strip()
                                            except: pass
                                            if address and address not in Address_list:
                                                Address_list.append(address)
                                        except: pass
                                            
                            except Exception as e:
                                traceback.print_exc()

                            try:
                                if (Not_Beneficiary_Found):
                                    text = page.extract_text()
                                    if "Beneficiary" in text:
                                        lines = text.split('\n')
                                        for idx, line in enumerate(lines):
                                            if "Beneficiary" in line:
                                                for next_line in lines[idx+1:idx+4]:
                                                    if "Provn" in next_line:
                                                        Beneficiary = ["Provn"]
                                                        Not_Beneficiary_Found = False
                                                    
                                                    elif "CE" in next_line:
                                                        Beneficiary = ["Engineer"]
                                                        Not_Beneficiary_Found = False

                                                    elif "CSO" in next_line:
                                                        Beneficiary = ["signal"]
                                                        Not_Beneficiary_Found = False
                                                        
                                                    elif "signal" in next_line.lower():
                                                        Beneficiary = ["signal"]
                                                        Not_Beneficiary_Found = False

                                                    elif "Officer" in next_line:
                                                        Not_Beneficiary_Found = False

                                                break
                            except: pass

                        if Item_Category =='': 
                            print(f"error in finding Item_Category for: {bid_title.text}")
                            return
                        
                        event_data={}
                        event_data["DATE OF SEARCH"] = today.strftime("%d-%b-%Y")
                        event_data["TENDER ID"] = bid_title.text
                        
                        
                        
                        event_data["elementPut"] = Organisation 
                        event_data["MINISTRY"] = Ministry_Name
                        event_data["DEPARTMENT"] = Department_Name
                        event_data["ORGANISATION"] = Organisation
                        
                        event_data["START DATE"] = start_date
                        event_data["END DATE"] = end_date
                        event_data["END Time"] = end_date_time
                        event_data["DAY LEFT"] = ''
                        event_data["EMD AMOUNT"] = emd_amount
                        event_data["TENDER VALUE"] = Tender_value
                        event_data["Consignee Reporting"] = Consignee_Reporting_list 
                        event_data["ADDRESS"] = Address_list
                        event_data["BRANCH"] = Beneficiary[0]
                        event_data["MSE"] = MSE_value
                        event_data["file_path"] = download_path
                        event_data["link"] = link_href
                        event_data["epbg_percentage"] = epbg_percentage
                        
                        try:event_data["ITEM CATEGORY"] = event_data["ITEM DESCRIPTION"] = Item_Category
                        except:
                            try: event_data["ITEM DESCRIPTION"] = from_card_discription
                            except: pass
                        try:
                            if quantity == 0: event_data["QTY"] = Total_Quantity
                            else: event_data["QTY"] = quantity
                                
                        except: pass
                        return event_data
                except:
                    if os.path.exists(download_path):
                        os.remove(download_path)
                        print(f"Corrupt PDF removed. Re-downloading might help.: {bid_title.text}")
            
            else:
                print(f"ERORROROROROOROROROROROROROROROORORORR\nLink is not a downloadable file or not found: {link_href}")
        except:
            traceback.print_exc()
            print(f"Error downloading link for gem id: {bid_title.text}")
    except:
        print(f"Error")
        traceback.print_exc()
        
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
        # checkbox = wait.until(EC.element_to_be_clickable((By.ID, "bidrastatus")))
        # checkbox.click()
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
                        tenders.append(gem_find(driver, card_elements, card))
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
GEM/2025/B/6486267
"""
# GEM/2025/B/76901

tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)


split_arrays = split_into_parts(tender_ids, 6)
Main(split_arrays)


