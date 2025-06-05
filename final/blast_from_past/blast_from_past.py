import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os
from datetime import date
from datetime import datetime as ds
import pyodbc
from datetime import datetime

today = date.today()

from time import sleep
import re
max_page= 9999

def clean_text(text):
    if text:
        text = re.sub(r'\(cid:\d+\)', '', text)
        text = text.replace('\n', ' ').replace('\r', ' ').strip()
        return text

    return ''

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

            # Check if tender_id exists in DB
            cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (tender_id,))
            exists = cursor.fetchone()[0]


            try:
                end_date = datetime.strptime(tender_data["END DATE"], "%d-%b-%Y").date()
            except Exception as e:
                raw_end_date = tender_data.get("END DATE") or tender_data.get("closed_date")
                try:
                    end_date = datetime.strptime(raw_end_date, "%d %b %Y").date()
                except Exception as e:
                    print(f"Invalid END DATE for tender {tender_id}: {raw_end_date}")
                    end_date = None

            end_time = str(tender_data.get("END Time", ""))
            date_of_search_str = tender_data.get("DATE OF SEARCH", "")
            try:
                extended = datetime.strptime(date_of_search_str, "%d-%b-%Y").strftime("%Y-%m-%d")
            except Exception as e:
                print(f"Invalid DATE OF SEARCH for tender {tender_id}: {date_of_search_str}")
                extended = ""

            if exists:
                update_sql = """
                    UPDATE tender_data
                    SET end_date = ?, end_time = ?, extended = ?
                    WHERE tender_id = ?
                """
                cursor.execute(update_sql, (end_date, end_time, extended, tender_id))
                print(f"Tender ID {tender_id} exists. Updated end_date, end_time, extended.")
                conn.commit()
                continue

            insert_sql = """
            INSERT INTO tender_data (
                date_of_search, tender_id, element_put, item_description, qty,
                 end_date, end_time, day_left_formula,
                emd_amount, tender_value, item_category,
                consignee_reporting, address, MSE,
                ministry, department, branch, link_href, file_path,
                matches, matched_products
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """
            end_time = "12:00 PM"

            values = (
                datetime.strptime(tender_data["DATE OF SEARCH"], "%d-%b-%Y").date(),
                str(tender_data["TENDER ID"]),
                str(tender_data.get("elementPut", "")),
                str(tender_data.get("ITEM DESCRIPTION", "")),
                int(tender_data.get("QTY", 0)),
                end_date,
                end_time,
                str(tender_data.get("DAY LEFT", "")),
                float(tender_data.get("EMD AMOUNT") or 0),
                float(tender_data.get("TENDER VALUE") or 0),
                str(tender_data.get("ITEM CATEGORY", "")),
                json.dumps(tender_data.get("Consignee Reporting", [])),
                json.dumps(tender_data.get("ADDRESS", [])),
                str(tender_data.get("MSE", '')),
                str(tender_data.get("MINISTRY", "")),
                str(tender_data.get("DEPARTMENT", "")),
                str(tender_data.get("BRANCH", "")),
                str(tender_data.get("link", '')),
                str(tender_data.get("file_path", '')),
                int(tender_data.get("matches", False)),
                json.dumps(tender_data.get("matched_products", []))
            )

            cursor.execute(insert_sql, values)
            conn.commit()
            print(f"Tender ID {tender_id} inserted successfully.")

        cursor.close()
        conn.close()

def bidassist(driver,tenders,MINISTRY,department):
    cards = driver.find_elements(By.CSS_SELECTOR, ".col.s12 .block.card.clearfix")
    for card in cards:
        data = {
            "DATE OF SEARCH": today.strftime("%d-%b-%Y"),
            "MINISTRY":MINISTRY,
            "DEPARTMENT":department,
            "TENDER ID": "",
            "link": "",
            "ADDRESS": [],
            "description": "",
            "END DATE": "",
            "tender_amount": "",
            "emd_amount":"",
            "ITEM CATEGORY":"",
        }

        try:
            a_tag = card.find_element(By.CSS_SELECTOR, "a.anchor-wrap")
            data["link"] = a_tag.get_attribute("href")
            title = a_tag.get_attribute("title")

            match = re.search(r"(GEM/\d{4}/B/\d+)", title)
            if match:
                data["TENDER ID"] = match.group(1)
            
            else: continue
        except: continue

        try:
            gem_span = card.find_element(By.CSS_SELECTOR, "span.inline-heading.disable")
            data["gem"] = gem_span.get_attribute("title")
        except:
            pass

        try:
            loc_span = card.find_element(By.CSS_SELECTOR, ".tender-locations span")
            data["ADDRESS"] = [loc_span.text.strip()]
        except:
            pass

        try:
            desc_div = card.find_element(By.CSS_SELECTOR, "div.description")
            data["ITEM CATEGORY"] = data["description"] = desc_div.get_attribute("title").replace("Description:", "").strip()
             
        except:
            pass

        try:
            closed_date = card.find_element(By.CSS_SELECTOR, "span.truncate.textHeading")
            data["END DATE"] = closed_date.text.strip()
        except:
            pass

        try:
            amount_span = card.find_element(By.CSS_SELECTOR, ".amount-wrap .truncate.textHeading")
            amt_text = amount_span.text.strip().replace(",", "")

            # Convert to int if it's all digits
            if amt_text.isdigit():
                tender_amount = int(amt_text)
                data["tender_amount"] = tender_amount
                data["emd_amount"] = tender_amount // 50 
            else:
                pass
        except:
            pass

        tenders.append(data)


db_lock = threading.Lock()

def bidassist_funtion(past_tender_name,iteams):
    driver = webdriver.Edge()
    MINISTRY = past_tender_name[0]
    department = past_tender_name[1] 
    tenders = []
    department2 = department.replace(" ", "%20")
    
    for iteam in iteams:  
        # iteam = iteam.replace(" ", "%20")
        tender_id = iteam.replace("/", "%2f")
        # GEM%2F2024%2FB%2F5179431
        link= f"https://bidassist.com/all-tenders/archived?sort=RELEVANCE:DESC&pageNumber=0&pageSize=10&tenderType=ARCHIVED&tenderEntity=TENDER_LISTING&year=2024&filter=KEYWORD:{tender_id}&removeUnavailableTenderAmountCards=false&removeUnavailableEmdCards=false"
        # link= f"https://bidassist.com/all-tenders/archived?sort=RELEVANCE:DESC&pageNumber=0&pageSize=10&tenderType=ARCHIVED&tenderEntity=TENDER_LISTING&year=2025&filter=PURCHASER_NAME:{department2}&filter=KEYWORD:{iteam}&removeUnavailableTenderAmountCards=false&removeUnavailableEmdCards=false"
        driver.get(link)
        sleep(0.1)
        

        while True:
            try:
                bidassist(driver,tenders,MINISTRY,department)

                next_button = driver.find_element(By.CSS_SELECTOR, "ul[role='navigation'] li.next a[rel='next'][aria-disabled='false']")
                next_href = next_button.get_attribute("href")

                if next_href:
                    driver.get(next_href)
                else:
                    break  
            except:
                break
    sql(tenders)
    driver.quit()
    

tender_ids = [
    'GEM/2024/B/5113433', 'GEM/2024/R/378645', 'GEM/2024/B/4568536', 'GEM/2024/R/329749',
    'GEM/2024/B/5003503', 'GEM/2024/R/427460', 'GEM/2024/B/5512048', 'GEM/2024/B/5558220',
    'GEM/2024/B/5612315', 'GEM/2024/B/5483168', 'GEM/2024/B/5659812', 'GEM/2024/B/5526863',
    'GEM/2024/B/5511326', 'GEM/2024/R/422113', 'GEM/2024/B/5631624', 'GEM/2024/B/5643064',
    'GEM/2024/B/5643002', 'GEM/2024/B/5649841', 'GEM/2024/B/5618063', 'GEM/2024/B/5643089',
    'GEM/2024/B/5566511', 'GEM/2024/R/418591', 'GEM/2024/B/5510221', 'GEM/2024/R/416293',
    'GEM/2024/B/5581211', 'GEM/2024/B/5505387', 'GEM/2024/R/412755', 'GEM/2024/B/5536711',
    'GEM/2024/B/5580968', 'GEM/2024/B/5415863', 'GEM/2024/B/5185116', 'GEM/2024/R/408635',
    'GEM/2024/B/5540465', 'GEM/2024/B/5526860', 'GEM/2024/B/5086729', 'GEM/2024/R/404493',
    'GEM/2024/B/5358015', 'GEM/2024/R/404082', 'GEM/2024/B/5562499', 'GEM/2024/B/5386437',
    'GEM/2024/B/5534853', 'GEM/2024/B/5477215', 'GEM/2024/B/5477554', 'GEM/2024/B/5477680',
    'GEM/2024/B/5430828', 'GEM/2024/B/5333788', 'GEM/2024/R/393592', 'GEM/2024/B/5400689',
    'GEM/2024/B/5401591', 'GEM/2024/B/5400209', 'GEM/2024/B/5413073', 'GEM/2024/B/5396459',
    'GEM/2024/B/4781381', 'GEM/2024/R/389911', 'GEM/2024/B/5299482', 'GEM/2024/R/386506',
    'GEM/2024/B/5240830', 'GEM/2024/R/386406', 'GEM/2024/B/5247453', 'GEM/2024/R/386409',
    'GEM/2024/B/5253268', 'GEM/2024/R/386413', 'GEM/2024/B/5240700', 'GEM/2024/R/383401',
    'GEM/2024/B/5318254', 'GEM/2024/B/5335423', 'GEM/2024/B/5234770', 'GEM/2024/R/380614',
    'GEM/2024/B/5319954', 'GEM/2024/B/5151263', 'GEM/2024/B/5202790', 'GEM/2024/R/377167',
    'GEM/2024/B/5179431', 'GEM/2024/R/375707', 'GEM/2024/B/5126691'
]



past_tender_name=["MINISTRY OF HOME AFFAIRS","Assam Rifles"]
    
# bidassist_funtion(past_tender_name,iteams)
bidassist_funtion(past_tender_name,tender_ids)



