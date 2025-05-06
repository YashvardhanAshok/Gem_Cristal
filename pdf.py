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
import ntpath
import re

extracted_data = []  
download_path= r'C:\vs_code\TenderHunter2.1.3\download_pdf\yes.pdf'

if os.path.exists(download_path):
    emd_amount = None
    epbg_percentage = None
    with pdfplumber.open(download_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()

            for section in tables:
                for row in section:
                    key = row[0]
                    value = row[1]
                    if key and 'EMD Amount' in key:
                        emd_amount = value
                    elif key and 'ePBG Percentage' in key:
                        epbg_percentage = value




if epbg_percentage!=None:
    print("ePBG Percentage(%):", epbg_percentage)

                        
print(extracted_data)