import json
import threading
from datetime import datetime
import pyodbc

db_lock = threading.Lock()
import traceback
# test_tender_data = [{
#     'DATE OF SEARCH': '26-Jul-2025',
#     'elementPut': 'ASSAM RIFLES',
#     'MINISTRY': 'MINISTRY OF HOME AFFAIRS',
#     'DEPARTMENT': 'CENTRAL ARMED POLICE FORCES',
#     'ORGANISATION': 'ASSAM RIFLES',
#     'DAY LEFT': '',
#     'EMD AMOUNT': 25834.0,
#     'TENDER VALUE': '861120',
#     'Consignee Reporting': ['Anil Kumar K M'],
#     'ADDRESS': ['793010,HQ Directorate General\nAssam Rifles, Laitkor Shillong-\n793010'],
#     'BRANCH': 'NA',
#     'MSE': 'No',
#     'file_path': 'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-8058147.pdf',
#     'link': 'https://bidplus.gem.gov.in/showbidDocument/8058147',
#     'epbg_percentage': '',
#     'QTY': 0,
#     'ITEM CATEGORY': 'Goods Transport Service – Per Trip based Service - Open\nWater; Water Tank Truck; Medium Tanker',
#     'ITEM DESCRIPTION': 'Goods Transport Service – Per Trip based Service - Open\nWater; Water Tank Truck; Medium Tanker',
#     'TENDER ID': 'GEM/2025/B/6425231',
#     'START DATE': '07-Jul-2025',
#     'END DATE': '28-Jul-2025',
#     'END Time': '11:00 AM',
#     'matches': False,
#     'matched_products': [],
#     'state': 'Meghalaya'
# }]

update_key = {
    'DATE OF SEARCH': 'date_of_search',
    'elementPut': 'element_put',
    'MINISTRY': 'ministry',
    'DEPARTMENT': 'department',
    'ORGANISATION': 'organisation',
    'DAY LEFT': 'day_left_formula',
    'EMD AMOUNT': 'emd_amount',
    'TENDER VALUE': 'tender_value',
    'Consignee Reporting': 'consignee_reporting',
    'ADDRESS': 'address',
    'BRANCH': 'branch',
    'MSE': 'MSE',
    'file_path': 'file_path',
    'link': 'link_href',
    'epbg_percentage': 'epbg_percentage',
    'QTY': 'qty',
    'ITEM CATEGORY': 'item_category',
    'ITEM DESCRIPTION': 'item_description',
    'START DATE': 'start_date',
    'END DATE': 'end_date',
    'END Time': 'end_time',
    'matches': 'matches',
    'matched_products': 'matched_products',
    'state': 'state'
}
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

            for tender in extracted_data:
                try:
                    if not tender or not tender.get("TENDER ID"):
                        continue

                    TENDER_ID = tender["TENDER ID"]

                    cursor.execute("SELECT COUNT(*) FROM tender_data WHERE tender_id = ?", (TENDER_ID,))
                    exists = cursor.fetchone()[0]

                    date_of_search = datetime.strptime(tender["DATE OF SEARCH"], "%d-%b-%Y").strftime("%Y-%m-%d")
                    try:
                        data = {
                            'DATE OF SEARCH': datetime.strptime(tender["DATE OF SEARCH"], "%d-%b-%Y").date(),
                            'elementPut': tender.get("elementPut", ""),
                            'MINISTRY': tender.get("MINISTRY", ""),
                            'DEPARTMENT': tender.get("DEPARTMENT", ""),
                            'ORGANISATION': tender.get("ORGANISATION", ""),
                            'DAY LEFT': tender.get("DAY LEFT", ""),
                            'BRANCH': tender.get("BRANCH", ""),
                            'MSE': tender.get("MSE", ""),
                            'file_path': tender.get("file_path", ""),
                            'link': tender.get("link", ""),
                            'ITEM CATEGORY': tender.get("ITEM CATEGORY", ""),
                            'ITEM DESCRIPTION': tender.get("ITEM DESCRIPTION", ""),
                            'END Time': tender.get("END Time", ""),
                            'START DATE': datetime.strptime(tender["START DATE"], "%d-%b-%Y").date(),
                            'END DATE': datetime.strptime(tender["END DATE"], "%d-%b-%Y").date(),
                            'QTY': int(tender.get("QTY") or 0),
                            'matches': int(tender.get("matches") or 0),
                            'EMD AMOUNT': float(tender.get("EMD AMOUNT") or 0),
                            'TENDER VALUE': float(tender.get("TENDER VALUE") or 0),
                            'Consignee Reporting': json.dumps(tender.get("Consignee Reporting", [])),
                            'ADDRESS': json.dumps(tender.get("ADDRESS", [])),
                            'matched_products': json.dumps(tender.get("matched_products", [])),
                            'state': tender.get("state", ""),
                            'epbg_percentage': tender.get("epbg_percentage", "")
                        }
                    except:
                        data2 = {
                            'END Time': tender.get("END Time", ""),
                        }
                    data2 = {
                            'END Time': tender.get("END Time", ""),
                        }
                    if exists:
                        update_query = "UPDATE tender_data SET "
                        update_values = []

                        for key in data2:
                            if key in update_key:
                                update_query += f"{update_key[key]} = ?, "
                                try:
                                    update_values.append(data2[key])
                                except: pass
                        update_query += "extended = ? WHERE tender_id = ?"
                        update_values.append(date_of_search)
                        update_values.append(TENDER_ID)

                        cursor.execute(update_query, update_values)
                        conn.commit()
                        print(f"Tender extended {TENDER_ID}")
                    else:
                        columns = []
                        placeholders = []
                        insert_values = []

                        for key in data:
                            if key in update_key:
                                columns.append(update_key[key])
                                placeholders.append("?")
                                insert_values.append(data[key])

                        columns.append("tender_id")
                        placeholders.append("?")
                        insert_values.append(TENDER_ID)

                        insert_sql = f"INSERT INTO tender_data ({', '.join(columns)}) VALUES ({', '.join(placeholders)})"
                        cursor.execute(insert_sql, insert_values)
                        conn.commit()
                        print(f"Tender ID {TENDER_ID} inserted successfully.")

                except Exception as e:
                    print("DB Error:", e)
                    
                    print(tender)
                    
                    traceback.print_exc()
                    
                    
            cursor.close()
            conn.close()

    except Exception as e:
        print("DB Error:", e)
        traceback.print_exc()
        
