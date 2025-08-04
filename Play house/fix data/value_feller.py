import pyodbc
from lib.sql_upload import sql
from lib.pdf_flie_reader import gem_doc_reader
from time import sleep
import threading
import traceback
import logging

# Suppress noisy pdfminer logs
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# 🧠 Process one chunk of tenders
def data_fixer(tender_chunk):
    print(f"[Thread] Started with {len(tender_chunk)} tenders")
    json = []
    for tender_info in tender_chunk:
        tender_id = tender_info[0]
        try:
            tender_link = tender_info[1]
            pdf_data = gem_doc_reader(tender_link)
            pdf_data["TENDER ID"] = tender_id
            json.append(pdf_data)
            print(f"[OK] Fixed: {tender_id}")
        except Exception as e:
            print(f"[ERROR] Problem with {tender_id}: {e}")
    sql(json)

# 🔀 Split list into N parts as evenly as possible
def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    result = [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]
    print(f"📦 Split into {len(result)} parts.")
    return result

# 🔁 Main function to run threads
def Main(tender_ids, max_threads):
    try:
        threads = []
        item_list = split_into_parts(tender_ids, 6)

        for elements in item_list:
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                sleep(0.5)

            t = threading.Thread(target=data_fixer, args=(elements,))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    except Exception:
        traceback.print_exc()

# 🗄️ Fetch tenders from DB with matching tender_ids
def fetch_local_tender_files(tender_ids):
    try:
        if not tender_ids:
            print("⚠️ No tender IDs provided.")
            return []

        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        formatted_ids = ','.join(f"'{tid.strip()}'" for tid in tender_ids)

        query = f"""
            SELECT tender_id, file_path 
            FROM tender_data 
            WHERE tender_id IN ({formatted_ids})
        """

        cursor.execute(query)
        result = []

        for tender_id, file_path in cursor.fetchall():
            if file_path and not str(file_path).lower().startswith(('http://', 'https://')):
                result.append([tender_id, file_path])

        return result

    except pyodbc.Error as e:
        print("❌ Database error:", e)
        return []

    finally:
        if 'conn' in locals():
            conn.close()

# 🚀 Entry point
if __name__ == "__main__":
    # Prepare list of tender IDs
    raw_data ="""
   GEM/2025/B/6182163
    GEM/2025/B/6181340


    """
    data_array = list(set(line.strip() for line in raw_data.strip().splitlines() if line.strip()))

    # Fetch from DB
    local_files = fetch_local_tender_files(data_array)
    print(f"📄 Total tenders to process: {len(local_files)}")

    # Start threaded processing
    Main(local_files, max_threads=6)
