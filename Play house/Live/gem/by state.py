import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import traceback
import time
import pandas as pd
import json
import os
from datetime import date
from datetime import datetime as ds
import pyodbc
from datetime import datetime
from selenium.webdriver.chrome.options import Options

today = date.today()

from time import sleep
import time

import requests
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
from lib.gem_card import gem_find


def convert_date_format(date_str):
    date_obj = ds.strptime(date_str, "%d-%m-%Y")
    return date_obj.strftime("%d-%b-%Y")

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
            try:
                tender_id = tender_data["TENDER ID"]
                cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (tender_id,))
                exists = cursor.fetchone()[0]

                try: end_date = datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date()
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
                        SET end_date = ?, end_time = ?, extended = ?,Cancel	 = ?, state= ? 
                        WHERE tender_id = ?
                    """
                    cursor.execute(update_sql, (end_date, end_time, extended,"", str(tender_data.get("state", "")),  tender_id))
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
                    matches, matched_products, organisation,state
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
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
                    str(tender_data.get("state", "")),
                    
                )

                cursor.execute(insert_sql, values)
                conn.commit()
                print(f"Tender ID {tender_id} inserted successfully.")

            except:print("sql False",tender_data)
        cursor.close()
        conn.close()


gemlog_="gem_log.txt"

def gem_funtion(state):
    options = Options()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), "download_pdf"),
        "download.prompt_for_download": False,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Edge(options=options)

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
    WHERE state = ? 
    AND (end_date > CAST(GETDATE() AS DATE)) 
    AND (Cancel IS NULL OR Cancel = '');
    '''

    query_close = '''
    SELECT * 
    FROM tender_data 
    WHERE state = ? 
    AND end_date < CAST(GETDATE() AS DATE);
    '''


    df_on = pd.read_sql(query_on, conn, params=[state])
    df_close = pd.read_sql(query_close, conn, params=[state])
    conn.close()

    gem_ids = df_on['tender_id'].tolist()
    gem_ids_copy = gem_ids.copy()
    
    close_tender_id_list = df_close['tender_id'].tolist()
    
    location_tab = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'location-tab')))
    location_tab.click()
    sleep(5)



    select_element = driver.find_element("id", "state_name_con")
    select = Select(select_element)
    select.select_by_visible_text(state)
    
    driver.execute_script("searchBid('con')")
    card_count = 1
    extracted_data = []
    live_tenders =''
    try:
        while True:
            
            try:
                card_elements = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
            except: break

            for card in card_elements:
                bid_title = card.find_element(By.CLASS_NAME, 'bid_no_hover')
                live_tenders += str(card_count) + f". {bid_title.text}\n"
                card_count += 1

                org_name=state 
                ministry_name=None
                try:
                    json_data = gem_find(driver, card_elements, card, gem_ids, org_name, ministry_name, close_tender_id_list,gem_ids_copy)
                    json_data['state'] = state
                    if json_data: extracted_data.append(json_data)
                except: pass
            
            try:
                next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='light-pagination']//a[contains(@class, 'next')]")))
                next_button.click()
            except: break
                    
    except:
        print(f"main loop brok for {state}: {state}") 
        traceback.print_exc() 
    
    with open('gemlog_.txt', 'a', encoding='utf-8') as outfile:
        outfile.write(live_tenders + '\n')
    
    try:
        product = [['solar battery cells', 'multi spectral camo vehicle cover', 'printer', 'multi spectral camo dress',"a.c", 'static meter', 'gym', 'kitchen',"bed","hospital", 'amc', 'ac static watthour meters-energy meter', 'access control solutions', 'air freight shipping', 'air curtain', 'all range hospital furniture', 'all types of commercial ro plants', 'all types of wire and cables', 'amc', 'amc of ac', 'amc of commercial kitchen', 'amc of fire extinguishers',"fire extinguishers", 'amc of generators',"generators", 'amc of gym equipement',"gym equipement", 'amc of kitchen equipement', 'amc of lightning arrestors',"lightning", 'amc of ro and irp', 'amc of solar power plant',"solar power plant", 'amc of solar water heaters',"solar water", 'amc of transformers',"transformers", 'amc of dg sets and transformer', 'anti drone system',"drone system","drone", 'anti climb fence',"climb fence","fence", 'automobile batteries other batteries', 'bain marie', 'bain marie', 'barbed wire', 'battery', 'body worn camera', 'bola wrap remote restrain device', 'braille embosser', 'bricks', 'bucket mop wringer trolly', 'butter', 'cctv', 'cew', ' conducted electrical weapon', 'cgi sheet', 'cement', 'chainlink fence', 'change over switch', 'chapati warmer', 'clip on weapon sites', 'commercial mixer', 'commercial vaccum cleaner', 'computer and peripherals', 'construction of admin blocks', 'construction of hospital', 'construction of internal roads', 'construction of klps for defense', 'convex security mirror', 'cranes', 'cyber forensics software', 'cyber security solutions', 'dg sets', 'data management solutions', 'decorative bollard', 'decorative street light', 'development of infrastructure for defense', 'development of sewerage treatement plant', 'development of water supply', 'domestic casserole', 'dough kneader', 'dough kneader 15kg', 'dry ration', 'rice', 'pulses', 'sugar', 'coffee', 'tea', 'dustbin', 'electric fence', 'electric wires/cable', 'electric milk boiler', 'frp', 'frp tank', 'flood light', 'flooring', 'forklifts', 'fresh fruits', 'fresh vegetable', 'fuel cell', 'fuel cell genrators', 'gps', 'gps', 'global positioning system', 'ghillie suits', 'ghilly suit', 'gi pipe', 'gyser', 'hhti (hand held thermal imagers)', 'hand held gas detector',"gas detector", 'hand held thermal imager', 'handheld gps', 'hardware item', 'headphones', 'high intensity light infrared beam', 'honey sucker / sewer cum jetting machine', 'hybrid ups', 'idli steamer', 'incinerators', 'inflatable shelters', 'inverters', 'jcb bacholoader', 'jet spray', 'jungle boots', 'kunda gadi', 'lgsf building', 'large compartmental stainless steel tiffin', 'led bulbs', 'less lethal weapons', 'lighting arrestor', 'lightning arrestor', 'long range acoustic hailing device', 'lorros', 'mcb', 'mccb', 'meat cutting machine', 'mild steel lpg barbecues', 'milk', 'milk boiler', 'miltary rain poncho', 'miniature circuit breaker switches', 'monitor', 'multi function laser aiming system', 'nano uav', 'new lpg cooking appliances', 'oil', 'online ups', 'outdoor gym', 'oven', 'pnvg', 'ppgi sheets', 'patient bed fowler', 'patient care mattress', 'picket steel', 'pickup truck', 'plotter', 'plywood', 'porta cabin', 'portable kitchen', 'portable houses', 'poultry product', 'chicken', 'egg', 'mutton', 'ppgi sheet', 'prefab shelters with puf panel', 'printer', 'projector', 'puff cabin', 'puff shelter', 'punched tape concertina coil ptcc', 'reverse osmosis', 'remote restraint device', 'rice boiler', 'rice boiler', 'road sweeping machines', 'robotics', 'room heater', 'roti making machine', 'roti making machine auto matic', 'rucksack bags', 'sanitary napkin vending machine', 'ss', 'ss thermos', 'stp', 'sewage treatment plants', 'sand', 'sanitary items', 'sanitary napkins incinetator machine with smoke controlunit', 'satellite tracker', 'sea food (fish)', 'search light', 'sedan ', ' suvs', 'semi automatic', 'sewer suction machines', 'shooting range', 'skid steer loader', 'software', 'software defined radio', 'solar battery', 'solar lantern', 'solar pv panel', 'solar panel', 'solar pv plant', 'solar power plant', 'solar street light', 'solar street light all type', 'solar tublar batteries', 'solar water heater', 'solar inverter', 'solar water heater', 'solar water pump', 'speakers', 'street light', 'switch fuse unit', 'tablet', 'tandoor', 'tandoor, height 481-500 millimeter', 'tubes', 'uav', 'under water torch', 'unmanned aerial vehicle', 'vaccum cleaner', 'vegetable cutter', 'video survelliance ', ' analytics solutions', 'wtp', 'walkie talkie', 'waste management', 'waste management plants', 'water bowser', 'water cooling', 'water dispenser', 'water tanker', 'weapon sight', 'weapon sites', 'weapon support system', 'wet grinder', 'wheel barrow', 'x-ray machine', 'xlpe cables', 'water cooler']]
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

        state_list = ["MANIPUR", "NAGALAND", "SIKKIM", "ASSAM", "MEGHALAYA","TRIPURA","ARUNACHAL","MIZORAM"]
        state_list = [ "NAGALAND", "SIKKIM", "ASSAM", "MEGHALAYA","TRIPURA","ARUNACHAL","MIZORAM"]
        # state_list = ["MANIPUR"]
        # state_list = ["CHHATTISGARH","CHHATTISGARH","CHHATTISGARH","CHHATTISGARH"]
        

        for state in state_list:
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                sleep(0.5)

            t = threading.Thread(target=gem_funtion, args=(state,))
            t.start()
            threads.append(t)
    except:
        pass
        traceback.print_exc() 

gem()


