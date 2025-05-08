import os
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

# Define paths
base_dir = os.path.dirname(__file__)
# json_path = os.path.join(base_dir, 'website', 'json', 'gem.json')
json_path = os.path.join(os.path.dirname(__file__), 'db',"json", 'MINISTRY OF HOME AFFAIRS.json')
excel_path = os.path.join(base_dir, 'db',"json", 'MINISTRY OF HOME AFFAIRS.xlsx')

with open(json_path, 'r', encoding='utf-8') as f:
    data = pd.read_json(f)

data.to_excel(excel_path, index=False)
