import pyodbc
import pandas as pd
import os
import pdfplumber
import re
import traceback
import json

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM tender_data WHERE address = '[]'"
df = pd.read_sql(query, conn)
cursor = conn.cursor()
a = []

for index, row in df.iterrows():
    file_path = row['file_path']
    tender_id = row['tender_id']
    if os.path.exists(file_path):
        try:
            with pdfplumber.open(file_path) as pdf:
                Consignee_Reporting_list = []
                Address_list = []

                for page in pdf.pages:
                    try:
                        tables = page.extract_tables()
                        for table in tables:
                            if not table or len(table) < 2:
                                continue

                            headers = [cell.strip() if cell else "" for cell in table[0]]
                            if any("Consignee" in h for h in headers):
                                for data_row in table[1:]:
                                    data = dict(zip(headers, data_row))
                                    
                                    consignee = data.get(next((h for h in headers if "Consignee" in h), ""), "")
                                    if consignee:
                                        consignee = consignee.replace("*", "").strip()
                                        if consignee and consignee not in Consignee_Reporting_list:
                                            Consignee_Reporting_list.append(consignee)

                                    address = data.get(next((h for h in headers if "Address" in h), ""), "")
                                    if address:
                                        address = address.replace("*", "").strip()
                                        if address and address not in Address_list:
                                            Address_list.append(address)
                    except Exception:
                        traceback.print_exc()

            # Save as stringified JSON or comma-separated string (choose one)
            address_str = json.dumps(Address_list)  # or ", ".join(Address_list)
            consignee_str = json.dumps(Consignee_Reporting_list)

            a.append([tender_id,address_str,consignee_str])


        except Exception:
            traceback.print_exc()
    else:
        print(f"⚠️ File not found for tender_id: {tender_id}")

for x in a:
    tender_id = x[0]
    address_str = x[1]
    consignee_str = x[2]
    update_query = "UPDATE tender_data SET address = ?, consignee_reporting = ? WHERE tender_id = ?"
    cursor.execute(update_query, (address_str, consignee_str, tender_id))
    print(f"✅ Updated tender_id: {tender_id}")

conn.commit()
cursor.close()
print("✅ All updates committed.")
