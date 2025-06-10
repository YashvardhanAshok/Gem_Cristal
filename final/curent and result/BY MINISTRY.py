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


 
 

 
 
 

def gem_find(driver,card_elements , card, gem_ids, element,close_tender_id_list,gem_ids_copy):
    # scroll
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
    sleep(0.01)
    try:
        bid_title = card.find_element(By.CLASS_NAME, 'bid_no_hover')
        link_href = bid_title.get_attribute("href")

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

        except:
            quantity = 0

        try:
            department_div = card.find_element(By.CSS_SELECTOR, "div.col-md-5 > div:nth-child(2)")
            department_address = department_div.get_attribute('innerHTML')
            
            if isinstance(department_address, str) and "<br>" in department_address:
                department_address_parts = department_address.split("<br>")
            else:
                department_address_parts = [department_address, None]
                
        except:
            department_address_parts=[None,None]

        try:
            a_tag = card.find_element(By.CSS_SELECTOR, 'a[title][data-content]')
            title = a_tag.get_attribute("data-content")
        except:
            titles = []
            for card_element in card_elements:
                text = card_element.text
                if text.startswith(bid_title.text):
                    title = titles.append(text)

        if bid_title.text in gem_ids_copy:
            try: gem_ids.remove(bid_title.text)
            except: pass
            print(f"gem id skipped:{bid_title.text} and started at: {start_date}")
            return {"extended": today.strftime("%d-%b-%Y"),"DATE OF SEARCH": today.strftime("%d-%b-%Y"),"TENDER ID": bid_title.text,"END DATE": end_date,"END Time": end_date_time}
        elif bid_title.text in close_tender_id_list:
            print(f"--xx gem id {bid_title.text} extended xx--")
            return {"extended": today.strftime("%d-%b-%Y"),"DATE OF SEARCH": today.strftime("%d-%b-%Y"),"TENDER ID": bid_title.text,"END DATE": end_date,"END Time": end_date_time}

        print(f"New tender:{bid_title.text} and started at: {start_date}")

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

                # print(f"{bid_title.text} for: {download_path}")

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
        except:
            # traceback.print_exc()
            try:
                gem_ids.remove(bid_title.text)
            except:pass
            print(f"Error downloading link for gem id: {bid_title.text}")
    except:
        print(f"Error")
        traceback.print_exc()
        
        
        
def cancelled_fun(driver,gem_ids):
    Cancel_ids = [] 
    driver.get('https://bidplus.gem.gov.in/all-bids')


    def update_sql(gem_ids):
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        
        cursor = conn.cursor()
        update_query = """UPDATE tender_data SET Cancel = ? WHERE tender_id = ?"""
        
        for gem_id in gem_ids:
            cursor.execute(update_query, "Cancel", gem_id)
            conn.commit()
            print(f"{gem_id}: Cancel")
            
        cursor.close()
        conn.close()
    
    for gem_id in gem_ids:
        try:
            search = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'searchBid')))
            driver.execute_script("arguments[0].scrollIntoView(true);", search)
            sleep(0.5)
            search.clear()
            search.send_keys(gem_id)
            search.send_keys(Keys.RETURN)

            try:
                alerts = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.alert.alert-danger')))
                for alert in alerts:
                    print()
                    try:
                        if alert.text == "No data found":
                            Cancel_ids.append(gem_id) 
                    except: pass
            except: pass 

        except:
            # traceback.print_exc() 
            print(f"Search failed for {gem_id}")

    update_sql(Cancel_ids)

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

options = uc.ChromeOptions()
options.add_argument("--profile-directory=Default") 
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("--disable-blink-features=AutomationControlled")

gemlog_="gem_log.txt"

def gem_funtion(ministry_name, Organization_name):
    driver = uc.Chrome(options=options, headless=False)
    for org_name in Organization_name:

        driver.get('https://bidplus.gem.gov.in/advance-search')
        sleep(0.1)

        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )

        query_on = "SELECT * FROM tender_data WHERE department = ? AND live = 'Yes' AND (Cancel IS NULL OR Cancel = '')"
        query_close = "SELECT * FROM tender_data WHERE department = ? AND live = 'No'"

        df_on = pd.read_sql(query_on, conn, params=[org_name])
        df_close = pd.read_sql(query_close, conn, params=[org_name])
        conn.close()

        gem_ids = df_on['tender_id'].tolist()
        gem_ids_copy = gem_ids.copy()
        
        close_tender_id_list = df_close['tender_id'].tolist()
        
        ministry_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ministry-tab')))
        ministry_tab.click()
        sleep(5)
        
        ministry_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-ministry-container']")))
        
        ministry_dropdown.click()
        sleep(2)
        
        ministry_search__field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
        ministry_search__field.clear()
        
        ministry_search__field.send_keys(ministry_name)
        ministry_search__field.send_keys(Keys.RETURN)

        json_dir = os.path.join(os.getcwd(), 'db', 'json')
        os.makedirs(json_dir, exist_ok=True)

        sleep(2)



        extracted_data = []
        Organization_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-organization-container']"))
        )
        Organization_dropdown.click()
        Organization_search__field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'select2-search__field')))
        Organization_search__field.clear()
        Organization_search__field.send_keys(org_name)
        Organization_search__field.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(lambda d: d.execute_script("return typeof searchBid === 'function'"))
 
        driver.execute_script("searchBid('ministry-search')")
        
        card_count = 0 

        live_tenders = org_name + ":\n"
        try:
            for page_no in range(9999):
             
                try:
                    card_elements = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
                except: break

                for card in card_elements:
                    bid_title = card.find_element(By.CLASS_NAME, 'bid_no_hover')
                    live_tenders += str(card_count) + f". {bid_title.text}\n"
                    card_count += 1

                    try:
                        json_data = gem_find(driver, card_elements, card, gem_ids, org_name,close_tender_id_list,gem_ids_copy)
                        if json_data: extracted_data.append(json_data)
                    except: pass
                
                try:
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]")))
                    next_button.click()
                except: break
                      
        except:
            print(f"main loop brok for {ministry_name}: {org_name}") 
        
        

        
        with open('input_file.ext', 'a', encoding='utf-8') as outfile:
            outfile.write(live_tenders + '\n')
        
        try:
            product = [['2 V Solar Battery cells', '3D Multi Spectral Camo Vehicle Cover', '3D Printer', '3d Multi Spectral Camo Dress', 'A.C Static Meter', 'ALL Types of commercial Gym Equipment', 'AMC OF COMMERCIAL KITCHEN EQUIPMENT', 'AMC OF Gym EQUIPMENT', 'Ac static watthour meters-energy meter', 'Access Control Solutions', 'Air Freight Shipping', 'Air curtain', 'All Range Hospital Furniture', 'All Types of Commercial RO PLANTS', 'All Types of Wire and Cables',"Amc", 'Amc Of Ac', 'Amc Of Commercial Kitchen', 'Amc Of Fire Extinguishers', 'Amc Of Generators', 'Amc Of Gym Equipement', 'Amc Of Kitchen Equipement', 'Amc Of Lightning Arrestors', 'Amc Of Ro And IRP', 'Amc Of Solar Power Plant', 'Amc Of Solar Water Heaters', 'Amc Of Transformers', 'Amc of DG Sets and Transformer', 'AntI Drone system', 'Anti climb Fence', 'Automobile Batteries other batteries', 'Bain Marie', 'Bain marie', 'Barbed Wire', 'Battery', 'Body Worn Camera', 'Bola wrap Remote Restrain device', 'Braille Embosser', 'Bricks', 'Bucket Mop Wringer Trolly', 'Butter', 'CCTV', 'CEW',' Conducted Electrical Weapon', 'CGI Sheet', 'Cement','Chainlink Fence', 'Change over Switch', 'Chapati Warmer', 'Clip On Weapon Sites', 'Commercial Mixer', 'Commercial Vaccum Cleaner', 'Computer and peripherals', 'Construction Of Admin Blocks', 'Construction Of Hospital', 'Construction Of Internal Roads', 'Construction Of Klps For Defense', 'Convex Security Mirror', 'Cranes', 'Cyber Forensics Software', 'Cyber Security Solutions', 'DG SETS', 'Data Management solutions', 'Decorative Bollard', 'Decorative Street Light', 'Development Of Infrastructure For Defense', 'Development Of Sewerage Treatement Plant', 'Development Of Water Supply', 'Domestic casserole', 'Dough Kneader', 'Dough kneader 15kg', 'Dry Ration', 'Rice' , 'Pulses' , 'Sugar' , 'Coffee', 'Tea', 'Dustbin', 'Electric Fence', 'Electric Wires/Cable', 'Electric milk boiler', 'FRP', 'FRP Tank', 'Flood Light', 'Flooring', 'Forklifts', 'Fresh Fruits', 'Fresh Vegetable', 'Fuel Cell', 'Fuel cell genrators', 'GPS', 'GPS', 'Global Positioning System', 'Ghillie Suits', 'Ghilly Suit', 'Gi Pipe','Gyser', 'HHTI (Hand Held Thermal Imagers)', 'Hand Held Gas Detector', 'Hand held Thermal Imager', 'Handheld GPS', 'Hardware Item', 'Headphones', 'High Intensity Light Infrared beam', 'Honey Sucker / Sewer Cum Jetting Machine', 'Hybrid UPS', 'Idli Steamer', 'Incinerators', 'Inflatable Shelters', 'Inverters', 'JCB Bacholoader', 'Jet Spray', 'Jungle Boots', 'Kunda Gadi', 'LGSF Building', 'Large compartmental stainless steel tiffin', 'Led Bulbs', 'Less Lethal Weapons', 'Lighting Arrestor', 'Lightning Arrestor', 'Long Range Acoustic Hailing Device', 'Lorros', 'MCB', 'MCCB', 'Meat Cutting Machine', 'Mild Steel LPG Barbecues', 'Milk', 'Milk Boiler', 'Miltary Rain Poncho', 'Miniature Circuit Breaker Switches', 'Monitor', 'Multi Function Laser Aiming System', 'Nano Uav', 'New lpg cooking appliances', 'Oil', 'Online UPS', 'Outdoor Gym', 'Oven', 'PNVG', 'PPGI Sheets','Patient Bed Fowler', 'Patient Care Mattress', 'Picket Steel', 'Pickup Truck', 'Plotter', 'Plywood', 'Porta Cabin', 'Portable Kitchen', 'Portable houses', 'Poultry Product', 'Chicken', 'Egg' , 'Mutton', 'Ppgi Sheet', 'Prefab shelters with puf panel', 'Printer', 'Projector', 'Puff Cabin', 'Puff Shelter', 'Punched Tape concertina Coil PTCC', 'Reverse Osmosis', 'Remote Restraint Device', 'Rice Boiler', 'Rice boiler', 'Road Sweeping Machines', 'Robotics', 'Room Heater', 'Roti Making Machine', 'Roti Making Machine Auto matic', 'Rucksack Bags', 'SANITARY NAPKIN VENDING MACHINE', 'SS', 'SS Thermos', 'STP', 'Sewage Treatment Plants', 'Sand', 'Sanitary Items', 'Sanitary Napkins Incinetator Machine with Smoke ControlUnit', 'Satellite Tracker', 'Sea Food (Fish)', 'Search Light', 'Sedan ',' SUVS', 'Semi Automatic', 'Sewer Suction Machines', 'Shooting Range', 'Skid steer Loader', 'Software','Software Defined Radio', 'Solar Battery', 'Solar Lantern', 'Solar PV Panel','Solar Panel', 'Solar PV Plant', 'Solar Power Plant', 'Solar Street Light', 'Solar Street Light all Type', 'Solar Tublar Batteries', 'Solar Water Heater', 'Solar inverter', 'Solar water Heater', 'Solar water pump', 'Speakers', 'Street Light', 'Switch fuse unit', 'Tablet', 'Tandoor', 'Tandoor, Height 481-500 Millimeter', 'Tubes', 'UAV', 'Under Water Torch', 'Unmanned Aerial Vehicle', 'Vaccum Cleaner', 'Vegetable Cutter', 'Video Survelliance ',' Analytics Solutions', 'WTP', 'Walkie Talkie', 'Waste Management', 'Waste Management Plants', 'Water Bowser', 'Water Cooling', 'Water Dispenser', 'Water Tanker', 'Weapon Sight', 'Weapon Sites', 'Weapon Support system', 'Wet Grinder', 'Wheel Barrow', 'X-ray Machine', 'XLPE Cables', 'water cooler']]
            flat_products = [item.lower() for sublist in product for item in sublist]

            for item in extracted_data:
                title = item.get("ITEM DESCRIPTION", "").lower()
                matches = [prod for prod in flat_products if prod in title]
                item["matches"] = bool(matches)
                item["matched_products"] = matches
        
        except:
            print("error")
        sql(extracted_data)
        cancelled_fun(driver,gem_ids)

    driver.quit()

def gem():
    try:
        max_threads = 4
        threads = []

        MINISTRY_list = [
            ["MINISTRY OF DEFENCE", ["INDIAN ARMY"]],
            ["MINISTRY OF COMMUNICATIONS", ['']],
            ["MINISTRY OF HOUSING & URBAN AFFAIRS", ["HINDUSTAN STEELWORKS CONSTRUCTION LIMITED"]],
            ["MINISTRY OF POWER", ["NTPC LIMITED"]],
            ["MINISTRY OF HEALTH AND FAMILY WELFARE", ["HLL INFRA TECH SERVICES LIMITED"]],
            ["MINISTRY OF CIVIL AVIATION", ["AIRPORTS AUTHORITY OF INDIA"]],
            ["MINISTRY OF HOME AFFAIRS", ["NATIONAL SECURITY GUARD", "INDO TIBETAN BORDER POLICE", "NATIONAL DISASTER RESPONSE FORCE","SASHASTRA SEEMA BAL"]],
            ["MINISTRY OF HOME AFFAIRS", ["ASSAM RIFLES","CENTRAL RESERVE POLICE FORCE", "BORDER SECURITY FORCE","CENTRAL INDUSTRIAL SECURITY FORCE"]],
            ["MINISTRY OF WATER RESOURCES RIVER DEVELOPMENT AND GANGA REJUVENATION", ["NATIONAL PROJECTS CONSTRUCTION CORPORATION LIMITED"]],
            ["MINISTRY OF DEFENCE", ["INDIAN NAVY"]],
            ["MINISTRY OF DEFENCE", ["INDIAN AIR FORCE"]],
            ["MINISTRY OF DEFENCE", ["BORDER ROAD ORGANISATION"]]
            ]

        MINISTRY_list =  [["MINISTRY OF HOME AFFAIRS", ["ASSAM RIFLES"]]]

        for MINISTRY in MINISTRY_list: 
            ministry_name=MINISTRY[0]
            Organization_name=MINISTRY[1]

            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                sleep(0.5)

            t = threading.Thread(target=gem_funtion, args=(ministry_name,Organization_name))
            t.start()
            threads.append(t)
    except:
        traceback.print_exc() 

gem()