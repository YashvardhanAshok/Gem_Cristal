import os
import json
import pandas as pd
import traceback
product = [['2 V Solar Battery cells', '3D Multi Spectral Camo Vehicle Cover', '3D Printer', '3d Multi Spectral Camo Dress', 'A.C Static Meter', 'ALL Types of commercial Gym Equipment', 'AMC OF COMMERCIAL KITCHEN EQUIPMENT', 'AMC OF Gym EQUIPMENT', 'Ac static watthour meters-energy meter', 'Access Control Solutions', 'Air Freight Shipping', 'Air curtain', 'All Range Hospital Furniture', 'All Types of Commercial RO PLANTS', 'All Types of Wire and Cables', 'Amc Of Ac', 'Amc Of Commercial Kitchen', 'Amc Of Fire Extinguishers', 'Amc Of Generators', 'Amc Of Gym Equipement', 'Amc Of Kitchen Equipement', 'Amc Of Lightning Arrestors', 'Amc Of Ro And IRP', 'Amc Of Solar Power Plant', 'Amc Of Solar Water Heaters', 'Amc Of Transformers', 'Amc of DG Sets and Transformer', 'AntI Drone system', 'Anti climb Fence', 'Automobile Batteries other batteries', 'Bain Marie', 'Bain marie', 'Barbed Wire', 'Battery', 'Body Worn Camera', 'Bola wrap Remote Restrain device', 'Braille Embosser', 'Bricks', 'Bucket Mop Wringer Trolly', 'Butter', 'CCTV', 'CEW (Conducted Electrical Weapon)', 'CGI Sheet', 'Cement','Chainlink Fence', 'Change over Switch', 'Chapati Warmer', 'Clip On Weapon Sites', 'Commercial Mixer', 'Commercial Vaccum Cleaner', 'Computer and peripherals', 'Construction Of Admin Blocks', 'Construction Of Hospital', 'Construction Of Internal Roads', 'Construction Of Klps For Defense', 'Convex Security Mirror', 'Cranes', 'Cyber Forensics Software', 'Cyber Security Solutions', 'DG SETS', 'Data Management solutions', 'Decorative Bollard', 'Decorative Street Light', 'Development Of Infrastructure For Defense', 'Development Of Sewerage Treatement Plant', 'Development Of Water Supply', 'Domestic casserole', 'Dough Kneader', 'Dough kneader 15kg', 'Dry Ration (Rice , Pulses , Sugar , Coffee, Tea)', 'Dustbin', 'Electric Fence', 'Electric Wires/Cable', 'Electric milk boiler', 'FRP', 'FRP Tank', 'Flood Light', 'Flooring', 'Forklifts', 'Fresh Fruits', 'Fresh Vegetable', 'Fuel Cell', 'Fuel cell genrators', 'GPS', 'GPS (Global Positioning System)', 'Ghillie Suits', 'Ghilly Suit', 'Gi Pipe','Gyser', 'HHTI (Hand Held Thermal Imagers)', 'Hand Held Gas Detector', 'Hand held Thermal Imager', 'Handheld GPS', 'Hardware Item', 'Headphones', 'High Intensity Light Infrared beam', 'Honey Sucker / Sewer Cum Jetting Machine', 'Hybrid UPS', 'Idli Steamer', 'Incinerators', 'Inflatable Shelters', 'Inverters', 'JCB Bacholoader', 'Jet Spray', 'Jungle Boots', 'Kunda Gadi', 'LGSF Building', 'Large compartmental stainless steel tiffin', 'Led Bulbs', 'Less Lethal Weapons', 'Lighting Arrestor', 'Lightning Arrestor', 'Long Range Acoustic Hailing Device', 'Lorros', 'MCB', 'MCCB', 'Meat Cutting Machine', 'Mild Steel LPG Barbecues', 'Milk', 'Milk Boiler', 'Miltary Rain Poncho', 'Miniature Circuit Breaker Switches', 'Monitor', 'Multi Function Laser Aiming System', 'Nano Uav', 'New lpg cooking appliances', 'Oil', 'Online UPS', 'Outdoor Gym', 'Oven', 'PNVG', 'PPGI Sheets','Patient Bed Fowler', 'Patient Care Mattress', 'Picket Steel', 'Pickup Truck', 'Plotter', 'Plywood', 'Porta Cabin', 'Portable Kitchen', 'Portable houses', 'Poultry Product (Chicken, Egg , Mutton)', 'Ppgi Sheet', 'Prefab shelters with puf panel of size 7.620 m x 13.271 m', 'Printer', 'Projector', 'Puff Cabin', 'Puff Shelter', 'Punched Tape concertina Coil PTCC', 'RO (Reverse Osmosis)', 'Remote Restraint Device', 'Rice Boiler', 'Rice boiler', 'Road Sweeping Machines', 'Robotics', 'Room Heater', 'Roti Making Machine', 'Roti Making Machine Auto matic', 'Rucksack Bags', 'SANITARY NAPKIN VENDING MACHINE', 'SS', 'SS Thermos', 'STP', 'STP (Sewage Treatment Plants)', 'Sand', 'Sanitary Items', 'Sanitary Napkins Incinetator Machine with Smoke ControlUnit', 'Satellite Tracker', 'Sea Food (Fish)', 'Search Light', 'Sedan / SUVS', 'Semi Automatic', 'Sewer Suction Machines', 'Shooting Range', 'Skid steer Loader', 'Software','Software Defined Radio', 'Solar Battery', 'Solar Lantern', 'Solar PV Panel','Solar Panel', 'Solar PV Plant', 'Solar Power Plant', 'Solar Street Light', 'Solar Street Light all Type', 'Solar Tublar Batteries', 'Solar Water Heater', 'Solar inverter', 'Solar water Heater', 'Solar water pump', 'Speakers', 'Street Light', 'Switch fuse unit', 'Tablet', 'Tandoor', 'Tandoor, Height 481-500 Millimeter', 'Tubes', 'UAV', 'Under Water Torch', 'Unmanned Aerial Vehicle', 'Vaccum Cleaner', 'Vegetable Cutter', 'Video Survelliance & Analytics Solutions', 'WTP', 'Walkie Talkie', 'Waste Management', 'Waste Management Plants', 'Water Bowser', 'Water Cooling', 'Water Dispenser', 'Water Tanker', 'Weapon Sight', 'Weapon Sites', 'Weapon Support system', 'Wet Grinder', 'Wet grinder 5', 'Wheel Barrow', 'X-ray Machine', 'XLPE Cables', 'water cooler']]

def json_fexer(MINISTRY_name,json_path):
    flat_products = [item.lower() for sublist in product for item in sublist]
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        title = item.get("ITEM DESCRIPTION", "").lower()
        matches = [prod for prod in flat_products if prod in title]
        item["matches"] = bool(matches)
        item["matched_products"] = matches
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Updated JSON written with match information.")

import pandas as pd
from collections import defaultdict

def xl_file(MINISTRY_name,json_path,excel_path):

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
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

MINISTRY_list =['Su_0',"Su_3"]

for MINISTRY in MINISTRY_list: 
    
    Json_Pail = os.path.join(os.path.dirname(__file__), 'db', "Gem_ministry","gem_bid_id_ministry", f"{MINISTRY}.json")
    excel_path = os.path.join(os.path.dirname(__file__), 'db', "Gem_ministry","xl_file", f'{MINISTRY}.xlsx')
    try:
        json_fexer(MINISTRY,Json_Pail)
        print(f"\nMINISTRY:{MINISTRY}")
        xl_file(MINISTRY,Json_Pail,excel_path)
    except:
        traceback.print_exc() 
        print("\nerror:",MINISTRY)
        print(MINISTRY)
        pass


# json_fexer("gem")
# xl_file("gem")
