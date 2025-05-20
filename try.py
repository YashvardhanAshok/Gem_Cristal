download_path=r"C:\vs_code\TenderHunter2.1.3\download_pdf\GeM-Bidding-7862763.pdf"
import os
import pdfplumber
import re
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
                            if key and 'MSE Purchase Preference' in key and value:
                                MSE_value = value
                                print()
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
                Beneficiary = ['']
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

        try:
            try:
                event_data["ITEM DESCRIPTION"] = Item_Category
            except:
                pass
            event_data["QTY"] = Total_Quantity
                
        except:
            pass
        
        event_data["EMD AMOUNT"] = emd_amount
        event_data["TENDER VALUE"] = Tender_value
        try:
            event_data["ITEM CATEGORY"] = Item_Category
        except:
            pass
        event_data["MSE"] = MSE_value
        
        event_data["Consignee Reporting"] = Consignee_Reporting_list 
        event_data["ADDRESS"] = Address_list

        
        # event_data["DEPARTMENT"] = department_address_parts[1]
        event_data["BRANCH"] = Beneficiary[0]
        event_data["file_path"] = download_path
        
print(event_data)


{'ITEM DESCRIPTION': '', 'QTY': '', 'EMD AMOUNT': 103000.0, 'TENDER VALUE': '', 'ITEM CATEGORY': '', 'MSE': '', 'Consignee Reporting': ['Shambhu Kumar', 'Pankaj Dwivedi', 'Yatendra Kumar\nRajput', 'Prashant Kumar\nSahu'], 'ADDRESS': ['442705,Commandant 9 Bn,\nCRPF, Pranhita Police Complex,\nAheri, TQ. Aheri, Pin- 442705', '934024,Commandant 24 Bn,\nCRPF, Yatriniwas, Jawahar\nTunnel, Kulgam, J&K, Pin-\n934024.', '799012,Group Centre CRPF,\nAgartala ( Tripura), Tripura,\nWest Tripura-799012', '767001,189 BN, CRPF,\nGoushala Shantipara Balangir,\nODISHA-767001'], 'BRANCH': '', 'file_path': 'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-6721012.pdf'}