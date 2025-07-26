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
    a.append([tender_id,file_path])

# for x in a:
#     tender_id = x[0]
#     address_str = x[1]
#     consignee_str = x[2]
#     update_query = "UPDATE tender_data SET address = ?, consignee_reporting = ? WHERE tender_id = ?"
#     cursor.execute(update_query, (address_str, consignee_str, tender_id))
#     print(f"✅ Updated tender_id: {tender_id}")

print(a)
with open('gemlog_.txt', 'a', encoding='utf-8') as outfile:
    outfile.write(str(a ))





def fix_(tenders):
    a =[]
    for tender in tenders:
        tender_id = tender[0]
        file_path = tender[1]
        if os.path.exists(file_path):
            try:
                with pdfplumber.open(file_path) as pdf:
                    first_page_text = pdf.pages[0].extract_text()
                    if tender_id in first_page_text: 
                        print(f"Tender ID {tender_id} found on the first page.")
                        continue
                    else:
                        print(f"Tender ID {tender_id} NOT found on the first page.")
                        a.append(tender_id)
                        continue
            except Exception as e:
                print(f"Error while processing PDF: {e}")
            except Exception:
                traceback.print_exc()
        else:
            print(f"⚠️ File not found for tender_id: {tender_id}")
    return a


tenders = [item for item in a if "https://bidplus.gem.gov.in" not in item[1]]
a = fix_(tenders)
with open('gemlog_.txt', 'a', encoding='utf-8') as outfile:
    outfile.write(str(a))










# conn.commit()
# cursor.close()
print("✅ All updates committed.")
