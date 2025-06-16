import pyodbc
import pandas as pd
import ast
from datetime import datetime

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

# Fetch data
query = "SELECT * FROM tender_data WHERE id >= 24258 ;"
df = pd.read_sql(query, conn)

# Drop unnecessary columns
columns_to_drop = [
    'id', 'matches', 'matched_products', "element_put", "consignee_reporting", "item_category",
    "date_of_search", "updated_at", 'file_path', 'link_href', 'Live', "extended", "Cancel", "L1_update"
]
df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

# Replace 0s with empty strings
df.replace(0, '', inplace=True)

# Expand L_Placeholder column
def expand_l_placeholder(row):
    try:
        val = row.get("L_Placeholder") or row.get("L Placeholder")
        values = ast.literal_eval(val) if isinstance(val, str) else val
        result = {}
        for i, pair in enumerate(values, 1):
            if isinstance(pair, list) and len(pair) == 2:
                result[f"L{i}"] = pair[0]
                result[f"L{i} Amount"] = pair[1]
        return result
    except Exception:
        return {}

if "L_Placeholder" in df.columns:
    expanded = df.apply(expand_l_placeholder, axis=1, result_type='expand')
    df = pd.concat([df.drop(columns=["L_Placeholder"]), expanded], axis=1)

# Normalize and rename columns
df.columns = [col.replace('_', ' ').title() if col != 'day_left_formula' else 'Day Left' for col in df.columns]

# Compute 'Day Left' from 'Start Date' and 'End Date' if present
if 'Start Date' in df.columns and 'End Date' in df.columns:
    try:
        df['Start Date'] = pd.to_datetime(df['Start Date'], errors='coerce')
        df['End Date'] = pd.to_datetime(df['End Date'], errors='coerce')
        df['Day Left'] = (df['End Date'] - pd.Timestamp.now()).dt.days
        df['Day Left'] = df['Day Left'].apply(lambda x: 'CLOSED' if pd.isna(x) or x < 0 else f"{x} days")
    except Exception:
        pass

# Identify department column
department_col = next((col for col in df.columns if col.strip().lower() == "department"), None)

import os
save_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"xl files")) 
output_file = f"{save_file}/No-workbook.xlsx"

if department_col:
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        workbook = writer.book
        header_format = workbook.add_format({
            'bold': True, 'bg_color': '#D9D9D9',
            'border': 1, 'align': 'center', 'valign': 'vcenter'
        })
        cell_format = workbook.add_format({'text_wrap': True, 'valign': 'top', 'border': 1})
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

        for department, group_df in df.groupby(department_col):
            sheet_name = str(department).strip()[:31] or "Dept"
            sheet_name = "Assam Rifles"  # force if needed

            group_df.to_excel(writer, sheet_name=sheet_name, index=False, startrow=1, header=False)
            worksheet = writer.sheets[sheet_name]

            # Write custom title
            title = f"{sheet_name} – Exported on {date_str}"
            worksheet.merge_range('A1:{}1'.format(chr(65 + len(group_df.columns) - 1)), title, workbook.add_format({
                'bold': True, 'font_size': 14, 'align': 'left'
            }))

            # Write headers manually
            for col_num, value in enumerate(group_df.columns.values):
                worksheet.write(1, col_num, value, header_format)

            # Apply formatting
            worksheet.set_column(0, len(group_df.columns)-1, 18, cell_format)
            worksheet.set_landscape()
            worksheet.fit_to_pages(1, 0)

    print(f"✅ Fast export complete: {output_file}")
else:
    print("❌ 'Department' column not found.")
