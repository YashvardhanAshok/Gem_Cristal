import os
import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

# filter data true and False 
def json_fexer(MINISTRY_name):
    product = [
      ["Electric Cable",'Electric Wires', "A.C Static Meter", "Lightning Arrestor", "Miniature Circuit Breaker Switches"],
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
    
    product = [
    # "PRE-ENGINEERED BUILDING": 
    [
        "Prefab shelters with puf panel of size 7.620 m x 13.271 m",
        "LGSF Building",
        "Inflatable Shelters",
        "Porta Cabin",
        "Portable houses",
        "Portable Kitchen",
        "PPGI Sheets",
        "CGI Sheet"
    ],
    # "ELECTRICAL": 
        [
        "Led Bulbs / Tubes",
        "Street Light",
        "Flood Light",
        "Gyser",
        "Room Heater",
        "XLPE Cables",
        "All Types of Wire and Cables",
        "MCB",
        "MCCB",
        "Ac static watthour meters-energy meter",
        "Switch fuse unit/Change over Switch",
        "Decorative Street Light",
        "Decorative Bollard",
        "water cooler",
        "Lighting Arrestor"
    ],
    # "COMMERCIAL KITCHEN EQUIPMENT": 
        [
        "Domestic casserole",
        "Bain marie",
        "Wet grinder 5",
        "Dough kneader 15kg",
        "water cooler",
        "Commercial Mixer",
        "Vegetable Cutter",
        "Electric milk boiler",
        "Mild Steel LPG Barbecues/ Tandoor, Height 481-500 Millimeter",
        "Large compartmental stainless steel tiffin",
        "New lpg cooking appliances",
        "Air curtain",
        "Rice boiler",
        "Chapati Warmer",
        "Roti Making Machine Auto matic / Semi Automatic",
        "Meat Cutting Machine",
        "Idli Steamer",
        "SS Thermos"
    ],
    # "SOLAR": 
        [
        "Solar PV Panel",
        "Solar PV Plant",
        "2 V Solar Battery cells",
        "Solar inverter",
        "Solar Tublar Batteries",
        "Solar Street Light all Type",
        "Solar water Heater",
        "Solar water pump"
    ],
    # "WATER TREATMENT": 
        [
        "All Types of Commercial RO PLANTS",
        "STP",
        "WTP"
    ],
    # "SECURITY SURVEILLANCE": 
        [
        "CCTV",
        "Body Worn Camera",
        "Anti climb Fence",
        "Electric Fence",
        "Chainlink Fence",
        "Picket Steel",
        "Barbed Wire",
        "Punched Tape concertina Coil PTCC",
        "UAV",
        "Nano Uav",
        "AntI Drone system",
        "High Intensity Light Infrared beam",
        "Handheld GPS",
        "Convex Security Mirror"
    ],
    # "ELECTRO OPTICS": 
        [
        "Hand held Thermal Imager",
        "Weapon Sites",
        "PNVG",
        "Lorros",
        "Clip On Weapon Sites",
        "Multi Function Laser Aiming System"
    ],
    # "TACTICAL ITEMS": 
        [
        "Miltary Rain Poncho",
        "Ghilly Suit",
        "Jungle Boots",
        "Rucksack Bags",
        "3D Multi Spectral Camo Vehicle Cover",
        "Shooting Range",
        "Weapon Support system",
        "Long Range Acoustic Hailing Device",
        "3d Multi Spectral Camo Dress",
        "Bola wrap Remote Restrain device"
    ],
    # "MATERIAL / CONSTRUCTION EQUIPMENT": 
        [
        "JCB Bacholoader",
        "Skid steer Loader",
        "Cranes",
        "Forklifts"
    ],
    # "SWACHH BHARAT ITEMS": 
        [
        "Waste Management Plants",
        "Road Sweeping Machines",
        "Sewer Suction Machines",
        "Dustbin / SS/FRP",
        "Commercial Vaccum Cleaner",
        "Sanitary Napkins Incinetator Machine with Smoke ControlUnit",
        "SANITARY NAPKIN VENDING MACHINE"
    ],
    # "ENERGY SOLUTIONS": 
        [
        "DG SETS",
        "Automobile Batteries other batteries",
        "Fuel cell genrators",
        "Inverters"
    ],
    # "AMC SERVICES": 
        [
        "Amc of DG Sets and Transformer",
        "AMC OF COMMERCIAL KITCHEN EQUIPMENT",
        "AMC OF Gym EQUIPMENT"
    ],
    # "GYM EQUIPMENT": 
        [
        "ALL Types of commercial Gym Equipment",
        "Outdoor Gym"
    ],
    # "COMPUTER / ADVANCE SECURITY SOLUTIONS": 
        [
        "Computer and peripherals",
        "Data Management solutions",
        "Access Control Solutions",
        "Cyber Security Solutions",
        "Video Survelliance & Analytics Solutions"
    ]
    ]

    # Flatten product list
    flat_products = [item.lower() for sublist in product for item in sublist]

    # Construct path to JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'db', 'json', f'{MINISTRY_name}.json')
    print(f"Reading: {json_path}")

    # Load data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Annotate with match info
    for item in data:
        title = item.get("ITEM DESCRIPTION", "").lower()
        matches = [prod for prod in flat_products if prod in title]
        item["matches"] = bool(matches)
        item["matched_products"] = matches

    # Save updated data
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Updated JSON written with match information.")

import pandas as pd
from collections import defaultdict

def xl_file(MINISTRY_name):
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(os.path.dirname(__file__), 'db',"json", f'{MINISTRY_name}.json')
    excel_path = os.path.join(base_dir, 'db',"xl_file", f'{MINISTRY_name}.xlsx')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Group data by title
    grouped = defaultdict(list)
    for entry in data:
        grouped[entry['ITEM DESCRIPTION']].append(entry)

    summary_data = []
    grouped_rows = []

    for title, entries in grouped.items():
        summary_data.append({
            "Title": title,
            "Entries Count": len(entries)
        })
        
        for entry in entries:
            row = {"Group Title": title}
            row.update(entry)
            grouped_rows.append(row)

    summary_df = pd.DataFrame(summary_data)
    detailed_df = pd.DataFrame(grouped_rows)

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

MINISTRY_list = ['9ZRLmmxP MINISTRY OF COMMUNICATIONS'
,'DWaDzXu0 MINISTRY OF POWER'
,'QCpNKez1 MINISTRY OF HOME AFFAIRS'
,'SQdAXrbv MINISTRY OF CIVIL AVIATION'
,'WBdiDTzq MINISTRY OF HEALTH AND FAMILY WELFARE']

MINISTRY_list =['main']
import traceback
for MINISTRY in MINISTRY_list: 
    try:
        json_fexer(MINISTRY)
        print(f"\nMINISTRY:{MINISTRY}")
        xl_file(MINISTRY)
    except:
        traceback.print_exc() 
        print("\nerror:",MINISTRY)
        print(MINISTRY)
        pass


# json_fexer("gem")
# xl_file("gem")
