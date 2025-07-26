import pyodbc
from lib.sql_upload import sql
from lib.pdf_flie_reader import gem_doc_reader


def fetch_local_tender_files():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT tender_id, file_path FROM tender_data")
        result = []

        for tender_id, file_path in cursor.fetchall():
            if file_path and not str(file_path).lower().startswith(('http://', 'https://')):
                result.append([tender_id, file_path])

        return result

    except pyodbc.Error as e:
        print("Database error:", e)
        return []

    finally:
        if 'conn' in locals():
            conn.close()

# Example usage
data_array = fetch_local_tender_files()

data_array = [['GEM/2025/B/6483446', 'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-8124036.pdf']]

json = []
for tender_info in data_array:
    tender_id = tender_info[0]
    tender_link = tender_info[1]
    pdf_data = gem_doc_reader(tender_link)
    pdf_data["TENDER ID"] = tender_id
    json.append(pdf_data)
print(json)
sql(json)




[{'DATE OF SEARCH': '26-Jul-2025', 'elementPut': 'INDO TIBETAN BORDER POLICE (ITBP)', 'MINISTRY': 'MINISTRY OF HOME AFFAIRS', 'DEPARTMENT': 'CENTRAL ARMED POLICE FORCES', 'ORGANISATION': 'INDO TIBETAN BORDER POLICE (ITBP)', 'DAY LEFT': '', 'EMD AMOUNT': 39760.0, 'TENDER VALUE': 1988000.0, 'Consignee Reporting': ['Manoj Sah'], 'ADDRESS': ['246429,8th bn itbp gauchar'], 'BRANCH': 'NA', 'MSE': 'No', 'file_path': 'C:\\vs_code\\TenderHunter2.1.3\\download_pdf\\GeM-Bidding-8124036.pdf', 'epbg_percentage': '5.00', 'QTY': 2760, 'ITEM CATEGORY': 'Chilly as per IS 2322 (Q4) , Spices And Condiments -Coriander, Whole And Ground (V2) Conforming to IS 2443(Q3) , FPO - Spices And Condiments - Turmeric, Whole AndGround As Per IS 3576 (Q2) , Spices and Condiments -Cloves, Whole and Ground as per IS 4404 (Q3) , LargeCardamom (Badi Elaichi) as per IS 13446 (Q4) , BlackPepper (Q4) , Fenugreek (Methi) as per IS 3795 (Q4) , Cumin(Q4)', 'ITEM DESCRIPTION': 'Chilly as per IS 2322 (Q4) , Spices And Condiments -Coriander, Whole And Ground (V2) Conforming to IS 2443(Q3) , FPO - Spices And Condiments - Turmeric, Whole AndGround As Per IS 3576 (Q2) , Spices and Condiments -Cloves, Whole and Ground as per IS 4404 (Q3) , LargeCardamom (Badi Elaichi) as per IS 13446 (Q4) , BlackPepper (Q4) , Fenugreek (Methi) as per IS 3795 (Q4) , Cumin(Q4)', 'TENDER ID': 'GEM/2025/B/6483446'}]
