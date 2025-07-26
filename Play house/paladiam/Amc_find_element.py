import os
import pandas as pd

# Define folder and items to search (converted to lowercase)
folder_path = r"C:\vs_code\TenderHunter2.1.3\final\paladiam\result\AMC"
item_keywords = ['kitchen']
item_keywords = [
    "Gas Ranges",
    "Griddle ",
    " Flat Top",
    "Charbroiler",
    "Deep Fryer",
    "Tandoor",
    "Salamander ",
    " Overhead Broiler",
    "Induction Cooktops",
    "Tilting Bratt Pan",
    "Steam Cooking Units",
    
    "Pizza Ovens",
    "Convection Ovens",
    "Combi Ovens",
    "Baking Ovens",
    "Microwave Ovens",

    "Reach-in Refrigerator", 
    "Freezer",
    "Undercounter Refrigerator",
    "Blast Chiller",
    " Freezer",
    "Cold Room",
    "Ice Machines",
    "Display Refrigerators",

    "Food Processors",
    "Dough Mixers",
    "Planetary",
    "Spiral",
    "Meat Mincer",
    "Grinder",
    "Dough Sheeter ",
    "Divider",
    "Vegetable Cutter",
    "Commercial Blenders','Juicers",

    "Dishwashers",
    "Garbage Disposal Systems",
    "Sinks "," Spray Units",
    "Water Softener "," Filtration Units",

    "Bain Marie",
    "Hot Food Cabinets",
    "Plate Warmers",
    "Food Display Counters",
    "Heat Lamps "," Strip Heaters",

    "Coffee Machines",
    "Tea Dispensers",
    "Soda Machines ",
    "Dispensers",
    "Bar Blenders",

    "Kitchen Exhaust Systems",
    "Fresh Air Units",
    "Duct Cleaning",
    "Grease Filters",
    "Air Curtains",
    "Fire Suppression Systems",

    "SS Work Tables ",
    " Racks ",
    " Trolleys",
    "Gas Pipeline "," Manifold Systems",
    "Control Panels"
]

item_keywords = [item.lower() for item in item_keywords]

"Food Processor","Commercial Mixer","Blender ","Meat Slicer","Vegetable Cutter","Dough Sheeter","Potato Peeler Machine","Meat Mincer","Grinder","Juicer ","Chopping Boards" 
# Store matching rows from all CSVs
matching_rows = []

# Iterate through all CSV files
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        try:
            # Try reading with utf-8
            df = pd.read_csv(file_path, encoding='utf-8')
        except Exception:
            try:
                # Fallback to latin1 if utf-8 fails
                df = pd.read_csv(file_path, encoding='latin1')
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                continue

        if 'title' not in df.columns:
            print(f"'title' column not found in {filename}")
            continue

        # Convert 'title' to lowercase and search for keywords
        df['title'] = df['title'].astype(str).str.lower()
        mask = df['title'].apply(lambda title: any(keyword in title for keyword in item_keywords))
        matched = df[mask]

        if not matched.empty:
            matching_rows.append(matched)

# Combine and export results
if matching_rows:
    result_df = pd.concat(matching_rows, ignore_index=True)
    output_path = os.path.join(folder_path, "matched_items.xlsx")
    result_df.to_excel(output_path, index=False)
    print(f"✅ Matching items saved to {output_path}")
else:
    print("❌ No matching items found.")
