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
# import close_date_caculate

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

from lib.gem_card import gem_find
from lib.sql_upload import sql

gemlog_="gem_log.txt"

from selenium.webdriver.chrome.options import Options
def gem_funtion(ministry_name, Organization_name):
    options = Options()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "download_pdf"),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options)

    for org_name in Organization_name:

        driver.get('https://bidplus.gem.gov.in/advance-search')
        sleep(0.1)

        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )

        query_on = '''
        SELECT * 
        FROM tender_data 
        WHERE department = ? 
        AND (end_date > CAST(GETDATE() AS DATE)) 
        AND (Cancel IS NULL OR Cancel = '');
        '''

        query_close = '''
        SELECT * 
        FROM tender_data 
        WHERE department = ? 
        AND end_date < CAST(GETDATE() AS DATE);
        '''


        df_on = pd.read_sql(query_on, conn, params=[org_name])
        df_close = pd.read_sql(query_close, conn, params=[org_name])
        conn.close()

        gem_ids = df_on['tender_id'].tolist()
        gem_ids_copy = gem_ids.copy()
        
        close_tender_id_list = df_close['tender_id'].tolist()
        
        extracted_data = []

        def create_window():
                import tkinter as tk
                from tkinter import ttk
                root = tk.Tk()
                root.title("Click to Destroy")

                ttk.Button(root, text="Close Window", command=root.destroy).pack(padx=20, pady=20)

                root.mainloop()
        create_window()

        
        card_count = 1

        live_tenders = org_name + ":\n"
        try:
            while True:
             
                try:
                    card_elements = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
                except: break

                for card in card_elements:
                    bid_title = card.find_element(By.CLASS_NAME, 'bid_no_hover')
                    live_tenders += str(card_count) + f". {bid_title.text}\n"
                    card_count += 1

                    try:
                        json_data = gem_find(driver, card_elements, card, gem_ids, org_name, ministry_name, close_tender_id_list,gem_ids_copy)
                        if json_data: extracted_data.append(json_data)
                    except: pass
                
                try:
                    next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]")))
                    next_button.click()
                except: break
                      
        except:
            print(f"main loop brok for {ministry_name}: {org_name}") 
        
        

        
        with open('gemlog_.txt', 'a', encoding='utf-8') as outfile:
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
        # cancelled_fun(driver,gem_ids)

    driver.quit()

def gem():
    try:
        max_threads = 4
        threads = []

        # MINISTRY_list =  [["MINISTRY OF HOME AFFAIRS", ["Roti Making Machine"]]]
        MINISTRY_list =  [["MINISTRY OF DEFENCE", ["INDIAN ARMY"]]]

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

# ongc full form and Ntpc