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
from selenium.common.exceptions import TimeoutException
from datetime import datetime as ds
from time import sleep

from datetime import date
today = date.today()
from selenium.common.exceptions import NoSuchElementException
import pyodbc
import pyodbc
import pandas as pd

today = date.today()
failed_downloads = []

from time import sleep

import requests
import ntpath
import pdfplumber

import requests
from urllib.parse import urlparse
import re

db_lock = threading.Lock()
def sql(tenders):
    with db_lock:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        try:
            for tender_data in tenders:
                if not tender_data:
                    continue  
                tender_id = tender_data["TENDER ID"]

                # Check if tender exists
                cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (tender_id,))
                exists = cursor.fetchone()[0]

                # Parse end_date safely
                try:
                    end_date = datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date()
                except:
                    print(f"Invalid END DATE for tender {tender_id}: {tender_data.get('END DATE')}")
                    end_date = None

                end_time = str(tender_data.get("END Time", ""))

                if exists:
                    update_sql = """
                        UPDATE tender_data
                        SET
                            date_of_search = ?, element_put = ?, item_description = ?, qty = ?,
                            start_date = ?, end_date = ?, day_left_formula = ?,
                            emd_amount = ?, tender_value = ?, item_category = ?,
                            consignee_reporting = ?, address = ?, MSE = ?,
                            ministry = ?, department = ?, branch = ?, link_href = ?, file_path = ?,
                            matches = ?, matched_products = ?, end_time = ?
                        WHERE tender_id = ?
                    """

                    values = (
                        datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                        str(tender_data.get("elementPut", "")),
                        str(tender_data.get("ITEM DESCRIPTION", "")),
                        int(tender_data.get("QTY", 0)),
                        datetime.strptime(tender_data["START DATE"], "%d-%b-%Y").date(),
                        end_date,
                        str(tender_data.get("DAY LEFT", "")),
                        float(tender_data.get("EMD AMOUNT") or 0),
                        float(tender_data.get("TENDER VALUE") or 0),
                        str(tender_data.get("ITEM CATEGORY", "")),
                        json.dumps(tender_data.get("Consignee Reporting", [])),
                        json.dumps(tender_data.get("ADDRESS", [])),
                        str(tender_data.get("MSE", '')),
                        str(tender_data.get("MINISTRY", "")),
                        str(tender_data.get("DEPARTMENT", "")),
                        str(tender_data.get("BRANCH", "")),
                        str(tender_data.get("link", '')),
                        str(tender_data.get("file_path", '')),
                        int(tender_data.get("matches", False)),
                        json.dumps(tender_data.get("matched_products", [])),
                        end_time,
                        tender_id
                    )

                    cursor.execute(update_sql, values)
                    conn.commit()
                    print(f"Tender ID {tender_id} updated successfully.")

                else:
                    insert_sql = """
                        INSERT INTO tender_data (
                            date_of_search, tender_id, element_put, item_description, qty,
                            start_date, end_date, end_time, day_left_formula,
                            emd_amount, tender_value, item_category,
                            consignee_reporting, address, MSE,
                            ministry, department, branch, link_href, file_path,
                            matches, matched_products, Cancel
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """

                    values = (
                        datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                        tender_id,
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
                        ""  # default Cancel field
                    )

                    cursor.execute(insert_sql, values)
                    conn.commit()
                    print(f"Tender ID {tender_id} inserted successfully.")

        except Exception:
            traceback.print_exc()
            print("Error in SQL function")

        finally:
            cursor.close()
            conn.close()
            
def gem_find(driver, card_elements, card):
    global failed_downloads
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
    time.sleep(0.2)
    try:
        bid_title1 = card.find_element(By.CLASS_NAME, 'bid_no_hover')
        bid_title = bid_title1
        link_href = bid_title1.get_attribute("href")

        start_date = card.find_element(By.CLASS_NAME, 'start_date').text
        end_date = card.find_element(By.CLASS_NAME, 'end_date').text

        def convert_date_format(date_str):
            date_obj = ds.strptime(date_str, "%d-%m-%Y")
            return date_obj.strftime("%d-%b-%Y")

        opening_date_parts = start_date.split(" ")
        start_date = convert_date_format(opening_date_parts[0])

        closing_date_parts = end_date.split(" ")
        end_date = convert_date_format(closing_date_parts[0])
        end_date_time = closing_date_parts[1] + " " + closing_date_parts[2]
        
        
        try:
            quantity_element = card.find_element(By.XPATH, ".//div[contains(@class, 'col-md-4')]//div[contains(text(), 'Quantity')]")
            quantity_text = quantity_element.text.strip()
            if "Quantity:" in quantity_text:
                quantity = quantity_text.split("Quantity:")[-1].strip()
            else:
                quantity = 0

        except Exception as e:
            quantity = 0

        try:
            department_div = card.find_element(By.CSS_SELECTOR, "div.col-md-5 > div:nth-child(2)")
            department_address = department_div.get_attribute('innerHTML')
            
            if isinstance(department_address, str) and "<br>" in department_address:
                department_address_parts = department_address.split("<br>")
            else:
                department_address_parts = [department_address, None]
                
        except Exception as e:
            department_address_parts=[None,None]
            print(f"Could not extract department address: {e}")

        try:
            a_tag = card.find_element(By.CSS_SELECTOR, 'a[title][data-content]')
            title = a_tag.get_attribute("data-content")
        except:
            titles = []
            for card_element in card_elements:
                text = card_element.text
                if text.startswith(bid_title.text):
                    title = titles.append(text)

        try:
            try:
                response = requests.get(link_href, stream=True, timeout=15)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return
            
            
            event_data = {
            "DATE OF SEARCH": today.strftime("%d-%b-%Y"),

            "START DATE": start_date,
            "END DATE": end_date,
            "END Time": end_date_time,
            "DAY LEFT": '',
            "MINISTRY": department_address_parts[0],
            "DEPARTMENT": department_address_parts[1],
            "TENDER ID": bid_title.text,
            "QTY" : quantity
            }
            return event_data
            
            
            if response.status_code == 200 and "text/html" not in response.headers.get("Content-Type", ""):
                if 'Content-Disposition' in response.headers:
                    file_name = response.headers.get('Content-Disposition').split('filename=')[-1].strip('\"')
                else:
                    parsed_url = urlparse(link_href)
                    file_name = ntpath.basename(parsed_url.path)

                download_path = os.path.join(os.getcwd(), 'DOWNLOAD_PDF2', file_name)
                os.makedirs(os.path.dirname(download_path), exist_ok=True)

                with open(download_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"{bid_title.text} for: {download_path}")
               
                
                # if os.path.exists(download_path):
                #     with pdfplumber.open(download_path) as pdf:
                #         emd_amount = None
                #         epbg_percentage = None
                #         Tender_value = None
                #         MSE_value = None
                #         Beneficiary = ['NA']
                #         for page in pdf.pages:

                #             tables = page.extract_tables()
                #             for section in tables:
                #                 try:
                #                     for row in section:
                #                         key = row[0]
                #                         value = row[1]
                #                         try:
                #                             if key and 'MSE Purchase Preference' in key and value:
                #                                 MSE_value = value
                #                                 print()
                #                         except:
                #                             pass
                #                         try:
                #                             if key and 'Total Quantity' in key and value:
                #                                 Total_Quantity = value
                #                         except:
                #                             pass
                #                         try:
                #                             if key and 'Item Category' in key and value:
                #                                 Item_Category = value
                #                         except:
                #                             pass
                #                         try:
                #                             if key and 'EMD Amount' in key and value:
                #                                 emd_amount = float(re.sub(r'[^\d.]', '', value))
                #                                 Tender_value = emd_amount * 50
                #                         except:
                #                             pass
                #                         try:
                #                             if key and 'ePBG Percentage' in key:
                #                                 epbg_percentage = value
                #                         except:
                #                             pass    
                #                 except:
                #                     print('error in EMD Amount')

                #         for page in pdf.pages:
                #             text = page.extract_text()
                #             try:
                #                 if "Beneficiary" in text:
                #                     lines = text.split('\n')
                #                     for line in lines:
                #                         if "Beneficiary" in line:
                #                             index = lines.index(line)
                #                             for i in range(index + 1, index + 4):
                #                                 if "Provn" in lines[i]:
                #                                     Beneficiary = ["Provn"]
                #                                     break
                                                    
                #                                 elif "CE" in lines[i]:
                #                                     Beneficiary = ["Engineer"]
                #                                     break
                #                                 elif "CSO" in lines[i]:
                #                                     Beneficiary = ["signal"]
                #                                     break
                                                    
                #                                 elif "Officer" in lines[i]:
                #                                     # Beneficiary = ["signal"]
                #                                     # Beneficiary = ["Officer"]
                #                                     break
                #             except:
                #                 pass

                #         Consignee_Reporting_list = []
                #         Address_list = []
                #         Capacity_Value = []
                        
                #         for page in pdf.pages:
                #             tables = page.extract_tables()
                #             for table in tables:
                #                 headers = table[0]
                #                 if any("S.No" in (cell or "") for cell in headers):
                #                     for row in table[1:]:
                #                         row2 = [(cell or "").strip() for cell in row]
                #                         row = row + [""] * (len(headers) - len(row))
                #                         data = dict(zip(headers, row))
                                        
                #                         try:
                #                             consignee_value = data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").replace("*", "").strip()
                #                             if consignee_value and consignee_value not in Consignee_Reporting_list:
                #                                 Consignee_Reporting_list.append(consignee_value)
                #                         except:
                #                             pass

                #                         try:
                #                             address_value = data.get(next((h for h in headers if "Address" in (h or "")), ""), "").replace("*", "").strip()
                #                             if address_value and address_value not in Address_list:
                #                                 Address_list.append(address_value)
                #                         except:
                #                             pass

                #                         # Check for row containing "Nominal Rated Capacity (kVA)"
                #                         if any("Nominal Rated Capacity" in cell for cell in row2):
                #                             for i, cell in enumerate(row2):
                #                                 if "Nominal Rated Capacity" in cell:
                #                                     # Look for value in next cell (same row)
                #                                     if i + 1 < len(row2):
                #                                         Capacity_Value.append(row2[i + 1])
                #                                     break  

                #         for page in pdf.pages:
                #             tables = page.extract_tables()
                #             for table in tables:
                #                 for row in table:
                #                     # Normalize row content to avoid NoneType issues
                #                     row = [(cell or "").strip() for cell in row]

                #                     # Check for row containing "Nominal Rated Capacity (kVA)"
                #                     if any("Nominal Rated Capacity" in cell for cell in row):
                #                         for i, cell in enumerate(row):
                #                             if "Nominal Rated Capacity" in cell:
                #                                 # Look for value in next cell (same row)
                #                                 if i + 1 < len(row):
                #                                     Capacity_Value.append(row[i + 1])
                #                                 break  

                #         print("Extracted Capacity:", Capacity_Value)

                #         print("Extracted Capacity:", Capacity_Value)
                #         event_data["Capacity_Value"]=Capacity_Value


                #         event_data["DATE OF SEARCH"] = today.strftime("%d-%b-%Y")
                #         try: event_data["ITEM DESCRIPTION"] = title
                #         except:
                #             try: event_data["ITEM DESCRIPTION"] = Item_Category
                #             except: pass
                #         try:
                #             if quantity == 0: event_data["QTY"] = Total_Quantity
                #             else: event_data["QTY"] = quantity
                #         except: pass
                        
                #         event_data["START DATE"] = start_date
                #         event_data["END DATE"] = end_date
                #         event_data["END Time"] = end_date_time
                #         event_data["DAY LEFT"] = ''
                #         event_data["EMD AMOUNT"] = emd_amount
                #         event_data["TENDER VALUE"] = Tender_value
                #         try: event_data["ITEM CATEGORY"] = Item_Category
                #         except: pass
                        
                #         event_data["Consignee Reporting"] = Consignee_Reporting_list 
                #         event_data["ADDRESS"] = Address_list

                #         event_data["BRANCH"] = Beneficiary[0]
                        
                #         event_data["MSE"] = MSE_value
                #         event_data["file_path"] = download_path
                #         event_data["link"] = link_href

                #         # global MINISTRY_word
                #         # global department_word
                #         # event_data["MINISTRY"] = MINISTRY_word
                #         # event_data["DEPARTMENT"] = department_word
                #         event_data["MINISTRY"] = department_address_parts[0]
                #         event_data["DEPARTMENT"] = department_address_parts[1]

                #         event_data["TENDER ID"] = bid_title.text
                #         with open('input_file.ext', 'a', encoding='utf-8') as outfile:
                #             outfile.write(json.dumps(event_data, ensure_ascii=False) + '\n\n')
                #         return event_data
                        
            
            else:
                print(f"Link is not a downloadable file or not found: {link_href}")
                traceback.print_exc()

        except Exception as download_error:
            traceback.print_exc()
            print(f"Error downloading or reading file from {link_href}: {download_error}")
    
    except Exception as e:
        traceback.print_exc()

def gem_funtion(elements_list):
    tenders = []
    try:
        driver = webdriver.Edge()
        driver.get('https://bidplus.gem.gov.in/all-bids')
        wait = WebDriverWait(driver, 30)
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
                        tenders.append(gem_find(driver, card_elements, card))
                        break

            except Exception as e:
                print(f"error in gem id:{element}")
                traceback.print_exc() 
        driver.quit()
    except: pass
    print(tenders)
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


# MINISTRY_word = 'MINISTRY OF HOME AFFAIRS'
# department_word = 'ASSAM RIFLES'
raw_text = """  
GEM/2024/B/5682036
GEM/2024/B/5524276
GEM/2024/B/5486304
GEM/2024/B/5454145
GEM/2024/B/5458604
GEM/2024/B/5367152
GEM/2024/B/5076138
GEM/2024/B/5074655
GEM/2024/B/4896619
GEM/2024/B/4530127
GEM/2024/B/4777963
GEM/2023/B/4324622
GEM/2023/B/3814969
GEM/2023/B/4047184
GEM/2023/B/3817986
GEM/2023/B/4027762
GEM/2023/B/4000787
GEM/2023/B/3896183
GEM/2023/B/4016922
GEM/2023/B/3988151
GEM/2023/B/3987994
GEM/2023/B/3960160
GEM/2023/B/3808769
GEM/2023/B/3947819
GEM/2023/B/3927153
GEM/2023/B/3927062
GEM/2023/B/3916901
GEM/2023/B/3861391
GEM/2023/B/3895981
GEM/2023/B/3895944
GEM/2023/B/3858161
GEM/2023/B/3848537
GEM/2023/B/3816284
GEM/2023/B/3816092
GEM/2023/B/3803873
GEM/2023/B/3802680
GEM/2023/B/3800180
GEM/2023/B/3785028
GEM/2023/B/3792859
GEM/2023/B/3792848
GEM/2023/B/3727364
GEM/2023/B/3741761
GEM/2023/B/3743952
GEM/2023/B/3730654
GEM/2023/B/3684037
GEM/2023/B/3713607
GEM/2023/B/3710981
GEM/2023/B/3700378
GEM/2023/B/3699453
GEM/2023/B/3695707
GEM/2023/B/3687045
GEM/2023/B/3686841
GEM/2023/B/3681107
GEM/2023/B/3669910
GEM/2023/B/3670418
GEM/2023/B/3670464
GEM/2023/B/3643054
GEM/2023/B/3668314
GEM/2023/B/3666711
GEM/2023/B/3657846
GEM/2023/B/3657529
GEM/2023/B/3654574
GEM/2023/B/3481496
GEM/2023/B/3634216
GEM/2023/B/3605192
GEM/2023/B/3566897
GEM/2023/B/3618556
GEM/2023/B/3618485
GEM/2023/B/3508857
GEM/2023/B/3589920
GEM/2023/B/3570388
GEM/2023/B/3567657
GEM/2023/B/3567015
GEM/2023/B/3585895
GEM/2023/B/3510611
GEM/2023/B/3555586
GEM/2023/B/3555535
GEM/2023/B/3552271
GEM/2023/B/3549736
GEM/2023/B/3549801
GEM/2023/B/3549605
GEM/2023/B/3542817
GEM/2023/B/3526669
GEM/2023/B/3531778
GEM/2023/B/3493200
GEM/2023/B/3529879
GEM/2023/B/3515497
GEM/2023/B/3520363
GEM/2023/B/3522419
GEM/2023/B/3509189
GEM/2023/B/3509021
GEM/2023/B/2981567
GEM/2023/B/3157094
GEM/2023/B/3394493
GEM/2023/B/3315775
GEM/2023/B/3162820
GEM/2023/B/3244935
GEM/2023/B/3214069
GEM/2023/B/3191338
GEM/2023/B/3089110
GEM/2023/B/3048825
GEM/2023/B/3058082
GEM/2023/B/3000004
GEM/2023/B/3039415
GEM/2023/B/3028357
GEM/2023/B/3009651
GEM/2023/B/2948532
GEM/2022/B/2909382
GEM/2022/B/2900742
GEM/2022/B/2811013
GEM/2022/B/2835175
GEM/2022/B/2809505
GEM/2022/B/2692023
GEM/2022/B/2622857
GEM/2022/B/2594976
GEM/2022/B/2592739
GEM/2022/B/2529473
GEM/2022/B/2524299
GEM/2022/B/2487900
GEM/2022/B/2483610
GEM/2022/B/2479705
GEM/2022/B/2455103
GEM/2022/B/2196376
GEM/2022/B/2396267
GEM/2022/B/2345581
GEM/2022/B/2374603
GEM/2022/B/2335435
GEM/2022/B/2286388
GEM/2022/B/2312540
GEM/2022/B/2274959
GEM/2022/B/2271553
GEM/2022/B/2229967
GEM/2022/B/2252791
GEM/2022/B/2201339
GEM/2022/B/2172587
GEM/2022/B/2154347
GEM/2022/B/2083691
GEM/2022/B/1921597
GEM/2022/B/1833181
GEM/2022/B/1830412
GEM/2022/B/1829593
GEM/2022/B/1829211
GEM/2022/B/1818994
GEM/2021/B/1802013
GEM/2021/B/1796153
GEM/2021/B/1796232
GEM/2021/B/1781483
GEM/2021/B/1772940
GEM/2021/B/1772594
GEM/2021/B/1740596
GEM/2021/B/1732639
GEM/2021/B/1699601
GEM/2021/B/1674452
GEM/2021/B/1676004
GEM/2021/B/1655112
GEM/2021/B/1587893
GEM/2021/B/1604831
GEM/2021/B/1509160
GEM/2021/B/1502051
GEM/2021/B/1400978
GEM/2021/B/1347323
GEM/2021/B/1344023
GEM/2021/B/1300231
GEM/2021/B/1024417
GEM/2020/B/826272
GEM/2020/B/830021
GEM/2020/B/830200
GEM/2020/B/765371
GEM/2020/B/725933
GEM/2020/B/760579
GEM/2020/B/686119
GEM/2020/B/677194
GEM/2020/B/675544
GEM/2020/B/644680
GEM/2020/B/668361
GEM/2020/B/661548
GEM/2020/B/661511
GEM/2020/B/660793
GEM/2020/B/617476
GEM/2020/B/613295
GEM/2019/B/426719
GEM/2019/B/344692
GEM/2019/B/309907
GEM/2019/B/290820
GEM/2019/B/290645
GEM/2019/B/273293
GEM/2019/B/268044
GEM/2019/B/268215
GEM/2019/B/260220
GEM/2023/B/4189006
GEM/2023/B/4143988
GEM/2023/B/4105209
GEM/2023/B/4069365
GEM/2023/B/4105343
GEM/2023/B/4116127
GEM/2023/B/4189131
GEM/2023/B/4144711
GEM/2023/B/4188965
GEM/2023/B/3685069
GEM/2023/B/4069632
GEM/2023/B/3528708
GEM/2023/B/4142035
GEM/2023/B/3757875
GEM/2023/B/3612371
GEM/2023/B/3008420
GEM/2023/B/4149925
GEM/2023/B/3187588
GEM/2023/B/3061272
GEM/2023/B/3855944
GEM/2023/B/3940295
GEM/2023/B/3630373
GEM/2023/B/4131320
GEM/2023/B/3863595
GEM/2023/B/4118376
GEM/2023/B/3675466
GEM/2023/B/3866761
GEM/2023/B/3844160
GEM/2024/B/4455173
GEM/2023/B/3161326
GEM/2023/B/3405047
GEM/2021/B/1655153
GEM/2024/B/4491191
GEM/2023/B/4017865
GEM/2023/B/3478606
GEM/2023/B/3614058
GEM/2023/B/3658007
GEM/2023/B/3613992
GEM/2023/B/3542005
GEM/2023/B/3741459
GEM/2023/B/3657873
GEM/2022/B/2556537
GEM/2022/B/2411842
GEM/2023/B/3856747
GEM/2022/B/2551581
GEM/2022/B/2320429
GEM/2022/B/2395866
GEM/2022/B/2551416
GEM/2023/B/3531563
GEM/2022/B/2457715
GEM/2022/B/2457570
GEM/2022/B/2084736
GEM/2022/B/2762603
GEM/2022/B/2093666
GEM/2022/B/2556107
GEM/2023/B/4106483
GEM/2022/B/2090779
GEM/2022/B/2260068
GEM/2022/B/2508415
GEM/2023/B/3546927
GEM/2023/B/3299466
GEM/2023/B/4058345
GEM/2023/B/3896972
GEM/2023/B/4158477
GEM/2023/B/3707596
GEM/2023/B/3830833
GEM/2022/B/2416368
GEM/2023/B/3904373
GEM/2022/B/2375937
GEM/2022/B/2401964
GEM/2022/B/2312870
GEM/2022/B/2488126
GEM/2022/B/2434670
GEM/2023/B/3722889
GEM/2023/B/3791844
GEM/2022/B/2475582
GEM/2023/B/3722447
GEM/2023/B/3586078
GEM/2023/B/4200564
GEM/2023/B/3740556
GEM/2023/B/3893099
GEM/2023/B/3723290
GEM/2022/B/2698697
GEM/2022/B/2430191
GEM/2023/B/3922552
GEM/2022/B/2435566
GEM/2023/B/3511516
GEM/2022/B/1968672
GEM/2023/B/3769542
GEM/2023/B/3021421
GEM/2023/B/3761557
GEM/2023/B/3827247
GEM/2023/B/3890734
GEM/2022/B/2536267
GEM/2022/B/2655453
GEM/2023/B/3761538
GEM/2020/B/599275
GEM/2023/B/3687612
GEM/2022/B/2872873
GEM/2023/B/3765669
GEM/2023/B/3788595
GEM/2023/B/3982827
GEM/2022/B/2475949
GEM/2023/B/4011731
GEM/2023/B/3785226
GEM/2023/B/3847509
GEM/2023/B/3929924
GEM/2022/B/2500793
GEM/2023/B/3741425
GEM/2022/B/2087105
GEM/2022/B/2416927
GEM/2023/B/4003532
GEM/2022/B/2511699
GEM/2023/B/3634182
GEM/2023/B/3662060
GEM/2022/B/2433365
GEM/2023/B/3788549
GEM/2023/B/3810110
GEM/2023/B/3732102
GEM/2023/B/3896234
GEM/2023/B/3717503
GEM/2023/B/3573617
GEM/2022/B/2479678
GEM/2023/B/3498851
"""

tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)

split_arrays = split_into_parts(tender_ids, 5)
Main(split_arrays)
