import pdfplumber
import re
import json
from datetime import date
import os

download_path = r'C:\vs_code\TenderHunter2.1.3\download_pdf\yes.pdf'
today = date.today()
extracted_data = []

if os.path.exists(download_path):
    with pdfplumber.open(download_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"

        emd_match = re.search(r"EMD Amount[^|\n]*\|\s*([\d,]+)", full_text)
        epbg_match = re.search(r"ePBG Percentage[^|\n]*\|\s*([\d.]+)", full_text)
        epbg_duration_match = re.search(r"Duration of ePBG required[^|\n]*\|\s*([\d.]+)", full_text)

        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                headers = table[0]
                if any("S.No" in (cell or "") for cell in headers):
                    for row in table[1:]:
                        row = row + [""] * (len(headers) - len(row))
                        data = dict(zip(headers, row))

                        event_data = {
                            "dateOfSearch": today.strftime("%d-%b-%Y"),
                            "website": 'GEM',
                            "EMD Amount": emd_match.group(1) if emd_match else None,
                            "ePBG Percentage": epbg_match.group(1) if epbg_match else None,
                            "Duration of ePBG required": epbg_duration_match.group(1) if epbg_duration_match else None,
                            "Consignee Reporting": data.get(next((h for h in headers if "Consignee" in (h or "")), ""), "").strip(),
                            "Address": data.get(next((h for h in headers if "Address" in (h or "")), ""), "").strip(),
                            "Quantity": data.get(next((h for h in headers if "Quantity" in (h or "")), ""), "").strip(),
                            "Delivery Days": data.get(next((h for h in headers if "Delivery Days" in (h or "")), ""), "").strip()
                        }

                        extracted_data.append(event_data)

print(json.dumps(extracted_data, indent=4))
