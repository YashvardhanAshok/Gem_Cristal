import pyodbc
import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime
from openpyxl.worksheet.page import PageMargins
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter
from datetime import datetime
from openpyxl.worksheet.page import PageMargins
import os

save_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"xl files", "filtered")) 
log_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"xl files", "log")) 

def by_iteam(keywords):
    keywords = keywords.lower()
    print(keywords)
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=gem_tenders;"
        "Trusted_Connection=yes;"
    )

    query = "SELECT * FROM tender_data"
    df = pd.read_sql(query, conn)
    columns_to_drop = ['id', 'matches', 'matched_products', "element_put", "consignee_reporting", "DATE OF SEARCH", "link"]
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    def filter_rows(row):
        desc = str(row.get("item_description", "")).lower()
        cat = str(row.get("item_category", "")).lower()
        return (
            all(keyword.lower() in desc for keyword in keywords) or
            all(keyword.lower() in cat for keyword in keywords)
        )

    df = df[df.apply(filter_rows, axis=1)]

    # ✅ Check if there's any matching data
    if df.empty:
        print("❌ No matching data found. File not created.")
        return  # Exit close

    df = df.replace(0, '')
    df.columns = [col.replace('_', ' ').title() if col != 'day_left_formula' else 'Day Left' for col in df.columns]
    output_file = f"{save_file}/I-{keywords}.xlsx"

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df.index = df.index + 1  
        df = df.sort_index()
        df.to_excel(writer, sheet_name="Filtered Data", index=False, startrow=1)

    # (rest of your formatting code follows unchanged)
    # ...
    wb = load_workbook(output_file)
    ws = wb["Filtered Data"]
    # ...
    wb.save(output_file)
    print(f"✅ Filtered data exported successfully to {output_file} with all formatting applied.")

def by_address(keywords):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=gem_tenders;"
        "Trusted_Connection=yes;"
    )
    query = "SELECT * FROM tender_data"
    df = pd.read_sql(query, conn)
    columns_to_drop = ['id', 'matches', 'matched_products', "element_put", "consignee_reporting", "DATE OF SEARCH", "link"]
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

    def address_match(row):
        address = str(row.get("address", "")).lower()
        return any(keyword.lower() in address for keyword in keywords)

    filtered_df = df[df.apply(address_match, axis=1)].copy()
    filtered_df.replace(0, '', inplace=True)
    filtered_df.columns = [col.replace('_', ' ').title() if col != 'day_left_formula' else 'Day Left' for col in filtered_df.columns]

    output_file = f"{save_file}/AD-{keywords}.xlsx"

    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        filtered_df.index = filtered_df.index + 1
        filtered_df.sort_index(inplace=True)
        filtered_df.to_excel(writer, sheet_name="Filtered Data", index=False, startrow=1)

    # Load the workbook for styling
    wb = load_workbook(output_file)
    ws = wb["Filtered Data"]

    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'),
                         top=Side(style='thin'), bottom=Side(style='thin'))
    centered_wrap_alignment = Alignment(wrap_text=True, horizontal='center', vertical='center')
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Add title row
    sheet_title = f"Filtered Export – {current_date}"
    max_col = ws.max_column
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=max_col)
    title_cell = ws.cell(row=1, column=1)
    title_cell.value = sheet_title
    title_cell.font = Font(size=16, bold=True)
    title_cell.alignment = Alignment(horizontal="center", vertical="center")

    # Setup printing
    ws.auto_filter.ref = f"A2:{get_column_letter(max_col)}2"
    ws.print_title_rows = '1:2'
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_margins = PageMargins(left=0.25, right=0.25, top=0.75, bottom=0.75, header=0.3, footer=0.3)

    # Style header row
    header_fill = PatternFill(start_color="bdbdbd", end_color="bdbdbd", fill_type="solid")
    bold_font = Font(bold=True, size=15)
    for cell in ws[2]:
        cell.fill = header_fill
        cell.font = bold_font
        cell.border = thin_border
        cell.alignment = centered_wrap_alignment

    # Style data rows
    for row_idx, row in enumerate(ws.iter_rows(min_row=3, max_row=ws.max_row), start=3):
        ws.row_dimensions[row_idx].height = 120
        for idx, cell in enumerate(row):
            cell.font = Font(size=15)
            cell.border = thin_border
            cell.alignment = centered_wrap_alignment

            col_name = ws.cell(row=2, column=idx + 1).value
            if col_name == 'Day Left':
                h_col = 'F'  # Start Date
                i_col = 'G'  # End Date
                formula = f'=IF((INDIRECT("{h_col}"&ROW())+INDIRECT("{i_col}"&ROW()))-NOW() <= 0, "CLOSED", INT((INDIRECT("{h_col}"&ROW())+INDIRECT("{i_col}"&ROW()))-NOW()) & " days")'
                cell.value = formula
                cell.font = Font(size=18, color="FF0000")

    # Set column widths
    for col_idx, col_cell in enumerate(ws[2], start=1):
        col_letter = get_column_letter(col_idx)
        col_title = col_cell.value
        if col_title == 'Qty':
            ws.column_dimensions[col_letter].width = 10
        elif col_title in ['Start Date', 'End Date', 'End Time', 'Day Left']:
            ws.column_dimensions[col_letter].width = 15
        elif col_title == 'Item Description':
            ws.column_dimensions[col_letter].width = 35
        elif col_title == 'Address':
            ws.column_dimensions[col_letter].width = 40
        else:
            ws.column_dimensions[col_letter].width = 18

    wb.save(output_file)
    print(f"✅ Filtered data exported successfully to {output_file} with all formatting applied.")


# keywords = ["fencing"]
# by_iteam(keywords)
# keywords = ["manipur"]
# by_address(keywords)



raw_text='''Long Range Acoustic Hailing Deviced
2 V Solar Battery cellsd
3D Multi Spectral Camo Vehicle Coverd
3D Printerd
3d Multi Spectral Camo Dressd
A.C Static Meterd
ALL Types of commercial Gym Equipmentd
AMC OF COMMERCIAL KITCHEN EQUIPMENTd
AMC OF Gym EQUIPMENTd
Ac static watthour meters-energy meterd
Access Control Solutionsd
Air Freight Shippingd
Air curtaind
All Range Hospital Furnitured
All Types of Commercial RO PLANTSd
All Types of Wire and Cablesd
Amcd
Amc Of Acd
Amc Of Commercial Kitchend
Amc Of Fire Extinguishersd
Amc Of Generatorsd
Amc Of Gym Equipementd
Amc Of Kitchen Equipementd
Amc Of Lightning Arrestorsd
Amc Of Ro And IRPd
Amc Of Solar Power Plantd
Amc Of Solar Water Heatersd
Amc Of Transformersd
Amc of DG Sets and Transformerd
AntI Drone systemd
Anti climb Fenced
Automobile Batteries other batteriesd
Bain Maried
Bain maried
Barbed Wired
Batteryd
Body Worn Camerad
Bola wrap Remote Restrain deviced
Braille Embosserd
Bricksd
Bucket Mop Wringer Trollyd
Butterd
CCTVd
CEWd
Conducted Electrical Weapond
CGI Sheetd
Cementd
Chainlink Fenced
Change over Switchd
Chapati Warmerd
Clip On Weapon Sitesd
Commercial Mixerd
Commercial Vaccum Cleanerd
Computer and peripheralsd
Construction Of Admin Blocksd
Construction Of Hospitald
Construction Of Internal Roadsd
Construction Of Klps For Defensed
Convex Security Mirrord
Cranesd
Cyber Forensics Softwared
Cyber Security Solutionsd
DG SETSd
Data Management solutionsd
Decorative Bollardd
Decorative Street Lightd
Development Of Infrastructure For Defensed
Development Of Sewerage Treatement Plantd
Development Of Water Supplyd
Domestic casseroled
Dough Kneaderd
Dough kneader 15kgd
Dry Rationd
Rice 
Pulses 
Sugar 
Coffeed
Tead
Dustbind
Electric Fenced
Electric Wires
Cabled
Electric milk boilerd
FRPd
FRP Tankd
Flood Lightd
Flooringd
Forkliftsd
Fresh Fruitsd
Fresh Vegetabled
Fuel Celld
Fuel cell genratorsd
GPSd
GPSd
Global Positioning Systemd
Ghillie Suitsd
Ghilly Suitd
Gi Piped
Gyserd
HHTI (Hand Held Thermal Imagers)
Hand Held Gas Detectord
Hand held Thermal Imagerd
Handheld GPSd
Hardware Itemd
Headphonesd
High Intensity Light Infrared beamd
Honey Sucker 
Fenced
Sewer Cum Jetting Machined
Hybrid UPSd
Idli Steamerd
Incineratorsd
Inflatable Sheltersd
Invertersd
JCB Bacholoaderd
Jet Sprayd
Jungle Bootsd
Kunda Gadid
LGSF Buildingd
Large compartmental stainless steel tiffind
Led Bulbsd
Less Lethal Weaponsd
Lighting Arrestord
Lightning Arrestord
Lorrosd
MCBd
MCCBd
Meat Cutting Machined
Mild Steel LPG Barbecuesd
Milkd
Milk Boilerd
Miltary Rain Ponchod
Miniature Circuit Breaker Switchesd
Monitord
Multi Function Laser Aiming Systemd
Nano Uavd
New lpg cooking appliancesd
Oild
Online UPSd
Outdoor Gymd
Ovend
PNVGd
PPGI Sheetsd
Patient Bed Fowlerd
Patient Care Mattressd
Picket Steeld
Pickup Truckd
Plotterd
Plywoodd
Porta Cabind
Portable Kitchend
Portable housesd
Poultry Productd
Chickend
Egg 
Muttond
Ppgi Sheetd
Prefab shelters with puf paneld
Printerd
Projectord
Puff Cabind
Puff Shelterd
Punched Tape concertina Coil PTCCd
Reverse Osmosisd
Remote Restraint Deviced
Rice Boilerd
Rice boilerd
Road Sweeping Machinesd
Roboticsd
Room Heaterd
Roti Making Machined
Roti Making Machine Auto maticd
Rucksack Bagsd
SANITARY NAPKIN VENDING MACHINEd
SSd
SS Thermosd
STPd
Sewage Treatment Plantsd
Sandd
Sanitary Itemsd
Sanitary Napkins Incinetator Machine with Smoke ControlUnitd
Satellite Trackerd
Sea Food (Fish)
Search Lightd
Sedan 
SUVSd
Semi Automaticd
Sewer Suction Machinesd
Shooting Ranged
Skid steer Loaderd
Softwared
Software Defined Radiod
Solar Batteryd
Solar Lanternd
Solar PV Paneld
Solar Paneld
Solar PV Plantd
Solar Power Plantd
Solar Street Lightd
Solar Street Light all Typed
Solar Tublar Batteriesd
Solar Water Heaterd
Solar inverterd
Solar water Heaterd
Solar water pumpd
Speakersd
Street Lightd
Switch fuse unitd
Tabletd
Tandoord
Tandoord
Height 481-500 Millimeterd
Tubesd
UAVd
Under Water Torchd
Unmanned Aerial Vehicled
Vaccum Cleanerd
Vegetable Cutterd
Video Survelliance
Analytics Solutionsd
WTPd
Walkie Talkied
Waste Managementd
Waste Management Plantsd
Water Bowserd
Water Coolingd
Water Dispenserd
Water Tankerd
Weapon Sightd
Weapon Sitesd
Weapon Support systemd
Wet Grinderd
Wheel Barrowd
X-ray Machined
XLPE Cablesd
water cooler'''

Items = raw_text.strip().split('\n')
Items_set = set(Items)
Items_list = list(Items_set)
for Item in Items_list:
    print(Item)
    by_iteam(Item)
    
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
# not working
                                                                                                             