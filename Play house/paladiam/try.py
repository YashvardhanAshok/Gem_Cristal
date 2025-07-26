import csv
from collections import Counter

# Your raw input string
raw_data = """
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20000"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 100"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 300"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 12
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*7
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q3"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q3
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 3"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 500 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 21"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 21"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 21"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q3
" 5 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q3
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20001"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 101"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 301"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 13
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*8
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q4"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q3"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q4
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A7"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 4"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 501 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 22"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 22"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 22"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q4
" 6 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q4
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20002"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 102"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 302"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 14
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*9
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q5"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q4"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q5
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A8"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 5"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 502 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 23"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 23"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 23"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q5
" 7 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q5
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20003"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 103"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 303"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 15
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*10
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q6"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q5"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q6
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A9"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 6"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 503 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 24"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 24"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 24"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q6
" 8 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q6
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20004"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 104"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 304"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 16
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*11
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q7"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q6"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q7
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A10"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 7"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 504 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 25"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 25"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 25"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q7
" 9 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q7
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20005"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 105"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 305"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
 insulated vaccine delivery van (Q3)
" Utility Vehicle (Q1)
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Security
Supervisor , Security Manpower Service (Version 2.0) -
"
Entry and Mid Level Laptop - Notebook (Q2)
Jersey Woolen - IAF (Q2)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Desktop Calculator - Electronics (Q4) , Tags for Files (V2)"
" Bulk SMS Service (Version-2) - Transactional SMS; Domestic
SMS; Normal; MTNL, BSNL, Jio, Airtel, Vi; License service
provider, Telemarketer license holder, Authorized Channel"
" Paper-based Printing Services - Printing with Material; Poster
Calendar; Offset"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , High End Laptop - Notebook
(Q2) , Multifunction Machine MFM (V2) (Q2)"
" Retinal Camera or Fundus Camera for Eye Neonatal
Screening - RBSK (Q3)"
" Badminton Shuttle Cock (V2) as per IS 415 (Q3)
"
" Football (Q3) , Football Goal Post Net as per IS 3345 (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4)"
" Badminton Racket (Q3) , Badminton Net as per IS 3345 (Q4)
"
 Pre School Education Kit (By DWCD Assam) (Q3)
" LED Flash Light (Q4)
"
" Multifunction Machine MFM (V2) (Q2)
"
" Manpower Outsourcing Services - Minimum wage - HighlySkilled; Not Required; Others , Manpower Outsourcing
Services - Minimum wage - Skilled; Not Required; Others"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Conferences;
Conceptualization and Planning, Participation arrangements,"
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Nebulizer (V2) (Q2)
"
" Computer Printer (V2) (Q2)
"
" Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) ,
Line Interactive UPS with AVR (V2) (Q2)"
 Entry and Mid Level Desktop Computer (Q2)
" Manpower Outsourcing Services - Minimum wage - Skilled;
High School; Others , Manpower Outsourcing Services -
Minimum wage - Semi-skilled; Not Required; Others ,
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Padlock (General Use) (Q3)
Alkaline Battery 9V (Q3)
Household Laundry Detergent Powders as per IS 4955 (Q4) , scrubbing brush (Q3)
Solar Street Lighting System (NTPC) (Q3)
Mobile Blood Donation Van
 Household Insecticides (V2) (Q3)
Turntable Ladder (Fire and Rescue Trucks) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Conceptualization and Planning, Coordination and Staffing, IT related work, Marketing and Promotion, Participation arrangements, Venue Development; Third-part..
fire Hydrant AND pipe
Toner Cartridges / Ink Cartridges / Consumables for Printers (Q2)
Educational School Kits for States (Q4)
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Desks and Bench/Chair set for Classroom/Training Area (Q2)
Inks (V2) (Q4)
Monthly Basis Cab and Taxi Hiring Service - Without Fuel - Premium SUV; Toyota Innova; 2023; 25,000-50,000 kms; A/C; 17
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset , Paper-based Printing Services - Printing with Material; Leaflet; Offset
" SMART CLASS EQUIPMENT WITH DIGITAL CONTENTS
SOFTWARE (Q3)"
Cleaning, Sanitation and Disinfection Service - Outcome Based - Healthcare; As per terms and conditions of the tender uploaded; As per terms and conditions of the tender uploaded
Mobile Forensic Van (As per MHA Revised Specifications) (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
" Mobile Forensic Van (As per MHA Revised Specifications)
(Q3)
"
Power Generator - DG Set (up to 900 KVA) (Q2)
" book scanner (Q2)
"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness program; Participation arrangements; Buyer premise; Full day
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Security Guard
 Pulse Oximeter (V2) (Q2)
"Powder Based wheeled fire extinguishers (PNG) (Q2)
"
" Rope Ladder Swing - RBSK (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
 Water Curtain Nozzle (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)
"
" Electronic Lectern (Q2)
"
" Video Recorder for CCTV System (V2) (Q2)
"
Centchroman Tablets (Chhaya) For Family Welfare Programme of MOHFW (Q1)
OCP for Family Planning Programme (Q1)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)
"
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Notesheet (Azure Laid) (V2) (Q3) , Rollerball Pen (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Highlighter Pen (Q4) , Correspondence Envelopes (V2) (Q4) , Metric Steel Scales (V2) as per IS 1481 (Q4) , Black Lead Pencils (V2) as per IS 1375 (Q4) , Paper Adhesive, Liquid Gum and Office Paste Type as per IS 2257 (Rev) (Q3) , Tags for Files (V2) as per IS 8499 (Q4)
 Pulse Oximeter (V2) (Q2)
High End Laptop - Notebook (Q2)
Tablet Computer (V2) (Q2)
Financial Audit Services - Audit report, Review of Financial Statements, as per AAU ATC; CA Firm
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Vehicles; Service Provider
Financial Advisory Services - Offsite; Tax Advisory
Design Installation and Maintenance of Educational Lab - ICT Lab; Site Preparation, Supply and Installation of Hardware, Furniture; Buyer
Customized AMC/CMC for Pre-owned Products - Access Point; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes , Customized AMC/CMC for Pre-owned Products - Switch; Cisco; Annual Maintenance Contract (AMC); Quarterly; Yes
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Seminar; Venue Development, Participation arrangements, Coordination and Staffing, Conceptualization and Planning; Buyer premise; Three day
Entry and Mid Level Desktop Computer (Q2)
Split Air Conditioner (Ceiling Mount Type), as per IS: 1391 (part 2) (Q2)
Split Air Conditioner (Floor Type), as per IS: 1391 (part 2) (Q2)
Anaesthesia Machine (V2) (Q2)
Portable Ultrasound Machine (V2) (Q2)
Holter Monitor (V2) (Q2)
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2500 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Monthly Basis Cab & Taxi Hiring Services - SUV; 1200 km x 208 hours; Local 24*12
" Digital Duplicators (V4) (Q2)
"
Assets Insurance Service - All Risk Policy; Property Damage Cover, Business Interruption (Loss of Profit) Cover, MBD (Machinery breakdown) Cover; Optional , Assets Insurance Service - Terrorism Insurance, STANDALONE TERRORISM POLICY; Property Damage Cover, Business Interruption (Loss of Profit) Cover; Optional , Assets Insurance Service - Public Liability Industrial Policy; As Mentioned in Tender Document; Optional
Healthcare Kitchen and Dietary Service - General Private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Professional Painting Service - Walls; Exterior Walls; NA
Healthcare Kitchen and Dietary Service - General private ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; training; Participation arrangements; Buyer premise; Full day
Monthly Basis Cab & Taxi Hiring Services - Premium SUV; 2000 km x 320 hours; Local , Monthly Basis Cab & Taxi Hiring Services - Sedan; 1200 km x 208 hours; Local
Entry and Mid Level Desktop Computer (Q2)
Passenger Elevetor , Ducktable AC , Split AC 2TR , Split AC 1TR , Audio Podium , Gypsum Board
Revolving Chair (V4) (Q2)
Paper-based Printing Services - Printing with Material; Book/Booklet; Digital
Stationary Lead Acid Batteries (with Tubular Positive Plates) in Monobloc Containers as per IS 13369 (Q3)
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , File Board (Q4) , File Folder Cover (V2) (Q4) , Poker or AWL as per IS 10375 (Q4) , Self Adhesive Flags (V2) (Q4)
" Laundry Service - Healthcare purpose
"
Belt Waist Synthetic (ICK) (IAF) (Q3)
Beret Cap (MHA) (Q3)
Winter Jacket (Q3)
Shoes Leather Oxford DMS (Q3)
Surgical Operating ENT Microscope (Q2)
Real Time PCR Machine (V2) (Q2)
Super Sucker Machine (Q3)
Buses (V2) (Q1)
Blazer (Q3)
Pants (Q3) , Mens Casual Shirt (Q3)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; TRAINING FOR FARMERS; Participation arrangements; Buyer premise; Full day
Shoes Canvas Rubber sole - JSS Specification (Q3)
Workstation (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; training and awareness;
Participation arrangements; Buyer premise; Full day"
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
High End Desktop Computer (Q2)
Report Cover (Q4) , Register (V2) (Q4) , Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
Healthcare Kitchen and Dietary Service - general private icu; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , binding punch machine (Q3) , Photography Paper (V2) (Q4) , Staplers (V2) (Q3) , Stapler Pin / Staples (V2) (Q4) , Paper weights (Q4) , Rollerball Pen (V3) (Q4) , rubber bands (Q4) , stamp pads (Q4) , Waste Containers and Accessories - Domestic (V2) (Q3) , Permanent Marker Pen (Q4) , Fluid Correction Pen (V2) (Q4)
Power Tiller (Q2)
 Lab Multi Sample Thermal Mixer (Q3)
 Ferrule Printer (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - oxygen plant; oxygen
generation plant; Service Provider"
Fourier Transform Infra Red (FTIR) Spectrometer (Q2)
SPECTROPHOTOMETER (Q2)
Adjustable Spanner (Q3)
Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Treadmill (V2) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Multifunction Machine MFM (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)
Healthcare Kitchen and Dietary Service - General ICU private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low Sodium Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Healthcare Kitchen and Dietary Service - General ICU Private; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear Liquid Diet, Pediatric Diet, Low Protein Low Sodium Diet, Diabetic Diet, Burn Diet/ High Protein And High Calorie Diet, High Carbohyd..
Upper Primary Science Kit (By Samagra Shiksha Assam) (Q3)
Facility Management Services - LumpSum Based - Govt Office; Housekeeping, Security Services; Consumables to be provided by service provider (inclusive in contract cost)
Catering service (Duration Based) - Veg; Snacks/High Tea; Special Packet
Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , Computer Printer (V2) (Q2)
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Workshop; Participation arrangements, Venue Development, Coordination and Staffing, Conceptualization and Planning; Buyer premise; 5 day
Cardiology Cath Lab Consumables
INTERIOR FURNISHING WORKS OF DHAKUAKHANA CIRCUIT HOUSE
Cyber Security Audit - SLA Monitoring Audit, Security and Compliance Audit, Infrastructure Audit, Operations, Management Process and Control Audit
Office Chair (V3) (Q2) , Executive Table (V3) (Q2) , Metal Shelving Racks (Adjustable Type) confirming to IS 1883 (V2) (Q2) , Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3) (Q2)
Mosquito Nets as per IS 9886 (Q3)
Paper-based Printing Services - Printing with Material; Book/Booklet; Offset
Financial Advisory Services - Offsite; Tax Advisory
Vocational Training Services - Version 2 - offline; 4; Service providers location; Cooperative Training Program
All in One PC (Q2)
Anaesthesia Machine (V2) (Q2)
INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE - Theft Prevention, Remote Video Monitoring, Facility/Asset Protection, Monitor Operations; Capture Devices, Recording Devices; High media quality, Ability to archive footage, Maximum security footage; ..
Gowns Operating (Q3)
Refilling Ink for Toner (Q3)
Annual Maintenance service-AIR CONDITIONER
PCR Machine (Semi Quantitative) (Q3)
Entry and Mid Level Desktop Computer (Q2) , Entry and Mid Level Laptop - Notebook (Q2) , Line Interactive UPS with AVR (V2) (Q2)
4.5 m Rubberised Inflatable Boat (Rescue boats) (Q3)
digital signature certificate (Q2)
Financial Audit Services - As per ATC; CA Firm
" Facility Management Services - LumpSum Based -
Maintenance Repairing of Audio Visual Teaching Equipments
for various Departments of DBHRGFTI; Maintenance
Repairing of Audio Visual Teaching Equipments for various
Departments of DBHRGFTI; Consumables.."
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
Event or Seminar or Workshop or Exhibition or Expo Management Service - National; Training and Awareness Program; Participation arrangements; Buyer premise; Full day
" OTO - Acoustic Emissions (OAE) Instrument for New Born
Infant and Children (V2) - RBSK (Q3)"
" Flat Gym Bench (V2) (Q4) , Spin Bike (Q3) , Weight Lifting
Set (V2) (Q4) , Multi Station Gym (V2) (Q3) , Treadmill (V2)
(Q3) , Dip / Chin Assist Machine (Q4) , Dumbbell Rack (Q3) ,
Squats Rack (Version 2) (Q3) , Rubberized Weight
Dumbbells (Q3) , Rubberized Weight Plates (Q8"
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
Theft Prevention, Remote Video Monitoring, Facility/Asset
Protection, Monitor Operations, Vandalism Deterrence,
Employee Safety, Parking Lots, Event Video Surveillance;
eSATA, Network attached storage."
" Office Chair (V3) (Q2) , Revolving Chair (V4) (Q2) , Executive
Table (V3) (Q2) , Steel Shelving Cabinets (Adjustable Type)
confirming to IS 3312 (V3) (Q2) , Heavy Duty Storage Racks
(Q3)"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles,
Automobile; Service Provider"
 Office Suite Software (V2) (Q2)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - healthcare; Pipelines,
Medical Equipment and Devices; Service Provider
"
 Composite Synthetic Fibre Ropes as per IS 14928 (Q3)
 Inline Inductor (Q3)
 Mercurial Sphygmomanometer (Q2)
 blood pressure recording units (Q2)
 Garden Bench (Q3)
 Sofa Sets - Handcrafted (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q7"
" Portable Pump Set for Fire Fighting as per IS 942 (Q3)
"
 Trailer Pump for Fire Brigade use as per IS 944 (Q3)
 Electric Two Wheeler - Motorcycle, Scooter and Moped (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
programme in different development blocks of Dibrugarh
District of Assam; Participation arrangements; Buyer
premise; Full day"
 Variable Refrigerant Flow Air Conditioner (Q8
 Sofa Sets - Handcrafted (Q3)
 Entry and Mid Level Desktop Computer (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Workshop;
Conceptualization and Planning, Coordination and Staffing,
Participation arrangements, Venue Development; Buyer
premise; Full day"
 Twister - Outdoor Gym Equipment (Q3)
Heavy duty longspan storage System (Q3)
Stable Bleaching Powder (V2) for Household and Industrial use conforming to IS 1065 (Part 1) (Q3)
 Turntable Ladder (Fire and Rescue Trucks) (Q2)
" Cotton Pillow (Q3) , Bedsheets - Hotel Linen (Q3) ,
Handloom Blanket - Relief (Q3)"
" Treadmill (V2) (Q3) , Spin Bike (Q3) , Elliptical Cross Trainer
(Q3) , Medicine Ball (Q3) , Commercial Air Bike (Q4) , Yoga
Mats (Q3) , Battle Rope (Q4) , Swiss Gym Ball (Q4) , Gym
Foam Roller (V2) (Q3) , Flat Gym Bench (V2) (Q4) "
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2) , Computer Printers (Q2)
, Scanner (V2) (Q2)"
" Entry and Mid Level Desktop Computer (Q2)
"
 Computer Printers (Q2)
" Plastic Chairs for General Purposes confirming to IS 13713
(V3) (Q2)"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Household Laundry Detergent Powders as per IS 4955 (Q4) ,
Glue Stick (V2) (Q4) , Markers for White Board (V2) (Q4) ,
Stamp - Pad Ink as per IS 393 (Q4)
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - Office Space; Vehicles;
Service Provider"
 Consumables for Digital Duplicators (Q2) , Toner Cartridg
 Rope Ladder Swing - RBSK (Q3)
" CO2 Based Wheeled Fire Extinguishers (V2) as per IS 16018
(Q2)"
Powder Based wheeled fire extinguishers (PNG) (Q2)
" Water Curtain Nozzle (Q3)
"
 Standalone Ceiling Mounted Fire Suppression System (Q2)
" Vocational Training Services - Version 2 - offline; 8; Third
party location; Postsecondary vocational schoo"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others"
" Chipping hammer heavy weight (Q3)
"
 Nylon Life Jacket (MHA) (Q3)
 Power Generator - DG Set (up to 900 KVA) (Q2)
 Online UPS (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Program; Participation arrangements; Buyer premise; Full
day"
" Computer Table (V2) (Q2) ( PAC Only ) , Revolving Chair
(V4) (Q2) ( PAC Only ) , Office Chair (V3) (Q2) ( PAC Only
) , Modular Table (V2) (Q2) ( PAC Only )"
" Entry and Mid Level Desktop Computer (Q2) , Multifunction
Machines MFM (Q2) , Scanner (V2) (Q2) , Line Interactive
UPS with AVR (V2) (Q2)"
 Hydrochloric Acid in Tankers (V2) as per IS 265 (Q3)
" E-Learning Content Development - Non-iGOT; Translation of
existing e-learning content; Hindi, English; Mobile and
Laptop/Desktop Both; Law, Cyber Crime, Management, Big
Data Analytics, Compute, Storage & Virtualization, Cyber
Security, Rural Developm.."
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Annual Maintenance Service - Desktops, Laptops and
Peripherals - Desktop PC; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - All In One PC; hp ,
Annual Maintenance Service - Desktops, Laptops and
Peripherals - Scanner; hp , Annual Maintenance Service -
Desktops, Laptops and Peripherals - Laptop; hp , Annual
"
 Thermal Paper Roll (Q4)
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Office Suite Software (V2) (Q2)
 Office Suite Software (V2) (Q2)
 ial Advisory Services - Onsite; Tax Advisory
 Refilling Ink for Toner (Q3)
 Out Board Motor for Rescue Boats (Marine propellers) (Q3)
" Tours and Travel Service - Travel and Stay both; Pick and
Drop, Hotel/Resort Stay; National"
" Layer 2 Access Switch (V2) (Q2) , Networking / Server Rack
(Q2) , Cat 6 Cable for Indoor Use (Q2) , CAT 6 Information
outlet (Q3) , Cat 6 Patch cord (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
 Ceiling OT Light (V2) (Q2)
" Walk in Cooler (Q3)
"
" Desks and Bench/Chair set for Classroom/Training Area (Q2)
, Revolving Chair (V4) (Q2) , Office Chair (V3) (Q2) , Modular
Table (V2) (Q2) , Modular Extendable Conference Table (V2)
(Q2) , Computer Table (V2) (Q2) , Sofas (V2) (Q3) , "
 Endoscopic Ultrasound (Q2)
 Liquid Nitrogen Gas (Q3)
" Split Air Conditioner (Floor Type), as per IS: 1391 (part 2)
(Q2)"
 200KV High Resolution Transmission Electron Microscope
 Water Quality Meters / Analyzers (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) , Air
Freshener Liquid (Q4) , Pins, Paper, Straight as per IS 5653
(Q4) , Staplers (V2) (Q3) , Plastic Folder with Printing (Q4) ,
Desk Pads - Writing (V2) (Q4) , Stapler Pin / Staples (V2)
(Q4) , Highlighter Pen (Q4) , File Board (Q4) , File Folder
Cover (V2) (Q4) , Self Adhesive Flags (V2) (Q4) , Register
"
" Multifunction Machines MFM (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2)"
 Digital Medical X - Ray Films (V2) (Q2)
 White - LED Based Solar Street Lighting System (Q3)
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - MEDICAL GAS PIPELINE
AND MANIFOLD SYSTEM; Medical Equipment and Devices,
Pipelines; Service Provider"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Mazdoor/Labour; Not Required"
" Metal Shelving Racks (Adjustable Type) confirming to IS
1883 (V2) (Q2) ( PAC Only )"
" Revolving Chair (V4) (Q2) , Modular Table (V2) (Q2) , Office
Chair (V3) (Q2)"
" Group Personal Accidental Insurance Service - Contract
Employees; Temporary disabilities, Permanent partial
disability, Permanent total disability, Only accidental death
(not natural)"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A11"
 Auditorium Chair (V2) (Q2)
 SMA connector (Q4) , trolleys or accessories (Q3)
 General Operating Table (Q3)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Laptop - Notebook (Q2) , Multifunction Machines MFM (Q2)
 Signal Generator (Q3) , Digital Storage Oscilloscope (Q3)
 Annual Maintenance Service - D..
 Entry and Mid Level Desktop Computer (Q2)
 Wooden Almirah (Q3)
 High End Desktop Computer (Q2)
 1.5 T MRI Machine (Q2)
" Annual Maintenance service-AIR CONDITIONER
"
 Cardiac Monitor with defibrillator (Q2)
 Binocular Indirect Ophthalmoscope (V2) - RBSK (Q2)
" Financial Audit Services - Review of Financial Statements,
GST TDS Consultancy Return Filling Hospital Management
Services Fund Govt Transactions Professional Taxes In
addition firm should carry out audit of Hospital Management
Services Account for l.."
 Laboratory Deep Freezer (V2) (Q2)
" Catering service (Duration Based) - Veg; Lunch; Regular
Packet , Catering service (Duration Based) - Non veg;
Lunch; Regular Packet , Catering service (Duration Based) -
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard , Hiring of Sanitation Service - Sweeper; 6;
All Areas; All Areas; Daily; 8"
" Design Installation and Maintenance of Educational Lab - ICT
Lab; Maintenance of Hardware (AMC/CMC), Supply and
Installation of Hardware, Insurance, Teacher Training, Econtent, Deployment of Teachers/Faculty; Buyer
"
 Real time micro PCR (Q3) ( PAC Only )
" Paper-based Printing Services - Printing without Material;
Secured Mark sheets with Variable data; Offset"
" Paper-based Printing Services - Printing without Material;
Secured Degrees with Variable data; Offset"
 Micro PCR MTB Test Kit (Q3) ( PAC Only )
" Real time micro PCR (Q3) ( PAC Only )
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Healthcare; As per terms and conditions of the
tender uploaded; As per terms and conditions of the tender
uploaded"
  Lime (Q3)
" Language / multilingual software foreign language software
(Q2)"
" Facility Management Services - LumpSum Based - Industrial;
0; Consumables to be provided by service provider
(inclusive in contract cost)"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Paper-based Printing Services - Printing with Material;
Book/Booklet; Offset"
" Computer Printers (Q2)
"
 Mobile Digital Radiography System (V2) (Q2)
" Ultrasound Machine (V2) (Q2)
"
 505 mA X - Ray Machine (V2) (Q2)
" Dental autoclave with accessories (Q3)
"
" C Arm Fluoroscope X - Ray Machine (V2) (Q2)
"
 Thermocol Ice box for Medical purposes (Q3)
" Laptop - Notebook (Q2)
"
" Veterinary Artificial Insemination straws (Low absorption
type) (Q3)"
" pH Meter (Q3)
"
" Server (Q2) , Online UPS (V2) (Q2) , Entry and Mid Level
Desktop Computer (Q2) , Line Interactive UPS with AVR (V2)
(Q2) , Multifunction Machines MFM (Q2) , Scanner (V2) (Q2)"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Awareness Programme;
Participation arrangements, Venue Development; Buyer
premise; Full day
"
" Repair, Maintenance, and Installation of Plant/
Systems/Equipments (Version 2) - SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; SUPPLY COMPUTER
HARDWARE AND MEDICAL EQUIPMENTS; NA
"
" Scanning and Digitisation Service (Version 2) - 600; A0 A1
A2 A3 A4 A5 A6
"
 Multifunction Machines MFM (Q2)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
"Art Kit for Preschool (By Assam) (Q3)
"
" Operating System Software (V2) (Q2) , Designing Software
(V2) (Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Badminton Racket (Q3) , Cricket Bat (Q3)
"
 Laptop - Notebook (Q2) , Pen Drive (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and Awareness
Programme; Participation arrangements, Venue
Development; Buyer premise; Full day
"
" Security Manpower Service (Version 2.0) -
Office/Commercial/Institutions/ Residential; Unarmed
Security Guard
"
" Manpower Outsourcing Services - Minimum wage -
Unskilled; Not Required; Others
"
" File Board (Q4) , File Folder Cover (V2) (Q4) , Stapler Pin /
Staples (V2) (Q4) , Staplers (V2) (Q3) , Transparent Tape
(V2) (Q4) , Tags for Files (V2) as per IS 8499 (Q4) , Paper
Adhesive, Liquid Gum and Office Paste Type as per IS 2257
"
" Interactive Panels with CPU (Q2) , Audio Digital Signal
Processor (Q3)"
 Ion Chromatography System (Q3)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Training and awareness
"
" Cricket gloves (Q3) , Football (Q3) , Football Goal Post Net
as per IS 3345 (Q3)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 3 - O&M Service with
operational and comprehensive maintenance; 1; Upto 2000
Hours
"
 Office Suite Software (V2) (Q2)
 Accounting software (Q2)
" Upper Primary Science Kit (By Samagra Shiksha Assam)
(Q3)"
" Switch Mode Power Supply (SMPS) as per IS 14886: (Q3) ,
General Purpose Battery Chargers (Q3)"
" Financial Advisory Services - Onsite; Tax Advisory
"
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing Accommodation
for Holding of Residential Coaching Camp; Participation
arrangements; Buyer premise; 26"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Holding of Residential
Coaching Camp; Participation arrangements; Buyer
premise; 26"
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; Providing of Food For
Residential Coaching Camp; Participation arrangements;
Buyer premise; 26"
" High Speed Drill System for Neurosurgery & Spinal Surgery
(Q3)"
 Potash Derived from Molasses Natural K (Q8
" 10 Part Automated Hematology Analyser (V2) (Q2)
"
" Ultrasound Machine (V2) (Q2)
"
" Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1200
km x 208 hours; Local , Monthly Basis Cab & Taxi Hiring
Services - Sedan; 1200 km x 208 hours; Local"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printers (Q2) , Line Interactive UPS with AVR (V2) (Q2) ,
Scanner (V2) (Q2) , Pen Drive (Q3)"
 Hopper Tipper Dumper (Version 2) (Q3)
 Laundry Service - Healthcare purpose
" Controller for Global Navigation Satellite System (GNSS)
(Q3)"
" Automated HPLC System for Separation of complex
mixtures (Q3)"
" Wheeled Skid Steer Loader (V2) as per IS / ISO 7131 (Latest)
(Q2)"
" Solar Power Plant (Roof Top) for ONGRID System, Three
Phase (V2) (Q3)"
 Gas Chromatography Mass Spectrometry (GC - MS) (Q3)
" Handling and Transport on Lumpsum Basis - Transport
Service"
 Recycled Towel (Q3)
 Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4)
" Badminton Net as per IS 3345 (Q4) , Football (Q3) ,
Volleyballs as per IS 417:1986 (Q3) , Volleyball Net as per IS
3345 (Q4) , Air pump (Q4)"
" Table Tennis Rackets (Q3) , Table Tennis Ball (V2) (Q4) ,
Table Tennis Net Assembly-IS 3345 (Q3) , Carrom Board
(Q3) , Badminton Court Mat (Q3) , Badminton Racket (Q3)"
 Soda Ash, Technical for Bulk Purchase - IS 251 (Q8
" INTEGRATED SECURITY SURVEILLANCE SYSTEM SERVICE -
CCTV for Hospital Building of Silchar Medical College and
Hospital; Capture Devices, Recording Devices; Maximum
security footage; Buyer’s premises; Role-Based Access
Control System (RBAC); NA; NA; NA;"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)"
 Fiber Media converter (Q3)
" Entry and Mid Level Desktop Computer (Q2) , Line
Interactive UPS with AVR (V2) (Q2)"
" Hiring of Consultants - Milestone/Deliverable Based -
Subject Matter Experts; Forest and Environment; Yes;
Hybrid(As specified in scope of work"
" Exercise Band (Theraband) (Q4) , Measuring Tape (Q3) ,
Baton (MHA) (Q3) , Decorative Flag (Q4) , Skipping Rope
(V2) (Q3) , Football (Q3) , Volleyballs as per IS 417:1986
(Q3) , Football Goal Post Net as per IS 3345 (Q3) , Volleyball
Net as per IS 3345 (Q4) , Stable Rubber Mats (Q3) , Chess
Board (Q3)
"
" Blazer (Q3) , Mens Casual Shirt (Q3) , Pants (Q3) , Tie for VIP
Security Personnel (CRPF) (Q3) , Shoes Leather Oxford DMS
(Q3)
"
 Electronic Baby Weighing Scale - RBSK (Q3)
 blood pressure recording units (Q2)
" Foot Operated Pedal Bin or Bucket for Bio - Medical Waste
Collection (Q3)"
 Portable Suction Machine (V2) (Q2)
" Event or Seminar or Workshop or Exhibition or Expo
Management Service - National; TRAINING AND AWARENESS
PROGRAMME; Participation arrangements; Buyer premise;
Full day"
 Phototherapy Machine for (SNCU) (Q3)
 Phototherapy Machine for (SNCU) (Q3)
" Infant Warmer (V2) (Q2)
"
Entry and Mid Level Desktop Computer (Q2)
Sewing Machine as per IS 1610 (Q3)
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
File/Folder (V3) (Q4) , Fluid Correction Pen (V2) (Q4) , Glue
Stick (V2) (Q4)"
 Clinical Apron (Q2)
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Workstation (Q2)
Sutures (V3) (Q2)
Electric Ceiling Type Fan (V3) ISI Marked to IS 374 (Q2)
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 500 hours"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
 Business Intelligence and Data Analysis Software (V2) (Q2)
" Healthcare Kitchen and Dietary Service - Genral Ward,
Private & ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet,
Clear Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein
"
" Backhoe Loaders (V2) (Q2)
"
" Hiring of Consultants - Per Person Per Month Based - Subject
Matter Experts; Social Welfare, Livelihoods and Poverty
Alleviation; Post Graduate in Domain Area; Yes
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Activity Based Educational Kits for Biology (Q4) , Activity
Based Educational Kits for Physics (Q4) , Activity Based
Educational Kits for Chemistry (Q4)
"
" Supply of Liquid Medical Oxygen (LMO) - Kilograms; Steel
Tank Already installed; Steel tank capacity 20006"
 Refilling of Medical Gases in Cylinders
 Refrigerator Truck for Vaccine Transport (Q3)
" All in One PC (V2) (Q2)
"
" Entry and Mid Level Laptop - Notebook (Q2)
"
" Healthcare Kitchen and Dietary Service - General Privaye
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
High End Desktop Computer (Q2) , Line Interactive UPS with AVR (V2) (Q2)
 Financial Audit Services - Audit report; CA Firm
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; General
Cleaning (Sweeping, Mopping, dusting); Indoor"
" Power Tiller (Q2)
"
" Manpower Hiring for Financial Services - Onsite; Chartered
Accountant
"
" USB Type External Hard Disk Drive (V2) (Q3)
"
" Entry and Mid Level Desktop Computer (Q2) , Entry and Mid
Level Laptop - Notebook (Q2) , Multifunction Machine MFM
(V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
Backhoe Loaders (V2) (Q2)
" Manpower Hiring for Financial Services - Offsite; Chartered
Accountant"
"All in One PC (V2) (Q2)
"
" Stacker (Q3)
"
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 Vertical Autoclave (Q2)
" Reciprocal Shakers - Mechanical Shaker Machine with Timer
(Q3)
"
Entry and Mid Level Desktop Computer (Q2)
" Workstation (Q2)
"
" digital conductivity meter (Q3)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
" Stability Chamber (Q3)
"
" Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
"
 Professional Painting Service - Walls; Exterior Walls; NA
" File/Folder (V3) (Q4) , Register (V2) (Q4) , Staplers (V2) (Q3)
, Ball Point Pens (V2) as per IS 3705 (Q4) , Tags for Files (V2)
as per IS 8499 (Q4) , Plain Copier Paper (V3) ISI Marked to IS
14490 (Q4)
"
" Paper-based Printing Services - Printing with Material;
Answer Book; Offset
"
" Fixed Computer Workstation (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Vehicle Hiring Service - Per Vehicle-Day basis - Premium
SUV/MUV; 2023, 2024, 2025; Outstation; Plain; 500Kms x
24Hrs; Round Trip , Vehicle Hiring Service - Per Vehicle-Day"
" Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2025,
2024, 2023, 2022, 2021; Outstation; Plain; 500Kms x 24Hrs;
Round Trip , Vehicle Hiring Service - Per Vehicle-Day basis "
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Solar Street Lighting System (NTPC) (Q3)
"
" Flame Photometer (Q3)
"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Facility Management Services - LumpSum Based -
Government Offices; Housekeeping, Security Services,
Office Boy; Consumables to be provided by service provider
(inclusive in contract cost)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
 zero client (Q3)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Entry and Mid Level Desktop Computer (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Plain Copier Paper (V3) ISI Marked to IS 14490 (Q4) ,
Multifunction Machine MFM (V2) (Q2) , Toner Cartridges / Ink
Cartridges / Consumables for Printers (Q2) , Computer"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Cleaning, Sanitation and Disinfection Service - Outcome
Based - Office/Commercial/Institutions/Residential; dusting
moping of office rooms court rooms etc and cleaning of
"
" Manpower Outsourcing Services - Fixed Remuneration -
Cleaner; Mazdoor/Labour; Not Required"
" Manpower Outsourcing Services - Fixed Remuneration -
Others; Sweeper; Not Required"
" nternet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 106"
" Atomic Absorption Spectrophotometer , High Performance
Liquid Chromatography , Refractometer , Hot Plate Block
digester , MicroBalance , Nitrogen Concentrator"
" Internet Bandwidth and Replication Service - Internet
Leased Line; Goverment Service provider, Private Service
provider; Class A, Class B, Class C, Unified; Unified; 306"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
" Toner Cartridges / Ink Cartridges / Consumables for Printers
(Q2)
"
" Entry and Mid Level Desktop Computer (Q2) , Computer
Printer (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2)"
" Healthcare Kitchen and Dietary Service - GENERAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
Sodium Diet, Burn Diet/ High Protein And High Calorie Diet,
High Carbohyd.."
 Power Generator - DG Set (up to 900 KVA) (Q2)
" Split Air Conditioner Including Green AC, Wall Mount Type
(V2) (Q2)
"
 All in One PC (V2) (Q2) , Scanner (V2) (Q2)
" Healthcare Kitchen and Dietary Service - GENERAL Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low
"
 Professional Large Format Display (Q2)
" Financial Audit Services - Audit report, Review of Financial
Statements; CA Firm"
" Manpower Outsourcing Services - Minimum wage - Skilled;
Secondary School; Others , Manpower Outsourcing Services
- Minimum wage - Unskilled; High School; Others"
" Monthly Basis Cab & Taxi Hiring Services - Premium SUV;
2500 km x 320 hours; Local 24*7
"
 Line Interactive UPS with AVR (V2) (Q2) , Speakerphone (Q2)
Entry and Mid Level Desktop Computer (Q2) , Multifunction Machine MFM (V2) (Q2) , Scanner (V2) (Q2) , Line Interactive UPS with AVR (V2) (Q2) , High End Laptop - Notebook (Q2)
" Healthcare Kitchen and Dietary Service - GENRAL PRIVATE
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
Portable Ultrasound Machine (V2) (Q2)
" Alkaline Battery 9V (Q3)
"
" Safety Footwear as per IS 15298 (Q2)
"
" Office Chair (V3) (Q2) ( PAC Only ) , Modular Table /
Meeting Table / Centre Table (V2) (Q2) ( PAC Only ) , Steel
Shelving Cabinets (Adjustable Type) confirming to IS 3312
"
 Server (Q2)
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Healthcare Kitchen and Dietary Service - General Private
ICU; Diet; Full Regular Diet, Soft Diet, Liquid Diet, Clear
Liquid Diet, Pediatric Diet, Diabetic Diet, Low Protein Low"
" Digital Multimeter of Big Display Bijin , DC Voltmeter 0 to
25volts Bijin , DC Voltmeter 0 to 10volts Bijin , DC
Multimeter 0 to 25Ma Bijin , DC Ammeter 0 to 3amp Bijin ,"
" Digital Multimeter of Big Display Barama , DC Voltmeter 0 to
25volts Barama , DC Voltmeter 0 to 10volts Barama , DC
Multimeter 0 to 25Ma Barama , DC Ammeter 0 to 3amp"
" Digital Multimeter of Big Display Goreswar , DC Voltmeter 0
to 25volts Goreswar , DC Voltmeter 0 to 10volts Goreswar ,
DC Multimeter 0 to 25Ma Goreswar , DC Ammeter"
" Paracetamol Tabs IP 250 mg , Paracetamol Syrup IP
Contains 125 mg of Paracetamol in 5 ml , Gention Violet
Solution , Povidone Iodine Ointment , Absorbent cotton roll ,"
" Chadar for AWW , Mekhela for AWW , Chadar for AWH ,
Mekhela for AWH , Saree for AWW , Saree for AWH
"
" Non Paper Printing Services - Quantity Based - ID card;
Digital; PVC (as per ISO/IEC 7810)
"
" Operation and Maintenance Services of Power
Generator(DG-Set) - Package 1 - O&M Service with
operational and maintenance manpower; 1; Upto 1000
hours
"
"""

# Step 1 & 2: Split and clean lines (merge wrapped lines into a single entry)
import re
entries = [e.strip() for e in re.split(r'\n\s*\n', raw_data.strip()) if e.strip()]
entries = [' '.join(line.splitlines()) for line in entries]

# Step 3: Count repetitions
counter = Counter(entries)

# Step 4: Write to CSV
with open("repeated_items.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Item", "Count"])
    for item, count in counter.items():
        writer.writerow([item, count])

print("CSV created: repeated_items.csv")
