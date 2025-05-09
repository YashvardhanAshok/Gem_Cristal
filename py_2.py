from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
from selenium.common.exceptions import NoSuchElementException
import time
import json
import os
from datetime import date
from datetime import datetime as ds

today = date.today()

from datetime import datetime as datetime_udate
from time import sleep

import os
import requests
from urllib.parse import urlparse
import ntpath
import fitz  
import pdfplumber

import requests
from urllib.parse import urlparse
import re

def clean_text(text):
    if text:
        text = re.sub(r'\(cid:\d+\)', '', text)
        text = text.replace('\n', ' ').replace('\r', ' ').strip()
        return text
    return ''


def gem_funtion(threading_filename,ministry_name,Organization_name):
    
    driver = webdriver.Edge()
    driver.get('https://bidplus.gem.gov.in/advance-search')
    sleep(0.1)

    ministry_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ministry-tab')))
    ministry_tab.click()
    sleep(5)
    
    ministry_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-ministry-container']"))
    )
    ministry_dropdown.click()
    sleep(2)
    
    ministry_search__field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
    ministry_search__field.clear()
    
    ministry_search__field.send_keys(ministry_name)
    ministry_search__field.send_keys(Keys.RETURN)

    json_dir = os.path.join(os.getcwd(), 'db', 'json')
    os.makedirs(json_dir, exist_ok=True)
    file_Pail = os.path.join(json_dir, ministry_name + '.json')
    sleep(2)

    for org_name in Organization_name:
        string_name_file = ministry_name + org_name
        
        if not os.path.exists(threading_filename):
            with open(threading_filename, "w") as f:
                json.dump({string_name_file: []}, f)

        with open(threading_filename, "r") as f:
            gem_ids_json = json.load(f)
            gem_ids = gem_ids_json.get(string_name_file, [])
        #Organization
        Organization_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-organization-container']"))
        )
        Organization_dropdown.click()
        Organization_search__field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
        Organization_search__field.clear()
        Organization_search__field.send_keys(org_name)
        Organization_search__field.send_keys(Keys.RETURN)
        
        # surch_bu
        # Use JavaScript to click the button directly
        sleep(2)
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return typeof searchBid === 'function'")
        )
        driver.execute_script("searchBid('ministry-search')")
        sleep(2)

        try:
            pagination = driver.find_element(By.ID, "light-pagination")
            page_links = pagination.find_elements(By.CLASS_NAME, "page-link")
            page_numbers = [int(link.text) for link in page_links if link.text.isdigit()]
            max_page = max(page_numbers) if page_numbers else 1  # Default to 1 if no pages
            print("Max page number:", max_page)
            extracted_data = []
        except:
            continue
        try:
            for page_no in range(int(max_page)):
                
                card_elements = WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))

                for card in card_elements:
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
                        start_date_time = opening_date_parts[1] +" "+ opening_date_parts[2]  

                        closing_date_parts = end_date.split(" ")
                        end_date = convert_date_format(closing_date_parts[0])  
                        end_date_time = closing_date_parts[1] +" "+ closing_date_parts[2] 
                        
                        try:
                            a_tag = card.find_element(By.CSS_SELECTOR, 'a[title][data-content]')
                            title = a_tag.get_attribute("data-content")
                            
                        except:
                            abc = card.find_element(By.CLASS_NAME, 'row').text
                            titles = []
                            for card_element in card_elements:
                                text = card_element.text
                                if text.startswith(bid_title.text):
                                    title=titles.append(text)

                        json_dir = os.path.join(os.getcwd(), 'db', 'json')
                        os.makedirs(json_dir, exist_ok=True)
                        file_Pail = os.path.join(json_dir, ministry_name + '.json')

                        try:
                            response = requests.get(link_href, stream=True)
                            if response.status_code == 200 and "text/html" not in response.headers.get("Content-Type", ""):
                                if 'Content-Disposition' in response.headers:
                                    file_name = response.headers.get('Content-Disposition').split('filename=')[-1].strip('\"')
                                else:
                                    parsed_url = urlparse(link_href)
                                    file_name = ntpath.basename(parsed_url.path)
    
                                if bid_title.text in gem_ids:
                                    print("gem id skiped:",bid_title.text)
                                    continue
                                else:
                                    gem_ids.append(bid_title.text)
                                
                                download_path = os.path.join(os.getcwd(), 'download_pdf', file_name)
                                os.makedirs(os.path.dirname(download_path), exist_ok=True)


                                def flatten(lst):
                                    for item in lst:
                                        if isinstance(item, list):
                                            yield from flatten(item)
                                        else:
                                            yield item

                                with open(download_path, 'wb') as f:
                                    for chunk in response.iter_content(chunk_size=8192):
                                        if chunk:
                                            f.write(chunk)
                                
                                print(f"Downloaded file: {download_path}")

                                # ✅ Now safely open it using the full path
                                if os.path.exists(download_path):
                                    with pdfplumber.open(download_path) as pdf:
                                        emd_amount = None
                                        epbg_percentage = None
                                        Tender_value = None
                                        for page in pdf.pages:
                                            tables = page.extract_tables()

                                            for section in tables:
                                                for row in section:
                                                    key = row[0]
                                                    value = row[1]
                                                    if key and 'EMD Amount' in key:
                                                        emd_amount = float(value)
                                                        Tender_value = emd_amount * 50
                                                    elif key and 'ePBG Percentage' in key:
                                                        epbg_percentage = value


                                        for page in pdf.pages:
                                            tables = page.extract_tables()
                                            for table in tables:
                                                headers = table[0]
                                                if any("S.No" in (cell or "") for cell in headers):
                                                    for row in table[1:]:
                                                        row = row + [""] * (len(headers) - len(row))
                                                        data = dict(zip(headers, row))
                                                        # "Consignee Reporting": data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").strip(),
                                                        event_data = {
                                                            "dateOfSearch": today.strftime("%d-%b-%Y"),
                                                            "GEM-ID": bid_title.text,
                                                            "title": title,
                                                            "Consignee Reporting": (data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "") or "").strip(),
                                                            "Address":  (data.get(next((h for h in headers if "Address" in (h or "")), ""), "") or "").strip(),
                                                            "Quantity": (data.get(next((h for h in headers if "Quantity" in (h or "")), ""), "") or "").strip(),
                                                            "Delivery Days": (data.get(next((h for h in headers if "Delivery Days" in (h or "")), ""), "") or "").strip(),
                                                            "EMD Amount": emd_amount,
                                                            "Tender_value": Tender_value,
                                                            "ePBG Percentage": epbg_percentage,
                                                            "Opening Date": start_date,
                                                            "Opening Time": start_date_time,
                                                            "Closing Date": end_date,
                                                            "Closing Time": end_date_time,
                                                            "Time left":"""=IF(O40 + TIMEVALUE(P40) > NOW(), INT(O40 + TIMEVALUE(P40) - NOW()) & " days", "Closed")""",
                                                            "link": link_href
                                                        }
                                                        print(event_data)
                                                        extracted_data.append(event_data)

                            else:
                                print(f"Link is not a downloadable file or not found: {link_href}")
                        except Exception as download_error:
                            traceback.print_exc() 
                            
                            print(f"Error downloading or reading file from {link_href}: {download_error}")

                            event_data = {
                                "dateOfSearch":today.strftime("%d-%b-%Y"),
                                "website": 'GEM',
                                "GEM-ID":bid_title.text,
                                "title": title,
                                "Opening Date": start_date,
                                "Opening Time": start_date_time,
                                "Closing Date": end_date,
                                "Closing Time": end_date_time,
                                "link": link_href,
                                "Consignee Reporting": '',
                                "Address": '',
                                "Quantity": '',
                                "Delivery Days": ''
                            }

                        extracted_data.append(event_data) 
                    except Exception as e:
                        traceback.print_exc() 
                                        

                if page_no == max_page or page_no == 10:
                    break
                else:
                    next_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]"))
                    )
                    next_button.click()

        except Exception as e:
            print("An error occurred:", str(e))
            traceback.print_exc() 
        

        try:
            with open(file_Pail, "r") as json_file:
                existing_data = json.load(json_file)
            existing_data.extend(extracted_data)
            unique_entries = []
            for entry in existing_data:
                if (entry["elementPut"], entry["title"]) not in [(e["elementPut"], e["title"]) for e in unique_entries]:
                    unique_entries.append(entry)

            with open(file_Pail, "w") as json_file:
                json.dump(unique_entries, json_file, indent=4)       

        except:
            with open(file_Pail, "w") as json_file:
                json.dump(extracted_data, json_file, indent=4)
                
        with open(threading_filename, "w") as f:
            gem_ids_json[string_name_file] = gem_ids
            json.dump(gem_ids_json, f, indent=2)
        print(gem_ids)
    driver.quit()
    
import threading
def gem():
    try:
        count = 0 
        threads = []
        MINISTRY_list = [
            ["MINISTRY OF COMMUNICATIONS", ['']],
            ["MINISTRY OF HOUSING & URBAN AFFAIRS", ["HINDUSTAN STEELWORKS CONSTRUCTION LIMITED"]],
            ["MINISTRY OF POWER", ["NTPC LIMITED"]],
            ["MINISTRY OF HEALTH AND FAMILY WELFARE", ["HLL INFRA TECH SERVICES LIMITED"]],
            ["MINISTRY OF DEFENCE", ["INDIAN AIR FORCE", "INDIAN NAVY", "INDIAN ARMY"]],
            ["MINISTRY OF CIVIL AVIATION", ["AIRPORTS AUTHORITY OF INDIA"]],
            ["MINISTRY OF HOME AFFAIRS", ["ASSAM RIFLES", "CENTRAL RESERVE POLICE FORCE", "BORDER SECURITY FORCE", "CENTRAL INDUSTRIAL SECURITY FORCE", "NATIONAL SECURITY GUARD", "INDO TIBETAN BORDER POLICE", "NATIONAL DISASTER RESPONSE FORCE"]]
        ]

        for MINISTRY in MINISTRY_list: 
            ministry_name=MINISTRY[0]
            Organization_name=MINISTRY[1]
            threading_filename = os.path.join(os.path.dirname(__file__), 'db', "gem_bid_id_ministry",f"{count}.json")
            t = threading.Thread(target=gem_funtion, args=(threading_filename,ministry_name,Organization_name))
            t.start()
            threads.append(t)
            count = count  + 1 
            if count == 5:
                for t in threads:
                    t.join()
                count = 0
                
    except:
        traceback.print_exc() 



gem()




