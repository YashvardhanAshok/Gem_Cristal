import requests
import ntpath
import pdfplumber

import requests
from urllib.parse import urlparse
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

import traceback
import time
import json
from selenium.common.exceptions import TimeoutException
from datetime import datetime as ds
from time import sleep

from datetime import date
today = date.today()
from selenium.common.exceptions import NoSuchElementException
import threading
import requests

def sql(status, L_Placeholder, tender_id_to_update):
    pass

def gem_find(driver,card_elements , card, gem_ids, element,close_tender_id_list):
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

        if bid_title.text in gem_ids:
            print(f"gem id skipped:{bid_title.text} and started at: {start_date}")
            return
        
        elif bid_title.text in close_tender_id_list:
            print(f"--xx gem id {bid_title.text} extended xx--")
            return {"extended": today.strftime("%d-%b-%Y"),"DATE OF SEARCH": today.strftime("%d-%b-%Y"),"TENDER ID": bid_title.text,"END DATE": end_date,"END Time": end_date_time}
        
        else:
            gem_ids.append(bid_title.text)



        try:
            try:
                response = requests.get(link_href, stream=True, timeout=15)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                return
            
            if response.status_code == 200 and "text/html" not in response.headers.get("Content-Type", ""):
                if 'Content-Disposition' in response.headers:
                    file_name = response.headers.get('Content-Disposition').split('filename=')[-1].strip('\"')
                else:
                    parsed_url = urlparse(link_href)
                    file_name = ntpath.basename(parsed_url.path)

                
                download_path = os.path.join(os.getcwd(), 'download_pdf', file_name)
                os.makedirs(os.path.dirname(download_path), exist_ok=True)

                with open(download_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"{bid_title.text} for: {download_path}")

                if os.path.exists(download_path):
                    with pdfplumber.open(download_path) as pdf:
                        emd_amount = None
                        epbg_percentage = None
                        Tender_value = None
                        MSE_value = None
                        Beneficiary = ['NA']
                        for page in pdf.pages:

                            tables = page.extract_tables()
                            for section in tables:
                                try:
                                    for row in section:
                                        key = row[0]
                                        value = row[1]
                                        try:
                                            if key and 'MSE Purchase Preference' in key and value:
                                                MSE_value = value
                                                print()
                                        except:
                                            pass
                                        try:
                                            if key and 'Total Quantity' in key and value:
                                                Total_Quantity = value
                                        except:
                                            pass
                                        try:
                                            if key and 'Item Category' in key and value:
                                                Item_Category = value
                                        except:
                                            pass
                                        try:
                                            if key and 'EMD Amount' in key and value:
                                                emd_amount = float(re.sub(r'[^\d.]', '', value))
                                                Tender_value = emd_amount * 50
                                        except:
                                            pass
                                        try:
                                            if key and 'ePBG Percentage' in key:
                                                epbg_percentage = value
                                        except:
                                            pass    
                                except:
                                    print('error in EMD Amount')

                        for page in pdf.pages:
                            text = page.extract_text()
                            try:
                                if "Beneficiary" in text:
                                    lines = text.split('\n')
                                    for line in lines:
                                        if "Beneficiary" in line:
                                            index = lines.index(line)
                                            for i in range(index + 1, index + 4):
                                                if "Provn" in lines[i]:
                                                    Beneficiary = ["Provn"]
                                                    break
                                                    
                                                elif "CE" in lines[i]:
                                                    Beneficiary = ["Engineer"]
                                                    break
                                                elif "CSO" in lines[i]:
                                                    Beneficiary = ["signal"]
                                                    break
                                                    
                                                elif "Officer" in lines[i]:
                                                    # Beneficiary = ["signal"]
                                                    # Beneficiary = ["Officer"]
                                                    break
                            except:
                                pass
                        # if Beneficiary==[]:
                        #     try:
                        #         Beneficiary = lines[index+1].split("\n")
                        #     except:
                        #         Beneficiary = ['']

                        event_data = {}
                        Consignee_Reporting_list = []
                        Address_list = []
                        for page in pdf.pages:
                            tables = page.extract_tables()
                            for table in tables:
                                headers = table[0]
                                if any("S.No" in (cell or "") for cell in headers):
                                    for row in table[1:]:
                                        row = row + [""] * (len(headers) - len(row))
                                        data = dict(zip(headers, row))
                                        
                                        try:
                                            consignee_value = data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").replace("*", "").strip()
                                            if consignee_value and consignee_value not in Consignee_Reporting_list:
                                                Consignee_Reporting_list.append(consignee_value)
                                        except:
                                            pass

                                        try:
                                            address_value = data.get(next((h for h in headers if "Address" in (h or "")), ""), "").replace("*", "").strip()
                                            if address_value and address_value not in Address_list:
                                                Address_list.append(address_value)
                                        except:
                                            pass

                        event_data["DATE OF SEARCH"] = today.strftime("%d-%b-%Y")
                        event_data["TENDER ID"] = bid_title.text
                        event_data["elementPut"] = element
                        try:
                            event_data["ITEM DESCRIPTION"] = title
                        except:
                            try:
                                event_data["ITEM DESCRIPTION"] = Item_Category
                            except:
                                pass
                        try:
                            if quantity == 0:
                                event_data["QTY"] = Total_Quantity
                            else:
                                event_data["QTY"] = quantity
                                
                        except:
                            pass
                        
                        event_data["START DATE"] = start_date
                        event_data["END DATE"] = end_date
                        event_data["END Time"] = end_date_time
                        event_data["DAY LEFT"] = ''
                        event_data["EMD AMOUNT"] = emd_amount
                        event_data["TENDER VALUE"] = Tender_value
                        try:
                            event_data["ITEM CATEGORY"] = Item_Category
                            
                        except:
                            pass
                        
                        event_data["Consignee Reporting"] = Consignee_Reporting_list 
                        event_data["ADDRESS"] = Address_list

                        event_data["MINISTRY"] = department_address_parts[0]
                        
                        event_data["DEPARTMENT"] = element
                        
                        # event_data["DEPARTMENT"] = department_address_parts[1]
                        event_data["BRANCH"] = Beneficiary[0]
                        
                        event_data["MSE"] = MSE_value
                        event_data["file_path"] = download_path
                        event_data["link"] = link_href
                        return event_data
            
            else:
                print(f"Link is not a downloadable file or not found: {link_href}")
        except Exception as download_error:
            traceback.print_exc()
            print(f"Error downloading or reading file from {link_href}: {download_error}")
    except Exception as e:
        traceback.print_exc()




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
                        sql("Technical Evaluation", None, element)
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

                        sql("Bid Award", new_arr, element)
                        driver.close()
                        driver.switch_to.window(main_window)

        except Exception as e:
            print(f"error in gem id:{element}")
            traceback.print_exc() 

    driver.quit()
    
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

def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]

tender_ids = [
    'GEM/2024/B/5113433', 'GEM/2024/R/378645', 'GEM/2024/B/4568536', 'GEM/2024/R/329749',
    'GEM/2024/B/5003503', 'GEM/2024/R/427460', 'GEM/2024/B/5512048', 'GEM/2024/B/5558220',
    'GEM/2024/B/5612315', 'GEM/2024/B/5483168', 'GEM/2024/B/5659812', 'GEM/2024/B/5526863',
    'GEM/2024/B/5511326', 'GEM/2024/R/422113', 'GEM/2024/B/5631624', 'GEM/2024/B/5643064',
    'GEM/2024/B/5643002', 'GEM/2024/B/5649841', 'GEM/2024/B/5618063', 'GEM/2024/B/5643089',
    'GEM/2024/B/5566511', 'GEM/2024/R/418591', 'GEM/2024/B/5510221', 'GEM/2024/R/416293',
    'GEM/2024/B/5581211', 'GEM/2024/B/5505387', 'GEM/2024/R/412755', 'GEM/2024/B/5536711',
    'GEM/2024/B/5580968', 'GEM/2024/B/5415863', 'GEM/2024/B/5185116', 'GEM/2024/R/408635',
    'GEM/2024/B/5540465', 'GEM/2024/B/5526860', 'GEM/2024/B/5086729', 'GEM/2024/R/404493',
    'GEM/2024/B/5358015', 'GEM/2024/R/404082', 'GEM/2024/B/5562499', 'GEM/2024/B/5386437',
    'GEM/2024/B/5534853', 'GEM/2024/B/5477215', 'GEM/2024/B/5477554', 'GEM/2024/B/5477680',
    'GEM/2024/B/5430828', 'GEM/2024/B/5333788', 'GEM/2024/R/393592', 'GEM/2024/B/5400689',
    'GEM/2024/B/5401591', 'GEM/2024/B/5400209', 'GEM/2024/B/5413073', 'GEM/2024/B/5396459',
    'GEM/2024/B/4781381', 'GEM/2024/R/389911', 'GEM/2024/B/5299482', 'GEM/2024/R/386506',
    'GEM/2024/B/5240830', 'GEM/2024/R/386406', 'GEM/2024/B/5247453', 'GEM/2024/R/386409',
    'GEM/2024/B/5253268', 'GEM/2024/R/386413', 'GEM/2024/B/5240700', 'GEM/2024/R/383401',
    'GEM/2024/B/5318254', 'GEM/2024/B/5335423', 'GEM/2024/B/5234770', 'GEM/2024/R/380614',
    'GEM/2024/B/5319954', 'GEM/2024/B/5151263', 'GEM/2024/B/5202790', 'GEM/2024/R/377167',
    'GEM/2024/B/5179431', 'GEM/2024/R/375707', 'GEM/2024/B/5126691'
]

split_arrays = split_into_parts(tender_ids, 4)
Main(split_arrays,ministry,department,)
