import os
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

# filter data true and False 
def json_fexer(MINISTRY_name):
    product = [
      ["Electric Cable",'"Electric Wires', "A.C Static Meter", "Lightning Arrestor", "Miniature Circuit Breaker Switches"],
      ["Solar Street Light", "Solar Power Plant", "Solar Water Heater", "Solar Lantern", "Solar Battery"],
      ["Roti Making Machine", "Milk Boiler", "Dough Kneader", "Bain Marie", "Commercial Mixer", "Wet Grinder", "Vegetable Cutter", "Rice Boiler", "Idli Steamer", "Oven", "Tandoor", "Water Dispenser", "Water Cooling"],
      ["Hand Held Gas Detector", "Under Water Torch"],
      ["Fuel Cell"],
      ["Ppgi Sheet", "Plywood", "Puff Shelter", "Puff Cabin", "Gi Pipe", "Cement", "Bricks", "Sand", "Sanitary Items", "Hardware Item", "Flooring"],
      ["Online UPS", "Hybrid UPS"],
      ["Ghillie Suits"],
      ["X-ray Machine", "Patient Bed Fowler", "All Range Hospital Furniture", "Patient Care Mattress"],
      ["Under Water Torch"],
      ["Rucksack Bags"],
      ["Honey Sucker / Sewer Cum Jetting Machine", "Jet Spray", "Vaccum Cleaner", "Wheel Barrow", "Incinerators", "Dustbin", "FRP Tank", "Bucket Mop Wringer Trolly"],
      ["RO (Reverse Osmosis)", "STP (Sewage Treatment Plants)", "Battery"],
      ["Less Lethal Weapons", "CEW (Conducted Electrical Weapon)", "Remote Restraint Device", "HHTI (Hand Held Thermal Imagers)", "Weapon Sight", "Search Light", "GPS (Global Positioning System)", "Satellite Tracker", "Unmanned Aerial Vehicle", "Robotics"],
      ["Monitor", "Printer", "Speakers", "Headphones", "Projector", "GPS", "Plotter", "Braille Embosser", "3D Printer", "Tablet", "Walkie Talkie", "Software", "Software Defined Radio", "Cyber Forensics Software"]
    ]

    # Flatten product list
    flat_products = [item.lower() for sublist in product for item in sublist]
    # json_path = os.path.join(os.path.dirname(__file__), 'website', 'json', 'gem.json')
    json_path = os.path.join(os.path.dirname(__file__), 'db',"json", f'{MINISTRY_name}.json')

    print(json_path)
    # Load JSON file
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Update each item
    for item in data:
        title = item.get("title", "").lower()
        item["matches"] = any(prod in title for prod in flat_products)

    # Save the updated data
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

        


import pandas as pd
from collections import defaultdict

def xl_file(MINISTRY_name):
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(os.path.dirname(__file__), 'db',"json", f'{MINISTRY_name}.json')
    excel_path = os.path.join(base_dir, 'db',"xl_file", f'{MINISTRY_name}.xlsx')

    # with open(json_path, 'r', encoding='utf-8') as f:
    #     data = json.load(f)

    # grouped = defaultdict(list)
    # for entry in data:
    #     grouped[entry['title']].append(entry)

    # with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    #     for title, entries in grouped.items():
    #         df = pd.DataFrame(entries)
    #         safe_title = title[:30].replace('/', '_').replace('\\', '_')
    #         df.to_excel(writer, sheet_name=safe_title, index=False)

    # print("Excel file 'grouped_tenders.xlsx' has been created.")

    import json
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Group data by title
    grouped = defaultdict(list)
    for entry in data:
        grouped[entry['title']].append(entry)

    # Prepare summary
    summary_data = []
    grouped_rows = []

    for title, entries in grouped.items():
        summary_data.append({
            "Title": title,
            "Entries Count": len(entries)
        })
        
        # Add group label as a row separator (optional visual clarity)
        for entry in entries:
            row = {"Group Title": title}
            row.update(entry)
            grouped_rows.append(row)

    # Create dataframes
    summary_df = pd.DataFrame(summary_data)
    detailed_df = pd.DataFrame(grouped_rows)

    # Write to Excel
    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        summary_df.to_excel(writer, sheet_name='Group Summary', index=False)
        detailed_df.to_excel(writer, sheet_name='All Tenders Grouped', index=False)

    print("Excel file 'grouped_tenders.xlsx' created with grouped data and summary.")
    
    
    



MINISTRY_list = [
    "MINISTRY OF COMMUNICATIONS",
    "MINISTRY OF HOUSING & URBAN AFFAIRS",
    "MINISTRY OF POWER",
    "MINISTRY OF HEALTH AND FAMILY WELFARE",
    "MINISTRY OF DEFENCE",
    "MINISTRY OF CIVIL AVIATION",
    "MINISTRY OF HOME AFFAIRS",
]




for MINISTRY in MINISTRY_list: 
    try:
        json_fexer(MINISTRY)
        print("1")
        xl_file(MINISTRY)
    except:
        print("pass")
        pass

# 