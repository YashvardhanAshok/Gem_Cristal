from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
import ntpath
import re

log_path = os.path.join(os.path.dirname(__file__),'db','log.txt')
FIND_T_path = os.path.join(os.path.dirname(__file__),'db','ten_find.txt')
ND_FIND_T_path = os.path.join(os.path.dirname(__file__),'db','nd_ten_find.txt')

def clean_text(text):
    if text:
        # Remove (cid:##) like artifacts
        text = re.sub(r'\(cid:\d+\)', '', text)
        # Remove extra spaces and normalize Unicode
        text = text.replace('\n', ' ').replace('\r', ' ').strip()
        return text
    return ''


def gem(SearchKeywords,product):
    log_arry= f'GEM.{today}'+'\n'
    FIND_T_arry = f'GEM.{today}'+'\n'
    ND_FIND_T_arry = f'GEM.{today}'+'\n'

    try:
        driver = webdriver.Edge()
        driver.get('https://bidplus.gem.gov.in/all-bids')
        
        extracted_data = []  
        
        for row in SearchKeywords:
            for element in row:
                try:
                    time.sleep(0.1)
                    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchBid')))
                    search.clear()
                    search.send_keys(element)
                    search.send_keys(Keys.RETURN)
                    try:
                        card_elements = WebDriverWait(driver, 10).until(
                            EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
                        
                        log_arry = log_arry + 'Tender found: '+ element +'\n'
                        FIND_T_arry = FIND_T_arry + "   " + element +'\n'

                        for card in card_elements:
                            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                            # Optionally wait a bit to let the scroll complete or element render
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

                                try:
                                    response = requests.get(link_href, stream=True)
                                    if response.status_code == 200 and "text/html" not in response.headers.get("Content-Type", ""):
                                        if 'Content-Disposition' in response.headers:
                                            file_name = response.headers.get('Content-Disposition').split('filename=')[-1].strip('\"')
                                        else:
                                            parsed_url = urlparse(link_href)
                                            file_name = ntpath.basename(parsed_url.path)
                                        
                                        download_path = os.path.join(os.path.dirname(__file__), 'download_pdf', file_name)
                                        os.makedirs(os.path.dirname(download_path), exist_ok=True)

                                        def flatten(lst):
                                            for item in lst:
                                                if isinstance(item, list):
                                                    yield from flatten(item)
                                                else:
                                                    yield item

                                        flattened_machines = list(flatten(product))

                                        matches = [m for m in flattened_machines if re.search(re.escape(m), bid_title.text, re.IGNORECASE)]

                                        if matches:
                                            match = True
                                            print("Match found:", matches)
                                        else:
                                            match = False
                                            print("not found:", matches)

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
                                                                
                                                                event_data = {}
                                                                event_data["DATE OF SEARCH"]= today.strftime("%d-%b-%Y")
                                                                
                                                                event_data["matches"] = match
                                                                event_data["TENDER ID"]= bid_title.text
                                                                # event_data["elementPut"]= element
                                                                event_data["ITEM DESCRIPTION"]= title
                                                                try:
                                                                    event_data["Quantity"]= data.get(next((h for h in headers if "Quantity" in (h or "")), ""), "").strip()
                                                                except:
                                                                    pass
                                                                
                                                                event_data["START DATE"]= start_date
                                                                event_data["END DATE"]= end_date
                                                                event_data["END Time"]= end_date_time
                                                                event_data["DAY LEFT"]= end_date_time

                                                                event_data["EMD AMOUNT"]= emd_amount
                                                                event_data["TENDER VALUE"]= Tender_value
                                                                
                                                                try:
                                                                    event_data["Consignee Reporting"]= data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").strip()
                                                                except:
                                                                    pass
                                                                try:
                                                                    event_data["Address"]= data.get(next((h for h in headers if "Address" in (h or "")), ""), "").strip()
                                                                except:
                                                                    pass

                                                                try:
                                                                    # event_data["Delivery Days"]= data.get(next((h for h in headers if "Delivery Days" in (h or "")), ""), "").strip()
                                                                    pass
                                                                except:
                                                                    pass
                                                                
                                                                # event_data["ePBG Percentage"]= epbg_percentage
                                                                # event_data["Opening Time"]= start_date_time
                                                                # event_data["link"]= link_href
                                                                
                                                                extracted_data.append(event_data)

                                    else:
                                        print(f"Link is not a downloadable file or not found: {link_href}")
                                except Exception as download_error:
                                    print(f"Error downloading or reading file from {link_href}: {download_error}")

                            except Exception as e:
                                log_arry= log_arry + "Error found in card:" + element+'\n'
                                

                    except:
                        log_arry = log_arry + "Was not able to find table for: " + element+ '\n'
                            
                except:
                    ND_FIND_T_arry = ND_FIND_T_arry + "   " + element+'\n'
                    log_arry = log_arry + "Was not able to find search for: " + element+'\n'
        
        driver.quit()
        file_Pail = os.path.join(os.path.dirname(__file__), 'website', 'json', 'gem.json')
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
        
        log_arry = log_arry + "Was not able to find table for: " + element+'\n'
        
    except:
        log_arry = log_arry + "was not able to lunch: GEM"+'\n'
            
    with open(log_path, "a") as file:
        file.write(log_arry)
    with open(FIND_T_path, "a") as file:
        file.write(FIND_T_arry) 
    with open(ND_FIND_T_path, "a") as file:
        file.write(ND_FIND_T_arry)                  



SearchKeywords=[
  ["Amc Of Kitchen Equipement",
  "Amc Of Commercial Kitchen",
  "Amc Of Gym Equipement",
  "Amc Of Solar Power Plant",
  "Amc Of Generators",
  "Amc Of Transformers",
  "Amc Of Lightning Arrestors",
  "Amc Of Solar Water Heaters",
  "Amc Of Fire Extinguishers",
  "Amc Of Ac",
  "Waste Management",
  "Amc Of Ro And IRP"],

#   // Infrastructure Development
  ["Construction Of Klps For Defense",
  "Construction Of Admin Blocks",
  "Construction Of Hospital",
  "Construction Of Internal Roads",
  "Development Of Infrastructure For Defense",
  "Development Of Water Supply",
  "Development Of Sewerage Treatement Plant"],

#   // Supply Chain Of Food
  ["Fresh Vegetable",
  "Fresh Fruits",
  "Poultry Product (Chicken, Egg , Mutton)",
  "Sea Food (Fish)",
  "Dry Ration (Rice , Pulses , Sugar , Coffee, Tea)",
  "Butter",
  "Milk",
  "Oil"],

#   // CHT
  ["Water Bowser",
  "Water Tanker",
  "Sedan / SUVS",
  "Kunda Gadi",
  "Pickup Truck",
  "Air Freight Shipping"],

#   // Energy Solution
  ["Fuel Cell",
  "Solar Power Plant",
  "Solar Battery"],
  
  [ "Electric Wires/Cable",
  "A.C Static Meter",
  "Lightning Arrestor",
  "Miniature Circuit Breaker Switches"],

#   // PRODUCT - Solar
[  "Solar Street Light",
  "Solar Power Plant",
  "Solar Water Heater",
  "Solar Lantern",
  "Solar Battery"],

#   // Kitchen Equipment
  ["Roti Making Machine",
  "Milk Boiler",
  "Dough Kneader",
  "Bain Marie",
  "Commercial Mixer",
  "Wet Grinder",
  "Vegetable Cutter",
  "Rice Boiler",
  "Idli Steamer",
  "Oven",
  "Tandoor",
  "Water Dispenser",
  "Water Cooling"],

#   // Rescue Items
  ["Hand Held Gas Detector",
  "Under Water Torch"],

#   // Green Energy
  ["Fuel Cell"],

#   // Construction Material Supply
  ["Ppgi Sheet",
  "Plywood",
  "Puff Shelter",
  "Puff Cabin",
  "Gi Pipe",
  "Cement",
  "Bricks",
  "Sand",
  "Sanitary Items",
  "Hardware Item",
  "Flooring"],

#   // UPS
  ["Online UPS",
  "Hybrid UPS"],

[  "Ghillie Suits"],

[  "X-ray Machine",
  "Patient Bed Fowler",
  "All Range Hospital Furniture",
  "Patient Care Mattress"],

 [ "Under Water Torch"],

[  "Rucksack Bags"],

[  "Honey Sucker / Sewer Cum Jetting Machine",
  "Jet Spray",
  "Vaccum Cleaner",
  "Wheel Barrow",
  "Incinerators",
  "Dustbin",
  "FRP Tank",
  "Bucket Mop Wringer Trolly"],

#   // Water Treatement
[  "RO (Reverse Osmosis)",
  "STP (Sewage Treatment Plants)",

  "Battery"],
[
  "Less Lethal Weapons",
  "CEW (Conducted Electrical Weapon)",
  "Remote Restraint Device",
  "HHTI (Hand Held Thermal Imagers)",
  "Weapon Sight",
  "Search Light",
  "GPS (Global Positioning System)",
  "Satellite Tracker",
  "Unmanned Aerial Vehicle",
  "Robotics"

],[  "Monitor",
  "Printer",
  "Speakers",
  "Headphones",
  "Projector",
  "GPS",
  "Plotter",
  "Braille Embosser",
  "3D Printer",
  "Tablet",
  "Walkie Talkie",
  "Software",
  "Software Defined Radio",
  "Cyber Forensics Software"
]
]

product = [
#   // PRODUCT - Electric Items
 [ "Electric Wires/Cable",
  "A.C Static Meter",
  "Lightning Arrestor",
  "Miniature Circuit Breaker Switches"],

#   // PRODUCT - Solar
[  "Solar Street Light",
  "Solar Power Plant",
  "Solar Water Heater",
  "Solar Lantern",
  "Solar Battery"],

#   // Kitchen Equipment
  ["Roti Making Machine",
  "Milk Boiler",
  "Dough Kneader",
  "Bain Marie",
  "Commercial Mixer",
  "Wet Grinder",
  "Vegetable Cutter",
  "Rice Boiler",
  "Idli Steamer",
  "Oven",
  "Tandoor",
  "Water Dispenser",
  "Water Cooling"],

#   // Rescue Items
  ["Hand Held Gas Detector",
  "Under Water Torch"],

#   // Green Energy
  ["Fuel Cell"],

#   // Construction Material Supply
  ["Ppgi Sheet",
  "Plywood",
  "Puff Shelter",
  "Puff Cabin",
  "Gi Pipe",
  "Cement",
  "Bricks",
  "Sand",
  "Sanitary Items",
  "Hardware Item",
  "Flooring"],

#   // UPS
  ["Online UPS",
  "Hybrid UPS"],

[  "Ghillie Suits"],

[  "X-ray Machine",
  "Patient Bed Fowler",
  "All Range Hospital Furniture",
  "Patient Care Mattress"],

 [ "Under Water Torch"],

[  "Rucksack Bags"],

[  "Honey Sucker / Sewer Cum Jetting Machine",
  "Jet Spray",
  "Vaccum Cleaner",
  "Wheel Barrow",
  "Incinerators",
  "Dustbin",
  "FRP Tank",
  "Bucket Mop Wringer Trolly"],

#   // Water Treatement
[  "RO (Reverse Osmosis)",
  "STP (Sewage Treatment Plants)",
  "Battery"],
[
  "Less Lethal Weapons",
  "CEW (Conducted Electrical Weapon)",
  "Remote Restraint Device",
  "HHTI (Hand Held Thermal Imagers)",
  "Weapon Sight",
  "Search Light",
  "GPS (Global Positioning System)",
  "Satellite Tracker",
  "Unmanned Aerial Vehicle",
  "Robotics"

],
[ "Monitor",
  "Printer",
  "Speakers",
  "Headphones",
  "Projector",
  "GPS",
  "Plotter",
  "Braille Embosser",
  "3D Printer",
  "Tablet",
  "Walkie Talkie",
  "Software",
  "Software Defined Radio",
  "Cyber Forensics Software"
],
# "PRE-ENGINEERED BUILDING": 
[
    "Prefab shelters with puf panel of size 7.620 m x 13.271 m",
    "LGSF Building",
    "Inflatable Shelters",
    "Porta Cabin",
    "Portable houses",
    "Portable Kitchen",
    "PPGI Sheets",
    "CGI Sheet"
],
# "ELECTRICAL": 
    [
    "Led Bulbs","Tubes",
    "Street Light",
    "Flood Light",
    "Gyser",
    "Room Heater",
    "XLPE Cables",
    "All Types of Wire and Cables",
    "MCB",
    "MCCB",
    "Ac static watthour meters-energy meter",
    "Switch fuse unit","Change over Switch",
    "Decorative Street Light",
    "Decorative Bollard",
    "water cooler",
    "Lighting Arrestor"
],
# "COMMERCIAL KITCHEN EQUIPMENT": 
    [
    "Domestic casserole",
    "Bain marie",
    "Wet grinder 5",
    "Dough kneader 15kg",
    "water cooler",
    "Commercial Mixer",
    "Vegetable Cutter",
    "Electric milk boiler",
    "Mild Steel LPG Barbecues"," Tandoor, Height 481-500 Millimeter",
    "Large compartmental stainless steel tiffin",
    "New lpg cooking appliances",
    "Air curtain",
    "Rice boiler",
    "Chapati Warmer",
    "Roti Making Machine Auto matic "," Semi Automatic",
    "Meat Cutting Machine",
    "Idli Steamer",
    "SS Thermos"
],
# "SOLAR": 
    [
    "Solar PV Panel",
    "Solar PV Plant",
    "2 V Solar Battery cells",
    "Solar inverter",
    "Solar Tublar Batteries",
    "Solar Street Light all Type",
    "Solar water Heater",
    "Solar water pump"
],
# "WATER TREATMENT": 
    [
    "All Types of Commercial RO PLANTS",
    "STP",
    "WTP"
],
# "SECURITY SURVEILLANCE": 
    [
    "CCTV",
    "Body Worn Camera",
    "Anti climb Fence",
    "Electric Fence",
    "Chainlink Fence",
    "Picket Steel",
    "Barbed Wire",
    "Punched Tape concertina Coil PTCC",
    "UAV",
    "Nano Uav",
    "AntI Drone system",
    "High Intensity Light Infrared beam",
    "Handheld GPS",
    "Convex Security Mirror"
],
# "ELECTRO OPTICS": 
    [
    "Hand held Thermal Imager",
    "Weapon Sites",
    "PNVG",
    "Lorros",
    "Clip On Weapon Sites",
    "Multi Function Laser Aiming System"
],
# "TACTICAL ITEMS": 
    [
    "Miltary Rain Poncho",
    "Ghilly Suit",
    "Jungle Boots",
    "Rucksack Bags",
    "3D Multi Spectral Camo Vehicle Cover",
    "Shooting Range",
    "Weapon Support system",
    "Long Range Acoustic Hailing Device",
    "3d Multi Spectral Camo Dress",
    "Bola wrap Remote Restrain device"
],
# "MATERIAL "," CONSTRUCTION EQUIPMENT": 
    [
    "JCB Bacholoader",
    "Skid steer Loader",
    "Cranes",
    "Forklifts"
],
# "SWACHH BHARAT ITEMS": 
    [
    "Waste Management Plants",
    "Road Sweeping Machines",
    "Sewer Suction Machines",
    "Dustbin "," SS","FRP",
    "Commercial Vaccum Cleaner",
    "Sanitary Napkins Incinetator Machine with Smoke ControlUnit",
    "SANITARY NAPKIN VENDING MACHINE"
],
# "ENERGY SOLUTIONS": 
    [
    "DG SETS",
    "Automobile Batteries other batteries",
    "Fuel cell genrators",
    "Inverters"
],
# "AMC SERVICES": 
    [
    "Amc of DG Sets and Transformer",
    "AMC OF COMMERCIAL KITCHEN EQUIPMENT",
    "AMC OF Gym EQUIPMENT"
],
# "GYM EQUIPMENT": 
    [
    "ALL Types of commercial Gym Equipment",
    "Outdoor Gym"
],
# "COMPUTER "," ADVANCE SECURITY SOLUTIONS": 
    [
    "Computer and peripherals",
    "Data Management solutions",
    "Access Control Solutions",
    "Cyber Security Solutions",
    "Video Survelliance & Analytics Solutions"
]
]

SearchKeywords,product = [ 
 [ "Electric Wires/Cable" ]]

gem(SearchKeywords,product)
