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


 
 

 
 
 
download_path=r'C:\vs_code\TenderHunter2.1.3\download_pdf\GeM-Bidding-7973162.pdf'
   
if os.path.exists(download_path):
    with pdfplumber.open(download_path) as pdf:
        emd_amount = None
        epbg_percentage = None
        Tender_value = None
        MSE_value = None
        Beneficiary = ['NA']
        Consignee_Reporting_list = []
        Address_list = []
        Capacity_Value = []
        Not_Beneficiary_Found = True
        
        for page in pdf.pages:
            try:
                tables = page.extract_tables()
                
                for table in tables:
                    if not table or len(table) < 2:
                        continue

                    for row in table[1:]:
                        if len(row) >= 2:
                            key, value = row[0], row[1]
                            if "MSE Purchase Preference" in key and value:
                                MSE_value = value
                            elif "Total Quantity" in key and value:
                                Total_Quantity = value
                            elif "Item Category" in key and value:
                                Item_Category = value
                            elif "EMD Amount" in key and value:
                                try:
                                    emd_amount = float(re.sub(r'[^\d.]', '', value))
                                    Tender_value = emd_amount * 50
                                except: pass
                            elif "ePBG Percentage" in key:
                                epbg_percentage = value
                                
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

                                    elif "Officer" in next_line:
                                        Not_Beneficiary_Found = False

                                break
            except: pass
        
        
        
        
        event_data={}
        event_data["DATE OF SEARCH"] = today.strftime("%d-%b-%Y")
        event_data["DAY LEFT"] = ''
        event_data["EMD AMOUNT"] = emd_amount
        event_data["TENDER VALUE"] = Tender_value
        event_data["Consignee Reporting"] = Consignee_Reporting_list 
        event_data["ADDRESS"] = Address_list
        event_data["BRANCH"] = Beneficiary[0]
        event_data["MSE"] = MSE_value
        event_data["file_path"] = download_path
        event_data["epbg_percentage"] = epbg_percentage
        
        try:event_data["ITEM CATEGORY"] = event_data["ITEM DESCRIPTION"] = Item_Category
        except:pass
        
            
print(event_data)
        
    
{'DATE OF SEARCH': '26-Jun-2025', 
 'DAY LEFT': '', 
 'EMD AMOUNT': 180295.0, 
 'TENDER VALUE': 9014750.0, 
 'Consignee Reporting': ['Anil Kumar K M'], 
 'ADDRESS': ['793010,HQ Directorate General\nAssam Rifles, Laitkor Shillong-\n793010'], 
 'BRANCH': 'NA', 
 'MSE': None, 
 'file_path': 'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-7973162.pdf', 
 'epbg_percentage': None, 
 'ITEM CATEGORY': 'Goods Transport Service – Per Trip based Service - Open\nWater; Water Tank Truck; Heavy Tanker', 
 'ITEM DESCRIPTION': 'Goods Transport Service – Per Trip based Service - Open\nWater; Water Tank Truck; Heavy Tanker'}