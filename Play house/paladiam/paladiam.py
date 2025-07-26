import pandas as pd
import re
from collections import defaultdict
import os

# Define the input file name
a = 'punjab police'
csv_path = os.path.join('final', 'paladiam', 'result', f'{a}.csv')

# Read the CSV using the correct path
df = pd.read_csv(csv_path)

# Dictionary to store item -> set of ref_nos
item_dict = defaultdict(set)

# Loop through each row
for _, row in df.iterrows():
    ref_no = row['ref_no']
    title = row['title'].lower()  # normalize case

    # Split title by ',', 'and', 'or'
    items = re.split(r'\s*,\s*|\s+and\s+|\s+or\s+', title)

    # Remove empty strings and duplicates
    items = set(item.strip() for item in items if item.strip())

    # Update dictionary
    for item in items:
        item_dict[item].add(ref_no)

# Prepare the result list
result = []
for item, refs in item_dict.items():
    result.append({
        'item': item,
        'count': len(refs),
        'ref_nos': ', '.join(refs)  # convert list to string for Excel readability
    })

# Convert to DataFrame and save to Excel
result_df = pd.DataFrame(result)
excel_filename = f"{a}.xlsx"
result_df.to_excel(excel_filename, index=False)

print(f"Excel file saved as {excel_filename}")


""