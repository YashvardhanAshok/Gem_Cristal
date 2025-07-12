
import pyodbc
import pandas as pd
import os
import pdfplumber
import re
import traceback
import json


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

def file_filler(file):
    tender_d =[]

    for tender in file:
        try:
            tender_id = tender[0]
            download_path = tender[1]
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

                        for page in pdf.pages:
                            try:
                                tables = page.extract_tables()
                                for table in tables:
                                    if not table or len(table) < 2: continue

                                    for row in table[1:]:
                                        if len(row) >= 2:
                                            key, value = row[0], row[1]
                                            
                                            try: 
                                                if ("MSE Purchase Preference" in key or "MSE Purchase Preference" in value) or \
                                                    ("MSE Exemption for Years Of Experience" in key or "MSE Exemption for Years Of Experience" in value):
                                                    MSE_value = value

                                            except: pass
                                            
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

                        
                        event_data={}
                        event_data["TENDER ID"] = tender_id
                        
                        
                        
                        event_data["elementPut"] = Organisation 
                        event_data["MINISTRY"] = Ministry_Name
                        event_data["DEPARTMENT"] = Department_Name
                        event_data["ORGANISATION"] = Organisation
                        
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
                        except:
                            pass
                        try:
                            event_data["QTY"] = Total_Quantity
                        except: pass
                        tender_d.append(event_data)
                        
                except:
                    print(f"Corrupt PDF removed. Re-downloading might help: {download_path}, tender_id;{tender_id}")
            
            else:
                print(f"ERORROROROROOROROROROROROROROROORORORR\nLink is not a downloadable file or not found: {download_path}, tender_id;{tender_id}")
        except:
            traceback.print_exc()
            print(f"Error downloading link for gem id: {download_path}, tender_id;{tender_id}")

    sql(tender_d)

import threading
def Main(item_list):
    try:
        
        threads = []
        
        max_threads = 5
        for elements in item_list: 
            print("elements: ",elements)
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                
                time.sleep(0.5)

            t = threading.Thread(target=file_filler, args=(elements,))
            t.start()
            threads.append(t)
                
    except:
        traceback.print_exc() 

raw_text = """  
GEM/2023/B/4129589
GEM/2023/B/3454760
GEM/2023/B/3205487
GEM/2021/B/1389120
GEM/2023/B/4339569
GEM/2022/B/2245408
GEM/2023/B/2995743
GEM/2023/B/3416695
GEM/2023/B/3390320
GEM/2023/B/3388048
GEM/2023/B/3329404
GEM/2023/B/3304192
GEM/2023/B/3250466
GEM/2023/B/3215293
GEM/2023/B/3045416
GEM/2023/B/3045356
GEM/2023/B/2984382
GEM/2022/B/2749770
GEM/2022/B/2757647
GEM/2022/B/2742576
GEM/2022/B/2592808
GEM/2022/B/2733623
GEM/2022/B/2718666
GEM/2022/B/2710849
GEM/2022/B/2673345
GEM/2022/B/2668634
GEM/2022/B/2657987
GEM/2022/B/2620321
GEM/2022/B/2623285
GEM/2022/B/2541525
GEM/2022/B/2514538
GEM/2022/B/2509375
GEM/2022/B/2503301
GEM/2022/B/2457912
GEM/2022/B/2372910
GEM/2022/B/2366031
GEM/2022/B/2302659
GEM/2022/B/2330822
GEM/2022/B/2229965
GEM/2022/B/2221335
GEM/2022/B/2159921
GEM/2022/B/2171350
GEM/2022/B/2164319
GEM/2022/B/2145897
GEM/2022/B/2145472
GEM/2022/B/2127315
GEM/2022/B/2038040
GEM/2022/B/2106346
GEM/2022/B/2090722
GEM/2022/B/2051345
GEM/2022/B/2041968
GEM/2022/B/2003257
GEM/2022/B/1969616
GEM/2022/B/1945112
GEM/2022/B/1913382
GEM/2022/B/1899752
GEM/2022/B/1880063
GEM/2022/B/1850373
GEM/2021/B/1816896
GEM/2021/B/1790428
GEM/2021/B/1768945
GEM/2021/B/1783368
GEM/2021/B/1785756
GEM/2021/B/1788131
GEM/2021/B/1746447
GEM/2021/B/1704221
GEM/2021/B/1650516
GEM/2021/B/1659117
GEM/2021/B/1601182
GEM/2021/B/1644067
GEM/2021/B/1623763
GEM/2021/B/1634682
GEM/2021/B/1630550
GEM/2021/B/1529585
GEM/2021/B/1610168
GEM/2021/B/1575516
GEM/2021/B/1551458
GEM/2021/B/1490570
GEM/2021/B/1556101
GEM/2021/B/1508236
GEM/2021/B/1494767
GEM/2021/B/1480138
GEM/2021/B/1473912
GEM/2021/B/1398924
GEM/2021/B/1423184
GEM/2021/B/1413128
GEM/2021/B/1413101
GEM/2021/B/1407046
GEM/2021/B/1375859
GEM/2021/B/1376813
GEM/2021/B/1340719
GEM/2021/B/1334398
GEM/2021/B/1331390
GEM/2021/B/1313377
GEM/2021/B/1304527
GEM/2021/B/1311278
GEM/2021/B/1288851
GEM/2021/B/1277351
GEM/2021/RA/77898
GEM/2021/B/1252359
GEM/2021/B/1249940
GEM/2021/RA/76719
GEM/2021/B/1216195
GEM/2021/B/1203110
GEM/2021/B/1214178
GEM/2021/B/1217558
GEM/2021/B/1197264
GEM/2021/B/1191335
GEM/2021/B/1185265
GEM/2021/B/1176488
GEM/2021/B/1176489
GEM/2021/B/1176114
GEM/2021/B/1171649
GEM/2021/RA/73291
GEM/2021/B/1157459
GEM/2021/B/1156859
GEM/2021/B/1153416
GEM/2021/B/1135234
GEM/2021/B/1145349
GEM/2021/B/1117226
GEM/2021/B/1115671
GEM/2021/B/1070276
GEM/2021/B/1063477
GEM/2021/B/1061165
GEM/2021/B/988833
GEM/2021/B/989122
GEM/2020/B/905971
GEM/2020/B/909219
GEM/2020/RA/51595
GEM/2020/B/867984
GEM/2020/B/853061
GEM/2020/B/843805
GEM/2020/B/836436
GEM/2020/B/813073
GEM/2020/B/788571
GEM/2020/B/768314
GEM/2020/B/771237
GEM/2020/B/760574
GEM/2020/B/718329
GEM/2020/B/688224
GEM/2020/B/699792
GEM/2020/B/680766
GEM/2020/B/657053
GEM/2020/B/637956
GEM/2020/B/589323
GEM/2020/B/627303
GEM/2020/B/627220
GEM/2020/B/620281
GEM/2020/B/615201
GEM/2020/B/599869
GEM/2020/B/602659
GEM/2020/B/573680
GEM/2020/B/560479
GEM/2020/B/544014
GEM/2020/B/548422
GEM/2020/B/555235
GEM/2020/B/545485
GEM/2020/B/543240
GEM/2020/B/533861
GEM/2019/B/466673
GEM/2019/B/443614
GEM/2019/B/443610
GEM/2019/B/461127
GEM/2019/B/451690
GEM/2019/B/442671
GEM/2019/B/406587
GEM/2019/RA/22058
GEM/2019/B/368367
GEM/2019/B/373130
GEM/2019/B/357823
GEM/2019/B/346918
GEM/2019/B/306185
GEM/2019/RA/12080
GEM/2019/B/288241
GEM/2019/B/280437
GEM/2019/B/272792
GEM/2019/B/272765
GEM/2019/B/272772
GEM/2019/B/272813
GEM/2019/B/272806
GEM/2019/B/262992
GEM/2019/B/224881
GEM/2019/B/224864
GEM/2019/B/208303
GEM/2019/B/198105
GEM/2019/B/196214
GEM/2020/B/516476
GEM/2019/B/472906
GEM/2020/B/506175
GEM/2024/B/4649797
GEM/2024/B/4649697
GEM/2023/B/4094891
GEM/2019/B/387610
GEM/2022/B/2652563
GEM/2025/B/6325701
GEM/2025/B/6373810
GEM/2025/B/6373850
GEM/2025/B/6348573
GEM/2025/B/6367667
GEM/2025/B/6371349
GEM/2025/B/6363964
GEM/2025/B/6365440
GEM/2025/B/6365378
GEM/2025/B/6365571
GEM/2025/B/6364533
GEM/2025/B/6364336
GEM/2025/B/6364301
GEM/2025/B/6367185
GEM/2025/B/6367146
GEM/2025/B/6364093
GEM/2025/B/6364070
GEM/2025/B/6364126
GEM/2025/B/6364137
GEM/2025/B/6350947
GEM/2025/B/6343967
GEM/2025/B/6339410
GEM/2025/B/6297575
GEM/2025/B/6210721
GEM/2025/B/6347599
GEM/2025/B/6355265
GEM/2025/B/6355273
GEM/2025/B/6355244
GEM/2025/B/6355258
GEM/2025/B/6355254
GEM/2025/B/6325739
GEM/2025/B/6325692
GEM/2025/B/6350983
GEM/2025/B/6327636
GEM/2025/B/6350457
GEM/2025/B/6346926
GEM/2025/B/6346927
GEM/2025/B/6346971
GEM/2025/B/6346964
GEM/2025/B/6346961
GEM/2025/B/6346967
GEM/2025/B/6346541
GEM/2025/B/6346542
GEM/2025/B/6346534
GEM/2025/B/6346525
GEM/2025/B/6286565
GEM/2025/B/6346521
GEM/2025/B/6270342
GEM/2025/B/6330309
GEM/2025/B/6330285
GEM/2025/B/6330294
GEM/2025/B/6343842
GEM/2025/B/6330329
GEM/2025/B/6343848
GEM/2025/B/6330277
GEM/2025/B/6327498
GEM/2025/B/6338093
GEM/2025/B/6338221
GEM/2025/B/6330475
GEM/2025/B/6337279
GEM/2025/B/6328617
GEM/2025/B/6330483
GEM/2025/B/6345263
GEM/2025/B/6327723
GEM/2025/B/6343917
GEM/2025/B/6343656
GEM/2025/B/6343643
GEM/2025/B/6338565
GEM/2025/B/6338462
GEM/2025/B/6338997
GEM/2025/B/6338722
GEM/2025/B/6308706
GEM/2025/B/6338349
GEM/2025/B/6338409
GEM/2025/B/6338668
GEM/2025/B/6338468
GEM/2025/B/6338624
GEM/2025/B/6338281
GEM/2025/B/6338568
GEM/2025/B/6337743
GEM/2025/B/6341856
GEM/2025/B/6338187
GEM/2025/B/6337998
GEM/2025/B/6343077
GEM/2025/B/6342991
GEM/2025/B/5859933
GEM/2025/B/5860015
GEM/2025/B/5859979
GEM/2025/B/6341759
GEM/2025/B/6326854
GEM/2025/B/6331492
GEM/2025/B/6331454
GEM/2025/B/6331372
GEM/2025/B/6330851
GEM/2025/B/6330228
GEM/2025/B/6150509
GEM/2025/B/6326816
GEM/2025/B/6326696
GEM/2025/B/6326158
GEM/2025/B/6245203
GEM/2025/B/6326539
GEM/2025/B/6318797
GEM/2025/B/6324040
GEM/2025/B/6324486
GEM/2025/B/6324397
GEM/2025/B/6324532
GEM/2025/B/6324109
GEM/2025/B/6324358
GEM/2025/B/6323892
GEM/2025/B/6323765
GEM/2025/B/6324158
GEM/2025/B/6299789
GEM/2025/B/6324451
GEM/2025/B/6316050
GEM/2025/B/6315983
GEM/2025/B/6320412
GEM/2025/B/6320190
GEM/2025/B/6299504
GEM/2025/B/6299566
GEM/2025/B/6312781
GEM/2025/B/6312806
GEM/2025/B/6312817
GEM/2025/B/6312840
GEM/2025/B/6312918
GEM/2025/B/6312789
GEM/2025/B/6321367
GEM/2025/B/6308426
GEM/2025/B/6308338
GEM/2025/B/6315587
GEM/2025/B/6297405
GEM/2025/B/6285507
GEM/2025/B/6297419
GEM/2025/B/6097683
GEM/2025/B/6097684
GEM/2025/B/6097665
GEM/2025/B/6097675
GEM/2025/B/6315824
GEM/2025/B/6279142
GEM/2025/B/6319464
GEM/2025/B/6319807
GEM/2025/B/6308544
GEM/2025/B/6308594
GEM/2025/B/6315630
GEM/2025/B/6259344
GEM/2025/B/6311071
GEM/2025/B/6302375
GEM/2025/B/6315341
GEM/2025/B/6301215
GEM/2025/B/6301865
GEM/2025/B/6301875
GEM/2025/B/6312337
GEM/2025/B/6315132
GEM/2025/B/6319789
GEM/2025/B/6283502
GEM/2025/B/6302947
GEM/2025/B/6307370
GEM/2025/B/6310808
GEM/2025/B/6307862
GEM/2025/B/6102270
GEM/2025/B/6307577
GEM/2025/B/6303018
GEM/2025/B/6304274
GEM/2025/B/6304719
GEM/2025/B/6305498
GEM/2025/B/6305302
GEM/2025/B/6305622
GEM/2025/B/6304396
GEM/2025/B/6304512
GEM/2025/B/6304554
GEM/2025/B/6306479
GEM/2025/B/6301361
GEM/2025/B/6297532
GEM/2025/B/6297528
GEM/2025/B/6280782
GEM/2025/B/6298021
GEM/2025/B/6298029
GEM/2025/B/6298026
GEM/2025/B/6299685
GEM/2025/B/6297932
GEM/2025/B/6297919
GEM/2025/B/6300848
GEM/2025/B/6297921
GEM/2025/B/6297463
GEM/2025/B/6297460
GEM/2025/B/6270372
GEM/2025/B/6295150
GEM/2025/B/6262748
GEM/2025/B/6294431
GEM/2025/B/6294434
GEM/2025/B/6294413
GEM/2025/B/6294421
GEM/2025/B/6242514
GEM/2025/B/6242462
GEM/2025/B/6271680
GEM/2025/B/6295801
GEM/2025/B/6262261
GEM/2025/B/6262289
GEM/2025/B/6262357
GEM/2025/B/6118853
GEM/2025/B/6152117
GEM/2025/B/6227307
GEM/2025/B/6269605
GEM/2025/B/6227576
GEM/2025/B/6294599
GEM/2025/B/6227191
GEM/2025/B/6152167
GEM/2025/B/6269612
GEM/2025/B/6269618
GEM/2025/B/6286385
GEM/2025/B/6277079
GEM/2025/B/6272478
GEM/2025/B/6272482
GEM/2025/B/6273130
GEM/2025/B/6284996
GEM/2025/B/6284970
GEM/2025/B/6283529
GEM/2025/B/6281914
GEM/2025/B/6276710
GEM/2025/B/6276770
GEM/2025/B/6275091
GEM/2025/B/6289637
GEM/2025/B/6276565
GEM/2025/B/6276550
GEM/2025/B/6282219
GEM/2025/B/6276136
GEM/2025/B/6260167
GEM/2025/B/6260163
GEM/2025/B/6283299
GEM/2025/B/6283475
GEM/2025/B/6283443
GEM/2025/B/6062049
GEM/2025/B/6279715
GEM/2025/B/6281284
GEM/2025/B/6259895
GEM/2025/B/6279281
GEM/2025/B/6062097
GEM/2025/B/6275130
GEM/2025/B/6275002
GEM/2025/B/6275060
GEM/2025/B/6173089
GEM/2025/B/6221366
GEM/2025/B/6272740
GEM/2025/B/6272715
GEM/2025/B/6272522
GEM/2025/B/6272054
GEM/2025/B/6272641
GEM/2025/B/6272375
GEM/2025/B/6271691
GEM/2025/B/6271678
GEM/2025/B/6271412
GEM/2025/B/6272341
GEM/2025/B/6272340
GEM/2025/B/6272353
GEM/2025/B/6272339
GEM/2025/B/6272041
GEM/2025/B/6271141
GEM/2025/B/6271128
GEM/2025/B/6271089
GEM/2025/B/6272358
GEM/2025/B/6264839
GEM/2025/B/6264836
GEM/2025/B/6242636
GEM/2025/B/6272450
GEM/2025/B/6272547
GEM/2025/B/6272447
GEM/2025/B/6272546
GEM/2025/B/6244433
GEM/2025/B/6244480
GEM/2025/B/6244453
GEM/2025/B/6244565
GEM/2025/B/6252821
GEM/2025/B/6235650
GEM/2025/B/6270721
GEM/2025/B/6191103
GEM/2025/B/6191112
GEM/2025/B/6269586
GEM/2025/B/6269611
GEM/2025/B/6269603
GEM/2025/B/6269599
GEM/2025/B/6260116
GEM/2025/B/6260108
GEM/2025/B/6260102
GEM/2025/B/6268889
GEM/2025/B/6138439
GEM/2025/B/6266566
GEM/2025/B/6268920
GEM/2025/B/6269003
GEM/2025/B/6262847
GEM/2025/B/6262433
GEM/2025/B/6145401
GEM/2025/B/6265047
GEM/2025/B/6160490
GEM/2025/B/6262406
GEM/2025/B/6260113
GEM/2025/B/6256918
GEM/2025/B/6261822
GEM/2025/B/6254859
GEM/2025/B/6256330
GEM/2025/B/6260181
GEM/2025/B/6260185
GEM/2025/B/6256291
GEM/2025/B/6262561
GEM/2025/B/6266875
GEM/2025/B/6256659
GEM/2025/B/6268778
GEM/2025/B/6254012
GEM/2025/B/6260372
GEM/2025/B/6260367
GEM/2025/B/6260497
GEM/2025/B/6260531
GEM/2025/B/6261770
GEM/2025/B/6256876
GEM/2025/B/6235875
GEM/2025/B/6262029
GEM/2025/B/6269392
GEM/2025/B/6269374
GEM/2025/B/6242274
GEM/2025/B/6242270
GEM/2025/B/6269353
GEM/2025/B/6260754
GEM/2025/B/6260323
GEM/2025/B/6260313
GEM/2025/B/6269519
GEM/2025/B/6256181
GEM/2025/B/6256276
GEM/2025/B/6259276
GEM/2025/B/6259230
GEM/2025/B/6253716
GEM/2025/B/6253759
GEM/2025/B/6253907
GEM/2025/B/6253837
GEM/2025/B/6255318
GEM/2025/B/6255344
GEM/2025/B/6160549
GEM/2025/B/6145400
GEM/2025/B/6250576
GEM/2025/B/6250566
GEM/2025/B/6255863
GEM/2025/B/6258393
GEM/2025/B/6255958
GEM/2025/B/6260025
GEM/2025/B/6258717
GEM/2025/B/6256074
GEM/2025/B/6256221
GEM/2025/B/6256155
GEM/2025/B/6250308
GEM/2025/B/6250329
GEM/2025/B/6253294
GEM/2025/B/6244198
GEM/2025/B/6242356
GEM/2025/B/6201496
GEM/2025/B/6250271
GEM/2025/B/6245443
GEM/2025/B/6250250
GEM/2025/B/6249612
GEM/2025/B/6172426
GEM/2025/B/6249022
GEM/2025/B/6246216
GEM/2025/B/6248179
GEM/2025/B/6248218
GEM/2025/B/6187801
GEM/2025/B/6187823
GEM/2025/B/6187810
GEM/2025/B/6245946
GEM/2025/B/6245938
GEM/2025/B/6245941
GEM/2025/B/6245950
GEM/2025/B/6245919
GEM/2025/B/6245913
GEM/2025/B/6232795
GEM/2025/B/6245293
GEM/2025/B/6199380
GEM/2025/B/6237397
GEM/2025/B/6232801
GEM/2025/B/6244079
GEM/2025/B/6244270
GEM/2025/B/6244068
GEM/2025/B/6244094
GEM/2025/B/6237423
GEM/2025/B/6235052
GEM/2025/B/6116149
GEM/2025/B/6116167
GEM/2025/B/6116127
GEM/2025/B/6141578
GEM/2025/B/6116211
GEM/2025/B/6116196
GEM/2025/B/6116231
GEM/2025/B/6227046
GEM/2025/B/6216223
GEM/2025/B/6230604
GEM/2025/B/6177701
GEM/2025/B/6177891
GEM/2025/B/6214164
GEM/2025/B/6153456
GEM/2025/B/6143324
GEM/2025/B/6222785
GEM/2025/B/6208414
GEM/2025/B/6208404
GEM/2025/B/6208403
GEM/2025/B/6185821
GEM/2025/B/6213934
GEM/2025/B/6213905
GEM/2025/B/6213923
GEM/2025/B/6211120
GEM/2025/B/6211179
GEM/2025/B/6131824
GEM/2025/B/6197138
GEM/2025/B/6189145
GEM/2025/B/6189150
GEM/2025/B/6189159
GEM/2025/B/6205775
GEM/2025/B/6185909
GEM/2025/B/6210503
GEM/2025/B/6191233
GEM/2025/B/6189286
GEM/2025/B/6205778
GEM/2025/B/6214949
GEM/2025/B/6206928
GEM/2025/B/6197643
GEM/2025/B/6197639
GEM/2025/B/6196207
GEM/2025/B/6173147
GEM/2025/B/6173162
GEM/2025/B/6173173
GEM/2025/B/6173159
GEM/2025/B/6182145
GEM/2025/B/6150228
GEM/2025/B/6191061
GEM/2025/B/6191067
GEM/2025/B/6121844
GEM/2025/B/6184153
GEM/2025/B/6175486
GEM/2025/B/6137187
GEM/2025/B/6175490
GEM/2025/B/6199875
GEM/2025/B/6199793
GEM/2025/B/6179549
GEM/2025/B/6154773
GEM/2025/B/6179541
GEM/2025/B/6193832
GEM/2025/B/6193823
GEM/2025/B/6188672
GEM/2025/B/6184131
GEM/2025/B/6166876
GEM/2025/B/6191458
GEM/2025/B/6188394
GEM/2025/B/6188453
GEM/2025/B/6188480
GEM/2025/B/6135819
GEM/2025/B/6122150
GEM/2025/B/6181907
GEM/2025/B/6181893
GEM/2025/B/6153108
GEM/2025/B/6098019
GEM/2025/B/6185134
GEM/2025/B/6187701
GEM/2025/B/6187711
GEM/2025/B/6187691
GEM/2025/B/6191501
GEM/2025/B/6191051
GEM/2025/B/6184467
GEM/2025/B/6165511
GEM/2025/B/6135401
GEM/2025/B/6176106
GEM/2025/B/6176104
GEM/2025/B/6163331
GEM/2025/B/6138834
GEM/2025/B/6176096
GEM/2025/B/6176094
GEM/2025/B/6176091
GEM/2025/B/6176086
GEM/2025/B/6176100
GEM/2025/B/6176087
GEM/2025/B/6176101
GEM/2025/B/6176083
GEM/2025/B/6176099
GEM/2025/B/6176102
GEM/2025/B/6176103
GEM/2025/B/6174552
GEM/2025/B/6174528
GEM/2025/B/6114001
GEM/2025/B/6161147
GEM/2025/B/6161161
GEM/2025/B/6174928
GEM/2025/B/6156621
GEM/2025/B/6156619
GEM/2025/B/6158129
GEM/2025/B/6149691
GEM/2025/B/6161200
GEM/2025/B/6161150
GEM/2025/B/6149697
GEM/2025/B/6161168
GEM/2025/B/6174554
GEM/2025/B/6167640
GEM/2025/B/6175530
GEM/2025/B/6167599
GEM/2025/B/6152775
GEM/2025/B/6161098
GEM/2025/B/6161588
GEM/2025/B/6150988
GEM/2025/B/6138444
GEM/2025/B/6138442
GEM/2025/B/6161585
GEM/2025/B/6141629
GEM/2025/B/6138541
GEM/2025/B/6138560
GEM/2025/B/6169616
GEM/2025/B/6169645
GEM/2025/B/6171608
GEM/2025/B/6171535
GEM/2025/B/6170019
GEM/2025/B/6164971
GEM/2025/B/6164976
GEM/2025/B/6138557
GEM/2025/B/6161134
GEM/2025/B/6161083
GEM/2025/B/6161120
GEM/2025/B/6161109
GEM/2025/B/6145392
GEM/2025/B/6145390
GEM/2025/B/6145387
GEM/2025/B/6160696
GEM/2025/B/6160707
GEM/2025/B/6160736
GEM/2025/B/6160724
GEM/2025/B/6163003
GEM/2025/B/6162970
GEM/2025/B/6163303
GEM/2025/B/6145394
GEM/2025/B/6145396
GEM/2025/B/6160905
GEM/2025/B/6160898
GEM/2025/B/6160875
GEM/2025/B/6160887
GEM/2025/B/6160867
GEM/2025/B/6164960
GEM/2025/B/6160853
GEM/2025/B/6160881
GEM/2025/B/6156860
GEM/2025/B/6158990
GEM/2025/B/6153560
GEM/2025/B/6156867
GEM/2025/B/6156777
GEM/2025/B/6147581
GEM/2025/B/6141687
GEM/2025/B/6156481
GEM/2025/B/6005391
GEM/2025/B/6005399
GEM/2025/B/6156478
GEM/2025/B/6140293
GEM/2025/B/6139620
GEM/2025/B/6140165
GEM/2025/B/6143385
GEM/2025/B/6144084
GEM/2025/B/6144090
GEM/2025/B/6152001
GEM/2025/B/6151983
GEM/2025/B/6150044
GEM/2025/B/6152880
GEM/2025/B/6152888
GEM/2025/B/6149394
GEM/2025/B/6150245
GEM/2025/B/6148611
GEM/2025/B/6149026
GEM/2025/B/6149063
GEM/2025/B/6148999
GEM/2025/B/6148927
GEM/2025/B/6148805
GEM/2025/B/6148752
GEM/2025/B/6148682
GEM/2025/B/6143814
GEM/2025/B/6145228
GEM/2025/B/6137943
GEM/2025/B/6143854
GEM/2025/B/6144198
GEM/2025/B/6123354
GEM/2025/B/6137964
GEM/2025/B/6137176
GEM/2025/B/6125804
GEM/2025/B/6135124
GEM/2025/B/6113435
GEM/2025/B/6113411
GEM/2025/B/6117260
GEM/2025/B/6103970
GEM/2025/B/5957068
GEM/2025/B/6101783
GEM/2025/B/6097701
GEM/2025/B/6074533
GEM/2025/B/6084478
GEM/2025/B/6074247
GEM/2025/B/6031295
GEM/2025/B/5943852
GEM/2025/B/5867128
GEM/2025/B/5830022
GEM/2025/B/5910030
GEM/2025/B/5910034
GEM/2025/B/5876605
GEM/2025/B/5876511
GEM/2025/B/5927709
GEM/2025/B/5927673
GEM/2025/B/5927693
GEM/2025/B/5927729
GEM/2025/B/5870442
GEM/2025/B/5920659
GEM/2025/B/5921030
GEM/2025/B/5919313
GEM/2025/B/5918101
GEM/2025/B/5919883
GEM/2025/B/5918742
GEM/2025/B/5919664
GEM/2025/B/5918449
GEM/2025/B/5920805
GEM/2025/B/5919119
GEM/2025/B/5920824
GEM/2025/B/5920787
GEM/2025/B/5917995
GEM/2025/B/5917904
GEM/2025/B/5919982
GEM/2025/B/5920050
GEM/2025/B/5919522
GEM/2025/B/5920816
GEM/2025/B/5920793
GEM/2025/B/5918267
GEM/2025/B/5907953
GEM/2025/B/5907946
GEM/2025/B/5907747
GEM/2025/B/5907781
GEM/2025/B/5907843
GEM/2025/B/5895237
GEM/2025/B/5907113
GEM/2025/B/5903673
GEM/2025/B/5895961
GEM/2025/B/5896196
GEM/2025/B/5896208
GEM/2025/B/5868366
GEM/2025/B/5896254
GEM/2025/B/5896258
GEM/2025/B/5897832
GEM/2025/B/5897954
GEM/2025/B/5897862
GEM/2025/B/5897940
GEM/2025/B/5894475
GEM/2025/B/5878452
GEM/2025/B/5869053
GEM/2025/B/5869068
GEM/2025/B/5866835
GEM/2025/B/5866814
GEM/2025/B/5866823
GEM/2025/B/5866820
GEM/2025/B/5866809
GEM/2025/B/5873344
GEM/2025/B/5873500
GEM/2025/B/5869136
GEM/2025/B/5861170
GEM/2025/B/5859377
GEM/2025/B/5856592
GEM/2025/B/5856766
GEM/2025/B/5856641
GEM/2025/B/5856810
GEM/2025/B/5856678
GEM/2025/B/5856728
GEM/2025/B/5861165
GEM/2025/B/5859331
GEM/2025/B/5863580
GEM/2025/B/5859258
GEM/2025/B/5859824
GEM/2025/B/5838589
GEM/2025/B/5818382
GEM/2025/B/5845657
GEM/2025/B/5845683
GEM/2025/B/5846306
GEM/2025/B/5839921
GEM/2025/B/5839908
GEM/2025/B/5839961
GEM/2025/B/5839948
GEM/2025/B/5839934
GEM/2025/B/5840022
GEM/2025/B/5840002
GEM/2025/B/5840009
GEM/2025/B/5839052
GEM/2025/B/5839046
GEM/2025/B/5839248
GEM/2025/B/5806029
GEM/2025/B/5839985
GEM/2025/B/5836885
GEM/2025/B/5832171
GEM/2025/B/5817156
GEM/2025/B/5816790
GEM/2025/B/5814219
GEM/2025/B/5783867
GEM/2025/B/5809267
GEM/2025/B/5802755
GEM/2025/B/5796293
GEM/2025/B/5792377
GEM/2024/B/5749202
GEM/2025/B/5780732
GEM/2025/B/5783019
GEM/2025/B/5782653
GEM/2025/B/5776734
GEM/2025/B/5776726
GEM/2024/B/5766608
GEM/2024/B/5739816
GEM/2024/B/5761033
GEM/2024/B/5757862
GEM/2024/B/5758853
GEM/2024/B/5716578
GEM/2024/B/5750787
GEM/2024/B/5752566
GEM/2024/B/5752697
GEM/2024/B/5747061
GEM/2024/B/5742341
GEM/2024/B/5692120
GEM/2024/B/5728869
GEM/2024/B/5718338
GEM/2024/B/5718834
GEM/2024/B/5718505
GEM/2024/B/5718448
GEM/2024/B/5718203
GEM/2024/B/5705453
GEM/2024/B/5697383
GEM/2024/B/5676749
GEM/2024/B/5669308
GEM/2024/B/5675946
GEM/2024/B/5646664
GEM/2024/B/5616863
GEM/2024/B/5575956
GEM/2024/B/5553321
GEM/2024/B/5557224
GEM/2024/B/5523458
GEM/2024/B/5544126
GEM/2024/B/5504844
GEM/2024/B/5484301
GEM/2024/B/5462252
GEM/2024/B/5481001
GEM/2024/B/5482721
GEM/2024/B/5482942
GEM/2024/B/5471889
GEM/2024/B/5419767
GEM/2024/B/5464196
GEM/2024/B/5461528
GEM/2024/B/5455975
GEM/2024/B/5449375
GEM/2024/B/5439461
GEM/2024/B/5441703
GEM/2024/B/5443903
GEM/2024/B/5441114
GEM/2024/B/5437953
GEM/2024/B/5413660
GEM/2024/B/5426169
GEM/2024/B/5423439
GEM/2024/B/5420040
GEM/2024/B/5420789
GEM/2024/B/5330044
GEM/2024/B/5329979
GEM/2024/B/5404010
GEM/2024/B/5400836
GEM/2024/B/5398566
GEM/2024/B/5398609
GEM/2024/B/5398536
GEM/2024/B/5397977
GEM/2024/B/5398214
GEM/2024/B/5398295
GEM/2024/B/5398369
GEM/2024/B/5398494
GEM/2024/B/5384344
GEM/2024/B/5172252
GEM/2024/B/5367522
GEM/2024/B/5364167
GEM/2024/B/5364842
GEM/2024/B/5361749
GEM/2024/B/5348887
GEM/2024/B/5348880
GEM/2024/B/5348900
GEM/2024/B/5325556
GEM/2024/B/5348873
GEM/2024/B/5240545
GEM/2024/B/5152375
GEM/2024/B/5344624
GEM/2024/B/5326235
GEM/2024/B/5306938
GEM/2024/B/5312234
GEM/2024/B/5268505
GEM/2024/B/5268964
GEM/2024/B/5269127
GEM/2024/B/5269151
GEM/2024/B/5269072
GEM/2024/B/5278142
GEM/2024/B/5268768
GEM/2024/B/5269201
GEM/2024/B/5248172
GEM/2024/B/5269255
GEM/2024/B/5269231
GEM/2024/B/5284874
GEM/2024/B/5276729
GEM/2024/B/5259508
GEM/2024/B/4579207
GEM/2024/B/5241702
GEM/2024/B/5277514
GEM/2024/B/5241031
GEM/2024/B/5271523
GEM/2024/B/5266866
GEM/2024/B/5253864
GEM/2024/B/5111126
GEM/2024/B/5238905
GEM/2024/B/5231882
GEM/2024/B/5216701
GEM/2024/B/5194357
GEM/2024/B/5217143
GEM/2024/B/5211930
GEM/2024/B/5208923
GEM/2024/B/5135933
GEM/2024/B/5188762
GEM/2024/B/5178925
GEM/2024/B/5184304
GEM/2024/B/5176239
GEM/2024/B/5176108
GEM/2024/B/5176458
GEM/2024/B/5176353
GEM/2024/B/5138962
GEM/2024/B/5134573
GEM/2024/B/5160570
GEM/2024/B/5132860
GEM/2024/B/5152475
GEM/2024/B/5107873
GEM/2024/B/5138514
GEM/2024/B/5139610
GEM/2024/B/5132661
GEM/2024/B/5132958
GEM/2024/B/5107429
GEM/2024/B/5106362
GEM/2024/B/5127407
GEM/2024/B/5101075
GEM/2024/B/5122847
GEM/2024/B/5107501
GEM/2024/B/5095372
GEM/2024/B/5046487
GEM/2024/B/5057957
GEM/2024/B/5070475
GEM/2024/B/5064677
GEM/2024/B/5063905
GEM/2024/B/5045782
GEM/2024/B/5015612
GEM/2024/B/4770603
GEM/2024/B/4724816
GEM/2024/B/4480000
GEM/2024/B/4675418
GEM/2024/B/4612674
GEM/2023/B/4138933
GEM/2024/B/4609976
GEM/2024/B/4602792
GEM/2024/B/4581756
GEM/2024/B/4575756
GEM/2024/B/4570113
GEM/2024/B/4571008
GEM/2024/B/4454519
GEM/2024/B/4433009
GEM/2023/B/4379224
GEM/2023/B/4379399
GEM/2023/B/4363336
GEM/2023/B/4182900
GEM/2023/B/4355697
GEM/2023/B/4319997
GEM/2023/B/4261770
GEM/2023/B/4213087
GEM/2023/B/4127798
GEM/2023/B/4045709
GEM/2023/B/4078917
GEM/2023/B/4053756
GEM/2023/B/4024682
GEM/2023/B/4006462
GEM/2023/B/3865893
GEM/2023/B/3756310
GEM/2023/B/3762276
GEM/2023/B/3763291
GEM/2023/B/3714528
GEM/2023/B/3752872
GEM/2023/B/3722699
GEM/2023/B/3703328
GEM/2023/B/3689264
GEM/2023/B/3681748
GEM/2023/B/3649447
GEM/2023/B/3566441
GEM/2023/B/3612779
GEM/2023/B/3520194
GEM/2023/B/3479343
GEM/2023/B/3324641
GEM/2021/RA/74044
GEM/2023/B/4095596
GEM/2025/B/5992674
GEM/2025/B/6140243
GEM/2025/B/6140216
GEM/2025/B/6140191
GEM/2025/B/6140280
GEM/2025/B/6139500
GEM/2025/B/6140268
GEM/2025/B/6156884
GEM/2025/B/6140255
GEM/2025/B/6150556
GEM/2025/B/6152975
GEM/2025/B/6150689
GEM/2025/B/6150700
GEM/2025/B/6145782
GEM/2025/B/6146988
GEM/2025/B/6145882
GEM/2025/B/6145825
GEM/2025/B/6145865
GEM/2025/B/6145847
GEM/2025/B/6147046
GEM/2025/B/6145804
GEM/2025/B/6137325
GEM/2025/B/6138817
GEM/2025/B/6138814
GEM/2025/B/6138804
GEM/2025/B/6138141
GEM/2025/B/6138508
GEM/2025/B/6138505
GEM/2025/B/6081549
GEM/2025/B/6137712
GEM/2025/B/6100253
GEM/2025/B/6100255
GEM/2025/B/6100259
GEM/2025/B/6100345
GEM/2025/B/6100264
GEM/2025/B/6100258
GEM/2025/B/6100261
GEM/2025/B/6111115
GEM/2025/B/6117284
GEM/2025/B/6137721
GEM/2025/B/6137717
GEM/2025/B/6114756
GEM/2025/B/6137555
GEM/2025/B/6137551
GEM/2025/B/6137559
GEM/2025/B/6136647
GEM/2025/B/6137420
GEM/2025/B/6137423
GEM/2025/B/6137417
GEM/2025/B/6137426
GEM/2025/B/6137444
GEM/2025/B/6111832
GEM/2025/B/6111754
GEM/2025/B/6135894
GEM/2025/B/6135856
GEM/2025/B/6135874
GEM/2025/B/6136844
GEM/2025/B/6101270
GEM/2025/B/6131094
GEM/2025/B/6101272
GEM/2025/B/6101273
GEM/2025/B/6131059
GEM/2025/B/5976222
GEM/2025/B/5976144
GEM/2025/B/6118406
GEM/2025/B/6130848
GEM/2025/B/6109269
GEM/2025/B/6119062
GEM/2025/B/6119087
GEM/2025/B/6119040
GEM/2025/B/6127451
GEM/2025/B/6129452
GEM/2025/B/6125592
GEM/2025/B/6125597
GEM/2025/B/6129449
GEM/2025/B/6113737
GEM/2025/B/6117387
GEM/2025/B/6127504
GEM/2025/B/6098370
GEM/2025/B/6098362
GEM/2025/B/6109302
GEM/2025/B/6109305
GEM/2025/B/6107625
GEM/2025/B/6107622
GEM/2025/B/6103968
GEM/2025/B/6120567
GEM/2025/B/6120097
GEM/2025/B/6099193
GEM/2025/B/6099142
GEM/2025/B/6117237
GEM/2025/B/6117251
GEM/2025/B/6117240
GEM/2025/B/6117241
GEM/2025/B/6117319
GEM/2025/B/6116852
GEM/2025/B/6116841
GEM/2025/B/6099148
GEM/2025/B/6115356
GEM/2025/B/6116059
GEM/2025/B/6114668
GEM/2025/B/6115331
GEM/2025/B/6115376
GEM/2025/B/6110765
GEM/2025/B/6111057
GEM/2025/B/6094647
GEM/2025/B/6110498
GEM/2025/B/6110374
GEM/2025/B/6110742
GEM/2025/B/6110477
GEM/2025/B/6110409
GEM/2025/B/6110328
GEM/2025/B/6110519
GEM/2025/B/6110776
GEM/2025/B/6099470
GEM/2025/B/6079114
GEM/2025/B/6081193
GEM/2025/B/6073352
GEM/2025/B/6091101
GEM/2025/B/6091060
GEM/2025/B/6091130
GEM/2025/B/6091112
GEM/2025/B/6091132
GEM/2025/B/6091109
GEM/2025/B/6091097
GEM/2025/B/6091038
GEM/2025/B/6091138
GEM/2025/B/6091120
GEM/2025/B/6091072
GEM/2025/B/6091082
GEM/2025/B/6091117
GEM/2025/B/6091125
GEM/2025/B/6067704
GEM/2025/B/6101404
GEM/2025/B/6101432
GEM/2025/B/6040345
GEM/2025/B/6040342
GEM/2025/B/6100968
GEM/2025/B/6089547
GEM/2025/B/6089583
GEM/2025/B/6097713
GEM/2025/B/6098215
GEM/2025/B/6098082
GEM/2025/B/6098074
GEM/2025/B/6097829
GEM/2025/B/6097836
GEM/2025/B/6097835
GEM/2025/B/6098212
GEM/2025/B/6089613
GEM/2025/B/6091568
GEM/2025/B/6091546
GEM/2025/B/6097681
GEM/2025/B/6097694
GEM/2025/B/6073378
GEM/2025/B/6070021
GEM/2025/B/6079043
GEM/2025/B/6080113
GEM/2025/B/6081121
GEM/2025/B/6081119
GEM/2025/B/6069511
GEM/2025/B/6069479
GEM/2025/B/6069500
GEM/2025/B/6081120
GEM/2025/B/6072128
GEM/2025/B/6079311
GEM/2025/B/6072862
GEM/2025/B/6072501
GEM/2025/B/6078598
GEM/2025/B/6072791
GEM/2025/B/6072839
GEM/2025/B/6073832
GEM/2025/B/6068103
GEM/2025/B/6072328
GEM/2025/B/6053104
GEM/2025/B/6045232
GEM/2025/B/6066001
GEM/2025/B/6067063
GEM/2025/B/6048002
GEM/2025/B/6055066
GEM/2025/B/6067203
GEM/2025/B/6067231
GEM/2025/B/6063968
GEM/2025/B/6062571
GEM/2025/B/6004949
GEM/2025/B/6057119
GEM/2025/B/6055798
GEM/2025/B/6055797
GEM/2025/B/6055794
GEM/2025/B/6055812
GEM/2025/B/6004718
GEM/2025/B/6045517
GEM/2025/B/6056963
GEM/2025/B/6040449
GEM/2025/B/6052523
GEM/2025/B/6052852
GEM/2025/B/6050370
GEM/2025/B/6050311
GEM/2025/B/6050338
GEM/2025/B/6050887
GEM/2025/B/6050660
GEM/2025/B/6043639
GEM/2025/B/6056154
GEM/2025/B/6031890
GEM/2025/B/6031895
GEM/2025/B/6017832
GEM/2025/B/6021939
GEM/2025/B/6021935
GEM/2025/B/6038550
GEM/2025/B/6040021
GEM/2025/B/6022237
GEM/2025/B/6038675
GEM/2025/B/6039749
GEM/2025/B/6035136
GEM/2025/B/6030771
GEM/2025/B/6027200
GEM/2025/B/6025143
GEM/2025/B/6029827
GEM/2025/B/6029802
GEM/2025/B/6029717
GEM/2025/B/6025125
GEM/2025/B/6022812
GEM/2025/B/6024350
GEM/2025/B/6021590
GEM/2025/B/6021606
GEM/2025/B/6009468
GEM/2025/B/5982007
GEM/2025/B/5941788
GEM/2025/B/6020203
GEM/2025/B/6013133
GEM/2025/B/5986987
GEM/2025/B/6014579
GEM/2025/B/6015106
GEM/2025/B/6016709
GEM/2025/B/6012796
GEM/2025/B/6012801
GEM/2025/B/6004217
GEM/2025/B/6002013
GEM/2025/B/5991009
GEM/2025/B/5991178
GEM/2025/B/6010523
GEM/2025/B/5991288
GEM/2025/B/6011036
GEM/2025/B/6020446
GEM/2025/B/6016837
GEM/2025/B/6005843
GEM/2025/B/6007524
GEM/2025/B/5890680
GEM/2025/B/5890622
GEM/2025/B/5890739
GEM/2025/B/5890785
GEM/2025/B/5890711
GEM/2025/B/5890764
GEM/2025/B/5890653
GEM/2025/B/5999401
GEM/2025/B/5971086
GEM/2024/B/5654700
GEM/2024/B/5654723
GEM/2025/B/5990456
GEM/2025/B/5974617
GEM/2025/B/5886246
GEM/2025/B/5963882
GEM/2025/B/5971679
GEM/2025/B/5971747
GEM/2025/B/5971723
GEM/2025/B/5971681
GEM/2025/B/5971732
GEM/2025/B/5971758
GEM/2025/B/5971630
GEM/2025/B/5971667
GEM/2025/B/5971648
GEM/2025/B/5971707
GEM/2025/B/5971845
GEM/2025/B/5957085
GEM/2025/B/5967091
GEM/2025/B/5967277
GEM/2025/B/5967621
GEM/2025/B/5968005
GEM/2025/B/5967036
GEM/2025/B/5967451
GEM/2025/B/5887622
GEM/2025/B/5964028
GEM/2025/B/5935016
GEM/2025/B/5935027
GEM/2025/B/5960361
GEM/2025/B/5961420
GEM/2025/B/5959514
GEM/2025/B/5958075
GEM/2025/B/5910029
GEM/2025/B/5956774
GEM/2025/B/5957762
GEM/2025/B/5956594
GEM/2025/B/5957855
GEM/2025/B/5939585
GEM/2025/B/5893984
GEM/2025/B/5917915
GEM/2025/B/5880737
GEM/2025/B/5839659
GEM/2025/B/5866828
GEM/2025/B/5866807
GEM/2025/B/5866808
GEM/2025/B/5866830
GEM/2025/B/5848334
GEM/2025/B/5866838
GEM/2025/B/5869230
GEM/2025/B/5859697
GEM/2025/B/5859756
GEM/2025/B/5859646
GEM/2025/B/5859570
GEM/2025/B/5861185
GEM/2025/B/5861188
GEM/2025/B/5861196
GEM/2025/B/5842906
GEM/2024/B/5714572
GEM/2024/B/5469983
GEM/2023/B/4222178
GEM/2023/B/3582301
GEM/2022/B/2668583
GEM/2021/B/1146390
GEM/2022/B/1917525
GEM/2025/B/6325716
GEM/2024/B/4774965
GEM/2021/B/1012920
GEM/2024/B/4574993
GEM/2024/B/4568027
GEM/2024/B/4482159
GEM/2023/B/4402670
GEM/2023/B/4393133
GEM/2023/B/4195529
GEM/2024/B/4443895
GEM/2023/B/4387464
GEM/2022/B/2533785
GEM/2024/B/4574129
GEM/2023/B/4125646
GEM/2023/B/3789891
GEM/2024/B/4520203
GEM/2024/B/4708246
GEM/2024/B/4714751
GEM/2023/B/3884369
GEM/2023/B/4123897
GEM/2023/B/4339460
GEM/2023/B/4144312
GEM/2023/B/4144326
GEM/2023/B/4053625
GEM/2023/B/3602846
GEM/2023/B/3351640
GEM/2023/B/3792040
GEM/2022/B/2466238
GEM/2024/B/4642845
GEM/2024/B/4635509
GEM/2025/B/6012631
GEM/2025/B/5946103

"""


tender_ids = raw_text.strip().split('\n')

tender_ids =["GEM/2025/B/5946103"]

formatted_ids = ",".join(f"'{tid}'" for tid in tender_ids)

# SQL Query
query = f'''
    SELECT tender_id, file_path
    FROM tender_data 
    WHERE tender_id IN ({formatted_ids})
'''



# Connect to the database
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

# Run the query
df = pd.read_sql(query, conn)


# Convert result to list of lists
result = df.values.tolist()


# tender_ids = split_into_parts(tender_ids, 5)
Main(result)



