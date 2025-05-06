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


# # filter data true and False 
# import os
# import json

# product = [
#   ["Electric Cable",'"Electric Wires', "A.C Static Meter", "Lightning Arrestor", "Miniature Circuit Breaker Switches"],
#   ["Solar Street Light", "Solar Power Plant", "Solar Water Heater", "Solar Lantern", "Solar Battery"],
#   ["Roti Making Machine", "Milk Boiler", "Dough Kneader", "Bain Marie", "Commercial Mixer", "Wet Grinder", "Vegetable Cutter", "Rice Boiler", "Idli Steamer", "Oven", "Tandoor", "Water Dispenser", "Water Cooling"],
#   ["Hand Held Gas Detector", "Under Water Torch"],
#   ["Fuel Cell"],
#   ["Ppgi Sheet", "Plywood", "Puff Shelter", "Puff Cabin", "Gi Pipe", "Cement", "Bricks", "Sand", "Sanitary Items", "Hardware Item", "Flooring"],
#   ["Online UPS", "Hybrid UPS"],
#   ["Ghillie Suits"],
#   ["X-ray Machine", "Patient Bed Fowler", "All Range Hospital Furniture", "Patient Care Mattress"],
#   ["Under Water Torch"],
#   ["Rucksack Bags"],
#   ["Honey Sucker / Sewer Cum Jetting Machine", "Jet Spray", "Vaccum Cleaner", "Wheel Barrow", "Incinerators", "Dustbin", "FRP Tank", "Bucket Mop Wringer Trolly"],
#   ["RO (Reverse Osmosis)", "STP (Sewage Treatment Plants)", "Battery"],
#   ["Less Lethal Weapons", "CEW (Conducted Electrical Weapon)", "Remote Restraint Device", "HHTI (Hand Held Thermal Imagers)", "Weapon Sight", "Search Light", "GPS (Global Positioning System)", "Satellite Tracker", "Unmanned Aerial Vehicle", "Robotics"],
#   ["Monitor", "Printer", "Speakers", "Headphones", "Projector", "GPS", "Plotter", "Braille Embosser", "3D Printer", "Tablet", "Walkie Talkie", "Software", "Software Defined Radio", "Cyber Forensics Software"]
# ]

# # Flatten product list
# flat_products = [item.lower() for sublist in product for item in sublist]

# # json_path = os.path.join(os.path.dirname(__file__), 'website', 'json', 'gem.json')
# json_path = os.path.join(os.path.dirname(__file__), 'db',"json", 'MINISTRY OF HOME AFFAIRS.json')

# # Load JSON file
# with open(json_path, 'r', encoding='utf-8') as f:
#     data = json.load(f)

# # Update each item
# for item in data:
#     title = item.get("title", "").lower()
#     item["matches"] = any(prod in title for prod in flat_products)

# # Save the updated data
# with open(json_path, 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=2, ensure_ascii=False)
