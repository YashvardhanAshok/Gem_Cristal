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
import ntpath
import pdfplumber

import requests
from urllib.parse import urlparse
import re
 
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
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


import tkinter as tk
from tkinter import ttk

def create_window():
    root = tk.Tk()
    root.title("Click to Destroy")

    ttk.Button(root, text="Close Window", command=root.destroy).pack(padx=20, pady=20)

    root.mainloop()

# Call the function to create the window
 

 
 
 

def e_procure(driver,card_elements , card, gem_ids, element,close_tender_id_list,gem_ids_copy):
  pass
          
        

db_lock = threading.Lock()
def sql(extracted_data):
    with db_lock:  
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        for tender_data in extracted_data:
            tender_id = tender_data["TENDER ID"]

            cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (tender_id,))
            exists = cursor.fetchone()[0]

            try:
                end_date = datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date()
            except:
                print(f"Invalid END DATE for tender {tender_id}: {tender_data.get('END DATE')}")
                end_date = None

            end_time = str(tender_data.get("END Time", ""))
            date_of_search_str = tender_data.get("DATE OF SEARCH", "")
            try:
                extended = datetime.strptime(date_of_search_str, "%d-%b-%Y").strftime("%Y-%m-%d")
            except:
                print(f"Invalid DATE OF SEARCH for tender {tender_id}: {date_of_search_str}")
                extended = ""

            if exists:
                update_sql = """
                    UPDATE tender_data
                    SET end_date = ?, end_time = ?, extended = ?,Cancel	 = ? 
                    WHERE tender_id = ?
                """
                cursor.execute(update_sql, (end_date, end_time, extended,"", tender_id))
                print(f"Tender ID {tender_id} exists.")
                conn.commit()
                continue

            insert_sql = """
            INSERT INTO tender_data (
                date_of_search, tender_id, element_put, item_description, qty,
                start_date, end_date, end_time, day_left_formula,
                emd_amount, tender_value, item_category,
                consignee_reporting, address, MSE,
                ministry, department, branch, link_href, file_path,
                matches, matched_products,Cancel 
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
                ""
            )

            cursor.execute(insert_sql, values)
            conn.commit()
            print(f"Tender ID {tender_id} inserted successfully.")

        cursor.close()
        conn.close()


gemlog_="e_procure_log.txt"

def e_procure(ministry_name, Organization_name):
    options = Options()
    prefs = {"download.default_directory": os.path.join(os.getcwd(), "download_pdf"),"download.prompt_for_download": False,"plugins.always_open_pdf_externally": True}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options)
    driver.get('https://eprocure.gov.in/eprocure/app')
    
    sleep(1)
    try: WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="alertbutclose" and text()="Close"]'))).click()   
    except: pass
    sleep(1)
    driver.find_element(By.XPATH, '//a[text()="Tenders by Organisation"]').click()

    create_window()


    ministry_mapping = {
        "MINISTRY OF HOUSING & URBAN AFFAIRS": ["HINDUSTAN STEELWORKS CONSTRUCTION LIMITED"],
        "MINISTRY OF POWER": ["NTPC LIMITED"],
        "MINISTRY OF HEALTH AND FAMILY WELFARE": ["HLL INFRA TECH SERVICES LIMITED"],
        "MINISTRY OF CIVIL AVIATION": ["AIRPORTS AUTHORITY OF INDIA"],
        "MINISTRY OF HOME AFFAIRS": [
            "NATIONAL SECURITY GUARD", "INDO TIBETAN BORDER POLICE", "NATIONAL DISASTER RESPONSE FORCE",
            "SASHASTRA SEEMA BAL", "ASSAM RIFLES", "CENTRAL RESERVE POLICE FORCE",
            "BORDER SECURITY FORCE", "CENTRAL INDUSTRIAL SECURITY FORCE"
        ],
        "MINISTRY OF WATER RESOURCES RIVER DEVELOPMENT AND GANGA REJUVENATION": [
            "NATIONAL PROJECTS CONSTRUCTION CORPORATION LIMITED"
        ],
        "MINISTRY OF DEFENCE": ["INDIAN AIR FORCE", "BORDER ROAD ORGANISATION", "INDIAN ARMY", "INDIAN NAVY"]
    }

    # Flatten ministry list for lookup
    ministry_lookup = {}
    for ministry, departments in ministry_mapping.items():
        for dept in departments:
            ministry_lookup[dept.upper()] = ministry



    rows = driver.find_elements(By.XPATH, "//table[@id='table']//tr[contains(@class, 'even') or contains(@class, 'odd')]")

    json_list = []

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) < 5:
            continue

        try:
            starting_date = cells[1].text.strip()
            closing_date = cells[2].text.strip()
            end_time = closing_date.split()[-2] + " " + closing_date.split()[-1]
            
            link_tag = cells[4].find_element(By.TAG_NAME, "a")
            link = link_tag.get_attribute("href")
            
            full_text = cells[4].text
            tender_id = full_text.split("[")[-1].split("]")[0]

            dept_info = cells[5].text.strip()
            dept_name = dept_info.split(" - ")[0].strip().upper()
            ministry_part = dept_info.split(" - ")[-1].strip().upper()

            ministry = ministry_lookup.get(dept_name, ministry_part)
            
            data = {
                "starting_date": starting_date,
                "closing_date": closing_date,
                "end_time": end_time,
                "tender_id": tender_id,
                "link": link,
                "department": dept_name,
                "ministry": ministry
            }

            json_list.append(data)
        except Exception as e:
            print(f"Skipping row due to error: {e}")

    driver.quit()
    print(json.dumps(json_list, indent=2))


def gem():
    try:
        max_threads = 3
        threads = []

        while True:
            threads = [t for t in threads if t.is_alive()]
            if len(threads) < max_threads:
                break
            sleep(0.5)
        ministry_name = Organization_name = None
        t = threading.Thread(target=e_procure, args=(ministry_name,Organization_name))
        t.start()
        threads.append(t)
    except:
        traceback.print_exc() 

gem()