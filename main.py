from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time
import json
import os
from datetime import datetime as ds
from time import sleep

import os
import requests
from urllib.parse import urlparse
import ntpath
import pdfplumber

import requests
from urllib.parse import urlparse
import re
from datetime import date
today = date.today()

def clean_text(text):
    if text:
        text = re.sub(r'\(cid:\d+\)', '', text)
        text = text.replace('\n', ' ').replace('\r', ' ').strip()
        return text
    return ''

def gem_find(driver,card_elements , card, gem_ids, element):
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
            response = requests.get(link_href, stream=True)
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
                        for page in pdf.pages:
                            tables = page.extract_tables()
                            for section in tables:
                                try:
                                    for row in section:
                                        key = row[0]
                                        value = row[1]
                                        
                                        if key and 'Item Category' in key and value:
                                            Item_Category = value
                                        
                                        if key and 'EMD Amount' in key and value:
                                            emd_amount = float(re.sub(r'[^\d.]', '', value))
                                            Tender_value = emd_amount * 50
                                        elif key and 'ePBG Percentage' in key:
                                            epbg_percentage = value
                                except:
                                    print('error in EMD Amount')

                        for page in pdf.pages:
                            tables = page.extract_tables()
                            for table in tables:
                                headers = table[0]
                                if any("S.No" in (cell or "") for cell in headers):
                                    for row in table[1:]:
                                        row = row + [""] * (len(headers) - len(row))
                                        data = dict(zip(headers, row))

                                        event_data = {}
                                        try:
                                            event_data["DATE OF SEARCH"] = today.strftime("%d-%b-%Y")
                                        except:
                                            pass
                                        try:
                                            event_data["TENDER ID"] = bid_title.text
                                        except:
                                            pass
                                        try:
                                            event_data["elementPut"] = element
                                        except:
                                            pass
                                        try:
                                            event_data["ITEM DESCRIPTION"] = title
                                        except:
                                            try:
                                                event_data["ITEM DESCRIPTION"] = Item_Category
                                            except:
                                                pass
                                        try:
                                            event_data["QTY"] = data.get(next((h for h in headers if "Quantity" in (h or "")), ""), "").strip()
                                        except:
                                            pass
                                        
                                        event_data["START DATE"] = start_date
                                        event_data["END DATE"] = end_date
                                        event_data["END Time"] = end_date_time
                                        event_data["DAY LEFT"] = end_date_time
                                        event_data["EMD AMOUNT"] = emd_amount
                                        event_data["TENDER VALUE"] = Tender_value
                                        
                                        try:
                                            event_data["ITEM CATEGORY"] = Item_Category
                                        except:
                                            pass
                                        
                                        try:
                                            event_data["Consignee Reporting"] = data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").replace("*", "").strip()
                                        except:
                                            pass
                                        try:
                                            event_data["ADDRESS"] = data.get(next((h for h in headers if "Address" in (h or "")), ""), "").replace("*", "").strip()
                                        except:
                                            pass

                                        event_data["MINISTRY"] = department_address_parts[0]
                                        event_data["DEPARTMENT"] = department_address_parts[1]

                                        return event_data
            else:
                print(f"Link is not a downloadable file or not found: {link_href}")
        except Exception as download_error:
            traceback.print_exc()
            print(f"Error downloading or reading file from {link_href}: {download_error}")
    except Exception as e:
        traceback.print_exc()



def gem_funtion(threading_filename,file_Pail ,elements_list):
    extracted_data = []
    
    driver = webdriver.Edge()
    driver.get('https://bidplus.gem.gov.in/all-bids')
    sleep(2)

    sleep(2)

    for element in elements_list:
        string_name_file = element
        
        if not os.path.exists(threading_filename):
            with open(threading_filename, "w") as f:
                json.dump({string_name_file: []}, f)

        with open(threading_filename, "r") as f:
            gem_ids_json = json.load(f)
            gem_ids = gem_ids_json.get(string_name_file, [])
        
        time.sleep(0.1)
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchBid')))
        search.clear()
        search.send_keys(element)
        search.send_keys(Keys.RETURN)

        try:
            pagination = driver.find_element(By.ID, "light-pagination")
            page_links = pagination.find_elements(By.CLASS_NAME, "page-link")
            page_numbers = [int(link.text) for link in page_links if link.text.isdigit()]
            max_page = max(page_numbers) if page_numbers else 1  
            print("Max page number:", max_page)
        
        except:
            try:
                pagination = driver.find_element(By.ID, "light-pagination")
                page_links = pagination.find_elements(By.CLASS_NAME, "page-link")
                page_numbers = [int(link.text) for link in page_links if link.text.isdigit()]
                max_page = max(page_numbers) if page_numbers else 1  
                print("Max page number:", max_page)
            except:
                max_page = 99999
        
        try:
            for page_no in range(int(max_page)):

                card_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))

                for card in card_elements:
                    json_data = gem_find(driver, card_elements, card, gem_ids, element)
                    if json_data:
                        # Gem-funtion
                        extracted_data.append(json_data)
                

                if page_no == max_page or page_no == 5:
                    break
                else:
                    try:
                        next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]")))
                        next_button.click()
                    except:
                        break
                        


        except Exception as e:
            print("An error occurred:", str(e))
            traceback.print_exc() 
        

        try:
            with open(file_Pail, "r") as json_file:
                existing_data = json.load(json_file)
            existing_data.extend(extracted_data)
            unique_entries = []
            for entry in existing_data:
                if (entry["elementPut"], entry["ITEM DESCRIPTION"]) not in [(e["elementPut"], e["ITEM DESCRIPTION"]) for e in unique_entries]:
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
def Main():
    try:
        count = 0 
        threads = []
        
        item_list = [['2 V Solar Battery cells', '3D Multi Spectral Camo Vehicle Cover', '3D Printer', '3d Multi Spectral Camo Dress', 'A.C Static Meter', 'ALL Types of commercial Gym Equipment', 'AMC OF COMMERCIAL KITCHEN EQUIPMENT', 'AMC OF Gym EQUIPMENT', 'Ac static watthour meters-energy meter', 'Access Control Solutions', 'Air Freight Shipping', 'Air curtain', 'All Range Hospital Furniture', 'All Types of Commercial RO PLANTS', 'All Types of Wire and Cables', 'Amc Of Ac', 'Amc Of Commercial Kitchen', 'Amc Of Fire Extinguishers', 'Amc Of Generators', 'Amc Of Gym Equipement', 'Amc Of Kitchen Equipement', 'Amc Of Lightning Arrestors', 'Amc Of Ro And IRP', 'Amc Of Solar Power Plant', 'Amc Of Solar Water Heaters', 'Amc Of Transformers', 'Amc of DG Sets and Transformer', 'AntI Drone system', 'Anti climb Fence', 'Automobile Batteries other batteries', 'Bain Marie', 'Bain marie', 'Barbed Wire', 'Battery', 'Body Worn Camera', 'Bola wrap Remote Restrain device', 'Braille Embosser', 'Bricks', 'Bucket Mop Wringer Trolly', 'Butter', 'CCTV', 'CEW (Conducted Electrical Weapon)', 'CGI Sheet', 'Cement','Chainlink Fence', 'Change over Switch', 'Chapati Warmer', 'Clip On Weapon Sites', 'Commercial Mixer', 'Commercial Vaccum Cleaner', 'Computer and peripherals', 'Construction Of Admin Blocks', 'Construction Of Hospital', 'Construction Of Internal Roads', 'Construction Of Klps For Defense', 'Convex Security Mirror', 'Cranes', 'Cyber Forensics Software', 'Cyber Security Solutions', 'DG SETS', 'Data Management solutions', 'Decorative Bollard', 'Decorative Street Light', 'Development Of Infrastructure For Defense', 'Development Of Sewerage Treatement Plant', 'Development Of Water Supply', 'Domestic casserole', 'Dough Kneader', 'Dough kneader 15kg', 'Dry Ration (Rice , Pulses , Sugar , Coffee, Tea)', 'Dustbin', 'Electric Fence', 'Electric Wires/Cable', 'Electric milk boiler', 'FRP', 'FRP Tank', 'Flood Light', 'Flooring', 'Forklifts', 'Fresh Fruits', 'Fresh Vegetable', 'Fuel Cell', 'Fuel cell genrators', 'GPS', 'GPS (Global Positioning System)', 'Ghillie Suits', 'Ghilly Suit', 'Gi Pipe','Gyser', 'HHTI (Hand Held Thermal Imagers)', 'Hand Held Gas Detector', 'Hand held Thermal Imager', 'Handheld GPS', 'Hardware Item', 'Headphones', 'High Intensity Light Infrared beam', 'Honey Sucker / Sewer Cum Jetting Machine', 'Hybrid UPS', 'Idli Steamer', 'Incinerators', 'Inflatable Shelters', 'Inverters', 'JCB Bacholoader', 'Jet Spray', 'Jungle Boots', 'Kunda Gadi', 'LGSF Building', 'Large compartmental stainless steel tiffin', 'Led Bulbs', 'Less Lethal Weapons', 'Lighting Arrestor', 'Lightning Arrestor', 'Long Range Acoustic Hailing Device', 'Lorros', 'MCB', 'MCCB', 'Meat Cutting Machine', 'Mild Steel LPG Barbecues', 'Milk', 'Milk Boiler', 'Miltary Rain Poncho', 'Miniature Circuit Breaker Switches', 'Monitor', 'Multi Function Laser Aiming System', 'Nano Uav', 'New lpg cooking appliances', 'Oil', 'Online UPS', 'Outdoor Gym', 'Oven', 'PNVG', 'PPGI Sheets','Patient Bed Fowler', 'Patient Care Mattress', 'Picket Steel', 'Pickup Truck', 'Plotter', 'Plywood', 'Porta Cabin', 'Portable Kitchen', 'Portable houses', 'Poultry Product (Chicken, Egg , Mutton)', 'Ppgi Sheet', 'Prefab shelters with puf panel of size 7.620 m x 13.271 m', 'Printer', 'Projector', 'Puff Cabin', 'Puff Shelter', 'Punched Tape concertina Coil PTCC', 'RO (Reverse Osmosis)', 'Remote Restraint Device', 'Rice Boiler', 'Rice boiler', 'Road Sweeping Machines', 'Robotics', 'Room Heater', 'Roti Making Machine', 'Roti Making Machine Auto matic', 'Rucksack Bags', 'SANITARY NAPKIN VENDING MACHINE', 'SS', 'SS Thermos', 'STP', 'STP (Sewage Treatment Plants)', 'Sand', 'Sanitary Items', 'Sanitary Napkins Incinetator Machine with Smoke ControlUnit', 'Satellite Tracker', 'Sea Food (Fish)', 'Search Light', 'Sedan / SUVS', 'Semi Automatic', 'Sewer Suction Machines', 'Shooting Range', 'Skid steer Loader', 'Software','Software Defined Radio', 'Solar Battery', 'Solar Lantern', 'Solar PV Panel', 'Solar PV Plant', 'Solar Power Plant', 'Solar Street Light', 'Solar Street Light all Type', 'Solar Tublar Batteries', 'Solar Water Heater', 'Solar inverter', 'Solar water Heater', 'Solar water pump', 'Speakers', 'Street Light', 'Switch fuse unit', 'Tablet', 'Tandoor', 'Tandoor, Height 481-500 Millimeter', 'Tubes', 'UAV', 'Under Water Torch', 'Unmanned Aerial Vehicle', 'Vaccum Cleaner', 'Vegetable Cutter', 'Video Survelliance & Analytics Solutions', 'WTP', 'Walkie Talkie', 'Waste Management', 'Waste Management Plants', 'Water Bowser', 'Water Cooling', 'Water Dispenser', 'Water Tanker', 'Weapon Sight', 'Weapon Sites', 'Weapon Support system', 'Wet Grinder', 'Wet grinder 5', 'Wheel Barrow', 'X-ray Machine', 'XLPE Cables', 'water cooler']]

        for elements in item_list: 
            threading_filename = os.path.join(os.path.dirname(__file__), 'db', "Gem_main", "gem_bid_id_ministry",f"{count}.json")
            file_Pail = os.path.join(os.path.dirname(__file__), 'db', "Gem_main",f"Su_{count}.json")

            t = threading.Thread(target=gem_funtion, args=(threading_filename,file_Pail ,elements))
            t.start()
            threads.append(t)
            count = count  + 1 
            if count == 4:
                for t in threads:
                    t.join()
                count = 0
                
    except:
        traceback.print_exc() 



Main()




