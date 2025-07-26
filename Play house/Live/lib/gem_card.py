
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

today = date.today()

from time import sleep
import time

import requests
import pdfplumber

import requests
from urllib.parse import urlparse
import re
 
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep,time
import os
import json
from selenium.webdriver.support import expected_conditions as EC
import configparser
config = configparser.ConfigParser()
import re
import threading
import traceback
import requests
from datetime import datetime
import pyodbc
from lib.pdf_flie_reader import gem_doc_reader

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

total_gem_ids_q = '''
SELECT * 
FROM tender_data 
'''

total_gem_ids_df = pd.read_sql(total_gem_ids_q, conn)
conn.close()
all_gem_ids = total_gem_ids_df['tender_id'].tolist()


def convert_date_format(date_str):
    date_obj = ds.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%b-%Y")

def gem_find(driver,card_elements , card, gem_ids, org_name, ministry_name,close_tender_id_list,gem_ids_copy):
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

        if bid_title.text in gem_ids_copy:
            try: gem_ids.remove(bid_title.text)
            except: pass
            print(f"gem id skipped: {org_name}, {bid_title.text} and started at: {start_date}")
            return 
        elif bid_title.text in close_tender_id_list:
            print(f"--xx gem id {org_name}, {bid_title.text} extended xx--")
            return {"extended": today.strftime("%d-%b-%Y"),"DATE OF SEARCH": today.strftime("%d-%b-%Y"),"TENDER ID": bid_title.text,"END DATE": end_date,"END Time": end_date_time}
        elif bid_title.text in all_gem_ids:
            print(f"--xx gem id {org_name}, {bid_title.text} in db xx--")
            return {"extended": today.strftime("%d-%b-%Y"),"DATE OF SEARCH": today.strftime("%d-%b-%Y"),"TENDER ID": bid_title.text,"END DATE": end_date,"END Time": end_date_time}
        
        try:
            bid_id_no = link_href.split('/')[-1]
            download_path = f'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-{bid_id_no}.pdf'

            if os.path.exists(download_path): 
                print(f"have file for:{org_name}, {bid_id_no}")
                try:
                    if bid_title.text in all_gem_ids:
                        all_gem_ids.append(bid_title.text)
                        print(f"alrady in db:{org_name}, {bid_title.text}")
                        return 
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
                event_data = gem_doc_reader(download_path)
                if not event_data or event_data == []:
                    print(f"error in tender _geting data {event_data}")
                    return
                
                if event_data and event_data.get("ITEM DESCRIPTION") == "":
                    try: event_data["ITEM DESCRIPTION"] = from_card_discription
                    except: pass
                
                event_data["TENDER ID"] = bid_title.text
                event_data["START DATE"] = start_date
                event_data["END DATE"] = end_date
                event_data["END Time"] = end_date_time
                event_data["link"] = link_href
                try:
                    if int(quantity) != 0:
                        event_data["QTY"]=int(quantity)
                except: pass
                return event_data

            else: print(f"ERORROROROROOROROROROROROROROROORORORR\nLink is not a downloadable file or not found: {link_href}")


        except:
            traceback.print_exc()
            try:
                gem_ids.remove(bid_title.text)
            except:pass
            print(f"Error downloading link for gem id: {bid_title.text}")
    except:
        print(f"Error")
        traceback.print_exc()
        
        
        
