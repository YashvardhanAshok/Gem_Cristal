import pyodbc
import pandas as pd

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM tender_data"
df = pd.read_sql(query, conn)

# Print column headers
print("Column headers:", df.columns.tolist())

id_array = df['tender_id'].tolist()

total_entries = len(id_array)
print(f"Total entries: {total_entries}")

['id', 'date_of_search', 'tender_id', 'element_put', 'item_description', 'qty', 'start_date', 'end_date', 'end_time', 'day_left_formula', 'emd_amount', 'tender_value', 'item_category', 'consignee_reporting', 'address', 'MSE', 'ministry', 'department', 'branch', 'link_href', 'file_path', 'matches', 'matched_products', 'status', 'L_Placeholder', 'Live']
# just completed Indian army and air force   

# Total Tender add today: 2,787
# Total tender: 7813

# monday
# 3603
# 4987 
# 4249

# tuseday
# 4743
# 4765
# 5026

# wednesday
# 6159, 6218, 6754 , 7813

# friday
# 7908, 9288

# satady
# 9514, 10864, 10984