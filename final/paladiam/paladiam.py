import pandas as pd
import os
from glob import glob
import ast

# Define folder path
folder_path = r'C:\vs_code\TenderHunter2.1.3\final\paladiam\result'
csv_files = glob(os.path.join(folder_path, '*.csv'))
df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    
    # Step 1: Clean result_bid_value
    if 'result_bid_value' in df.columns:
        df = df[df['result_bid_value'].notnull()]
    
    # Step 2: Clean bid_rank
    if 'bid_rank' in df.columns:
        df = df[df['bid_rank'].isnull() | (df['bid_rank'].astype(str).str.strip() == "") | (df['bid_rank'].astype(str).str.upper() == "L1")]
    
    df_list.append(df)

# Combine all cleaned DataFrames
final_df = pd.concat(df_list, ignore_index=True)

### === CSV 1: Count duplicates by title and list unique organisations === ###
if 'title' in final_df.columns and 'organisation' in final_df.columns:
    group_df = (
        final_df.groupby('title')
        .agg(
            count=('title', 'count'),
            organisations=('organisation', lambda x: list(set(x.dropna())))
        )
        .reset_index()
    )
    group_df.to_csv(os.path.join(folder_path, 'Grouped_Title_Count.csv'), index=False)

### === CSV 2: Extract only first value from ref_no list === ###
if 'ref_no' in final_df.columns:
    def extract_first_ref(ref):
        try:
            items = ast.literal_eval(ref) if isinstance(ref, str) and ref.startswith("[") else [ref]
            return items[0] if items else None
        except:
            return ref  # fallback if not a list or bad format

    final_df['ref_no_first'] = final_df['ref_no'].apply(extract_first_ref)
    final_df[['ref_no_first']].to_csv(os.path.join(folder_path, 'First_Ref_No_Only.csv'), index=False)

print("CSV 1 and CSV 2 created successfully.")
