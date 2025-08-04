import traceback
import os
from datetime import date
today = date.today()
import pdfplumber
import re

def gem_doc_reader(download_path):
    try:
        with pdfplumber.open(download_path) as pdf:
            emd_amount = None
            epbg_percentage = None 
            Tender_value = None 
            MSE_value = "No"
            Beneficiary = ['NA']
            Address_list = []
            Consignee_Reporting_list = []
            Not_Beneficiary_Found = True
            Item_Category=''
            found_mse = False
            Total_Quantity = 0
            
            for page in pdf.pages:
                try:
                    tables = page.extract_tables()
                    for table in tables:
                                                            
                        if not found_mse:
                            for row_num, row in enumerate(table):
                                if not row or all(cell is None or cell.strip() == '' for cell in row):
                                    continue
                                for i, cell in enumerate(row):
                                    if cell:
                                        norm_cell = re.sub(r'\W+', '', cell.lower())
                                        if "reservedformse" in norm_cell:
                                            if i + 1 < len(row) and row[i + 1]:
                                                value = row[i + 1].strip()
                                            else:
                                                value = next((c.strip() for c in row if c and "reservedformse" not in c.lower()), "No")
                                            MSE_value = "Yes" if "yes" in value.lower() else value
                                            found_mse = True
                                            break
                                if found_mse:
                                    break
                        
                        if not table or len(table) < 2: continue
                        
                        for row in table[1:]:
                            if len(row) >= 2:
                                key, value = row[0], row[1]
                                
                            
                                
                                try: 
                                    if "Total Quantity" in key and value: Total_Quantity = value
                                except: pass
                                
                                try: 
                                    if "Organisation Name" in key and value: Organisation = value.upper()
                                except: pass
                                
                                try: 
                                    if "Department Name" in key and value: Department_Name = value.upper()
                                except: pass
                                
                                try: 
                                    if "Ministry/State Name" in key and value: Ministry_Name = value.upper()
                                except: pass
                                
                                try: 
                                    if "Item Category" in key and value: Item_Category = value
                                except: pass
                                
                                try:
                                    if key and "EMD Amount" in key and value:
                                        try:
                                            emd_amount = float(re.sub(r'[^\d.]', '', value))
                                            if Tender_value == None: Tender_value = emd_amount * 50
                                        except: pass
                                except: pass
                                
                                try:
                                    if key and "Estimated Bid Value" in key and value: Tender_value = value
                                except: pass
                                
                                try:
                                    if "ePBG Percentage" in key: epbg_percentage = value
                                except: pass
                                
                                
                        headers = [cell.strip() if cell else "" for cell in table[0]]
                        if (any("Consignee" in h for h in headers)):
                            try:
                                data = dict(zip(headers, row))
                                address = data.get(next((h for h in headers if "Address" in h), ""), "")
                                consignee = data.get(next((h for h in headers if "Consignee" in h), ""), "")
                                try: consignee = consignee.replace("*", "").strip()
                                except: pass
                                if consignee and consignee not in Consignee_Reporting_list:
                                    Consignee_Reporting_list.append(consignee)

                                address = data.get(next((h for h in headers if "Address" in h), ""), "")
                                try: address = address.replace("*", "").strip()
                                except: pass
                                if address and address not in Address_list:
                                    address = address.replace('\n', '')
                                    Address_list.append(address)

                            except: pass
                                
                except Exception as e:
                    traceback.print_exc()

                try:
                    if (Not_Beneficiary_Found):
                        text = page.extract_text()
                        if "Beneficiary" in text:
                            lines = text.split('\n')
                            for idx, line in enumerate(lines):
                                if "Beneficiary" in line:
                                    for next_line in lines[idx+1:idx+4]:
                                        if "Provn" in next_line:
                                            Beneficiary = ["Provn"]
                                            Not_Beneficiary_Found = False
                                        
                                        elif "CE" in next_line:
                                            Beneficiary = ["Engineer"]
                                            Not_Beneficiary_Found = False

                                        elif "CSO" in next_line:
                                            Beneficiary = ["signal"]
                                            Not_Beneficiary_Found = False
                                            
                                        elif "signal" in next_line.lower():
                                            Beneficiary = ["signal"]
                                            Not_Beneficiary_Found = False

                                        elif "Officer" in next_line:
                                            Not_Beneficiary_Found = False

                                    break
                except: pass

            if Item_Category =='': 
                error = f"\n\n errorerrorerrorerrorerrorerrorerrorerror \n\n in finding Item_Category for: "
            try:
                Item_Category = Item_Category.replace('\n', '')
                event_data = {
                    "DATE OF SEARCH": today.strftime("%d-%b-%Y"),
                    "elementPut": Organisation or "",
                    "MINISTRY": Ministry_Name or "",
                    "DEPARTMENT": Department_Name or "",
                    "ORGANISATION": Organisation or "",
                    "DAY LEFT": "",  # Assuming calculated elsewhere, kept empty for now
                    "EMD AMOUNT": emd_amount or "",
                    "TENDER VALUE": Tender_value or "",
                    "Consignee Reporting": Consignee_Reporting_list or "",
                    "ADDRESS": Address_list or "",
                    "BRANCH": (Beneficiary[0] if Beneficiary and len(Beneficiary) > 0 else ""),
                    "MSE": MSE_value or "",
                    "file_path": download_path or "",
                    "epbg_percentage": epbg_percentage or "",
                    "QTY": int(float(Total_Quantity)) or 0,
                    "ITEM CATEGORY": Item_Category or "",
                    "ITEM DESCRIPTION": Item_Category or "",
                }
                return event_data

            except: 
                traceback.print_exc()
                print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrooooooo")    



    except:
        if os.path.exists(download_path):
            os.remove(download_path)
            print(f"Corrupt PDF removed. Re-downloading might help.: {download_path}")
