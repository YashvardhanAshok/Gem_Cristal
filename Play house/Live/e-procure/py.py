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
import traceback

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
from time import sleep
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
import html

import tkinter as tk
from tkinter import ttk

def create_window():
    root = tk.Tk()
    root.title("Click to Destroy")

    ttk.Button(root, text="Close Window", command=root.destroy).pack(padx=20, pady=20)

    root.mainloop()

gemlog_="e_procure_log.txt"


def get_field(driver, label_text):
    try:
        xpath = f"//td[.//b[contains(text(), '{label_text}')]]/following-sibling::td[1]"
        return driver.find_element(By.XPATH, xpath).text.strip()
    except:
        return "NA"

def extract_emd_fields(driver):
    emd_map = {
        "EMD Amount in ₹": "emd",
        # "EMD Exemption Allowed": "emd_exemption",
        # "EMD Fee Type": "emd_type",
        # "EMD Percentage": "emd_percent",
        # "EMD Payable To": "emd_payable_to",
        # "EMD Payable At": "emd_payable_at"
    }

    tender_fields = {}
    try:
        rows = driver.find_elements(By.XPATH, "//table[contains(@class, 'tablebg')]//tr")

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) < 2:
                continue

            for i in range(0, len(cells) - 1, 2):
                label = cells[i].text.strip()
                value = cells[i + 1].text.strip()
                if label in emd_map:
                    if label == "EMD Amount in ₹":
                        tender_fields[emd_map[label]] = value
            # try:
            #     tender_fields["emd"] = int(tender_fields["emd"].replace(",", ""))
            # except:
            #     print("erro can not convert to int")
    except Exception as e:
        print("❌ EMD parsing error:", e)
    return tender_fields

def e_procure():
    # Setup Edge driver
    options = Options()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "download_pdf"),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options)
    driver.maximize_window()
    
    driver.get('https://eprocure.gov.in/eprocure/app?page=FrontEndTendersByOrganisation&service=page')

    all_tenders = []

    org_rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'even') or contains(@class, 'odd')]")
    results = []
    for row in org_rows:
        try:
            dept_name = row.find_element(By.XPATH, "./td[2]").text.strip()
            href = row.find_element(By.XPATH, "./td[3]/a").get_attribute("href")
            results.append([dept_name, href])
        except Exception as e:
            print("Skipping org row:", e)

    for dept_name, org_link in results:
        
        
        # if dept_name not in ["Assam Rifles - MHA", "DG, Indo-Tibetan Border Police Force","DG,CRPF,MHA","DG,BSF,MHA"]: continue
        if dept_name not in [ "DG, Indo-Tibetan Border Police Force","DG,CRPF,MHA","DG,BSF,MHA"]: continue
        # if not dept_name == "Assam Rifles - MHA": continue
        print(f"🔎 Opening: {dept_name}")
        driver.get(org_link)
        sleep(2)

        tender_rows = driver.find_elements(By.XPATH, "//tr[contains(@class, 'even') or contains(@class, 'odd')]")

        for row in tender_rows:
            try:
                cells = row.find_elements(By.TAG_NAME, "td")
                if len(cells) < 6:
                    continue

                start_date, start_time = cells[2].text.strip().split(" ", 1)
                end_date, end_time = cells[3].text.strip().split(" ", 1)

                link_element = cells[4].find_element(By.TAG_NAME, "a")
                tender_title = link_element.text.strip()
                web_link = html.unescape(link_element.get_attribute("href"))

                full_text = cells[4].text
                tender_id = full_text.split("[")[-1].replace("]", "").strip()
                organization = cells[5].text.strip()

                # Open tender in new tab
                main_window = driver.current_window_handle
                driver.execute_script(f"window.open('{web_link}', '_blank');")
                sleep(2)

                all_windows = driver.window_handles
                for handle in all_windows:
                    if handle != main_window:
                        driver.switch_to.window(handle)
                        break

                sleep(2)

                tender_data = {
                    "start_date": start_date,
                    "start_time": start_time,
                    "end_date": end_date,
                    "end_time": end_time,
                    "tender_title": tender_title,
                    "tender_id": tender_id,
                    "web_link": web_link,
                    "organization": organization
                }

                # 🔍 EMD + extra info
                emd_fields = extract_emd_fields(driver)
                tender_data.update(emd_fields)

                # Location & Pincode
                location = get_field(driver, "Location")
                pincode = get_field(driver, "Pincode")
                tender_data["location"] = f"{location}, {pincode}".strip(", ")

                # Tender Value
                tender_value_raw = get_field(driver, "Tender Value in ₹")
                if tender_value_raw.replace(",", "").strip().isdigit():
                    tender_data["tender_value"] = int(tender_value_raw.replace(",", "").strip())
                else:
                    tender_data["tender_value"] = "NA"

                # print(tender_data)
                all_tenders.append(tender_data)

                driver.close()
                driver.switch_to.window(main_window)

            except Exception as e:
                print("❌ Error processing tender:", e)
                continue
        
    driver.quit()

    # Save or print
    with open("eprocure_tenders.json", "w", encoding="utf-8") as f:
        json.dump(all_tenders, f, indent=2, ensure_ascii=False)
    print("✅ Done. Tenders saved to eprocure_tenders.json")

if __name__ == "__main__":
    e_procure()
