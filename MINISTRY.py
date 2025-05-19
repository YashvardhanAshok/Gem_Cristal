import threading
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
import pyodbc
from datetime import datetime

today = date.today()
failed_downloads = []

from time import sleep

import requests
import ntpath
import fitz  
import pdfplumber

import requests
from urllib.parse import urlparse
import re
max_page= 9999

def clean_text(text):
    if text:
        text = re.sub(r'\(cid:\d+\)', '', text)
        text = text.replace('\n', ' ').replace('\r', ' ').strip()
        return text

    return ''

xl_count = 2
def gem_find(driver,card_elements , card, gem_ids, element):
    global failed_downloads
    global xl_count
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
    time.sleep(0.5)
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
        start_date_time = opening_date_parts[1] + " " + opening_date_parts[2]

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
                failed_downloads.append([bid_title.text,element])
                return
            
            if response.status_code == 200 and "text/html" not in response.headers.get("Content-Type", ""):
                if 'Content-Disposition' in response.headers:
                    file_name = response.headers.get('Content-Disposition').split('filename=')[-1].strip('\"')
                else:
                    parsed_url = urlparse(link_href)
                    file_name = ntpath.basename(parsed_url.path)

                if bid_title.text in gem_ids:
                    print("gem id skipped:", bid_title.text)
                    return
                else:
                    gem_ids.append(bid_title.text)

                download_path = os.path.join(os.getcwd(), 'download_pdf', file_name)
                os.makedirs(os.path.dirname(download_path), exist_ok=True)

                with open(download_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

                print(f"Downloaded file: {download_path}")

                if os.path.exists(download_path):
                    with pdfplumber.open(download_path) as pdf:
                        emd_amount = None
                        epbg_percentage = None
                        Tender_value = None
                        Beneficiary = ['NA']
                        for page in pdf.pages:

                            tables = page.extract_tables()
                            for section in tables:
                                try:
                                    for row in section:
                                        key = row[0]
                                        value = row[1]
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
                        event_data["DAY LEFT"] = """=IF((INDIRECT("H"&ROW()) + INDIRECT("I"&ROW())) - NOW() <= 0, "CLOSED", INT((INDIRECT("H"&ROW()) + INDIRECT("I"&ROW())) - NOW()) & " days")"""
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
                        return event_data
            
            else:
                print(f"Link is not a downloadable file or not found: {link_href}")
        except Exception as download_error:
            traceback.print_exc()
            print(f"Error downloading or reading file from {link_href}: {download_error}")
    except Exception as e:
        traceback.print_exc()

db_lock = threading.Lock()
def sql(extracted_data):
    with db_lock:  # Lock acquired here

        # Connect to SQL Server
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        # Loop through tenders
        for tender_data in extracted_data:
            tender_id = tender_data["TENDER ID"]

            # Check if the tender already exists
            cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (tender_id,))
            exists = cursor.fetchone()[0]

            if exists:
                print(f"Tender ID {tender_id} already exists. Skipping insert.")
                continue

            # Insert new tender
            insert_sql = """
            INSERT INTO tender_data (
                date_of_search, tender_id, element_put, item_description, qty,
                start_date, end_date, end_time, day_left_formula,
                emd_amount, tender_value, item_category,
                consignee_reporting, address,
                ministry, department, branch,
                matches, matched_products
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            values = (
                datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                str(tender_data["TENDER ID"]),
                str(tender_data.get("elementPut", "")),
                str(tender_data.get("ITEM DESCRIPTION", "")),
                int(tender_data.get("QTY", 0)),
                datetime.strptime(tender_data["START DATE"], "%d-%b-%Y").date(),
                datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date(),
                str(tender_data.get("END Time", "")),
                str(tender_data.get("DAY LEFT", "")),
                float(tender_data.get("EMD AMOUNT") or 0),
                float(tender_data.get("TENDER VALUE") or 0),
                str(tender_data.get("ITEM CATEGORY", "")),
                json.dumps(tender_data.get("Consignee Reporting", [])),
                json.dumps(tender_data.get("ADDRESS", [])),
                str(tender_data.get("MINISTRY", "")),
                str(tender_data.get("DEPARTMENT", "")),
                str(tender_data.get("BRANCH", "")),
                int(tender_data.get("matches", False)),
                json.dumps(tender_data.get("matched_products", []))
            )

            cursor.execute(insert_sql, values)
            conn.commit()
            print(f"Tender ID {tender_id} inserted successfully.")

        # Close connection
        cursor.close()
        conn.close()



def gem_funtion(threading_filename, file_Pail, ministry_name, Organization_name):
    extracted_data = []
    
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

    sleep(2)

    for org_name in Organization_name:
        string_name_file = ministry_name + " " + org_name
        
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
        except:
            continue
        
        try:
            for page_no in range(int(max_page)):

                card_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))

                for card in card_elements:
                    json_data = gem_find(driver, card_elements, card, gem_ids, org_name)
                    if json_data:
                        extracted_data.append(json_data)


                if page_no == max_page:
                    break
                try:
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]")))
                    next_button.click()
                except:
                    break
                      
        except Exception as e:
            print("An error occurred:", str(e))
            traceback.print_exc() 

        product = [['2 V Solar Battery cells', '3D Multi Spectral Camo Vehicle Cover', '3D Printer', '3d Multi Spectral Camo Dress', 'A.C Static Meter', 'ALL Types of commercial Gym Equipment', 'AMC OF COMMERCIAL KITCHEN EQUIPMENT', 'AMC OF Gym EQUIPMENT', 'Ac static watthour meters-energy meter', 'Access Control Solutions', 'Air Freight Shipping', 'Air curtain', 'All Range Hospital Furniture', 'All Types of Commercial RO PLANTS', 'All Types of Wire and Cables', 'Amc Of Ac', 'Amc Of Commercial Kitchen', 'Amc Of Fire Extinguishers', 'Amc Of Generators', 'Amc Of Gym Equipement', 'Amc Of Kitchen Equipement', 'Amc Of Lightning Arrestors', 'Amc Of Ro And IRP', 'Amc Of Solar Power Plant', 'Amc Of Solar Water Heaters', 'Amc Of Transformers', 'Amc of DG Sets and Transformer', 'AntI Drone system', 'Anti climb Fence', 'Automobile Batteries other batteries', 'Bain Marie', 'Bain marie', 'Barbed Wire', 'Battery', 'Body Worn Camera', 'Bola wrap Remote Restrain device', 'Braille Embosser', 'Bricks', 'Bucket Mop Wringer Trolly', 'Butter', 'CCTV', 'CEW (Conducted Electrical Weapon)', 'CGI Sheet', 'Cement','Chainlink Fence', 'Change over Switch', 'Chapati Warmer', 'Clip On Weapon Sites', 'Commercial Mixer', 'Commercial Vaccum Cleaner', 'Computer and peripherals', 'Construction Of Admin Blocks', 'Construction Of Hospital', 'Construction Of Internal Roads', 'Construction Of Klps For Defense', 'Convex Security Mirror', 'Cranes', 'Cyber Forensics Software', 'Cyber Security Solutions', 'DG SETS', 'Data Management solutions', 'Decorative Bollard', 'Decorative Street Light', 'Development Of Infrastructure For Defense', 'Development Of Sewerage Treatement Plant', 'Development Of Water Supply', 'Domestic casserole', 'Dough Kneader', 'Dough kneader 15kg', 'Dry Ration (Rice , Pulses , Sugar , Coffee, Tea)', 'Dustbin', 'Electric Fence', 'Electric Wires/Cable', 'Electric milk boiler', 'FRP', 'FRP Tank', 'Flood Light', 'Flooring', 'Forklifts', 'Fresh Fruits', 'Fresh Vegetable', 'Fuel Cell', 'Fuel cell genrators', 'GPS', 'GPS (Global Positioning System)', 'Ghillie Suits', 'Ghilly Suit', 'Gi Pipe','Gyser', 'HHTI (Hand Held Thermal Imagers)', 'Hand Held Gas Detector', 'Hand held Thermal Imager', 'Handheld GPS', 'Hardware Item', 'Headphones', 'High Intensity Light Infrared beam', 'Honey Sucker / Sewer Cum Jetting Machine', 'Hybrid UPS', 'Idli Steamer', 'Incinerators', 'Inflatable Shelters', 'Inverters', 'JCB Bacholoader', 'Jet Spray', 'Jungle Boots', 'Kunda Gadi', 'LGSF Building', 'Large compartmental stainless steel tiffin', 'Led Bulbs', 'Less Lethal Weapons', 'Lighting Arrestor', 'Lightning Arrestor', 'Long Range Acoustic Hailing Device', 'Lorros', 'MCB', 'MCCB', 'Meat Cutting Machine', 'Mild Steel LPG Barbecues', 'Milk', 'Milk Boiler', 'Miltary Rain Poncho', 'Miniature Circuit Breaker Switches', 'Monitor', 'Multi Function Laser Aiming System', 'Nano Uav', 'New lpg cooking appliances', 'Oil', 'Online UPS', 'Outdoor Gym', 'Oven', 'PNVG', 'PPGI Sheets','Patient Bed Fowler', 'Patient Care Mattress', 'Picket Steel', 'Pickup Truck', 'Plotter', 'Plywood', 'Porta Cabin', 'Portable Kitchen', 'Portable houses', 'Poultry Product (Chicken, Egg , Mutton)', 'Ppgi Sheet', 'Prefab shelters with puf panel of size 7.620 m x 13.271 m', 'Printer', 'Projector', 'Puff Cabin', 'Puff Shelter', 'Punched Tape concertina Coil PTCC', 'RO (Reverse Osmosis)', 'Remote Restraint Device', 'Rice Boiler', 'Rice boiler', 'Road Sweeping Machines', 'Robotics', 'Room Heater', 'Roti Making Machine', 'Roti Making Machine Auto matic', 'Rucksack Bags', 'SANITARY NAPKIN VENDING MACHINE', 'SS', 'SS Thermos', 'STP', 'STP (Sewage Treatment Plants)', 'Sand', 'Sanitary Items', 'Sanitary Napkins Incinetator Machine with Smoke ControlUnit', 'Satellite Tracker', 'Sea Food (Fish)', 'Search Light', 'Sedan / SUVS', 'Semi Automatic', 'Sewer Suction Machines', 'Shooting Range', 'Skid steer Loader', 'Software','Software Defined Radio', 'Solar Battery', 'Solar Lantern', 'Solar PV Panel','Solar Panel', 'Solar PV Plant', 'Solar Power Plant', 'Solar Street Light', 'Solar Street Light all Type', 'Solar Tublar Batteries', 'Solar Water Heater', 'Solar inverter', 'Solar water Heater', 'Solar water pump', 'Speakers', 'Street Light', 'Switch fuse unit', 'Tablet', 'Tandoor', 'Tandoor, Height 481-500 Millimeter', 'Tubes', 'UAV', 'Under Water Torch', 'Unmanned Aerial Vehicle', 'Vaccum Cleaner', 'Vegetable Cutter', 'Video Survelliance & Analytics Solutions', 'WTP', 'Walkie Talkie', 'Waste Management', 'Waste Management Plants', 'Water Bowser', 'Water Cooling', 'Water Dispenser', 'Water Tanker', 'Weapon Sight', 'Weapon Sites', 'Weapon Support system', 'Wet Grinder', 'Wet grinder 5', 'Wheel Barrow', 'X-ray Machine', 'XLPE Cables', 'water cooler']]

        flat_products = [item.lower() for sublist in product for item in sublist]

    for item in extracted_data:
        title = item.get("ITEM DESCRIPTION", "").lower()
        matches = [prod for prod in flat_products if prod in title]
        item["matches"] = bool(matches)
        item["matched_products"] = matches

    sql(extracted_data)
                
    with open(threading_filename, "w") as f:
        gem_ids_json[string_name_file] = gem_ids
        json.dump(gem_ids_json, f, indent=2)
    print(gem_ids)
    driver.quit()




    
def gem():
    try:
        max_threads = 4
        count = 0 
        threads = []

        MINISTRY_list = [
            ["MINISTRY OF COMMUNICATIONS", ['']],
            ["MINISTRY OF HOUSING & URBAN AFFAIRS", ["HINDUSTAN STEELWORKS CONSTRUCTION LIMITED"]],
            ["MINISTRY OF POWER", ["NTPC LIMITED"]],
            ["MINISTRY OF HEALTH AND FAMILY WELFARE", ["HLL INFRA TECH SERVICES LIMITED"]],
            ["MINISTRY OF CIVIL AVIATION", ["AIRPORTS AUTHORITY OF INDIA"]],
            ["MINISTRY OF HOME AFFAIRS", ["NATIONAL SECURITY GUARD", "INDO TIBETAN BORDER POLICE", "NATIONAL DISASTER RESPONSE FORCE"]],
            ["MINISTRY OF HOME AFFAIRS", ["ASSAM RIFLES", "CENTRAL RESERVE POLICE FORCE", "BORDER SECURITY FORCE","CENTRAL INDUSTRIAL SECURITY FORCE"]],
            ["MINISTRY OF DEFENCE", ["INDIAN NAVY"]],
            ["MINISTRY OF DEFENCE", ["INDIAN ARMY"]],
            ["MINISTRY OF DEFENCE", ["INDIAN AIR FORCE"]]
            ]

        for MINISTRY in MINISTRY_list: 
            ministry_name=MINISTRY[0]
            Organization_name=MINISTRY[1]
            
            threading_filename = os.path.join(os.path.dirname(__file__), 'db', "Gem_ministry","json", f"{count}.json")
            file_Pail = os.path.join(os.path.dirname(__file__), 'db', "Gem_ministry","gem_bid_id_ministry", f"Su_{count}.json")

            while True:
                # Clean up finished threads
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                time.sleep(0.5)  # Wait a bit before checking again

            # Start new thread
            t = threading.Thread(target=gem_funtion, args=(threading_filename,file_Pail,ministry_name,Organization_name))
            t.start()
            threads.append(t)
                
    except:
        traceback.print_exc() 



gem()

# with open

# failed_downloads = os.path.join(os.path.dirname(__file__), 'db', "Gem_ministry","gem_bid_id_ministry", f"Su_{count}.json")

print(failed_downloads)