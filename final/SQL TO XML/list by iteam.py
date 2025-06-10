from collections import Counter
from openpyxl import Workbook

# Your input string
data = """Generator Set 15 KVA (Q3)
PROC OF COLD DESERT OUTER MULTI LAYER CLOTHING SYSTEM CAMOUFLAGE SAND DIGITAL (CDO-MLCS)
PROC OF COLD DESERT OUTER MULTI LAYER CLOTHING SYSTEM CAMOUFLAGE SAND DIGITAL (CDO-MLCS)
PROC OF COLD DESERT MULTI LAYER DOWN CLOTHING SYSTEM CAMOUFLAGE DESERT / SAND (CDMLDCS-CDS)
COLD DESERT MULTI LAYER DOWN CLOTHING SYSTEM CAMOUFLAGE DESERT / SAND (CDMLDCS-CDS)
PROC OF GLACIER MULTI LAYER DOWN CLOTHING SYSTEM CAMOUFLAGE WHITE DIGITAL (GMLDCS-CWD)
PROC OF GLACIER WHITE OUTER MULTI LAYER CLOTHING SYSTEM CAMOUFLAGE WHITE DIGITAL (GWO-MLCS)
PROC OF GLACIER WHITE OUTER MULTI LAYER CLOTHING SYSTEM CAMOUFLAGE WHITE DIGITAL (GWO-MLCS)
Manpower Outsourcing Services - Fixed Remuneration - Others; Cargo Handler; Not Required
FS File Folder,Notice Board 3x4,Training Classes High Adjustable Stool,Folding Chair ops Training,M
Provn of Small Living Shelter comma Shelter Parts FOR TAKSING,Provn of Constr Mtrl for Small Living
Provn of OR Living Shelter Shelter Part Only FOR LAMANG,Provn of OR Living Shelter Shelter Part Onl
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
OIL FILTER ELEMENT,FUEL FILTER,ZINC ANODE 1,ZINC ANODE,IMPELLER WATER PUMP
M2 BOF 5049700 Guard Right Welding,M2 BOF 6135071 Catch,M2 BOF 5050408 2 Plate left,M2 IAN 97SA Val
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Admin
SMART MAP (6 x 4 FT)
Fabrication of Mockup for one Universal Driving Simulators for FFC Myanmar
Carburetor assy of 6 point 5KVA gen set for EW Sys,Fuel on off cock of 6 point 5KVA gen set for EW 
ASSY RELEASE BEARING,CLUTCH LINNING SET,COVER ASSY 1.75 INCH SPLINE DIA,GASKET CYL HEAD COVER,HOSE 
CLUTCH PLATE,MAIN CYLINDER DIA,CABLE,CLUTCH BOOSTER,CENTRIFUGAL OIL FILTER RHO,ROTATING LIGHT
ELECTRODES WELDING STEEL MILD GENERAL PURPOSE,SOLDERING WIRE,FLUX SOLDERING PASTE,M SEAL,INSULATION
Vane Pump,Dash Board Cover Assy,Disc Front Brake,Brake Pad,Hose Rediator Outlet,Brake booster kit,B
LIME JUICE CORDIAL
2990-016264 SILENCER ASSY,3040-023883 KICK STARTER SHAFT,6220-004597 TRAFFICATOR ASSY LH REAR,2510-
LV1-TR90-188-94-004SB,ICVBMP I-II AK-150-MVK,LV1-WZT-3 TD50-00-040,LV1-WZT-3 170-45-012,LV7-AV15-57
Nord VPN Complete Plan 1 Year,MS Office 2021 Business Lifetime,Quick Heal Antivirus for Desktop Com
LV7/HRV AV-15 578-903-910-352-80 Rotary Super Structure
4 MP PTZ Camera
Telescopic Handler (Q2)
Adjuster Speed Control,Eng Safety unit,Rectifier Assy,Switch Toggle,Self Starter,Air Pressure pipe,
FET 1215 of RS Stars V MK II,IC 7343 of RS Stars V MK II,IC 74 LVC 164245 of RS Stars V MK II,Micro
Repair of Rotary Pump,Repair of Rotary pump Assy,Repair of Turbo Charger,Repair of LBPV,Repair of A
BA NO 24A-079747H MOTOR CYCLE BAJAJ PLATINA,MOTOR CYCLE BAJAJ PLATINA,MOTOR,CYCLE,BAJAJ,PLATINA,Vec
Floor Mat,PVC floor Mat,Metal foldable Bar,Inner four men set cream colour,Replacement of rexine an
Diode Shtky BARR RECT SMT HSM190J,IC AMP HI Side Prec Curr Sense 8Pin 50B,Transistor Mosfet Pchan S
Grease aeroshell -33
Light Vehicle Non AC 08 hrs 80 km Plain local duties,Light Vehicle Non AC 08 hrs 80 km Hill local d
UG Bn Svl Centre
UG Comd Post
Clutch Master Cyl Assy,Clutch Cover Assy,RAM Kit,Protection Valve Assy,Stopper Cable,Speedometer Ca
LV6-MT14, 2610-001599 TYRE SIZE 18R 22.5 (445/65 R22.5 TL 168)
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others
Night Enabled Quadcopter
White Paint,Black Paint,Apex Distemper,Distamper Roller,Paint Brush,Ivory Sheet,Tape,Godrej Air Met
Adrenaline Tartrate 1 ml Inj,Lorazepam 2 mg per ml 2 ml Inj,Diltiazem 5 mg per ml Inj,Levo-Salbutam
Set of Rubber O Ring,Automatic Voltage Regulator,Leather Cloth Balck,Sheet Cellular,Rod welding Ste
JAAR,SEAT WHEEL CHAIR,CLAMP,BTY 16V,CONTRACTOR,BTY 12V,SIEVE BAD,HEATING ELEMENT 2000W
ICR 18650GA 3500MAH Cell,LR 123A Cell Rechargeable Cell,Rechargeable Cell 18650 2200MAH,Infinite Pl
PURCHASE OF HIGH VOLUME LOW SPEED FAN
H1 B 8040-000016 ADHESIVE NITRO CELLULOSE,H1 B 8040-000150 ADHESIVE UNIVERSAL,H1 B 8040-000008 ADHE
RO Purification Plant 500 LPH capacity
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Healthcare
Dry view laser films 12 inch x 10 inch compatible with 8900, kodak, carestream camera cartridge of 
Trimax TEX laser imaging film size 25 x 20 cm (10
Construction of Synthetic Surface Volleyball Court with Poles & Allied Accessories
Cabin Pump Assembly,Clutch Cyl Assembly,Ignition Switch,Spider Bearing,Seat Rest Handle,Alternator 
LIGHT ASSY INDICATOR,ASSY SUN VISOR RH,ASSY SUN VISOR LH,ASSY FACE SIDE LH,ASSY FACE SIDE RH,ARM WI
Dust Bin,Wall Clock small size,Table Glass 70 by 30 cm,Massager,Pipe,Scanner cum Printer,Swami hand
SS Hanging clothes rack,Cap Stand,Alarm Bell for emergency situation,Hanger with hanger stand,Broom
Fridge Medium size,Table Glass 150 by 70 cm,Steel Boxes,Heavy duty chimney for OR Mess,Heavy duty m
Table cloth OG,Iron Press,Pillow With Pillow Cover,Potato peeler,Cushion Chair,White Board,Plastic 
Repair of E-Rikshaw
Revolving chair Large Size with footstand,Office Revolving Chair,Fly catcher,Fly catcher tube,Dust 
Desert Cooler Symphony Arctic circle 120L,Desert Cooler Symphony Diet 3D 20i Tower,Desert Cooler Sy
LV7SCORPIO, NKSCORPIO008, LIGHT ASSY REAR LH,LV7SCORPIO, NKSCORPIO009, LIGHT ASSY REAR RH,LV7SCORPI
Clip Hose,Hose Plain,T Collar,Prop Shaft,Harness,Flywheel,Piston,Assy Flat,Reflector Red
Electric injector,Spark Plug,Ignition Coil,Annabond,Wiper Blade,Engine Oil,Transmission Oil,Coolant
Final Amplifier MOSFET 30282 of 40W Jammer Aqua,Driver card of 40W Jammer Aqua,Display Card of DSMD
LV7 TATA 2154-5420-9901 SPEEDO CABLE JIS 4300 LG,LV7 TATA 2641-6710-6305 RUBBER MOULD W-S GLASS,LV7
CLUTCH CYL ASSY,SLEEVE CYL ASSY,CLUTCH PLATE,COVER ASSY PLATE,SPIDER BEARING,BELT V RIBBED,ACCELATO
13 point 9 pct eflornithine cream 15g tube,dutasteride 0 point 5mg tab,finasteride 5 mg tab,l ornit
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Fish Fresh
BA NO 21A-075346P MOTOR CYCLE HERO HF,MOTOR,CYCLE,HERO,HF,Moter,Vech
PORTABLE TOILET CABIN,PORTABLE OFFICE CABIN
SHIM 1
Lignocaine Hcl 2 Solution With Adrenaline cartridge 1 80000 pkt of 50,Disposable Shoe Cover,Cloth G
SQA_V_Capillary_Disposable_50s_pack_50_test for automated semen analyser,SQA_V_Cleaning_Kit_25s for
AMILORIDE 5 MG Plus FUROSEMIDE 40 MG TAB,ANGISPANTR 2.5MG CAP NITROCONTIN,ASPIRIN 150 MG Plus CLOPI
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 70 km from 
LASER UNIT,PAPER TRAY,PRESSURE ROLLER,TEFLON,HDD,DVD WRITER,PAPER PICKUP ROLLER,GEAR ASSY,PROCESSOR
Welding rod 6AWs A51 E6013,Cutting wheel 14 inch,Cutting wheel 6 inch,Cutting wheel 4 inch,Welding 
Liquid developer for automatic processor with starter,Liquid fixer for automatic processor
Turmeric Haldi Powder 1 Kg pack,Turmeric Haldi Powder 100 Gms,Red Chilli Powder Mirchi Powder 1 Kg 
Z1-5950-038703 TRANSFORMER PULSE INDUCTANCE AT 100 MV 1KHZ
Multifunction Machine MFM (V2),Multifunction Machine MFM (V2),Line Interactive UPS with AVR (V2),On
OEM Spares for Automobiles (Q2)
Piston Assy,Ignition Coil Assy,Overload Relay,Piston Ring STD,Seal Oil
Inj Atropine Sulphate vial of 100 ml,Inj B Complex liver extract with vitamin B12 vial of 100 ml,In
SPARK PLUG,GASKET CYLINDER HEAD,GASKET TAPPET COVER,IGNATION COIL,LEAK OFF PIPE,HOUSING PLATE,LUB O
Structure of Cook House Dining Hall FEMS,Structure of Store Shelter FEMS,Structure of Office Shelte
Blue Force Tracking System 4060 Model Fx 507 LP287N Sno S7NRKD034046285,Laser Pointer Green,Pointer
QUICK REL VALVE,ALTERNATOR,CABIN LIFTING PUMP,RAM ASSY,CABIN LOCK,STRUT ASSY,SOLONOID VALVE EXHUST 
Binder,Binder,Binder,Binder,Calculator,Calculator,Cell,Cell,Clip,Clip Board,Cloth,Cutter Blade,Damp
Pressure Plate,Clutch Plate,Clutch Cable,Ignition Coil Assy,Bearing Clutch Release
Bush,Crank Case,Bush STD,Valve,P Rod,Filter,Ring,M Elemac,Strainer,Valve Inlet,Belt
Register,Rubber,Scale,Sharpener,Sheet,Sheet,Sheet,Sheet,Sketch pen,Sketch pen,Stapler,Stapler,Stapl
CRANK SHAFT ASSY WITH WEIGHT BOL,PIPE FLEXIBLE,PIPE FUEL INJECTION TO INJECTOR FUEL,V BELT,DISC COU
Decorative T,T Adhesive,T A Transparent,Boxes,B Fibre,Board Rigid,Fibre Board
ENTECAVIR 0.5 MG TAB,ESCITALOPRAM 5 MG TAB,ESOMEPRAZOLE 20 MG TAB,ESOMEPRAZOLE 40 MG RACIPER TAB,ET
CINITAPRIDE 1 MG TAB,CINNARIZINE 25MG TAB STUGERON,CLINDAMYCIN 1 Percent GEL 10 GM,CLOBAZAM 10MG TA
GASKET CYL HEAD,AC BELT,TIMING BELT,ALTERNATOR BELT,OIL FILTER,FUEL FILTER,HEAD LIGHT BULB,RELAY,WI
TIRE PNEU VEHICULAR 11.00-20 18 PR CC
TAIL GATE GLASS,FUEL FILTER,OIL FILTER,AIR FILTER,WEATHER STRIP FRT DOOR INNER,WEATHER STRIP REAR D
ARMD WELDING ROD,WELDING ROD,CUTTER BLADE,CUTTER BLADE 4 INCH,STARTING FLUID
Fan Belt Generator,Oil Filter,Air Filter,Fuel Filter,Fan Belt Water Pump,Head Light Bulb,Spark Plug
ROPE STARTING NYLON WITH WOODEN HANDLE,AMP METER,VOLTMETER,HOURS METER,SOLENOID FUEL OFF
FUEL FILTER ELEMENT,TRANSMISSION OIL FILTER,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
Plate Clutch,Pressure Plate,Clutch Plate,Clutch Booster Assy,RAM Assy,Air Equalizer Assy,Joint Assy
Hose Td Radiator,Coolant Hose Pipe,Speedometer,Repair Kit Air Dryer,Fuel Pipe Assy,Pinion Assy Stee
Propeller Shaft Rear,Brake Pipe No 02,Clutch Release Brg,Assy Coupling Flange,SR 40 24V,Belt A68,Di
Shaft,Plate,IBG Plate,Controller Assy,Field Coil Assy,Brake Booster Kit,Brake Booster Assy,Cross Di
ORVM LEFT,SOLENOID,ADJUSTING PIN,TIMING DEVICE PISTON,SEALING KIT,FRICTION WASHER,ROLLER
ASSY VACCUM HOSE,ASSY PARKING BRAKE CABLE,ASSY DOOR BEEDING,AC COMPRESSOR,OIL SEAL REAR AXLE
Pipe Oil For Compressor Lubricant,Pipe Assy Air Supply,Part Kit Hande Brake,Braided Hose For Exh Br
SVGA REV3 COLOUR OLED XL DISPLAY
Battery Dura Cell large,Battery Dura Cell small,Calculator,Carbon papers Large,Carbon papers small,
Wooden Shoe Rack,Wooden Double Bed,Wooden Dressing Table,Wooden Cabin For Refrigerator,Mattress,Sli
Z7-5999-720091679 Harness Electrical Battery Charger No-1,V6-6675-000248 Scale Artillery No. 3 Mk-2
Almirah steel medium with shelves,Chair Dining,Chair Verandah MAP,Chair school with hand board,Char
Structural Worksuite (STAAD. Pro+ ) STAAD Foundation Advanced+ RCDC) - Perpetual License
Glucosamine Sulphate 750mg Plus Metyul Sulphonylmethaone 200mg Plus Oxydents And Minerals,Ketoconaz
Soil Investigation
Grease Castrol LZV EP/ Energrease LC2/ Esso Multi Purpose Grease (Molly) /Mobile Gear OGL-461
Dextron-III Defence
PTZ Camera,55 Inch Monitor,OFC Cable D-Link,Steel Pole 25 Feet,Hard Disc 4 TB
Consultancy services on lumpsum basis for preparation of structural design of work services at Camp
Injector Nozzel,Tapper Roller Bearing,Air Horn Relay,Relay 12V,Clutch Fluid Pipe
Regulator assy,Rectifier assy,Kit pad assy front,Reverse light switch,Assy coolant pipe,Hose coolan
Hand brake shoe Scorpio,Rear disc pad Scorpio,Fuel filter Scorpio,Benjo bolt with filter,Pneumatic 
Tyre Buster Secure-S-TB-100,Metal Door Detector DFMD,PTZ Camera,Body Worn Camera,Hand Held Metal De
Repair of Cannon 2006n Photocopier,Repair of Cannon Laser Multifunctional Printer Image Class MF746
Provn of structure for Bathing Cubicle 8 by 1,Provn of Elect items for Bathing Cubicle 8 by 1,Provn
Gamla big size,Apple Gamla,Lemongrass oil,Jafri,Pen Stand,Grass cutting wire,Grass cutting Machine 
Ceiling,Wall Paneling,Lower ceiling,Parameter,Section
CLUTCH RELEASE BEARING,DOOR LOCK REAR,CLUTCH RETURN SPRING,OIL SEAL,THROTTLE GASKET,DOOR STOPPER,WO
Toe Plate for JCB with Cat Part No 61161ESCOU53138112,Seal for JCB with Cat Part No 61161ESCOU99000
Field Flush Latrine (3/1),Field Flush Latrine (2/1)
Bullet Camera,DVR,1 KVA UPS,32 Inch Television Display,12 V 5 AMP SMPS,Video Cable,Casing and Casin
LV7 STLN VF 2540-72-0151486 ARM REAR VIEW MIRROR,LV7 STLN VF X-3545815 U BOLT,LV7 STLN VF F-8284000
LV7 TATA 4720-015041 HOSE,LV7 TATA 3110-107083 BEARING ROLLER TAPER,LV7 TATA 2610-5440-0120 ASSY HE
M2 BOF 6105846 HANDLE FOR BRAKE HAND LEFT RIGHT,M2 IAN 227SA PIPE PRESSURE GAUGE REPLENISH P REAR,M
MASTIC FLOORING FOR LPG GODOWN
LV7 TATA 5930-028265 SWITCH PRESSURE,LV7 TATA 2154-3010-0105 PULL CABLE ACCELERATOR,LV7 TATA 2641-7
LV7 MARUTI 29610M83001 MOUNTING RH FRONT LH,LV7 MARUTI 5340-135143 MOUNTING ENGINE FRONT,LV7 MARUTI
LV6 MT14 2610-001563 TUBE INNER PNEU 215 75 R15 C W VALVE TR,LV6 MT14 2610-000104 TUBE INNER PNEU 8
CHEESE SPREAD,CHEESE CUBE,CHEESE SLICE,SPREAD CHEESE,CHEESE CUBES
Driver card of 10W Jammer Cris,RA 30H 1317M of 10W Jammer Cris,Toggle switch of 10W Jammer Cris,Fan
LV7 STLN 2530-018173 BRAKE LINING KIT,LV7 TATA 2198-4110-0101 ASSY PROPELLER SHAFT FRONT FROM AUX. 
Bathing Cubicle
Bathing Cubicle
ORD ITEMS 1,ORD ITEMS 2,ORD ITEMS 3,ORD ITEMS 4,ORD ITEMS 5,ORD ITEMS 6,ORD ITEMS 7,ORD ITEMS 8,ORD
Gear Shifter Fork,Fuel Hose,Pressure Plate Assy,Bush,Sleeve Cyl Assy,Water Pump,Cabin Shock Absorbe
DOOR MECHANISM FOR MARUTI GYPSY,SPIDER BEARING FOR MARUTI GYPSY,KNUCKLE BEARING FOR MARUTI GYPSY,TI
CARBONATED SOFT DRINKS,LIME BASED SOFT DRINKS,LIME BASED SOFT DRINKS 1,FRUIT JUICE,FRUIT JUICE 1
Prefab Hut / House of Size 4.88 M X 9.76 M (as per GeM Drawing)
Combat T - Shirt (Improved Version) (Defence)
Cheese Sprerad,Cheese Slice,Cheese Cube
Digital video recorder,Security Camera,HDD Disk,DVR Rack,Power Supply,Power Supply,Wire,KVM Switch,
Smartphone,Tablet Type 1,Tablet Type 2,Laptop Type-1,Laptop Type-2
LV7 STLN VF P-1305051 REP KIT FOR OH OF ROTARY FIP,LV7 STLN VF 1377-000335 CARTRIDGE ENG STARTER PR
Red Chilly,Coriander,Turmeric,Cumin,Black Pepper,Cardamom,Clove,Mustered Seed,Emli,Garlic
Napthaline ball coloured,Tissue Paper,Napkin Papers,Phynil 1 Ltrs,Refill Godreg,Hand wash refill 75
PTZ Camera,Bullet Camera,NVR 16 CH SATA,NVR 16 CH Covert Secure,NVR 8 CH SATA,8 Port POE Switch,HDD
Armature assy,Field Coil,Armature,Field coil,Transefar case out put flange,Solenoid switch,Brush ca
Aceclofenac 100mg plus Paracetamol 325mg and Chlorohexazone 250mg Tab,Antispamodic Drop Dicyclomine
Title1,Title2,Title3,Title4,Title5,Title6,Title7
SHOCK ABSORBER,FUEL WATER SEPARATOR,WHEEL BEARING,VANE PUMP STG,SELF STARTER ASSY,STG PUMP ASSY,HOR
Common Cold Tab Antihistiminics plus Paracetamol 325 to 500 mg without pseudoephedrine,Ibuprofen Sy
Comprehensive Annual Maintenance Contract for Intercom System for HQ CE (Navy) Mumbai
Custom Bid for Services - 1
Labrador Retriever Stock
Air Conditioner 1 Ton All Weather
Cement OPC 43 Grade packed in HDPE bag each 50 Kg wt conforming to IS 8112-1989 Make-Birla Gold,Amb
LV7 STLN VF 14683760174 AR DISTRIBUTOR HEAD,LV7 TATA 2786-1499-9936 TURBOCHARGER,LV7 MARUTI 89913M7
A4 Ream 100 GSM,Wireless mic set of two,Acrylic display board size 02 ft x 06 ft,Broom,Room Freshen
TRUCK TYRE CHANGER
Housing,Vane pump,Nozzle,Distributor head,Pump element,Valve fuel system delivery valve,Solenoid op
BELT TIMING MPFI,BELT WATER PUMP,HOSE RADIATOR OUTLET NO 1,COVER ASSY CLUTCH,DISC CLUTCH 415 MPFI,B
TC 00870 GP Bucket Assy With HD Tooth,4274663 Control Cable,TB20525 Pilot Piping,TE22613 Control Ca
125FL92676 Fuel filter spin on,11Z8200268 Starter motor,CFB2711045 Bolt for U Joint,CFW0111030 Wash
Paintball Gun of 0.68 calibre including two magazine,Hopper,12oz Co2 Tank empty,On Off Valve,Paintb
LV7 TATA 264182400135 ASSY KIT FOR WIPER MOTOR,LV7 TATA 2154-2810-0102 ASSY CABLE COMPLETE,LV7 TATA
H1 8010-000290 OIL LINSEED RAW,H2 8305-000047 CLOTH BUNTING NAVY BLUE 145 CM V.NO2,G2 3439-000101 R
LV7 MARUTI 82592M80060 COVER GATE HANDLE,LV7 STLN VF F-8824200 BRAKE SWITCH RELAY 24V 30A ALT FN200
Provn of Security Post Shelter part only FOR MENCHUKA,Provn of Security Post Shelter part only FOR 
ASSY CLUTCH DISC,PRESSURE PLATE,ARMATURE ASSY,FIELD COIL ASSY,BRUSH CARRIER PLATE,FOG LIGHT,AIR FIL
HAND BRAKE ASSY,DRANG LINK,CHAIN AND SPROCKET SET,CLUTCH CABLE ASSY,OIL FILTER,FAN BELT 8PK 1155,FA
SENSOR ASSY,FUEL RELAY,U BOLT,FRONT BRAKE PAD,REAR BRAKE SHOE,KICK STARTER RUBBER,BRAKE SHOE,SPARK 
NOZZLE,DELIVERY VALVE,GASKET SET,PUSH ROD,LEATHER CLOTH PVC BLACK,SHEET CELLULAR
BATTERY CUT OFF SWITCH,HOSE NON METALLIC DIA 1 HOSE P 522,CABIN LIFTING HOSE 14MM,SPRING BRAKE CHAM
KIT PAD ASSY,WIRING HARNESS,HEAD COMP CYLINDER,COOLANT CAP,ELEMENT OIL FILTER,ENGINE OIL SEAL KIT,K
Refined Musterd oil 15 kg Tin,Refined Musterd oil 1kg Poly Pouch,Refined Musterd oil 15 kg Tin_1,Re
Radiator assy for MPV,Spider bearing for MPV,Speedometer cable for ALS,Fan belt 1552 for MPV,Steeri
LV7 MARUTI 37870M80020 SWITCH HEATER FAN,LV7 STLN F-4731111 DE SPANNER 18X19,LV7 STLN F-4735211 RIN
LV7 TATA 278650006302 RUBBER BUFFER 38DIA X 12 THK,LV7 TATA 278607989961 switch pressure,LV7 T-815 
Sevoflurane Bottle of 250 ml,Isoflurane Bottle of 100 ml,Inj Diclofenac 25 mg ml IP 3 ml,Inj Fosphe
Dexorange Syp,Liv 52 Syp,Otipil ED,Neosporin Pdr,Aptiquik Spy,Dexacon 100 ml,Accusure Hb Test Strip
Connector for single point,Fan Motor Thin Shaft Clock wise,Six Point Connector Twenty Five amp,Refr
OIL PRESERVATIVE SAE-30/PX-16
FS Paper 80GSM,Index folder,File Binder,Digital Calculator,Stapler pin No 10 small,Binder Clip 1 in
G1 5305-002716 SCREW WOOD SLOTTED CSK HEAD MILD STEEL N,G1 5305-001655 SCREW UNF-2A X STEEL CAP SOC
NK002128 HUB CUP NUT,50 352 2 BACK PLATE LOCK PLATE,NK002191 VALVE RELAY,4720000413 HOSE ASSY RUBBE
Dexron II 60716902 (Breake Oil/ Dexro II) (Equivalent recommended by OEM is Mobil ATF 220 ex Mobl I
Refined Sunflower oil 15 kg Tin,Refined Sunflower oil 1kg Poly Pouch,Refined Sunflower oil 15 kg Ti
RFID Card,RFID Scanner,Access Management Software,Desktop Computer,2 KVA Online UPS,9U Rack
OIL FILTER ELEMENT,FUEL FILTER,ZINC ANODE 1,ZINC ANODE,IMPELLER WATER PUMP
Bearing Ball annular,Brg Tapper Rollar,Gaskit Cyl Head,Assy Cable Complete,Assy propeller Shaft fro
Provn of Officers JCOs Living Shelter FOR SHORANGDAM,Provn of Construction Material for Officer JCO
G Arabic,H Technical,S Pure,Rosin,L Raw,Dubbin,Chalk,SR-998,B Wax
L7-FC-VF-WT-BEL-2123-073-301-14,L7-FC-VF-WT-BEL-2123-072-101-25,L7-FC-VF-WT-BEL-2123-073-201-23,L7-
2610-001380 TYRE PNEUMATIC 9.00-16, 16/18 PR CC
SKF-32218 BEARING NO-7518
PART NO 7714 BEARING 7714
0/5210-415477 JACK HYDRAULIC HAND
TUBE INNER PNEUMATIC 130MM
Suspension clamp rear for Rakshak Plus,Steering tie rod for Rakshak Plus,Servicing and maintenance 
SPEEDO CABLE,BEARING TAPER ROLLER,BEARING TOPPER,BEARING,CLUTCH PRESSURE PLATE,ASSY CLUTCH DISC,SPE
Analog Locker 89 ltrs
Chilly,Turmeric,Dhaniya,Garam Masala,Chat Masala,Chole Masala,Chicken Masala,Mutton Masala,Biryani 
BEARING,ASSY OIL FILTER,SPEED SENSOR,RELAY,FUEL TEMP SENSOR,OIL FILTER,CABIN LIFTING HOSE,SEAL HUB,
Assy clutch Master Cyl,Starter,Isolator Switch,Tensioner Timimg Belt,Bush Self Starter,Major Rep Ki
Video Recorder for CCTV System (V2)
OKS 480 Grease
Track Roller Single Flange 80,Fuel pressure guage,Fuel sensor,Washer spring,Bolt,Water temp guage,B
Copra , Pickle , Papad
bearing,wiring assy front,air filter element,brake pipe,filter assy wo element,element oil filter,v
GASKET KIT GEAR BOX,NEEDLE BEARING,CYLINDRICAL ROLLER BEARING,SPRING KEY REPAIR KIT,GEAR OVER TOP C
S and fix in rep solar cat eye allum alloy shall 100 perc water proof design according to 65 of siz
13907Inj Fosaprepitant 150mg,11668Netupitant 300 mg plus Palonosetron0point5 mg Cap
Valve Relay Air,Part Kit Eng Oil Pump,Tank Coolant Veh,Air Dryer,24V DC DC Convertor,Part Kit Relay
Custom Bid for Services - Selection of an Firm for engaging 1 x Resource for redesign upgrade devp 
Tray White,Table with Chair,Napkin Holder white,Table Cloth,Cushion cover 20 x 20,Cushion Pad 20 x 
HARNES ASSY WRING ENG,COIL ASSY IGNATION,WHEEL BEARING REAR,HOLDER ASSY RECTIFIRE,SUSPENSION BUSH K
F1 5110-000286 BLADE HACK SAW HAND FLEXIBLE COARSE NOMI,H4 8135-000084 PAPER WRAPPING BROWN UNGLAZE
SWITCH ASSY COMBINATION,REGULATOR SR 40,VOLT METER D60 24 V,PNEUMATIC VALVE,CLUTCH PLATE,FEED PUMP,
VAG Cable,HDMI,Connector,Picket,Connector,Blower,Cable,Card
Custom Bid for Services - Soil Investigation
Thermostat,PTC Relay,Cooling l,Running,Frost free,PCB,Refrigerator,Compressor,Comp refri
Thermostat,Relay water,Relay w,Self closing,Running,Capacitor,Condenser,Compressor,Compressor s
G2 3439-000167 FLUX WELDING ALUMINIUM 110g container,G2 9525-000066 WIRE COPPER HARD 1.00 mm,G2 953
Custom Bid for Services - Consultancy services for preparing dpr fro storm water drain network
BOF- EC6S-10X16 N2-75 HEXAGONAL SOCKET SCREW,BOF- LB6M-10 N3-9 NUT LOW,BOF- KPG-10X30 PIN TAPER SCR
Assembly Table for Winch Reducer of ARV WZT III
Provn of Combined Toilet Bathroom Block Shelter Part Only FOR HOCHE,Provn of Combined Toilet Bathro
Saw blade habd hacksaw flexible fine 300mm,Blade hand hacksaw flexible coarse 300mm,Saws blades han
Workstation size 10 ft x 06 ft with 08mm Glass
CLUTCH CABLE,BRUSH SET,UNIVERSAL JOINT,BRUSH CARRIER ASSY,DUAL BRAKE VALVE KIT,WHEEL CYL REPAIR KIT
Steel Angles 45x 45x6 mm
H3 5510-000361 Timber Soft Wood (Coniferous) Sleepers G
Starting capacitor,Starting window,PCB window,Blower motor,Refrigerant Gas,Gas cylinder.,Compressor
P1 155 UG 176-6241 LEAF SPRING,P1 155 UG 176-6217 FLEXIBLE HOSE,P1 155 UG 176-6211 STOPPER FRONT RE
Brush Gear Assy,Drive Assy,Field Coil Assy,Tapper Roller Bearing Front Hub,Clutch Release Brg,Injec
V BELT,SRDG BALL BEARING,CLUTCH PLATE,ASSY CLUTCH PRESSURE PLATE 330 DIA,ASSY CLUTCH RELEASE BEARIN
5 Amino Salicylic Acid SR 1 point 2 g Tab,Tab Cap Dicyclomine 10mg,Glycerine Suppositories child si
POVIDONE IODINE SOLUTION 5 PERCENT BOTT OF 500ML,CHLORHEXIDINE GULOCONATE SOLUTION IN SOAP 4 PERCEN
EPIRUBICIN HCL 10 MG INJ,Isosfamide Inj 1g vial with 3 amp of 2 ml each Mesna,METHOTREXATE 15MG PRE
MITOMYCIN C 40 MG INJ,Recombinant Human Growth Hormone 5 mg to 15 mg Inj or equivalent in IUs,Caspo
BA NO 24A-079748A MOTOR CYCLE BAJAJ PLATINA,MOTOR,CYCLE,BAJAJ,PLATINA,Vech,Moter,Cycle
CLUTCH VALVE,CONTROL VALVE,HOSE,WIND SCREEN GLASS,FRONT WIND SCREEN WEATHER STRIP,GASKET CYL HEAD,S
STARTER MOTOR MICO,SPEED SENSOR AGB,BRUSH GEAR ASSEMBLY,RELAY EMERGENCY VALVE,MAIN RELAY TYCO MAKE,
Alternator Assy,Tank Coolant Vehicular,Slave Cyl,Switch,Master Cyl,Window Dropper,U J Cross,Assy Co
CLUTCH PLATE ASSY 330 DIA,PRESSURE PLATE ASSY,CHAIN SPROCKET SET,OIL SEAL,KNUCKLE BEARING,SPANDLE F
GLASS BACK DOOR,BEARING BUSH CE,BEARUNG BUSH INTER BKT,NUT REGULATOR HEXOGEN,SEAL KIT WORM SHAFT,NE
ARMATURE ASSEMBLY,SOLENOID SWITCH,BUSH SET,RESISTANCE,DRIVE ASSEMBLY PINION,BUSH SET,FIELD COIL ASS
Spider Brg,Spider Brg,Cabin Lifting Pump,Tie Rod Assy,Isolator Switch,Fog Light Assy,Propeller Shaf
PRESSURE COOKER 22 LTR GASKIT RUBBER,BASKET RATION WITH LID,BUCKET PLASTIC 13 LTR,BUCKET SS 325 MM 
Reservoir for insulin pump set of 10 Set Meditronic,Serratiopeptidase 5mg tab,Sevelamer 400 mg Tab,
TAPARIYA SPANNER SET 25 PCS,TAPARIA ALEN KEY 9 PCS,TAPARIA SOCKET SET 24 PCS,T HANDLE,VACUUM PUMP
Premarin Cream,Primaquine 7.5mg base Tab,Prochlorperazine Maleate 5mg Tab,Promethazine HCl 2.5perce
Pipe Fuel,Ignition Coil,Braided Hose For Exh Brake,Part Kit Hand,Pipe Nylon,Weather Strip,S A Of Pi
Red chilli powder 500gram,Turmeric powder 500gram,Coriander powder 500gram,Hing 100 gram,Kasturi me
Red chilli powder 500gram,Turmeric powder 500gram,Coriander powder 500gram,Hing 100 gram,Kasturi me
Haldi Powder,Mirchi Powder,Dhaniya Powder,Tej Patta,Zeera,Rai,Saboot Dhaniya,Chhoti Elaichi,Badi El
Oil M3-52
Paraformaldehyde Tab,Povidone Iodine 10 percent solution bott of 100 ml,Lorazepam 2mgml 2 ml Inj,Ba
H2 4020-000118 CORD COTTON BLUE 2MM DIA,H2 4020-000195 TWINE JUTE,H4 8135-000091 PAPER WRAPPING 118
Anti Ane post
OIL SERVO SYSTEM 57
Envy X360
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13
Rabeprazole 20mg plus Domperidone 30mg Sustained Released Cap,Rabeprazole 20mg plus Levosulpride 75
Starting Rope Assy,Injector Nozzle,Fuel Pipe,Automatic Voltage Regulator,Filter Air Complete
Cam Plate,Dia 3 8 Hose,Joint Assy Universal,Clutch Disc,Master Cyl Power Unit Clutch Master Cyl,Rep
Water Colour 12 number per packet,Poster Colour 12 number per packet,Drawing Pad,Drawing Colour Pen
High Mast Lighting Tower for large area with LED Flood Lighting System
Custom Bid for Services - Architectural and structure drawing
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Healthcare,Manpower 
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Admin
Risperidone 2 mg Tab,Risperidone 4 mg Tab,Salbutamol inhaltion 100mcg 200 metered dose MDI,Salmeter
CLUTCH SLAVE CYLINDER,CROSS UJ,DISC CLUTCH,MOUNTING ENG FRONT,BEARING,REPAIR KIT FOR MAIN CYL CLUTC
F1 5120-003544 BLADES STABBING 65 MM SHARP END AWLS,G1 5310-001377 WASHERS PLAIN STEEL ZINC PLATED 
Servo Hydrex-100
LV7 MARUTI 34100M80580 SPEEDOMETER ASSY,LV7 STLN VF F-2208800 COMBINATION SWITCH,LV7 STLN 2530-0179
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others,Manpower Outsourcing
CCTV Camera,Online UPS,TV 55 inch,DVR 24 Channel,Cable,Coverter,SMPS
Separator Water,Wheel Bolt,Hydraulic Aggregate HA 25-3V Pump,Fuel Filter Element,Oil Filter,Oil Pum
EMERGENCY AND PUBLIC BROADCAST SYSTEM
12101-KCC-940 CYLINDER,22-K-130 CAM CHAIN KIT,2830AKAA900 KICK ASSY,2805-002856 RING SET PISTON STD
Oil filterassembly,assembly filetr element,Poly V Belt,assembly caliper brake,Armature assembly,Air
Side view mirror LH,Head light assembly,Bonnet shock absorber,Rubber bush set,Kit pad brake front,M
10327161 LV7 T 815 442 973 180 324 REAR DOOR LH,10333402 LV7 T 815 5140 012790 TOOL BOX,10342926 LV
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Speedometer VDO,Hose Rubber 800 MM,Hose JS 8X800,Clutch Booster Hose,Oil Seal,Door Glass Gasket
G2 9505-000018 WIRE STEEL MILD ANNEALED O.56mm,G2 9505-000049 WIRE STEEL SPRING SOFT 0.500MM 25 SWG
LV6 MT13 2540-72-015-1433 X-4115800 TARPAULIN ASSY CANOPY,LV7 MARUTI 15100M830A1 PUMP ASSY FUEL,LV6
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Oil Servo Quench No 11
H1 B 5350-000012 ABRASIVE CLOTH GLASS IS GRIT 50 SIZE OF,H1 B 5350-000014 ABRASIVE CABRASIVE CLOTH 
Avr,Pipe Fuel Pump to Injector,Rectifire Assy,Starter Motor Pinion,Belt V Femmer A-50,Oil Filter 30
LV7 TATA L01402000036 FIELD COIL ASSY,LV6 MT1 5110-007355 BLOCK JACK,LV7 TATA 2641-7250-2301 DOOR G
LV7MARUTI 35100M800011,LV7MARUTI 15410M830A1,LV7MARUTI 33400M78L00,LV7MARUTI 17700M83112,LV7MARUTI 
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Almond,Amchur Powder,Black Channa,Black Papper,Black Papper Powder,Baby Cashew,Bread Crums,Cranberr
Needle Bearing,Fuel Filter,Water Separator Assy,Hub Seal,Gear Lever End Small,Gear Lever End Big,Ge
HONEY SUCKER
IFS Static Model Scale 1 is to10,NBC Recce Vehicle BMPII Static Model,WPS Model Scale 1is to 10,3 D
J2 7320 000012 SHIELD WIND CIRCULAR,J2 7310 000157 COOKER OIL STOVE,J2 7320 000006 CONTAINER GHEE O
Engine Oil Pressure guage,Manifold water,Seal kit,Hose Assy,Fuel Filter Primary 50,Hyd Pipe LH,Hyd 
EP-320
LV7T815 4433320370,LV7T816 9930502890,LV7T815 2073012694,LV7T815 2073012684,LV7T815HMV 2070310934S,
SUPPLY ONLY 02 X TOILET BLOCK INCLUDING CONSTR MATERIAL AND ELECTRICAL ITEMS AT JANGLOT
SHOWER BATHING TROLLEY
Z9/6140-005207 BATTERY SECONDARY PORTABLE LITHIUM
H1A 8010-000281 VARNISH INSULATING AIR DRYING OIL,H1A 8010-007501 PAINT RFU FIN SYN ENA BR-SPR OLIV
H4 8135-000041 PAPER WRAPPING 735 X 1120 MM X 0.04 MM,H4 8115-000518 BOXES FIBRE BOARD RIGID CORRUG
: Hydroxypropyl Methyl Cellulose (Hypromellose) Ophtalmic solution 10 ml,Hydroxypropyl Methyl Cellu
Provn of OR Living Shelter 20 Men Shelter Parts Only FOR TATO,Provn of OR Living Shelter 20 Men She
mobilising of manual drilling equipment,boring 150 mm dia bores,collection of undisturbed soil samp
CP-Plus 32 Channel NVR,CP-Plus 16 Channel NVR,CP-UVR-0401E1-CV5 4 Channel DVR,8 TB Surveillance HDD
HIRING OF 1 x P3 PIXEL DATA WALL SIZE 14 X 10 SQFT PER DAY REQD FOR 3 DAYS,HIRING OF 2 x P3 PIXEL D
Thermal Pouches for batteries
GLOW PLUG BERU,CLUTCH MASTER CYL,CLUTCH BOOSTER ASSY,QUICK RELEASE VALVE,FIP SOLENOID
Dak seen Rubber Stamp for A Br,Dak Seen Rubber Stamp for Q Br,Rubber Stamp Col CO Hindi and English
All in one professional screen,All in one professional screen 2,All in one professional screen 3,Ke
Battery Secondary Lead Acid MT Type (Defence),Battery Secondary Lead Acid MT Type (Defence),Battery
Tower Server,UPS 5KVA with battery and 60 mins backup,Layer 2 Access Switch 24 port fully managed,E
Solar Security Street Light 1,Solar Security Street Light 2,Solar Security Street Light 3,Solar Sec
DOOR LOCK ASSY RH,SLAVE CYLINDER ASSY,CYL HEAD GASKET,ASSY KIT LINED SHOE REAR,TURBO INLET PIPE
Biometric Access Control System
Bearing Ball,Bearing Ball Single Row,Bearing Ball Single Thrust,Bearing Ball Angular,Screw Cap Sock
10 mm 3 Core Electric Cable,4 mm 3 Core Electric Cable,Floor Mounted AC Bracket,Wall Mounted AC Bra
Firing Range Auto Scoring System FRASS 8 Lane System,RJ Connector,Target Sheet,Wifi Router,POE Swit
SYP CREMAFFIN WHITE EACH 15 ML CONTAINING MILK OF MAGNESIA 11 point 25 ML LIQ PARAFFIN 3 point 75 M
Spring Brake Chamber,Mirror Assy Rear View,Radiator Assy,Shock Absorber Front,Valve Relay Air,Maste
COATED GOLD CUP EEG ELECTRODES,TEN-20 CONDUCTIVE EEG PASTE(TIN 224GM),DISPOSABLE NCV ELECTRODES
Split Air Conditioner Including Green AC, Wall Mount Type (V2),Split Air Conditioner Including Gree
2610-001474 TYRE PNEUMATIC 8.25X19 PR 10CC
Supply of Ceiling microphone with Suspension,Supply of Wired Digital Gooseneck Microphones with Sta
IMPELLER WATER PUMP,SEAL OIL SEA WATER PUMP,SEALING COMPOUND,QUICK FIX,ADHESIVE SYN RESIN ARALDITE
PISTON ASSY,LINER ASSY,CR BEARING,CYL HEAD GASKET,TAPPET COVER,PISTON RING SET,AIR FILTER ELEMENT,R
MT SHED 1,MT SHED 2,MT SHED 3,MT SHED 4,MT SHED 5
Oil separator,Suspension bush kit,Crank angle sensor,Spider bearing,Solenoid switch,Disc pad front 
Tube light 36 Watt,SFP Module 120 KM,Battery Tester,Fiber Cleaver,Cutting Plier
UPS 1 KVA,Cat 5 RJ 45 connectors,Switch 8 Port,VGA Cable,BNC Connector,VGA to HDMI Converter,lsopro
Soldering Iron,Soldering Wax,Soldering Wire,Soldering jack,15 Amps Socket,5 Amps Socket,15 Amps Top
PTZ Camera 2 MPX 36X,NVR 32 Channel with 4 TB HDD,NVR 64 Channel with 16 TB HDD,OTE 20 KMS,UTP Cabl
Red Chilli Powder,Coriander Whole,Turmeric Powder,Jeera,Ajwain,Chicken Masala,Garam Masala,Panner M
Radio Master RP3 V2 Express LRS 2point 4gHz Nano Receiver,IMAX B6 AC professional Balance Charger o
DLD-NNK-K9-FF-REFILL-3 Fire Extinguisher 2 KG Halon 1211 Mtrl No 10586109
Shaft,Disc Plate,Plate,Gear Driven 4,Gear Driven 4,Gaskit,Gaskit,Cover,Boot,Leaver Change,Seal Oil,
K9/ARJ-174000177220 Assy Fire Ext 2 KG BCF Halon 1211 (Mtrl No 10491060)
FRUIT DRIED (RAISIN GREEN)
DISPLAY HOURS METER,AIR FILTER ASSY,CC COIL TRANSFORMER,NOZZLE,3 PHASE MEB
WEATHER STRIP BACK DOOR OPENING,WEATHER STRIP RR DOOR LH,WEATHER STRIP RR DOOR RH,FUSIBLE LINK A TY
P Emery,Cloth Emery,Abrasives C,A Cloth,E Corundum,A Cloabrasive,P Glass,Copper,H Technical,Solvent
S Bar,Bar Carbon,Hot Rolled,Hot R Round,S Sheet,Wire,S Spring,S Mild
Manpower Outsourcing Services - Minimum wage - Unskilled; Secondary School; Others
Glue A and B Tube,Feviquick,Solder Soft Grade C,Horizontal Cylinder Seal Set,Vertical Cylinder Seal
ASSY TUBE WITH CRIMROD RUBBER HOSE,ASSY TAIL LAMP RH,HOSE CLIP,BRAKE OIL CONTAINER PIPE,COOLANT PIP
OEM Spares for Automobiles (Q2)
OEM Spares for Automobiles (Q2)
Flex with frame,Steel tipen Five Cantaner,PVC Pipe,Wall Clock,Halipad Flage,Water Bottle 20 Ltr,Ser
Antistatic Training Table for Comn,Volumentric ESD Tap,Well Designed Perforated Traning Panel,Jigs 
LV7/HRV AV-15 578-903-910-752-34 Adjustable Brake
Training Automatic Switch for Lt Veh,Fixture Jig for Elect Training Charger,All Terrain Veh Chain J
All Terrain Veh Jigs System,Solar Path for Training,Training Solar Panal,Jigs Rigid Training Markar
LV3/ICVs 2920123508205 Starter S5-2S (SB 20-09-02-2)
Oil 2T Supreme 1,Oil 2T Supreme 2,Oil 2T Supreme 3,Oil 2T Supreme 4,Oil 2T Supreme 5
Wheel Brake Cyl,Clutch Plate,Slave Cylinder Assy,Cabin Lifting Pipe,Mud Flap,Door Trim,Four Way Val
Spirax S3 ATF MD3 Caltex Texmatic 1888 1,Spirax S3 ATF MD3 Caltex Texmatic 1888 2,Spirax S3 ATF MD3
SPROCKET SET FOR MC RE,SHOCKER GASKET FOR MC RE,OIL SEAL FOR SHOCKER FOR MC RE,BRAKE SHOE FOR MC RE
Refrigerant R407C
Aeroshell Grease 33
Grey Cloth,Wooden Sofa,Foam thick,White Cloth,Pillow Cover,Jhulla,Green Net,Acrylic Board
Valve Brake Pneumatic,Phase Plate,Diode,Change Over Switch,Major Repair Kit Air Compressor,SA Drive
W Brown,Hessian C,W Kraft,W B Unglazed,W W Plain,Paper W,P W Brown,Paper W 1189,W Proof Plain,B Swe
B TIN , BLOCK , TABLE , NAIL B , NUT
Title1,Title2,Title3,Title4,Title5
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9
CCTV CAMERA WITH CABLE AND INSTALLATION
TREADMILL,GYM BIKE,LEG PRESS,MASSAGE CHAIR,INSTALLATION
Carpet 7 Ft by 10 Ft,Carpet 6 Ft by 8 Ft,Carpet 4 Ft by 6 Ft,Side Carpet 2 Ft by 6 Ft,Carpet 6 Ft b
WD 40 Anti Rust
STARTER MOTOR,CLUTCH BOOSTER,CLUTCH DISC,REPAIR KIT MAIN CYLINDER CLUTCH,MAIN CYLINDER DIA,STARTER 
Super Structure of Combined Toilet Bathroom CTB under Job No 2536 as per Appx A of stores list att 
Soiling,Asphalt work,Volleyball Court synthetic work,Volleyball Court synthetic work,Volleyball Cou
BATTERY,AIR CONDITIONER,CARPET,JAFFARI,DOOR CURTAIN,DOOR CURTAIN
Ethicyl Estradiol 0.035mg Cyproterone Acetate 2 mg pack of 21 Tablets,Hydroxyprogesterone Caproate 
DRR UHF BASE SIGNAL EXTENDER
Smart Map 9ft x 7ft
360 Laptop
Pinion,Bushing,Ignition Switch,Solenoid Switch 24V,Trailer Brake Valve,Ram Assy,Repair Kit sys Prot
Cord Set High Tension,O Ring Spark Plug,Hose Inlet Joint,O Ring,Gasket Cyl Head Cover,Gasket Intake
Resist-X Plus Anti Rust Oil (Equivalent Recommended by OEM is RESIST-X Plus ex Siddhi Enterprises
Tetanus Toxoid amp of 0 point-5 ml,Colistimethate Sodium 1 million IU Inj,Feropenem sodium 200 mg T
MCB Signal 16A,MCB Signal 10A,MCB Box 12 Way,DP 63A,MCB Signal 32A,Board Signal 16A,16 Amp Socket,5
ROD ASSY CONNECTING,OIL SEAL,OIL SEAL RETAINER,PUMP OIL GASKET,STARTER REALY 24V,NEELDLE BEARING,SH
DRIVEN CLUTCH PLATE,DRIVEN CLUTCH,COMBINATION SWITCH,ALTERNATOR,ASSY CLUTCH MASTER,ASSY SLEEVE CYL,
INSULATTION TAPE,THREAD TAPE,FEVIKWIK,M SEAL,ARADITE,ANOBOND,FUEL PIPE,SOLDERING WIRE,WELDING ROD,E
Gasket Timing Belt Cover,Coil Assy Ignition,Sensor Water Temp,Pump Assy Fuel,Gasket Cylinder Head,R
BIPAP Machine with humidifier,Auto CPAP Machine with Humidifier
Dusting Cloth,Dusting cloth yellow,Tag green full size,Register 500 pages,Register 300 pages,Regist
ASSY 01-02 SLIDE RAIL
ASSY 26-62 CONTROL VALVE (26-62)
Envelope White,Epson Printer Color Ink,Printed Register 350 pages,Tharmocol,Fevicol 500gm,Nail 2 In
Dicyclomine HCL IP 20 mg plus Paracetamol IP 500 mg Tab,Cap Doxycycline 100 mg,Amikacin Sulphate 25
LV7 TMB 2574 3325-3104 AXUAL ROLLER BRG,LV7 TMB 2573 4370 0181 SYSTEM PROTECTION VALVE,LV7 TMB 2752
FS Paper,A4 Paper,A4 Bond Paper,A4 Photo Paper,White File Cover without Crest,Reynolds Ball Pen Bla
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Custom Bid for Services - BOQ item No 1 Semi Skilled Electrician per shift of 08 hours          572
LIQUID MEDICAL OXYGEN(IP OXYGEN)
LV7 TATA 0460-426-337 PUMP FUEL INJECTION ROTARY,LV7 STLN B0N00720 WIPER BLADES,LV7 STLN 4810-00766
DAFC 60 percentage Indigenous,Protective PX 11,Oil OM 58,URF 80 20,Poly Ethylene Saloxena PES 3,Gre
Product1,Product2,Product3,Product4,Product5,Product6,Product7,Product8,Product9,Product10,Product1
Grease XG-240
Microsoft,Microsoft Endtable,Mousepad,Amplifieer,Speaker 200w,Microphone,Ergohuman,Wire,Racket,Shut
Round Pipe,Steel Angle 1x1x2mm,Steel Bar Carbon Hot Rolled Flat 25x3mm,Bolt with Nut,Paint RFU Glas
LV7 TATA 2912-8711-7034 RESERVOIR VISO F 27 4,LV6 MT13 2540-72-040-4397 2416-7000-0137 TARPAULIN AS
HIGH TEMPERATURE STEAM DISINFECTION SYSTEM
D IFA RE 24 Cycloserine 250 mg Cap,D IFA RE 24 Fluticasone propionate lotion 0 DOT 05 bott of 10 ml
Steel Angle 45 x 45 x5 MM,Aluminum sheet½ Hard 0.91 MM
Human Insulin Analogue Rapid acting Inj 100 IU per ml 300 IU Disposable Pen with 5 needles per pen,
Custom Bid for Services - BOQ item No 1 Skilled Electrician per shift of 08 hours        1023 Shift
Annual maintenance contract (AMC) for EPBX system and Biometric Machine and connected items.
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
AIR DUCT RIGHT,AIR NOZZLE,ASH TRAY,BALL,BATTERY CABLE CLIP,BATTERY CABLE CLIP,BATTERY CABLE CLIP,BA
3POINT JUNCTION CONNECTOR FOR 3 TERMINAL,5 POINT JUNCTION CONNECTOR FIVE POINT T,ADAPTOR,ADAPTOR RE
Tab Sertraline 50 mg,Propranolol TR 40 mg, Tab,Ivermectin Tab 6mg,Fluconazole 50 mg cap slaceTab,Sy
Solar Lamp (Solar Study Lamp) (Q3)
Semi Conductor Device Diode TVS IH 6063,Chok 4.7 MH 11.4 Amp,Inductor Radio Frequency Coil freq 10 
DOME LIGHT,DOOR HANDLE LH,DOOR LOCK LH,DOOR LOCK RH,FUEL FILTER,HAND PUMP DHP,PROTECTIVE BAG,REDUCT
Flex Banner,Caps,mementos,Medals,Incentives to the participants,Photography and video coverage,Expe
Bag Pack,Stationary and study material,Hiring charges of 02 x teachers,Hiring Charges of Class Room
Bag Pack,Stationary,Hiring of 02 Teachers,Hiring of Vehicles,Daily Refreshment,Hiring Charge of Cla
Preservation Fluid MIL- L-6082E GDE SAE 30
Mother Board,SMPS,Graphics Card,CPU Cooler,RAM 32 GB
SSD 1 TB,SSD256 GB,Cabinet,Processor,Keyboard
Bullet Proof Shield and Bomb Blast Inhibitors for Light Vehs (Maruti gypsy)
Bullet Proof Shield and Bomb Blast Inhibitors for 7.5 Ton ALS Truck
Bullet Proof Shield and Bomb Blast Inhibitors for 2.5 Ton Truck
Protective PX-7 (For ground Equipment only)
AD Blue Mixture
2.5 Ton TATA 407 08 hrs 80 km Plain Local duties,2.5 Ton TATA 407 08 hrs 80 km Hill Local duties,2.
4140003331,2530720477095,P4329039,2530720306882,NK1,NK2,B-9100105
Steam Coal
Common Cold Cetrizine 5 10 mg Paracetamol 500 mg Pseudoephedrine 30 60 mg,Deflazacort 6 mg Tab,Indo
10345226,10612640,10456948,10323997,10325837,10601600,10448218,10470695,10454522,10610824,10592711,
TOOL KIT CVD-30166 ANCHOR HOLD FAST NO 1,TOOL KIT CVD-X-4704011 RING SPANNER 18X19 METRIC,TOOL KIT 
LV7 T-815 443-400-143-000 SPEEDPMETER,LV7 T-815 443-311-119-000 TURN INDICATOR - 9446-0. OR 892007,
WHITE FILE BLANK,WHITE FILE PRINTED MONOGRAM,PRINTED COLOUR FILES,LEAVE CERTIFICATE PAD,WORK ORDER 
title1,title2,title3,title4,title5
Revision Knee Prosthesis (Linked Rotating hinge and metaphyseal sleeves) with 1. femoral component,
QUADCOPTER WITH HIGH RESOLUTION CAMERA
Aluminium Alloy Connector with Olive drab chromate over cadmium Plate with Protective Cap 19 Pin Fe
O/1020-001855 ROD WITH PISTON
2610-000286 COVER PNEUMATIC 14.00X25 20PR OTR TYPE
Military Tourniquet Advanced,Hemostatic Combat Gauze,Emergency Compression Bandage,Chest Seal dress
Military Tourniquet Advanced,Hemostatic Combat Gauze,Emergency Compression Bandage,Chest Seal dress
CLUTCH PLATE ASSY,COVER ASSY CLUTCH,SENSOR ASSY 4X4,BRAKE HOSE LH,BRAKE HOSE RH,ASSY VACCUM HOSE FO
Advanced Hexacopter Drone,Battery for Advanced Hexacopter Drone,Propeller Set for Advanced Hexacopt
DAFC-60
C Solid,Rod,Mild General,Bolt,N Steel,Iron Cast,Rod W,W Copper,Hard Facing,Rod W H,W Cast,Screw,S W
SWITCH PRESSURE,INDICATOR LIGHT GLASS,CONVOY LAMP,SENSOR SPEED,REPAIR KIT,ASSY CLUTCH PRESSURE PLAT
Digital Hearing Aid Model A,Digital Hearing Aid Model B,Digital Hearing Aid Model C,Digital Hearing
Wall Lamp with LED bulb for dining hall,Polishing of Wooden Table and Chairs,Calling Bell Wireless,
F1 5210-000073 Callipers Outside Firm Joint 150 MM,F1 3439-000209 Iron Soldering Elect 6V-25W,F1 51
Flying Insect Control Traps - Fly Catcher
High Pressure Portable Pump for large fire fighting as per IS 12717
LV7TMB2786 0798 9916,V56650 005426AGD 10549715,V56650 00542610546030,LV7TMB2786 1499 9938,LV7TATA26
J1 7330 000361 FLASK THERMOS 1.5 LTRS JAR VACCUM 1000ML,J1 5120 001442 SHOVEL HAND ROUND NOSE 1.6 K
REP KIT AIR DRYER ASSY,UJ KIT,CLUTCH CYLINDER,SLAVE CYLINDER CLUTCH,ASSY ARM WIPER,SPEEDOMETER CABL
chlorhexidine gel,mucopain,kenacort ointment,chlorhexidine mouthwash,waxed dental floss,mouthwash b
LED HANGING AND LED WALL LIGHT
ATF Dextron II D/ Dextron II
Syrup pronefra 180ml,Syrup Hepamust 200ml,Powder collagen mupirocin and metronidazole combination 5
CLUTCH PLATE,DOOR LOCK LH,DOOR LOCK RH,ELECTRIC PUMP,MAIN BRAKE VALVE,WIPER MOTOR,MENUAL BRAKE VALV
Fluid container,Bar Light Assy,Toggle Switch,Starter Relay 24V 50A,Bulb 12v 21W,Fog Lamp bulb,Solen
RELIEF VALVE,SIDE INDICATOR LH,SIDE INDICATOR RH,WIPER BLADE,SWITCH,STARTER
Herbicide Atrazine 50 percent WP,Coragen Insecticide,Bajra seed,Makchari seed,Dhaincha seed
X2 IXC RH 4DA 49024A FAN BELT A 57,X2 ND MISC 000237760004 RELAY 12V DC,X3 ND IXC LUC 2625 0491 CAR
Suji,Dalia,Flour (Maida),Wheat Atta Whole Meal
VRLA BTY 12V 100AH @ C5
All in One Core i5 13th Gen 16GB 1TB SSD 23.8 Led Win 11 Pro 3 Yrs,Desktop Core i7 13th Gen 16GB RA
Microsoft Win 11 Pro 24H2,Microsoft MS Office 2021,Quick heal Total Security 10 User 3 Yrs,Adobe Pr
Windshield glass ciaz,Front suspension kit ciaz,Glass windshield dzire,Electronic mirror dzire,Susp
Paper Roll,SG Body FLU,10 CM Wide,Tape,Lug Brass
Fixed Basket ball Pole, Board, Ring and Net,Seating Arrangement for Players,Digital electronic Boar
Tunnel Cooler Large Size
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma; Healthcare
LV7 MARUTI 43813-60A00 GASKET,LV7 MARUTI 25121M83002 CASE SHIFTING LEVER,LV7 MARUTI 45623M80001 RET
Catheter Foleys Silicon 2 way Size 22 FG 20 to 30 ml retention balloon,Chlordiazepoxide 5 mg plus C
Eye Oint Acyclovir opth 3 percent wv,Adapalene 0 point 1per Tube of 15gm,Benzoyl Peroxide 2 point 5
ASSY BLADE WIPER,ASSY MASTER CYLINDER,CARTRIDGE LUB OIL FILTER,CYL ASSY HYDR BRAKE MASTER,FUEL FILT
Nycoprotec 04/ Oil Corrosion Preventive Fluid (MIL-C6529C Type III- Air-1504/B)
765 12 SB 102 DRIVEN DISC,BK002781 SMOKE PIPE ASSY,SB20 11 78 SEAL CERAMIC,520 07 006 02 WASHER,SB 
PRESSURE PLATE,ENGINE OIL CAP,SPEEDOMETER CABLE,WIPER BLADE,RELAY 24V,DOOR LOCK ASSY
Cab Tilting Oil
WIPER BLADE ASSY,WIPER ARM ASSY,WIPER WHEEL BOX ASSY,HEAD LIGHT ASSY,HEAD LIGHT BULB,SIDE INDICATOR
Knuckle brg,FRT WHEEL BRG,Vane pump Assy,Air cleaner hose,Steering Gear Box Kepair Kit,Clutch Plate
REPAIR oblic WORK IS REQUIRED FOR MARUTI GYPSY VEH BA NO 02B084662P AT DET EP 1125 FMA JAISALMER,M 
SUPPLY ONLY 02 X TOILET BLOCK (RELOC) WITH CONSTR MTRL & ELEC ITEMS AT 01 X JANGLOT & 01 X BASOLI
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
D IFA RE 21 Human Insulin Analogue Long acting basal Inj 100 IU ml Recombinant DNA origin 300 IU Di
Asphalt Base for Outdoor Basketball Court,8 Layers Cushion KDF Material,Court Line Marking,Flood Li
Multipurpose Endoscope Advance monitor and pre sterile Ambuscope
OIL FILTER,REAR DOOR SHOCKER,KILOMETER HEAD,ALTERNATOR CABLE,DOOR HANDLE,TURBOCHARGER,WATER PUMP,DO
Wall Mounted LED Display Modularized Fire alarm Control Panel,Intelligent Optical Smoke Detector wi
Aceclofenac 100 mg Paracetamol 500 mg Tab,Paracetamol 325 mg plus Diclofenac Sodium 50 mg Tab,Diclo
All in one PC,Visualiser,Projector,PC or Laptop,Point to Zoom Camera,HDMI Cable 15 Mtrs,Switch 4x4 
IC Flash U14 Programmed,IC Flash U15 Programmed,Capacitor CER 1000 UF,Schotky Diode,Micro Circuit D
LV6 MT7 3120-004922 BRG CLUTCH RELEASE 2326570 COO,LV7 STLN VF 14661116914 AR CAM PLATE,LV7 MARUTI 
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
SUPPLY OF PUFF TANK (1000 LTR)
SPSS Base Module Version 30 SPSS Data Preparation plus SPSS Bootstrapping Included,SPSS Advanced St
Banana,Mussambies,Mangoes,Papaya Ripe,Peaches,Musk Melon,Banana,Mussambies,Mangoes,Papaya Ripe,Peac
Brinjal,Cucumber,Lady Finger,Pumkin,Tinda,Bitter Gd,Cabbage,Tomato Ripe,Chillies Green,Coconut Whol
Potato,Onion,Garlic,Bread White,Whitemeal Bread,Potato,Onion,Garlic,Bread White,Whitemeal Bread,Pot
Tittle1,Tittle2,Tittle3,Tittle4,Tittle5,Tittle6,Tittle7,Tittle8,Tittle9
Pressure plate,Clutch plate,Tappet cover gasket,Flange Nut,Pressure plate,Accelerator Cable
Tea CTC 1,Tea CTC 2,Tea CTC 3,Tea CTC 4,Tea CTC 5
Rear View Mirror,Rear Brake Show,Ball Joint adjuster Nut,Clutch Cyl Kit,Pressure plate,Sleeve Cyl A
Backing Badges red,Badge Beret cap oblique pagri,Shouder title metal,Collar Badge Bn alphabet,Beret
Pressure plate,Clutch Plate1,Gear Box Fork,Clutch plate,Planger
Cheese Spread 1,Cheese Spread 2,cheese Slice 1,cheese Slice 2,Cheese Cube
Shirt Terry cotton OG stitched as per the measurement taken for each indl,Trouser Terry cotton OG s
V BELT,LUB OIL FILTER ASSY,FUEL PIPE,BRUSHES CARBON,M SEAL
Ham Fresh 1,Ham Fresh 2,Bacon Fresh 1,Bacon Fresh 2,Chicken Sausage
BONET CATCH CABLE,TAPER ROLLER BRG,ASSY CLUTCH MASTER CYL,CYLINDER HEAD GASKET,HEX NUT,ARMATURE ASS
monitor stand powder coated with ss basket
Angel Wall,Two in One Angel wall,Soap Stand,Corner set,Mirror Set,Waste Pipe,Connecting Pipe,Pillar
Kilometer Cable,Gear Speedometer,Arm Assy Comp Kick Starter,Spark Plug for HH,Relay Assy,AC Filter,
room attendant,housekeeper,washermen,Cook,Gardener,Office Clerk,Steward
LV7 T 815 MAIN BRAKE VALVE,LV7 T 815 HOSE PIPE 8X400,LV7 MG BEARING PILOT,LV7 T 815 HAND PUMP,LV7 T
LV7 TATA PRESSURE PLATE OM,LV7 TATA WATER PUMP,LV7 TATA DUAL BRAKE VALVE,LV7 TMB ASSY SLEEVE CYL,LV
Fixed T Handle,Ratchet Spanner 6 32mm,Flexible Magnetic Stick,Electric Impact Wrench,T Handle Hex K
Advanced Hexacopter Drone,Battery for Advanced Hexacopter Drone,Propeller Set for Advanced Hexacopt
LV7 MARUTI 09482M00551 SPARK PLUG CHAMPION RC and YC,LV7 MARUTI 38860M76M00 RELAY ASSY,LV7 MARUTI 2
LV6/MT14 NIV-01-2016/TYRE TYRE 355/80 R20 141K M/P TYRE
INJ NOVORAPID,TAB ATORVASTATIN 80 MG,TAB ISOSORBIDE DINITRATE HYDRALZINE37 point 5MG,TAB PREGABALIN
plateletpheresis (SDP) kit S5L
CG4+ Cartridge (box of 25 kits),EG7+ Cartridge (box of 25 kits)
RING SEALING,OIL SEAL,OIL SEAL RUBBER,OIL SEAL AND SPRING SET,PACKING
Key Board with Mouse,SMPS,Printer Head EPSON 3216,Bty Cyber Power,Bty 12 V 7 AH,UPS 1 KVA,DVD Write
G1 5315-000060 PINS COTTER SPLIT STEEL 1 MM X 12 MM,G1 5315-000196 PINS COTTER SPLIT STEEL 6.3 MM X
Pencil Cell,9 Volt Battery,Audio Communication Device Set,Rechargeable Battery Charger Envie Rapid 
FACE AND FINGER READER TIME ATTENDANCE MAHCINE WITH PRINTER ALONGWITH AMC OF SOFTWARE AND MACHINE
Glucose EM 360 Sys Pack of 10 x 44 ml,Urea EM 360 Sys Pack of R1 5 x 44 ml and R2 5 x 11 ml,Creatin
HIGH MASKED LIGHT SET OF FIVE FOR THIMAYYA TRG NODE
WATER PUMP,BRAKE HOSE,SPG BRAKE ACUTATOR,HUB OIL SEAL,AUX WATER TANK,FUEL FEED PUMP,BALL BEARING
Dish,Container,S Pona,Dasta,Tumbler,Degchie,Jug SS,Degchi 305MM
RECHARGEABLE FLOOD LIGHT
Fuel filter FJ4A4,Cover Holder,Hose L650mm,Repair Kit,clutch cyl Repair Kit
DRR UHF HAND HELD RADIO SET
GH6-32 Gear Oil GHE 632 (Proprietary Product of Kluber)
Egg Printing Machine
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Metronidazole 400mg Tab,Chlorhexidine solution Potassium Hyderoxide 13.6g chlorixylenol solution 50
5G CU-DU Software Binary,USRP with Antenna-B210,Mobile with Test Sim Card,Desktop Computers,Install
Asus Vivobook s15 O led Laptop
Lignocaine HCL solution 2 persant for IV use 50 ml Inj,Povidone Iodine solution 5 persant bottle of
Natural sand confirming to IS 383 1970 Specifications for coarse and fine aggregates.,Aggregate 5mm
RAGULATOR REPAIR
Steering System Rack and Pinion model of Maruti Gypsy
LInseed Crushed
LV6-MT3 6240-013448 Box Tin Lamp Filament Size 102MM x 83MM,LV7-T-815 DMD-NIV-3100 Baby Filter Assy
X3 MG19-DYNAF-8-47-006-007 ACTUATOR ASSY HEAVY DUTY
FIEDL COIL WITH THERMAL CUT OFF,ARMATURE ASSY,BRUSH CARRIER ASSY,FIELD COIL,ROLLER WITH PIN,VANE PU
WIPER MOTOR ASSY,BUSH SET,POLE SCREW,BRUSH CARRIER ASSY,BRAKE SWITCH RELAY,REGULATOR ENG GEN,PISTON
BMP Track Links,Strela Track Pins,Strela Track links,Drone jammer,Rf Detector for Drone
Dhaniya Powder,Turmeric,Mirch Powder,Black Papper,Cumins
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Shift Cylinder Body,Shift Cylinder Body,Flexible Hose Assy,Selector and Shifter Shaft,Repair Kit Di
Cement OPC 43 Grade packed in HDPE bag each 50 Kg wt conforming to IS 8112-1989 as per store list u
81mm MORTAR INTEGRATED SIMULATOR
BOOSTER DIAPHRAM,LUBRICANTING NIPPLE HEAD CONICAL,CONTROL VALVE KI,RAM KIT,ELECTROMEGNETIC VALVE
Air Filter Element for SSL Engine with Cat Part No 10X471,Air Filter Element for SSL Engine With Ca
LV6MT1 5120000357,LV7TATA 261433750107,LV7TMB 278615999966,LV7TMB 252307150104,LV7TATA 261433750108
Oil seal,Fly wheel ring,Gear lever end,Fuel filter,Knuckle bearing,Speedometer,Stopper cable,Oil fi
COVER ASSY CLUTCH,WHEEL BEARING REAR,COIL ASSY IGNATION,BEARING FRONT,BALL JOINT,HOSE ASSY AIR OUTL
Folding Spine Board,Canopy,Fogging Machine Liquid,Grass Medicine Grass Killer Medicine,Grass Cuttin
10519584 LV6/MT14 2610-001523 TYRE 14.00 X 20 22 PR SCH NON DIRECTION,10519704 LV6/MT14 2610-001524
Emergency lighting and accessories  (PORTABLE EMERGENCY LIGHTING SYSTEM  Tower type  With AC Genset
LV7 MARUTI 78471M79000-5ES BEZEL HANDLE RH,LV7 MARUTI 06111M10004 BALL,LV7 MARUTI 22400M83060 DISC 
Main Board AC DC Adopter
Kit for estimation of Glucose 2 x200 ml Erba Semi Auto,Kit for estimation of urea 5X20 ml Erba Kine
IRON FRAME,WATER MOTOR PUMP1 2 HP,WATER MOTOR PIPE,HEDGE CUTTER,BUSH CUTTER
Disposable syringe plastic sterile 5ml with needle,Disposable syringe plastic sterile 10ml with nee
Kit for estimation of Alkaline Phospate 6x6ml Erba semi Auto,Kit for estimation of Calcium 2x50 ml 
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Rapid Pregnancy strips 50 test kit,Strips Albumin and glucose bottle of 100 strips uristiX,strips k
Kit Estimation of Albumin 5x50ml Erba Semi Auto,kit for estimation of GGT Erba 5 x 6.5ml Semi Auto,
Steel Philips Screw One by Two inch,Brazing Rod Copper,LPG Cartridge,Gas Charging Line Five Zero Ze
Cutting Wheel 4 inch,Grinding Wheel 4 inch,Rubber Coupling,Oil Temperature Gauge,Gate Valve 50 mm,B
Erba H360 Diluent pack of 20 ltr,Erba H360 Elite clean 50ml bott,Erba H360 Control LxNxH,Erba wash 
765 08 SB357 HOSE ASSY,765 08 SB 361 HOSE ASSY,175 01 464 IGB MOUNTING BOLT,NK000938 PINION SELF ST
SOLAR ELECTRIFICATION SET 6KW (RELOCATABLE)
Climbing Rope,Repelling Anchor Rope,Climbing Seat Harness,Full Body Harness,Helmet,Rock Climbing Sh
Resin Tank,Resin Bottles White 500ml,Resin Bottles Transparent 500ml,Resin Tubing,Flow System Senso
Rear Brake Booster NM,Oil Filter,Rear Hub Oil Seal,Air Copmressor Plate,Air Compressor Seal,Oil Fil
Glass Wind Shield,S A of Hose M18NX,Pump Major Service Kit,Hose Engine Inlet,Hose Clip Screw Type,H
Hydraulic Cylinder HM,Speed sensor AGB Alt f 2015600,Ram Hydraulic Ram Assy,Tapper Roller Bearing,B
Luminous flower stand,Luminous butterfly light,DJ Light,Luminous Tree light,Cob light
SPEEDOMETER CABLE,SOLONOID SWITCH,FUEL FILTER CATRIDGE,DOOR LOCK,REGULATOR 24V,STEERING HWEEL,SLEEV
Plastic Toilet Block,Septic Tank 1000ltr,Iron Stand for tank,PVC Pipe,PVC Pipe Socket,Water storage
Portable Equine Walker
King Pin Upper,King Pin Lower,Bearing,Axual Roller Brg,Combination Switch,Sleeve Cyl Assy,Wheel Dis
Nozzle for Fip,Delivery Valve,Element of FIP,Washer for Injector,Nozzle 1829
CYLINDER COMPLETE SET,BRAKE SHOE REAR,BRAKE SHOE FRT,GASKET FUEL SET,HAND BRAKE CABLE,GASKET SET CO
Terrain model1
PLYWOOD 12MM,PLYWOOD 6MM,PAINT BLACK,PAINT GOLDEN BROWN,HEATING HELIMENT ROD,FLEX KWIK
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Coronary Imaging catheter for Intra Vascular Ultrasound 40 MHz compatible,Coronary Orbital Atherect
SEDAN NON AC 4HRS,SEDAN NON AC 8HRS,SEDAN NON AC 12 HRS,SEDAN NON AC EXTRA KMS,SEDAN NON AC EXTRA H
BUS NON DELUXE 32-34 SEATER,BUS NON DELUXE 32-34 SEATER EXTRA KMS,BUS NON DELUXE 32-34 SEATER ONE W
Guide wire for Rotablation Floppy support,High Pressure 2 Port Manifold,Polycarbonate Luer Lock Syr
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Earthing Test Meter,Float Cum Boost Charger,Power Cable 8mm 2 Core,Earthing Cable,Krone Module,Equi
Track Suit,Windcheater,T Shirt,Sleavless,Shoes,Shorts,Soft Towel,Trolley Bag
Almond,Cashew Nut,Raisin,Protein Isolate,Glucose Hyspeed
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Others
LEATHER CLOTH BLACK,LEATHER CLOTH WHITE,PLY WOOD,PLY WOOD 1800X1200MM,DASOOTI YELLOW,DASOOTI OG,CLO
KIT PAD ASSY FRONT,ASSY FUEL INJECTOR,AIR FILTER ELEMENT,ASSY OIL FILTER,CLUTCH ASSY 260 DIA,ALTERN
Potato Fresh , onion
BREAD WHITE , Bread wheatmeal
CHEESE SPREAD,CHEESE CUBE,CHEESE SLICE,SPREAD CHEESE,CHEESE CUBES
Fan 24V,Tube Light,Brake Switch,Fan Switch,Wiper Motor,U Bolt
Bonnet Relay,Junction Relay,LED Light,Fog Light,Fan 24V,Toggle Switch,Parking Solenoid,Air Filter E
Printer Drum,Monitor,UPS 1 KVA,Bty 12V 7 AH,Processor,Mother Board H610,Key Board and Mouse Combo,R
seating stair platform extension 21ft into 30 ft including 6 steps,shed extension 21ft into 32 ft w
Navigation Aids,Cable Tie 6,Cable Tie 8,Cable Tie 10,Cable Tie 12
Spare Battery,Insulation Tape,8mm wire Clip,1mm Nail,AA Size Battery
Hours Meter Time Totalizer,Brake Hose Connecting Trailor,Fuel Pipe Pump to Injector,Hose Pipe,Anabo
Nalidixic Acid 500 mg Tab,Naloxone 400mg Inj,Naproxen 500mg Tab,Nimodipine Inj 0.2 mg to 0.6 mgobil
2920 001912 RELAY SOLONOID SWITCH,432 40 093 1 GASKET,432 40 368 GASKET,54 09 011 UNIVERSAL JOINT,n
Lipo Battery,Distilled Water,Fan Capacitors,5mm Wire Clip,Wire Cutting Blade
MTP Combipack of One Mifepristone 200 mg and four Misoprostol each of 200 mcg Tablet,Multivitamin a
Bearing ball,Ring Sealing Push Rod Top,Gasket Cyl Head LD 84 mm,Fuel Pipe Pump to injector,Washer C
Door Outer handle,Piston Seal Kit sheval clamp for JCB,Piston Seal Kit sheval clamp for tata JD,Sol
Metoclopramide 10 mg Tab,Metoprolol 1 mgobiliqueml 5 ml Inj,Metronidazole 1percent tube of 30gm,Met
Spy Camera,Connector,Cable Clip,Batten Clip,Electrical Insulation Tape
Volleyball,Volleyball Net,Volleyball Net Antenna Strip,Football,Football Goal Net,Football Stocking
BLANKET HOSPITAL BRICK RED,BLANKET HOSPITAL BROWN,TOWEL BATH BLEACHED LARGE 155 X 80 CMS,TOWEL BATH
Disposable Sterile Eye Drape with Pouch
Robin Seed,Cuppress Torlusa Surai,Thuja Combacta,Devdar Seed,Bamboo Seed,Compostable Poly Bag
Drone Charger,Celling Light,Electric Wire 1.5mm,Eletric Wire 2.5mm,Power Cable 1.5mm 2 core,Adaptor
Paroxetin 25 mg Tab,Pioglitazone Hydrochloride 15 mg Tab,Pioglitazone Hydrochloride 30 mg Tab,Polid
Ovabless-Myo Tab,Paroxetine XR 12.5 Tab,Pethedine 50 mg 1 ml Inj,Pheniramine Maleate Inj 22.75 mgob
Red Chilli,Mustard,Turmeric,Tamarind,Black Pepper,Cloves,Cardamom Large,Corrinder,Cumin Seed,Garlic
Modified Cycle,Bearing Light,Bearing Heavy,Wire Insulated,Spring,Pipe Chudi,Pipe Patti,Nut Bolt Was
Air pressure pipe,Sensor,AC gas cylinder,Piston assy,Van pump assy
GI Tee 12 ft,GI Tee 4 ft,GI Tee 2 ft,GI Tee Wall Angle,PVC Gatti,35 by 8 Screw,GI Wire,Gypsum Tile,
Oestriol Cream,Oestrogen Cream Concentration 0.06percent to0.1percent wobiliquew Tube of 15 to 50 g
ASSEMBLY CONDENSER FAN COMP,VALVE ASSEMBLY WATER,AIR FILTER ELEMENT,ASSEMBLY OUTER HANDLE RH,REPAIR
Custom Bid for Services - AMC of Local Area Network
Repair and Overhauling Service - electro hydraulic mechanical tyre buster; faa; Yes; Buyer Premises
Check Off Road Water Dispenser Machine and repair comma replace the UNSV part comma if reqd,Check a
Henry Kissinger on China,Himalayan Blunder,The rise and fall of great powers by paul Kennedy,Indian
Repair/Maint Motor Cycle
FUEL LINE,WATER PUMP REP KIT,SPARK PLUG,CARBURETOR ASSY,COVER,CARBURETOR REP KIT,FUEL PUMP,IGNITION
TAB NAOROXEN 250MG,INJ PHENARAMINE MALEATE 22POINT 75MG PER ML,TAB PREDNISOLONE 5MG,TAB CLOBAZAM 5M
Desktop Computer Terminal,Desktop Computer server,UPS 1 KVA,UPS 5 KVA,Networking components
Belt Vee Endless A 51,Hose Pipe,Pipe Flexible Guage Oil Pressure,Pipe Lub Oil Connecting Filter,Ove
UPS 1KVA
DESKTOP COMPUTER WITH 22 INCH LED DISPLAY
LINE BRAKE RL TR,BRAKE LINE REAR TRAIL,THROTTLE CABLE TYPE 734,FRONT DISC BRAKE TYPE 217,K-ASM PAD 
Refinded Sunflower Oil as per DFS 423
Loperamide 2mg Tab,Loratadine 10 mg Tab,Lorazepam 1 mg Tab,Lorazepam 2mg Tab,Losartan 50mg Amlodipi
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Refined Mustard Oil as per DFS No 425
7 Inch Analog FPV Drone
harpic five hundred ml,lizol two litre,brasso five hundred ml,room freshner two fourty ml,broom sof
Laying of Basketball Court
Cover Assy 353 Dia 1050 Kg,Distt Piece,Seating Block,Clutch Plate,Ball Joint LH
ZMR 250 Analog FPV Drone
ROOF AFZA
LV7 MARUTI 09482M00551,LV7 STLN F 4034200 OPTL P3101540,LV7 TMB 2786 0798 9916,LV7 MARUTI MAJ 99000
BEARING TAPERED ROLLER,PIPE SEAMLESS,PIPE OD,PIPE G,CLAMP
Nozzle Injector,Bush,Hose,Seal,Gasket
POTATO FRESH , ONION FRESH
Filter Air Complete,Injector Nozzle,Fuel Feed Pump,Hours Meter,Eng Packing Kit,Element,IEVR,Connect
CLUTCH CABLE,BRAKE SHOE,ARM BUSH,ADOPTER BOOSTER,BONNET CABLE,OIL FILTER,NOZZLE 1465,STARTER KIT PI
Solenoid Switch,Volt Meter DC,Frequency Meter,AMP Meter,Relay,Electrical Welding Rod,Fevi Quick,Ben
Monthly Basis Cab & Taxi Hiring Services - Sedan; 60KMX08HRS FOR 26 DAYS IN A MONTH TOTAL SERVICE R
Surface Mounted 15W LED, Recess Mounting 42W 2x2 LED, Recess Mounting 28W 4x1 LED, Flat Panel 4x1,
Net Camouflage Shrimp Type (Defence)
Side Hand Rail Plastic Body,PU Bag Asian of 10 Ltr pack,Bituman Tape 4inch wide of 10 Mtr Long,85 x
PU Bag Asian of 10 Ltr Pack,Bituman Tape 4 inch wide 10 Mtr Long,85 x 25 Bituman of 50 Kgs Bag,Sola
Electric Ceiling Fan with BLDC Motor (V3) ISI Marked to IS 374
Uniball pen blue,Uniball pen red,Uniball pen green,Stapler pin 24 by 6 1000 staples 20x50,Stapler p
Combination Plier eight inch,Nipper Plier,Screw Driver Set Taparia,Snake Eye Screw two point five m
Repair and Overhauling Service - Repairing of roots cleaning machine; Repairing of roots cleaning m
RECTIFIER PLATE,REGULATOR 12V,RELAY 24V,RELEAGE BRG,REVERSE LIGHT SWITCH,ROTOR ASSY 12V,SLEEVE CYL 
Universal Filter membrane with membrane filter,Microbion Control Kit,Erba EM 180 Reaction tray,Samp
Macbook Sky Blue,Macbook Blue,Macbook Mid Night,Macbook Silver,Macbook Star Light
Gloves HIMCLOS
Underpant Wollen (Improved Version)
Push Rod,Gasket Set,Fan Belt A42,Engine Mounting Pad,Oil Filter,Air Filter,Fuel Filter,Fuel Pipe 17
MAIN SHAFT,REVERSE LIGHT SWITCH,OIL PUMP ASSY,OIL SEAL,CONTROL VALVE
Cross Member RHS 40 x 80 x 3 point 2mm lower with ISA 50x50x4mm of 1505mm long,Cross Member RHS 40 
Prefabricated structure 8500x6000x2400mm,Pre painted Galvalume corrugated sheet 3600x1050x0 point 5
Hot water boiler of capacity 150 Ltrs,Hot water boiler of capacity 150 Ltrs having average performa
PVC sheathead copper cable 2 point 50 Sqmm single core with multistrand 1100 Volts grade,PVC condui
PUF Insulated 55mm thick water tank 1000 Ltrs with GI flange for connection with nipple and gasket,
OR Living Shelter Relocatable 16 Men Similar to Porta Cabin 16 Men FEMS will be erected with PUF in
Z1/5995-020902, Cable Assy Special Purpose Electrical
Night Vision Binoculars
Supply and installation of outdoor Basketball court
ASSY RADIATOR PIPE WITH HOSE,BRAKE SHOE ASSY REAR,AIR COMPRESSOR REPAIR KIT,CE BUSH,OIL SEAL,ARMATU
Custom Bid for Services - BOQ item No 1 Semi Skilled FGM per shift of 08 hours       3668        Sh
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
Powerful Desert Air Cooler 115 Ltrs Equipped with honeycomb cooling pads optimal Airflow,Borosil Vi
Antacid gel each 5ml containing dried aluminium hydroxide gel IP 250 mg Magnesium hydroxide NF 250m
NEEDLE DARNING TAILOR 47 MM,NEEDLE SEWING HAND NO 1,NEEDLE TAILOR DARNING 65 MM X 1PT4 MM,S COTTON 
FLY WHEEL ASSY,PISTON ASSY,PISTON PIN,PISTON RING SET,SPARK PLUG
GREASE CENTOPLEX EP-02
ASSY PULL CABLE,SWITCH ASSY STOP LAMP,OIL SEAL,KIT FOR ALTERNATOR 12 VOLTS 65 AMPS,MOTOR ASSY WIPER
ARMATURE ASSY,CLUTCH RELEASE BRG,CLUTCH MASTER CYLINDER,CARTRIDGE FUEL WATER SEPARATOR,FIELD COIL A
Head Torch,3 mm GI Binding Wire,Hexa Blade,Table Glass 12mm,Golden Katar Signallers Acrylic letters
Hand Set cord,RJ 11 Connector,Roset Box,Long nose plier,Digital Multi Meter,Nylon tool bag,Clamp Me
VALVE EMERGENCY AIR PRESSURE,CLAMP,PIN COTTER SPLIT,PIN COTTER SPLIT STEEL,BOURDEN TUBE PRESSURE GA
Tent Frame 40 x 30 Ft,Pro Inner Lower Male,Mirror,Pro Inner Upper Male,Cloth for Camo Net
Tie Rod End,AC Belt,Spring Brake Chamber Front,Spring Brake Chamber Rear,Spider Bearing New Model,V
Wall Clock Battery,Paper Pin,Cello Tape 2,Dusting Cloth Yellow,Good Knight Machine,Phynyl Tiger Bra
All in One PC (V2) (Q2)
Inj Lignocaine HCl 2 prcnt without Adrenalin,inj Lignocaine HCl 2 prcnt with Adrenaline 30 ml Inj,D
BCC 950 Conf Camera,HD super delux HDMI cable 20 mtr,Power Conf S500 Speakerphone,Monitor 27 inch,K
OLOPATODINE 0.1 per BOTT OF 5 ML EobiliqueD,ONDANSETRON 4 MG TAB,PANTOPRAZOLE 40 MG plus DOMPERIDON
BEHIND THE EAR BTE PROGRAMMABLE DIGITAL HEARING AID
hand held gps (Q2) ( PAC Only )
Meat Masala 100 gram,Paneer Masala 100 gram,Cumin 200 gm,Red Chilli Powder,Chat Masala Size 100 gra
White File Cover,Pencil,Sketch Pen,Eraser Non Dust,Sharpner,Box File PTO Folder,Register 200 Pages,
EARTH MOVER VEHICLE JCB
Biosafety Level -2 Lab (Phase-I)
OIL FILTER ASSY TATA,SLEAVE CYL ASSY TATA,CLUTCH CYL ASSY TATA,CABIN LIFTING KIT ALS,FLASHER UNIT 2
BLADE HACK SAW HAND FLEXIBLE FINE NOMINA,BLD HACK SAW FLXB MEDIUM NOML 300MM,NAILS STEEL LATH CUT 1
Clutch Fork rod,Clutch Plate,Brush carrier plate,Hydraulic Pipe,Self Starter,Brake Booster kit,Comm
LV7 MARUTI 36620M830M0 HARNESS ASSY WIRING NO.2,LV7 MARUTI 37740M66010 SWITCH ASSY STOP LAMP,LV7 MA
SILICON OIL INJECTION KIT 1000 CENTISTOKES 10 ML
Kit Master Cyl,Sleeve Cyl Rep Kit,Head Lamp,Brush Set,Major Kit Clutch Master Cyl,Pull Cable Accele
Diazepam 10 mg ampoule of 2 ml injection,Silver sulphadiazine 1 percent cream w oblique v jar of 25
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Banana,Mango,Papaya,Mussambies,Pineapple
WHEEL CYL ASSY 26.99 DIA,ASSY LATCH FRONT DVR RH,ASSY BALL JOINT UPPER WISHBON,LOWER BALL JOINT ASS
Custom Bid for Services - As per BOQ item No 1 Outsourcing services for Semi Skilled Electrician 05
FOG LIGHT BULB 24V,FOG LIGHT BULB 12 V,BULB 12V 5W,TAIL LIGHT BULB,INDICATOR BULB,INDICATOR GLASS T
Deaeration Tank,2.5 Ton,RAM Assy Kit, 2.5 Ton,Visco Fan, Safari,Turbo Charger, Safari,Air Dryer, AL
Charts of Radio Net,Putty for flotation Trg of CV,Display Musketry charts,Equipment Charecteristics
Hub Bearing Outer,Bty Cut Off Switch,KM Cable,Fan Belt,Feed Pump,Hose Pipe Air,U Bolt,Water Pump,Fr
Oil Filter,Fuel Filter,Slave Cyl Assy,Clutch Cyl Assy,Fuel Solenoid,Spider Bearing,Hub Seal Front,K
Shock absorber Front,Shock absorber Rear,Ignition Coil,Spark Plug,Wiper Motor,Hand Brake Cable,Fron
INJ PCM 1gm,LOTION LACTO CALAMINE,LOTION KETOCONAZOLE,TAB ACYCLOVIR 400 mg,TAB ACYCLOVIR 500 mg,CRE
Clutch Plate,Pressure Plate,Fuel Filter,Oil Filter,Spider Bearing,Air Filter,Eng Mounting Pad,Fan B
Slave Cyl Assy,Slave Cyl Repair Kit,Clutch Cyl Assy,Spider Bearing,Hub Seal Front,Accelerator Cable
Eng Mount Front,Zest Wiper Blade Dvr,Front Wiper Arm Assy Dvr,Zest Wiper Blade Co Dvr,Assy Rear Wip
DRONE
LV2/ICVS 4810-000432(765-22-SB217) VALVE BOX
CUT MODEL OF MULTIMODE HAND GRENADE,CUT MODEL OF GRENADE HAND NO 80 SMOKE WP WITH DETNATOR NO 75,CU
Supply and installation of Genr Set 30 KVA FOR MENCHUKA,Supply and installation of Genr Set 30 KVA 
Drone
G2 9530 000081 LEADED BRASS ROD ROUND 20 0 MM,H9 5330 005411 JOINTING SHEET 0 8 MM THICK 1 6 MM,X3 
Haldi Powder,Mirchi Powder,Dhania Powder,Custard Powder,Small Elachi,Kali Mirchi,Long,Auijbain,Tej 
LED Light for Garden
76571480 K9BMPNBC GASKETDRNO76571480,77078SB141 LV2RCV ELECTROPHENUMATICVALVEEK48,ADU2S1 LV2RCV AUT
675713075330395783 K9BMPNBC GASKET,765711462 K9BMPNBC GASKET,67571CB2104240000069 K9BMPNBCNBC FILTE
Soluble Coffee Powder (Refill Packs) (V2) (Defence)
Goods Transport Service – Per Trip based  Service - Various Types of Goods; Containerized Truck; 
cctv camera,Tv 55 inch qled smart android,accessories,cable,amplifier,software and installation cha
20 Amp Fuse,15 Amp Fuse,10 Amp Fuse,5 Amp Fuse,Oil filter spanner strap type small,61-I-61-JCB-334-
X3 NK000231 AIR FILTER,MT6 MT1 LI3076 FIBER SHEET 1 32IN THICK OR MTR DIA,X3 NK00074 ANABOND TUBE,X
Power Generator - DG Set (up to 900 KVA)
Counter UAS (Anti Drone Gun)
Genr Set
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Others,Manpower Outsourcing Se
GEAR LEVER KIT,FUEL PUMP ASSY,AIR PRESSURE PIPE,AIR CLEANER HOSE,CLUTCH BOOSTER,EQUILISER KIT,SPARK
MEDICAL AND VETERINARY CAMP
Simulator Receiver,Cotton Tape,PVC Saddle 3 oblique 4 inch,PVC Saddle 1 inch,PVC Getty 35x8
File Cover White,V7 Blue Pen,Permanent Marker,Temp Marker Blue,Paper FS Size,Paper A4 Size,Drawing 
LV1/R72 346.00 SB OIL PRIMING PUMP MZN-2 W/ELE MOTOR MN1-2S
ALL SEASON GREASE OR GREASE CONFIRMING TO NLGI NO 2
U JOINT GREASE
Containerised Tubular Shooting Range (CTSR) 40 Feet
Supply and installation open air gym
Oil Alpha SYN EP 320
Egg Fresh,Poultry Alive,Potato,Onion,Beans,Brinjal,Lady Finger,Cucumber,Cabbage,Tomato,Corriander,G
Odonil Air Freshner,Phenyle Black,Phenyle White,Pocha Cloth,Room Freshner Gel Pocket,Scurbber Stain
B1 922200000100 IMAGE INTENSIFIER TUBE
IT TRAINING FOR IT LEG OF TICC
Custom Bid for Services - COMPREHENSIVE MAINTENANCE OF FIRE ALARM CUM GAS SUPRESSION SYSTEM FOR OLD
Battle Field Artillery Recon Drone
ASSY MASTER CYLINDER,CLUTCH SLEEVE CYL,ASSY SLEEVE CYL,SPRING BRAKE CHAMBER,SPEEDOMETER CABLE,HOSE 
Black Tea as per IS 3633 (Q4)
FULL PLATES,QUARTER PLATES,BOWLS,SPOON HEAVY,BIG BOWL,PLATES,BOWLS,SPOON NORMAL,BEER MUGS,WHISKEY G
Room Freshener Spray,Colin 200 ml,Broom Phool Jharu,Lizole 500 ml,Detol Liquid,Poucha with Handle,D
Knee Bend Pad,Wrist Bend Pad,Hand Locked strip,Finger Strips,Chinup Bend,Drill Marker Flags
ANTI CUTTING SECURITY FENCE
Fd water Supply Scheme (RO Purification Plant)
Manpower Outsourcing Services - Minimum wage - Unskilled; 8TH PASSED; Admin,Manpower Outsourcing Se
Coriander Powder,Red Chili Powder,Turmeric Powder,Cumin Whole,Coardamom,Black Peper,Tamarind,Clove 
Alcohol Absolute Pure Ethanol,Diamond glass marker pencil,SODIUM META BISULPHATE AR,Perl s Stain So
Large Cardamom (Badi Elaichi) as per IS 13446,Small Cardamom as per IS 1907,Black Pepper,Bay Leaf,S
ALS GEAR BOX REPAIR,ALS SELF STARTER REPAIR,ALS ALTERNATOR REPAIR,ALS FUEL PIPE REPAIR,ALS AIR PIPE
Specification and Superstructure elements of Fd Security Fence,Concertina coil mild steel and barbe
LV7 T 815 CLUTCH PLATE,LV7 T 815 WATER PROOF STARTER,LV7 T 815 EQUALIZER ASSY,LV7 T 815 ELECTRO MAG
Generator Set 3.5 KVA,Generator Set 5 and 6 KVA,Generator Set 7.5 KVA,Generator Set 15 KVA,Generato
FUEL FILTER PRIMARY,BLADE ASSY WIPER,WIPER BLADE FRONT 600 DRIVER MS BCS,BRAKE FLUID CONTAINER,GAUG
ADSP-2185NBST 320 U5,IC SF DGTL CKT AD9954 YSV U9,IC V REG LT 1963 AEST 3.3V,CRYSTAL TCXO 30.72 Y2,
OIL FILTER,ELEMENT KIT FUEL FILTER,PARTICLE FILTER FUEL HVAC,AIR FILTER,WEATHER STRIP FRT DOOR INNE
Provision for One Speed & Ice Climbing Wall for Trg Purpose
A4 Paper JK Copier,FS Paper JK Copier,A3 Paper JK Copier,Pilot Pen Ink Gel V5 Blue,Pilot Pen Ink Ge
Computer Training Lab
Labour Charge for servicing and replacement and fixing of unserviceable filter,Engine oil 15W40,Die
Detacting fault in unserviceable solar power inverter system by authorised manufacturer of make ABB
Dynamic Microphone,Lithium Ion Battery,Molex Connector 8 Pin with Wire,HST Adhe Jacket Size 28 MM,S
CHAIN AND SPROCKET KIT,CENTRE STAND SPRG POST,BRAKE SHOE ASSY,FOOT REST ASSY,CLUTCH PUSH PAD,BALL B
Oil Pump Assy,Crank Assy,Rubber Seal,Hose Pipe,Brake Reservoir,Gasket
Expense book register 400 pages,OPD Registration Book Register 400 pages,Treatment Book Register 40
Silastic sheet 1X1X0 point 005inch,Hemostatic Gelatin Sponge Gelfoam oblique Sponge Stan,Shah Venti
Cement OPC 43 Grade packed in HDPE bag each 50 Kg wt conforming to IS 8112-1989 Make-Birla Gold,Amb
Battery Secondary Lead Acid MT Type (Defence),Stationary Valve Regulated Lead Acid Batteries (V2) a
UPS Offline 1KVA,BTY 12 V 7AH,DVD Writer Slim Type,Motherboard,Processor,RAM,Keyboard,Keyboard and 
Clipping Blade,Clipping Head,Clipping Shaft,Router Armateur,Carbon Plate,Chutkinut Head,L Nut,Chuck
SPO2 PROBE 3 MTR,BP CUFF DIGITAL,BTY 14.8 V 2200 MAH,BTY 12 V 3000 MAH,BULL NOSE OXYGEN CYLINDER,BT
thinner,Paint Rfu Black,Paint Rfu White,Paint Rfu Yellow,Paint Rfu Blue,M Seal
W 10 3510 NIV WASHING MACHINE 25 TO 30 KG,W 10 6675 000011 COMPASS DRAWING PIVOT PENCIL BOW DOUBLE,
LV7 MARUTI 09305M13002 BUSH SPRG SHACKLE,LV7 MARUTI 11342M75M00 SEAL CRANK SHAFT REAR OIL,LV7 MARUT
SOLENOID SWITCH 24V,SPIDER BRG,STEERING GEAR BOX OIL SEAL,WATER PUMP,WHEEL CYL ASSY TATA OLD MODEL,
AUXILIARY GEAR BOX,INJECTOR ASSY,PTO PUMP GASKET,SEALANT LIQUID GASKET,BUSH KING PIN
FET DU 2820 of RS Stars V MK II,MRF 174 of RS Stars V MK II,IC 7343 of RS Stars V MK II,BMC 1533 of
High End Desktop Computer (Q2)
PIPE HIGH PRESSURE WITH END CONNECTION,VOLT METER,OIL FILTER,FUEL PIPE PUMP TO INJECTOR L H,COCK FU
Distance End Piece,Set Screw,Rear Clamp Plate,Bearing,Sprial Beve oblique Pinion Reverse,Oil Seal R
CABIN LIFTING PUMP,RAM ASSY,THRUST WASHER,STARTER RELAY 24 V,RING BRG RETAINER,S A OF RELAY VALVE
CLUTCH SLAVE CYLINDER,FIELD COIL ASSY,SOLENOID SWITCH,JOINT ASSY UNIVERSAL,WABCO CLUTCH BOOSTER ALT
iPhone 16 pro
Deltamethrin Liq 1.25 percent EC,Inj Adrenaline Tartrate 1 ml,Copper sulphate,Inj Metoclopramide HC
Alternator Assy 15 KVA AC single Phase 230V
Flex for displaying of Welfare scheme for ESM,Banned Apps Flex,URC Timing flex,URC Name display fle
Pad Disc Assy,Pump Steering ZE,Throttle Body Assy,Shock Absorber Assy Frt,Cable Throttle,Regulator 
Banner 6 x 4 feet,Winner Trophy,Runner Up Trophey,Best Archery Player Award,Archery Medal with ribb
Synthetic Layer All Weather Synthetic Surface 11 Layers,Basketball Court Accessories,Basketball,Cha
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Cover Assy 353 Dia 1050 Kg,Clutch Plate,Ball Joint Assy LH,Hose Assy,Hose Assy,Locking Ring,Selecto
Repair and Servicing of Turbo Charger of Scorpio Veh BA No 11B 707826P,Repair of Water Pump of Scor
RLS SENSOR,WIND SCREEN GLASS FRT,SEAL FLIP WIND SHIELD,GLASS FRT DR WINDOW LH,GLASS FRT DR WINDOW R
ASSY CLUTCH MASTER CYLINDER,HOSE NONMETALLIC,SLAVE CYLINDER,MASTER CYL ASSY WITH CONTAINER,REGULATO
CYL HEAD GASKET,INJECTOR,KNUCKLE BRG,PILOT BRG,PRESSURE PLATE,REAR BRK SHOE,RELAY 12V,RELEASE BRG
Industrial Desert Cooler Heavy Duty
ARMATURE ASSY NEW MODEL,CYL HEAD GASKET OLD MODEL,FIELD COIL 24V NEW MODEL,SYS PROTECTION VALVE ASS
AIR COMP TOP REP KIT OLD MODEL,AIR DRYER KIT OLD MODEL,BRAKE BOOSTER REP KIT OLD MODEL,BRAKE LIGHT 
SPARK PLUG,SPIDER BRG,TAIL BOARD LOCK ASSY,TEMP SENDING UNIT,WHEEL BRG,WHEEL CYL LH,WHEEL CYL RH,WI
smart map 8x7ft
Seal Set Telescopic Cylinder
INPUT SHAFT COVER,STEERING SEAL KIT,CRANK SHAFT SEAL,STEERING PIPE,PILOT BEARING,NOZZLE,BEARING SET
CYLINDER LINER,PISTON ASSY,PISTON RING SET,GASKET CYL HEAD,CYL HEAD ASSY,CR BEARING,NOZZLE,FUEL PUM
Z7/ISRAEL-9329-2000-20, FOV Assembly
Glycerin trinitrate CR 2.6 mg Tab NTG,Isosorbide Dinitrate 20 mg and Hydralazine Hydrochloride 37.5
OPEN CHILLER
Z1-MISC-2056-92146-00 PCB LED Pannel Assy,Z1-MISC-2056-92171-00 Main Switch,Z1-MISC-4017-80109-02 C
Bulb Instrument for JCB with Cart Part No 61161ESCOU309001,Ignition Switch for JCB with Cart Part N
Arm Cylinder Seal Kit for SSL Chesis with Cart Part No 10X321,Loader Lift Cylinder Pipe Rod End LH 
PT UNIFORM S/LARGE
BEARING 6207/2Z/C3,COUPLING RUBBER ELEMENT,HEATER PLUG FREE GLOW (1 SET= 4 NOS)
PT UNIFORM S/MED
Leader Flex Size 22G,Feeding Tube 6 FR,10ml sterile hypodermic syringe for single use with needle,1
Racket Electric,Fly Cather Double rod,Beans Coffee Machine,Plastic Tirpalium,DDT Spray Machine
2786-1499-9903,B1T04701,2754-54209904,2651-2910-0148,6210-000334,2786-0911-9903,2786-0999-9951,2198
Tea CTC,Tea CTC 1,Tea CTC 2,Tea CTC 3,Tea CTC 4
Practice Drone Frame,Motor for Practice drone,Flight Controller ESC AIO board for Practice drone,Ra
Red Chilly Pdr 5 Kg,Red Chilly Whole,Dhania Pdr 5 Kg,Jeera 500gm,Haldi Pdr 5Kg,Black Pepper 500gm,M
2MP Bullet camera,POE Switch 8 port,NVR 8 channel,NVR 4 channel,Hard disk 4 TB,OFC Cable Cat 6 01 K
Tea thermos 10 ltr,PAPER PIN,Binder clip,u clip,stick pad
Console Table,Split AC 1 and Half Ton,AC Insulation Tube,AC Brackets,Conference Table with Chair
55 Inch LED TV,Double Door Fridge 400 Ltr,Wall Mounting Stand,Fridge Stand,Sofa Set Three Seater
VALVE SEAL STEM,ENGINE MOUNTING PAD FRUNT,MASTER CYL,SLEAVE CYL,HOSE DEMISTER LINE TO BRT
CONTROL VALVE,DOOR CATCH,CENTRE BELT,CLUTCH CYLINDER ASSY,RECTIFIRE PLATE 24V,CLUTCH RELEASE BEARIN
Custom Bid for Services - Repair and maintenance of Veh 4x herohonda, 1 x maruti seift D zire, 3 x 
Bread White,Wheatmeal Bread,Ice (mm)
CLUTCH PLATE,SELF STARTER HOUSING,DOOR OUTER HANDLE,CHAIN SPROCKET RE,CHAIN SPROCKET HH,DOOR CATCH 
GENERATOR CRANK SHAFT CUTTING, SURFACING & POLISHING
Civil Hired Tralier Truck 20 Ton,Civil Hired Tralier Truck 30 Ton,Civil Hired Tralier Truck 40 Ton,
Bus Hiring Service - Short Term - Outstation; 40-42; Non Deluxe (NDX); 250
KNUCLE BEARING,SPIDER BEARING,SHOCK ABSORBER,CABIN LIFTING PUMP,BENDIX DRIVE,FIELD COIL,TAIL LIGHT 
Sabout Dhaniya,Chola Kabuli Chana,Semiya,Garlic,Kali Mirchi,Turmeric,Imli,Mathi 1 Kg,Groundnut Dana
All Wheel Hub greasing,All Transmission oil change,Rear both side brake wheel cylinder repair and b
Supply of Toilet FFL (4 Men)
BTY 12 V7AH,BTY 12 V5AH,IMAGE UNIT SAMSUNG,TEFLONE,PICK UP ROLLER,CIMOS BTY,DRUM UNIT B21,SMPS,BROT
BROTHER IMAGE UNIT 4 SET,L 310 HEAD ESPON,PCI EXPRESS LAN CARD,H DMI GRAPHIC CARD,BTY 12 V7AH,TEFLO
Generator Shed
Covered Shed
BTY 12 V7AH,BTY 12 V5AH,IMAGE UNIT SAMSUNG,TEFLONE,PICK UP ROLLER,SMPS,BROTHER IMAGE UNIT 4 SET,PRE
Ballistic Shiled NIJ Level IV
Ballistic Shield NIJ Level IV
anti seize lubricants
MOLYGRAPH SILLCONE GREASE
Starter Switch,Break Piston Seal,Light Headlamp,Cable Battery Negative,Shim 0 point 5mm,Hose 10 BSP
Envelop 9 Inch x 4 Inch,Yellow Dusting Cloth,Board Marker Black,Board Marker Blue,Fevi Stick 25 Gms
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7,MTITEMS 8,MTITEMS 9
Operation and  Maintenance Services of Power Generator(DG-Set) - Package 1 - O&M Service with opera
Repair and Overhauling Service - REPAIR AND OVERHAULING OF GENERATOR; REPAIR AND OVERHAULING OF GEN
VALVE EMERGENCY AIR PRESSURE,RELAY VLAVE,SIREN,POLE SCREW,HOSE
ICE MM
TWELVE PIN SOCKET,MINUS PLATE,REGULATOR ENGINE GENERATOR,HOSE THIRTY SIX OBLIQUE FOUTRY SIX,HOSE JS
MASTER CYLINDER ASSY,PROPELLER SHAFT,UNIVERSAL JOINT,BALL STUD,ABI DOOR GAS STRUTS,BELT 8 PK,LIFT P
GASKET CYL HEAD,COVER ASSY CLUTCH,CLUTCH RELEASE BEARING,OIL PUMP ASSY MPFI,CLUTCH MASTER CYLINDER,
BARBER FACE CLEANING HAIR BRUSH WITH NYLON HAIRS,HAIR CUTTING SHEET NYLON,SCISSOR STEEL,WHITE TOWEL
Repair of Door Guard of M and M Scorpio,Repair and Fitment of Front Wind Shield Assy of Tata Safari
Paracetamol,Combiflam,Levocetrizine,Avil,Chymoral Forte,Cipzox,Chest N Cold,Pantoprazole,Promethazi
Bookshelves,Hindi Books Related to National Leaders,English Books Related to National Leaders,Comic
Sound Box,Amplifier,Mike Set,Utensil Set,Kadahi Big Set,Full Plate,Bowls,Spoon,Quarter Plate,Tea Cu
FILTER ASSEMBLY FUEL,PISTON CUP SET,PAD,STEERING PINION BEARING,CABLE ASSY SPEEDOMETER,FRONT WHEEL 
Development of Four Prototypes of First Person View (FPV) Drone for Surveillance
Development of Four Prototypes of Kamikaze First Person View (FPV)
Flameproof Air Split Type Air Conditioner Suitable for 2 Ton,installation of flameproof,Supply and 
Roasted Pista Giri
MOB FD REPAIR BAY
9x19MM Machine Pistol
Refined Sunflower Oil as per DFS No 423
Refined Mustard Oil as per DFS No 425
Custom Bid for Services - undefined
Flywheel Skimming,AC Repair 1,Door Denting and Painting,Radiator Repaired,AC Repair 2,AC Repaired a
injection Tribivet,Injection Belamyle,Ointment Himax,liquid savlon,bolus metronidazole furazolidone
Amitriptyline 10mg,Brivaracetam 50mg Tab,Pramipexole 0 point 25mg Tab,Rizatriptan 5 mg Tab,Cinnariz
STARTER KIT,BLACK OUT CHANGE OVER SWITCH,BOLT FOR BRACKET,ISOLATOR SWITCH,SPIDER BEARING,ALTERNATOR
Lifebuoy Hand Cleaner Soap,Colene 500ml for Glass and Multi surface cleaner,Odonil Bathroom Freshen
LV7 TMB 2576-2410-0101 ASSY RUBBER SUPPORT FRONT,LV7 TMB 2576-8110-0114 REAR VIEW MIRROR,LV7 TMB 25
additional accesories for OES
Computer paper A4,HP 88A Cartridge,110A Cartridge,Canon NPG 59 Toner Black Genuine,SHARP Toner Cart
Y3 R72 5970-000576 INSULATION TAPE ELEC COTON SELF ADHESIVE,H1 B 3439-000447 FLUX SOLDERING ZINC CH
LV7 TMB 2101-5450-9905 MAIN LINE SWITCH,LV7 TMB 2574-4235-0112 WHEEL CYLINDER 44.45 MM DIA BI,LV7 T
GEAR LEVER KIT,DAMPER ASSY STRG,HORN ASSY 12V,OIL FILTER,ARMATURE ASSY,RADIATOR ASSY,BEARING,CLUTCH
Elect PVC,Cord Power,Flexible Tinned,Portable Nickel,C Alkaline,Power B,L Sulpher,B Lisoz,Port NI C
Actidiff 1 litre,Isoflux 20 litre,Ms card Ms 4s vet,CBC 3D Hematology control,Clot filter pack of 2
SEAL KIT GEAR BOX,RAM SERVICE KIT,REGULATOR ASSY LH,SPARK PLUG,POWER WINDOW SWITCH,FUEL FILTER,SHOC
FXO FXS 4 Ethernet,LAN Extender O,Optical To Ethernet Convertor,MDF Box 100 Lines,DP Box 10 Pair,DP
Main Clutch Seal,Main Clutch Disc,Main Clutch Plate,Inertia Brake Assy,Oil Filter,Fuel Filter,Hydra
Inj Somatotropin Recombinant Growth Hormone 4IU slace ml Each one Vial for insulin syringe and dist
Clutch Plate Assy,Pressure Plate,Brg Clutch Release,Joint Assy Universal,Road spring Assy front,Roa
COTTER PIN SPRING 17204506,HOSE CONNECTION CQA HV 531014,HOSE CONNECTION CQA HV 531020,HOSE CONNECT
SUGAR,SUGAR 1,SUGAR 2,SUGAR 3,SUGAR 4,SUGAR 5,SUGAR 6
SUGAR,SUGAR 1,SUGAR 2,SUGAR 3,SUGAR 4,SUGAR 5,SUGAR 6
Non Lethal 5.56MM Coloured Marking Carts for Tavor and M4A1 Aslt Rif
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Rectifier Plate,Brush Holder,Fuel Motor,Hub Axle Seal Front,Knuckle Bush,Knuckle Bearing,Universal 
Snow white colour European WC with S or P Trap concealed of size 650x405x770mm,Snow white colour wa
TMT Bar 8mm dia,TMT Bar 10mm dia,TMT Bar 16mm dia,Binding Wire,ISMB 150 Medium grade steel of lengt
The basic construction of Internal Ft Tr Covered will be prefab structure made of 49 point 5x49 poi
LED Security light 60 watt and Solar LED 60 watt street light HDGI Octagonal Tubular pipe of 8 mtr 
Prefabricated structure of size 9600 X 5000 x 2400 mm,Prepainted galvalume sheet 3200x1050x0 Point 
Prefabricated structure of size 7200 X 5000 x 2400 mm,Prepainted galvalume sheet 3200x1050x0 point 
Prefabricated Shelter Structure for FFL of size 2 point 4m x 1 point 28m,Non Skid Ceramic Tiles of 
Cross Member RHS 40 x 80 x 3 point 2mm lower with ISA 50x50x4mm of 1505mm long,Cross Member RHS 40 
Provision of the fencing consists of high security 358 welded mesh panels steel tubular posts Y arm
Side Indicator Assy,Front Indicator Assy,Arm Rest Handle Assy,Gear lever dust cover,Hood Light Assy
LINE SHOE ASSY,VANE PUMP,DISTRIBUTOR HEAD,COMBI SWITCH MS HARNESS,ASSY PARKING BRAKE,HAND BRAKE CAB
AC Compressor,Gasket exhaust manifold,Weather strip door,Disc clutch,Clutch R Bearing,Radiator fan 
Bosch GBL 650 Professional Blower,Stanley Glue Gun 40W,Agaro 62 in 1 mini Precision Screw driver se
Electrodes Welding Steel Mild,Steel Angles,Joint Thick Iron Sheet Covered,Nails Steel Wire Round,Na
Custom Bid for Services - CONSULTANCY SERVICES FOR SOIL INVESTIGATION AND PREPARATION OF ESTIMATE S
Chili Powder,Haldi,Jeera,Dhania,Imli ka Gudha,Ginger Dry,Methi Seeds,Sonf
Prefabricated Shelter Structure for FFL of size 2 point 4m x 1 point 28m as per drawing,Non Skid Ce
PUF insulated prefab modular shelter of size 12 point 6x7 point 72x2 point 5m out to out dimension 
Provn of Porta Cabin Re locatable modular shelter with Rockwool PUF Panel of size 6100 mm x 3050 mm
Eng Mounting Pad Bolt,Engine Mtg Paad,Fuel Feed Pump,Insulation Tape electrical PVC adhesive,Oil Se
Brake Shoe,Brake Pad Assy,Rod Spring Shackle Bush,Cable Assy Clutch Control Speedometer,Bulb Speedo
SHELL OMALA S4GX 220
Fish Fresh 1,Fish Fresh 2,Fish Fresh 3,Fish Fresh 4,Fish Fresh 5
Foldable Quad Night Surveillance Training Drone,Battery for Foldable Quad Night Surveillance Traini
V Belt,S A Fuel Hose,Assy Head Lamp,Main Shaft Gear Box,Mud Shaft Gear Box,Armature Assy,Assy Arm W
Gear box overhauling and repair work,Nipple greasing work,Pressure plate and fly wheel skiming with
Modification and Roof Repair work at unit Mandir
Superstructure of Gun Repair Shed of size 20.00 M x 10.00 M x 5.00 M height for Gun Repair Shed und
Supply of Security fence as per specification in RFP,Supply of LAIP 4400MM long for security fence 
Custom Bid for Services - Repair Replacement of GI pipe and gate valve for water supply to football
Pickup Roller Set,Pickup Shaft,Clutch Gear,UPS Bty 12 V 7.2 AH,Pickup Spring Small and Big
Paper A4,Paper A5,Pen Blue,File cover printed,Register,Glossy Paper,White file cover,Bond Paper 100
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
M2 BOF 6127308 ROD,M2 5930 003689 SWITCH BOX TERMINAL FIRE CONTROL EEUM,M2 5940 002238 TERMINAL BOX
O/5310-213982 (M46 26-257) NUT SLEEVE,O/3040-021652 (M46 26-247) SHAFT SHOULDERED,O/M46 26-134 WASH
M2 BOF 6137590 SPRING HAND OPERATING GEAR ARC PAWL PLUNGER FOR LOADER AUTOMATIC,M2 BOF 6105122 PIN 
M2 IAN 156SA PLUNGER FIRING ROD FOR GEAR FIRING,M2 BOF 6111443 BUSH VALVE SPINDLE GEAR AXLE RAISING
Supply of Store Shelter as per specification in RFP,Supply of Electrical items for Store Shelter as
Supply of Store Shelter as per specification in RFP,Supply of Electrical items for Store Shelter as
Supply of OR Living shelter 6 Men Kit Based FEMS as per specification in RFP,Supply of Electrical i
MT ITEM 1,MT ITEM 2,MT ITEM 3,MT ITEM 4,MT ITEM 5
WHEEL CYL REPAIR KIT,MAJOR KIT SLAVE CYL,STARTING RELAY,AIR CLEANER,CLUTCH SLAVE CYLINDER,AIR PRESS
Beans,Brinjals,Lady Finger,Bitter Gourd,Marrow,Bottle Gourd,Tori Jhinga,Cucumber,Tomato Ripe,Corian
Center Bolt,Cover Assy,Speed Sensor AGB ALT F 2015600,Bearing 34x72x16,bearing DR Bevel Pinion,Oil 
WHEEL BEARING FRONT FOR MARUTI GYPSY,WHEEL BEARING REAR FOR MARUTI GYPSY,CLUTCH PLATE FOR MARUTI GY
MICRO CCT VCO 610-1120 MHZ 5-19V 10 DBM,MICRO CCT LINEAR TYPE AD 847 AR,TRANSISTOR 2N2222A1,FRACTIO
Anti Corrosion Paste
DXH 500 Diluent, 10 ltr,DXH 500,LYSE, 0.5 ltr,DXH500 Cleaner 0.5 ltr,FP,DXH 500 Control 6x2.3 ml,FP
All in One PC (V2) (Q2)
MASTER CYLINDER,GASKET OIL SEAL HOUSING,BRUSH SET,COMPRESSOR ASSY,CABLE COMPLETE,SPRING KICK,GRIP,R
Hiring of Consultancy Services - Percentage based - Technology Consultants; Engineering Design; Yes
Dummy Inflatable Gun 105/ 37 mm LFG with Hot Air Blower
FIELD SECURITY LIGHT
G2 3439 000017 ELECTRIC WELDING ROD,G2 9515 000018 STEEL SHEET CARBON,G2 9520 000002 STEEL ANGLE 25
Camera,NVR,TV,HDD,PC,UTP,Pole,Rack,UPS,Switch,Cable,OTE,OTDR,Splicing Machine,OFC,Installation Comm
Excavation and Leveling of Surface,Construction of Plinth for Basketball Court,Complete Constructio
HYD HEAD,SUPPLY PUMP,ROLLER PIN,ROLLER BRG,DRIVE SHAFT,SOLENOID VALVE,TD PISTION,REPAIR KIT,RETURN 
Provn of Perimeter security light,Provn of Cement Bag of OPC 43 Gde,Provn of Sand,Provn of Aggregat
Superstructure for 01 x Dining Hall Modular 26M x 7.5M x 4.75M including as per technical specifica
PCC Footpath
Cook House Dining Hall
Grease OKS 480/ 9480
Rubber Seal Kit for AM-50 Bridge,Decco Putty,Araldite,Armoured Welding Rod,Jointing paste,Jointing 
LV7T-815, 483-512-014-000, TURBO BLOWER - HX 50 W 3850995,LV7T-815, 442-900-355-000, OIL FILTER CAR
Football,Shin Guards,Goal Keeper Gloves,Knee Pads,Goal Post Net,Football Shoes,Football Agility Lad
LV7T-815, 443-612-193-017, BRAKE CYLINDER,LV7T-815, 443-611-010-000, CLUTCH VALVE- 611006002,LV7T-8
REGULATOR ASSY RH,REGULATOR ASSY LH,ARENS CONTROL COMPLETE,SHIFT CYL BODY,SHIFT CYL BODY 2,BALL JOI
SELF STARTER 30KV,SELF STARTER REVERSE TYPE 7.5 KV,FUSE HOLDER WITH ASSY 63A,SET OF PAPER RING,FUSE
Garam Masala,Chicken Masala,Sambar Masala,Paneer Masala,Chana Masala,Rajma Masala,Kitchen King Masa
Red Chillies,Coriender,Turmeric,Imali,Zeera,Back Pepper,Cordem Large,Muster Sead,Cloves,Garlic,Tejp
Office Chair (STI)
COVER OUTER 600X9 REAR,TUBE INNER 600X9 REAR,TUBE INNER REAR,FLAP RUST 600X9
voice translation sys for foreign country students
Albendazole Tab,Alfacalcidol Vit D3 Cap,Allopurinol Tab,Amlodipine Besylate Tab,Amoxycillin plus Cl
TATA STORME 287142100120 KIT PAD ASSEMBLY FRONT,TATA STORME 278901160106 ASSEMBLY INJECTOR,ALS B 13
Intraoral photographic mirror,Y shape cheek retractor,Wing shape cheek retractor
Hand held circular elect saw,Hand saw twenty inch inch heavy duty for wood cutting,Spnr Open thirte
Two 6 KVA UPS with Web Control,Battery Bank for UPS 2 Sets for 60 Min,3 KVA UPS,UPS Digital CPDU Di
320 A7291 333 Y6130 WATER SEPARATOR ASSEMBLY 3DX SUPER CH XXX A,450 00202 DRIVE FLANGE 3DX SUPER CH
320 09661 STARTER MOTOR 12V 3DX SUPER ENG XXXIX F,320 07394 FILTER FUEL 5 MICRON 3DX SUPER ENG XXXV
Bandage Open Wove compressed 2 point 5 cm x 4 metres,Non rebreathing oxygen mask with reservoir bag
Renewal/ Upgradation of English Language Software with Technical support for 3 years
Packing Kit with Gasket for FLT two Ton,Piston Ring Standard Size for FLT two Ton,Star Cuppling rub
MCB four pole sixty three Amp,Mictofiber cloth of size thirteen into thirteen inch,Microfiber duste
459 30298 FORK SELECTOR 3RD 3DX SUPER CH XXI C,335 Y7093 CABLE BATTERY VE 3DX SUPER CH VIII E,332 F
WHEEL NUT,ASSY LOWER BALL JOINT,HOSE ASSY AIR OUTLET,COIL ASSY IGNATION,FIELD COIL,HOSE 722,SUSPENT
Chair,Table,Customised Table and Chair,UPS with Batteris,MFD Document Scanner,Projector,Screen,Wiri
Microsoft Surface,Loftbed,Allfoam Mattress,Standredfan,Solarstreet Controller with in built battery
CABIN LIFTING PUMP,CLUTCH BOOSTER REPAIR KIT,ASSY SLEEVE CYLINDER,SA OF HOSE WATER SEPARATOR FUEL F
Acralic Board,Mixer Grinder,Fire Extinguisher Ball,Desert Cooler,Executive Chair,Washing Machine
Banana,Mango,Muskmelon,Pineapple,Watermelon
Brake Master Cyl,Wiper blade,Air Hose Pipe,Door Balancer,Hose Pipe,Ignation Coil,Clutch Disc,Brush 
ALTERNATOR ASSY TVS,AIR FILTER BOSCH,OIL FILTER 1 LTR,FUEL FILTER SET 500ML,FUEL FILTER CLOTH 1L,FU
Sterile Disposable Drape sheet large size,Disposable Sterile Drape Medium Size 110cm x 160cm,Tube T
CLIMATE CONTROL SYSTEM
Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,Medicine,
Hand wash box,Calling bell with bty,Light sign board,Flex bd with frame,Steel Tank 15 ltr,Table cov
ACCELATOR CABLE,DOOR CATCH INNER LH,DOOR CATCH INNER RH,CLUTCH CABLE,CLUTCH PLATE ASSY,DOOR CATCH O
Bus Hiring Service - Short Term - Outstation; 40-42; Non Deluxe (NDX); Approx 250 km Palampur to Ja
Custom Bid for Services - As per BOQ item No 1 Outsourcing services for Semi Skilled Electrician 06
Custom Bid for Services - Refilling and Repair of fire Extinguisher all types
HIGH PRESSURE PIPE,FUEL PUMP MOTOR,FIELD COIL ASSY 24 V,ARMATURE ASSY 24 V,BRG BUSH SELF STARTER,BR
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 230 km from
MT ITEMS 1,MT ITEMS 2,MT ITEMS 3,MT ITEMS 4,MT ITEMS 5,MT ITEMS 6,MT ITEMS 7,MT ITEMS 8,MT ITEMS 9,
Grease XG-286
ORD ITEMS 1,ORD ITEMS 2,ORD ITEMS 3,ORD ITEMS 4,ORD ITEMS 5,ORD ITEMS 6,ORD ITEMS 7,ORD ITEMS 8
Bomb Suppression Blanket
VALVE FUEL SYSTEM,FILTER FLUID,AIR DRYER WITH UNLOADER VALVE,CLUTCH CYLINDER REP KIT,DISC CLUTCH,CO
Banana,Mango,Papaya,Mussambies,Pineapple
Apron Cook,Kettle Camp Oral 13.6 Ltrs Cover,Handle Powrah Wooden,Clock Wall Battery Operating Quart
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 370 km from
Repair/Maint Motor Cycle
2610-8240-0102,13731-83001,2576-7250-0124,2576-7250-0123,2069-5010-5849,2767-8240-0103,2069-5010-01
LAPTOP
TOILET AND BATHROOM BLOCK
Construction of the Squad post and overhead Shed work
01 x 1point5 Ton air conditioner 5 star inverter split ac with anti bacterial super fine mesh filte
Armature Outer BRG,AVR Plate,Cylinder Bone,Cylinder Assy with inlet and exhaust Valve,Push Rod,Push
Annual Maintenance Contract of 03 High Range Photocopier Machines as per BOQ Specification Ser No 1
SPEED SENSOR,GERA LEVER BRACKET SET,CLUTCH BOOSTER ASSY,BULB HEAD LIGHT,KIT RETURNING SPRING,MASTER
OIL SEAL,ASSY BALL JOINT RT THREADS,ASSY UNIVERSAL JOINT YOKE,FIXING BRACKET ASSY,GEAR LEVER BUSH K
Towel big,Hand towel,Comfort,Pillow,Bedsheet
FUEL FILTER,FUEL INJECTOR,OIL FILTER,KIT BRAKE SHOE,CLUTCH PALATE,CONCENTRIC SLAVE CYL ASSY
Touch Screen Laptop,Mobile IOS,Tablet IOS,Tablet Android,High end laptop IOS,High End Laptop - Note
Job should be carried out as per BOQ Specification Ser No 1,Job should be carried out as per BOQ Sp
processor,Mother board Gigabyte,Key board,Mouse,Main PCB Power supply card
LV7 TATA 215454601605 WIRING HARNESS MAIN,LV7 TATA 2157 5440 0115 ASSY HEAD LAMP WITH HALOGEN BULB 
Steel Angled,MS Flat 50MMX8MM,Steel Sheet,Connecting ROD,elect Welding ROD,Solonoid Fuel Off 12V,AV
Pointer steel as per sample,Board Magnetic buttons 30mm10 Nos,Odonil Gel Pocket Mix 60g Pack of 6,C
Art Sheet 23 36 220 GSM,Art Sheet 23 36 130 GSM,Brown Sheet Thick,Pulp Board 22 28 20 GSM white,Vel
LV7-TATA_1460-362-457_Pressure control valve,LV7-TATA_5315-002194_Wood ruf key,LV7-TATA_1463-429-30
Honey Sucker (Cleaning of Septic Tanks)
10337477,10343093,10340486,10343520,10333295,10311975,10315757,10324157
Custom Bid for Services - Condition Assessment of complete Air field including Runway, PTT and taxi
Custom Bid for Services - 106000
PUMP ASSY,DRUM ROLLER,KEY BD AND MOUSE,CLEANING BLADE,LOGIC CARD,BTY 12 V7AH,DVD WRITER SLIM,PROCES
AIR FILTER,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELE
WATER SEPRATOR FILTER ELEMENT,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,AIR FI
LV2/ICVS 2530-004815 (765-14-SB122) CYLINDER LEFT
Lady Finger,Pumpkin,Cucumber,Tinda,Brinjal,Amaranthus,Sponge Gd,Parwal,Tomato Ripe,Bitter Gourd,Gin
Haldi Powder,Mirchi Powder,Dhaniya Powder,Garam Mashala,Chicken Mashala,Biryani Mashala,Sambar Mash
FAN BELT,CAM SENSOR,THERMOSTATE SENSOR,OIL FILTER,FURL FILTER,IC HOSE TYPE STROME,TEMP SENSOR,KIT B
Paneer Masala 100 gm,Ajwain,Badi Elachi,Black Pepper Whole,Amchoor Pdr 100gm,Chana Masala 100gm,Cha
Insulation tape elect PVC,Cable elect 33-012 insulated braided,Tape adhesive PVC 5-8,Sleeve insulat
Acebrophyllin100 Plus Acetylcysteine 600 mg Tab,Aceclofenac 100mg Plus Serrotipeptidase15mg Plus Pa
Construction of Synthetic Surface Basketball Court with Fiber Glass BDS Light Poles and Allied Acce
AGS to Sadipora, Dangerpora, Arihal and back,AGS to Tahab, Zassow, Tumlahall, Arihal and back,AGS t
Custom Bid for Services - 25000
HYDRAULIC SHAFT,HYDRAULIC SHAFT BUSH,PTO OIL SEAL,HYDRAULIC CYL KIT,O RING,HYDRAULIC TOP COVER GASK
Inj Remifentanil hcl 5mg,Romovac drainage set size 16,Romovac drainage set size 18,Inj Rocuronium B
AIR FILTER,SPARK PLUG,OIL FILTER,REMOTE BTY,FUEL INJECTOR,BRAKE PAD FRONT,PRESSURE PLATE
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Cyclosporine A micro emulsion 100mg per ml bottle of 50ml,Clindamycin phosphate 1 percentage topica
TOOL BOX,SPARK PLUG CHAMPION RC 8 YC,BELT WATER PUMP,MOTOR ASSY STARTING,TOW BAR MOTOR VEHICLE
LV2 RCV MR KIT FOR FILTER,LV7 TATA FAN BELT,X3 AVR,LV1 R 72 HOSE PIPE LINE,LV1 R 72 HOSE 48 MM
ANABOND TUBE,ARALDITE,M SEAL,LOOM TAPE,INSULATION TAPE ELECT,FEVIQUICK,PACKING RING,GASKET RUBBER R
Mother Board Asus 510,HDD 1TB,12 V 7 AH Battery,DDR3 4 GB,DDR4 4 GB,Slim DVD Writer,PCI Lan Card
MOTHER BOARD G-31,MOTHERBOARD H310,UPS 1KVA,SMPS,BTY 12V 7AH
Sterile gloves size 6.5 sterile powder free Ansell,Stylet for Intubution,Suction Catheter S 12 FR,S
Tie rod end,Brake pad,Radiator assy,Hose pipe,ISC motor,Brake shoe assy,Hub lock washer,Gear box oi
Cartridge HP 88A,Cartridge HP 110A,Cartridge 166A,Epson L3250 Ink Btls No 003 - 3 Btls,Epson L805 I
Pad abdominal swab 40 x 25 cm with tape 30 cm,Pressure Monitoring Line 100 cm oblique 200cm Adult,P
CABLE ELECTRICAL SINGLE CORE,CABLE ELECTRICAL LT COPPER,LT WIRE,TAPE INSULATION COTTON,PROTECTIVE S
Identification Tag Mother and Baby,Infusion Set For Insulin Pump Meditronic,Laryngoscope cell 1.5 V
Fuel Dispensing Units (Q3)
Repair and Overhauling Service - Executive Chair Revolving; All Brands; Yes; Buyer Premises,Repair 
Repair and Overhauling Service - Split Air Conditioner including Green AC; All Brands; Yes; Buyer P
AAA Battery of 1 point 5V for IR Thermometer,Acamprosate 333 mg Tab,Acenocoumarol 1 mg Tab,Acenocou
Suture Vicryl No 01 round body 110 cm,Swab Stick Disposable Pkt of 100 swab,Synthetic absorabable p
Flooring,Matting,SR Solutions,Fevicol,Touchwood Wooden Polish
Meethi Dana,Meat Masala,Garam Masala,Chicken Masala,Samber Masala,Paneer Masala,Biryani Masala,Zeer
REP KIT WHEEL CYL,OIL SEAL FOR HUB,GEAR LEVER KIT,ASSYCOMBINATION SWITCH,CLUTCH RELEASE BEARING,BRA
Skin stapler with 35 stainless steel staples,Solution Chlorosol bott of 500 ml,Spray PAP Fixator,St
Suspension work with replacement of bush kit of TATA Safari Veh BA No 18B128944N,Complete overhauli
Ryles tube Size 14,Ryles tube Size 16,Ryles tube Size 18,Sterile gloves size 7.0 sterile powder fre
334 Y5525,335 47270,335 47271,40 301846,40 301773,335146895,113CS12018,113CS92128,113CS92136,113CS9
Syringe dosposable plastic sterile 10 ml with needle,Tube feeding smooth plastic infant 38 cm long 
Mother Board H81,Mother Board H61,Keyboard Mouse,Teflon Sleave,Presser roller,PCI Lan Card
NST paper 142mmX150mmX150 Sheets EMCO Sonycaid,Oxygen mask with reservoir,Vaccum Blood Collection t
Overhaul of Rotary pump assy of Truck 2.5 Ton TATA,Repair of hydraulic head of Rotary pump assy of 
Net Camouflage Shrimp Type (Defence)
Fire Ball Extinguisher 3Kg
Yoga Mats (Q3)
Room Freshener 500ml,Colin 500ml,Wonder Cleaner 1 Ltr,Hand Wash 500ml,Harpic 1 ltr,Dusting Cloth
PULL CABLE ACCELERATOR,FIELD COIL,ARMATURE ASSY,REPAIR KIT,FAN BELT,CARTRIDGE FUEL WATER SEPARATOR,
Dimension Transferrin Flex TRNF 10444985 box of 120 test,Dimension LOCI Folate Flex FOLA 10463370 b
LV7 MARUTI 78481M79000-5ES BEZEL HANDLE LH,LV7 MARUTI 09471M12076 BULB 12V 5W,LV7 MARUTI 29241-8005
Plain Copier Paper (V3) ISI Marked to IS 14490,Plain Copier Paper (V3) ISI Marked to IS 14490,Black
Carbidopa 18.75 Plus Levodopa 75 mg Plus Entacapone 200 mg tab,Carbidopa 25 mg Plus Levodopa 100 mg
Injector,Power Steering gear,Air Dryer Assy,Linning Kit,Wiring Harness Wiper Motor,Assy Clutch Pres
Cabin Bush,Cabin Lock,Banjo Washer,Tag,Fuel Filter,Anabond tube
GASKET OIL FILTER,REGULATOR WINDOW RH,BEARING NEEDLE,ASSY OIL FILTER,HOSE ASSY AIR FILTER,AIR FILTE
Ignition Coil,Brake light bulb double filamate,Reverse light bulb 12V 21W,Parking light bulb 12V 9W
Indicator bulb 24V 21W,Tail light bulb 24V 9W,Insulation tape,Gauge bulb 24V 5W,Knuckle brg upper,K
DRIVE PINION,SOLONOID SWITCH,IGNITION SWITCH,METAL DIODE,RUBBER HOSE,BTY CABLE WITH TERMINAL,AIR FI
AVR,BTY CABLE WITH TERMINAL,CLUTCH PLATE,RELEASE BEARING,RELEASE BEARING SLEEVE BEARING,FLY WHEEL R
G2 9520-000011 STEEL ANGLES 50X50X5 MM,F1 5110-000006 FILES FLAT BASTARD 350 MM,F1 5110-000015 FILE
LV7 STLN H-3610818 NYLON NUT M8,LV7 TATA 2520-72-0002398 PRESSURE PLATE ASSY,LV7 TATA 2069-5010-583
Fuel pump assy,Ignition Coil,Injector Assy,Oil Seal,Door lock left right,Front main leaf,Rear main 
Kobelco 220,Kobelco 220,EX 70,EX 70,EX 70,110MC02019,110MC11359,BD 80,113CV01001,BD 50
Arvi,Beans French Lobis Cluster Board Beans,Brinjal,Cauliflower,Cucumber,Lady Finger,Peas Green,Pum
Arvi,Beans French Lobis Cluster Board Beans,Brinjal,Cauliflower,Cucumber,Lady Finger,Peas Green,Pum
Chair Computer,Chair Visitor,Bench Workshop heavy duty,Heavy duty working table,Table Computer,Tabl
FUEL FILTER PRIMARY,FUEL FILTER SECONDARY,OIL FILTER,AIR FILTER,FUEL FLEXIBLE PIPE,FUEL FEED PUMP,F
Brush carrier Assy,Field coil assy,Solenoid,Combination switch MS Harness,Lining Fender RH,Lower Ar
Cheese Spread,Cornflakes,Custard Powder,Cornflour,Jelly,Horlicks,Bornvita,Tomato Sauce,Pickle,Dog B
CARBON HOLDER,HIGH TENSION LED,CARBON BUSH HOLDER,OIL FILTER,FUEL FILTER,OIL FILTER BS,FUEL FILTER 
Provn Store Shelter
Provn of Sentry Post Shelter part only FOR ORAK,Provn of Sentry Post Shelter part only FOR GELEMO,P
10129,10135,10201,10264,10279,10281,10294,10301,10319,10325,10533,10543,10544,10570,10579,10581,105
Provn of Officers JCOs Living Shelter FOR TAKSING,Provn of Officers JCOs Living Shelter FOR SHORANG
Van Pump,Armature Assy,Water Pump,Carburettor,Cylinder head Gasket,Eng Comp Gasket,Cam Chain Kit Co
Bearing Pedestal,Major Rep kit for master cyl,Belt Fan 7323 Section Bm,Eng Timing Chain Kit,Throttl
K5 6260-000026 1,H2 KND NIV TMAT 73,F1 5120-000062,H1B 6810-000042,A3 8340-000508
Y3 RP-6135-001362,Y3 6135-001363,Y3 5970-000576,Y3 5970-000575,Z9 RP-6140-MISC-CQAL-4484
H2 8305-000064,H7 6505-000020,H3 5530-400034,H-2 8305-000182-CASD,H4 8135-000094,H5 1080-000015 1,H
Dried Cow Peas (Lobia) (V2) (Defence)
Permanent Marker Pen Blue with Thin Tip,Permanent Marker Pen Blue with Thin Tip,Permanent Marker Pe
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Not Required; Admin
Goods Transport Service – Per KM Based Service - Household/Office; Open Body LCV Truck; 19 FT LCV
Short Term Cab & Taxi Hiring Services - Sedan; Local; 80Kms x 10Hrs,Short Term Cab & Taxi Hiring Se
Amoxycillin 875 mg and Clavulanic Acid 125 mg Tab,Azithromycin 500 mg Tab,Nitrofurantoin 100 mg TaB
Amoxycillin 875 mg and Clavulanic Acid 125 mg Tab,Azithromycin 500 mg Tab,Nitrofurantoin 100 mg TaB
Amoxycillin 875 mg and Clavulanic Acid 125 mg Tab,Azithromycin 500 mg Tab,Nitrofurantoin 100 mg TaB
Fuse assy main,Controller assy EPI,Mirror assy out rear view RH,Blade assy wiper,Front direction in
Frt Wind Shield Glass,Frt Wind Shield Glass Weather Strip,Wind Screen Selant,Timing Belt,AC Belt,As
pressure plate,clutch plate,clutch release brg,release brg sleeve,relay,drive assy,solenoid assy,pt
D F Cutter Kit,Tooth Kit Loader Bucket Forged,Filter Kit 3 DX,Seal Kit,Grease Nipple 1 8 BSP
hydraulic seal,fuel pipe,hydraulic pipe,buzzer 12v,sheet cellular 4 inch,gasket
Steering Gear Box,Assy Steering Drag Rod,Exhaust Brake Solenoid,Disc Pad,Rear Brake Shoe,AC Fan,Fus
Five Chamber Tail Light LH,Ram Hydraulic Ram Assy,Sparking Plug,bearing DR Bevel Pinion,Oil Seal,Ra
BOXES RIGID COLLAP 254X152PT5X101PT5MM,DELETED MANTALS 200 CD,NIPPLEGREASE BUTTON HEAD 1 8 BSP X 9M
ASSY PULL CABLE ACCELATOR,ASSY PISTON SET WITH PINS,ARMATURE ASSY,SOLENOID SWITCH,FIELD COIL ASSY
Adrenaline Tartrate 11000 1 ml Inj,Pheniramine Maleate Inj 22.75 mg ml amp of 2 ml,Atropine Sulphat
Falco T-01 Max Drone
Sheep Blood Agar (Q2)
PRESSURE PLATE,ASSY 310 DIA CLUTCH DISC,CLUTCH SLEEVE WITH BRG,PLATE CLUTCH DISC CLUTCH,PRESSURE PL
Combination Switch,Clutch Cylinder Assy,Field Coil Assy,RPM Meter,Solenoid Switch,Actuator Spring B
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Estimation of Provn of Defi OTM Accn1,Estimation of Provn of Defi OTM Accn2,Estimation of Provn of 
Inj Dexmedetomidine 100 mcg oblic ml 50 ml vial,Diethyl Ether Solvent Bott of 500 ml,Ketamine HCl 5
Inj Nano Liposomal Docetaxel vial of 20 mg,Isavuconazole 100 mg Cap,POMALIDOMIDE 4 MG TAB,Darbepoie
Lighter Socket for Veh,Unit Service Name Board,Dashboard Camers with 64 GB Memory Card,Pulse Oximet
Strinr P,Vent Pipe,P C 12 Ltr,Camp Oval,Basket
H3 5530-400114 PLY WOOD FOR GENERAL PURPOSES MR-AB 9 PL,H3 5530-000245 PLYWOOD FOR GENERAL PURPOSE 
Oil OX 320,Grease LG 320,Grease XG 340,Oil 2T Supreme,Oil OM 16,Oil 2T Synthetic Bombardier Injecti
PTZ Cables Repair or Replacement,PTZ Camera IP Camera Bullet Camera or Dome Camera repair or replac
OIL FILTER ELEMENT,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
Hose Assy,Air Cleaner Assy,Carburator assy,Fuel on off cock,Packing carburator,Packing insulator,Fu
LED Box,Stethoscope,Lamp,Thermometer,Nebulizer,Hemoglobin,Strips
Surgical Hand Gloves size 6 point 5 pair of,Surgical Hand Gloves size 7 pair of,Syringe disposable 
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others,Manpower Outsourci
WASHING MACHINE 25-30 KGS
ACP sheet 8x4,Aluminum Channel,Plywood Sheet 19 MM,Sunmica Sheet,Fevicol
Starter rope assy of 6 point 5 KVA gen set for EW Sys,Fuse of 6 point 5 KVA gen set for EW Sys,Air 
Copier Paper A4,Copier Paper Legal,Register 2 Quires,Register 4 Quires,Sketch pen Assorted colour,B
CN 8465-000078 Frog Cutter Wire Folding Mk-I,A3 8340-000593 Pin Tent Angle Iron Medium Tent Mk-2,CN
Excavation in trenches,Returning filling in including spreading leveling,Removing of excavated mate
Three seater steel SS 304 Chair with PU Cushion,Commercial RO 25 Ltrs,Water Cooler 25 Ltrs Blue Sta
Beans,Brinjals,Lady Finger,Pumpkin,Cucumber,Tinda,Arvi,Plantain Green,Carrots Country,Tomato Ripe,A
Custom Bid for Services - Custom Bid for service- Testing of Empty Fire Extinguisher CO2 Type, Cust
CHT for guest,Banners,Invitation Cards,Pamphlets,Posters,Media Coverage,Seating arrangement,PA Equi
Aceclofenac 100 mg Tab,Acenocoumarol 1mg tab,Acenocoumarol 4 mg Tab,Adrenaline Tartrate bracket 1 1
10 percentage Povidone iodine solution equivalent to 1 percentage available iodine 500 ml Bott,5 Am
LV6 MT7 09269-35009 BEARING 35X72X16.5,LV6 MT7 3110-001963 BEARING TAPERED ROLLER 15X42X14.25MM,LV6
LT WIRE,LINEAR GASKET,OIL PRESSURE GUAGE,VOLT METER,FREQUENCY METER
FUEL RELAY 12V,FUEL TANK HOSE,IGNITION COIL ASSY,SPARK PLUG ASSY,WATER PUMP ASSY,TEMP SENDING UNIT,
Repair of Commercial RO incl servicing and exchange of filter,Repair of 3 HP Grass cutting machine 
Clutch Release Brg,Brake Booster Kit,Wheel Cyl TVS,4x4 Cable,Bush CE Bracket,Change Over Switch,Arm
HYDRAULIC PIPE,TILT CYL SEAL,BUCKET CYL SEAL KIT,BOOM CYL SEAL KIT,OIL FILTER
Field Coil,Brush Plate,Bush Set,Fuel Flot Valve Set,Isolator Switch,Combination Switch,Bearing,Univ
Bipod T Grip with Picatinny Rail,Drone Motion Sensor,Wireless Mouse HP,Tripod Stand,Ethernet Fiber 
Vee Belt 102,Vee Belt 97,CRI 2HP 25 Stage Pump,CRI 2HP Panel,Steel Wire Green 6mm,Adaptor Set 1 Poi
Refined Sunflower Oil (V2) (Defence)
FIP TEST BENCH
Chain Link Fence,Angle Iron,Barbed Wire,Coil Wire,Nut and Bolts and screw with double washer,Plain 
UG Amn bunker precast,Fire extinguisher,LC with Earthing,Solar Lantern,Smoke Alarm
DRIVE SHAFT,TRANSPONDER AND RF KEY,AC FAN,REAR SHOCK ABSORBER,AIR FILTER
Supply of Quick Erectable Protection Barriers Hesco Basket,GI Wire Mesh,Spring Rings,Joining Pins,J
F1 5120-000148 HAMMERS BRICK MK-1,F1 5120-003036 SPANNER OPEN JAW FIXED DOUBLE ENDED STEE,F1 5110-0
REVERSE LIGHT SWITCH NEW MODEL,ROTARY SWITCH NEW MODEL,SLEEVE CYL ASSY NEW MODEL,SLEEVE CYL ASSY OL
PRESSURE PLATE OLD MODEL,RAM PIPE LINE NEW MODEL,RELAY,RELEASE BRG NEW MODEL,RELEASE BRG OLD MODEL
AP3 Grease
Elevated Security Post with Guard Room
Chain Link Fence with MS Pole, Barbed Wire of two Strands of four line
Mattress 4 inch 2 layer Single Bed,Tripal plastic 30 ft and 30 ft,Tripal Canvas 15 ft and 15 ft,Vis
Solar Street Lighting System (NTPC)
Goods Transport Service – Per KM Based Service - Vehicles, Machinery & Equipment; Platform Truck;
SPO2 PROBE SENSOR PROBE,ASSY OXYGEN ADJUSTMENT VALVE WITH HUMIDIFIER BOTTEL,ECG CABLE,PHOTOTHERAPY 
BEARING TAPPRED ROLER,MOUNTING ENG FRONT,SHOE SET REAR BRAKE,SPRING HANGER BKT,SHACKLE PIN,BEARING 
SEAL KIT,KIT UJ CROSS,PROPELLER SHAFT,HYDRAULIC HOSE,STARTER MOTOR 12VDC,AXLE SHAFT SEAL,FLANGE
Assy Cross kit,Assy clutch master cylinder,Brg needle,Shoe Comp Brake rear,Fan belt NK000514,Pad fo
WIPER BLADE,BEARING TAPPERED ROLLER,BEARING REAR WHEEL,REAR CONE WASHER LOCK,BRAKE PAD,SWITCH ASSY 
LV7/2.5 TON (1468532248) DELIVERY VALVE,LV7/STLN (24651309404) HOUSING
LV7/2.5TON (2786-0199-990) NOZZLE,LV7/2.5TON (24651309404) HOUSING
PTZ Camera with adapter,IR Camera with adapter,Pole with Hanging Bracket 65 mm,PTZ Camera rain shie
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others
LV7/STLN (2815-012241) REPAIR KIT ENG,LV7/MG (11110M52912) HEAD CYLINDER
Digital Medical X - Ray Films (V2),Digital Medical X - Ray Films (V2),Digital Medical X - Ray Films
SHELL SPIRAX S3 ATF MD3
Plug Expansion 30Z1110146,Valve intake 30Z1180399,Valve Exhaust 30Z1180269,Grommet oil 31Z1160104,G
TEMP CONTROL DEVICE FOR RegREM
Main Board,Micro CCT DGTL D27,Micro CCT DGTL D28,Regulator 7812,DC DC Convertor
Music Sys with inbuilt speaker,Tables with set of 03 Chairs,Podium,Wooden Sofa Set 5 Seater,Panelli
Drinking Water Container 35 Ltr,Container aluminium 10 Ltr,Container aluminium 18 Inch with lid,Wat
OIL FILTER,INSERT MICRO SUPER FILTER STAR TYPE,FILTER AIR COMPLETE,AUTOMATIC VOLTAGE REGULATOR,FUEL
ARMATURE ASSY 24V,FIELD COIL ASSY 24V,BUSH SET,SIREN 24V,COMBINATION SWITCH,AIR COMPRESSOR,REGULATO
24 Port Manageable GB 3 Layers Switch SFP Module,16 Port Manageable GB 3 Layers Switch SFP Module,4
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Diclofenac diethylamine 2 piont 32percent spray for topical use,Levetiracetam 1000 mg Tab,Tab Levod
PCO2 electrodes sensor 1 per pack for phox,PCO2 membrane pack of 3 phox ultra,Ph electrode sensor 1
Diclofenac Sodium Suppository One Hundred mg,Paracetamol with cysteine HCL monohydrate Infusion One
Kick Starter Crank,Cyl Barrel,Carburator Assy VM24,Spark Plug,Rectifire with Nut,Silencer Assy,Chai
DEMIL PLANT
BANDAGE CREPE 15CM,BETAHISTINE 8 MG TAB,BETAMETHASONE 0.05 PER PLUS GENTAMYCIN 0.1 PER OINT TUBE OF
ACEBROPHYLLINE 100 MG TAB,ACETAMINOPHEN 325 mg PLUS TRAMADOL 37.5 mg Tab,Alovera and Vit E Lotion b
CILINIDIUMPlusCHLORDIAZEPOXIDE Plus DICYCLOMINE NORMAXIN TAB,CILNIDIPINE 10 MG Plus METOPROLOL 50 M
Lady Finger,Pumpkin,Cucumber,Tinda,Brinjal,Amaranthus,Sponge Gd,Parwal,Tomato Ripe,Bitter Gourd,Gin
Bib cock 20 mm,Float Valve 20 mm,GI Gate Valve 20 mm,GI Tee 20 mm,GI Tee 40 mm,GI Flange Washer 50 
Mobility SHC-220
Outsourcing 1,Outsourcing 2,Outsourcing 3,Outsourcing 4,Outsourcing 5
OIL 15W50
Storage Shelter
Pressure Plate,Adopter,Air Pressure Pipe,Air Pressure Pipe 22 Nos Nut,Air Pressure Pipe 32 Nos Nut,
Banana,Mango,Papaya,Mussambies,Pineapple
Banana,Mango,Papaya,Mussambies,Pineapple
H1-B 5350-000007 Abrasive Cloabrasive Cloth Emery or Corundum,H1-B 3439-000165 Flux Soldering Paste
Dextron-III
Supply of stores for Sentry Post
Tooth,Bolt,Nut,Engine Oil Filter,Fuel Filter,Air Filter Outer,Air Filter Inner,Air Filter Set,Pin,P
CONSULTANCY SERVICES FOR PROTECTION OF BRIDGE AND AREA DEVELOPMENT
LEVER GEAR SHIFTING CONTROL,FOG LIGHT ASSY,WHEEL BRG REAR,TAIL LIGHT ASSY,REPAIR KIT,GASKET CYLINDE
Cam shaft complete,Cam shaft gear,Piston assy,Piston ring set,Fly ring set,Connecting brg set,O rin
SOLAR SECURITY LIGHTS
Balli / Wood Pole as per IS 876
Balli / Wood Pole as per IS 876
Short Term Cab & Taxi Hiring Services - SUV; Outstation 24*7; 500Kms x 14Hrs
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others
FUSER UNIT,CLEANING PLATE BLADE,OPC DRUM PHOTO COPY HOLDER,PRESSURE ROLLER HP 1020,DRUM,TEFLON SLEE
Hiring of Consultants - Milestone/Deliverable Based - Subject Matter Experts, Soil Investigation, S
Bone and Meat Band Saw Machine (Q3)
LV1 R90 54-07-028-1 WAHER ADJUSTING,LV1 R90 188.35.001SB GASKET,LV1 R90 188.31.257 GASKET,LV1 R90 5
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
Door Frame Metal Detector (Q2)
Tie Rod End,Assy Universal Joint,Slave Cyl Assy,Assy Clutch Master Cylinder,Suspension Bush Kit,Bea
Water Dispenser with Fridge,Juicer Mixer Grinder Havells,Water Bottle 20 Litre,Tea Strainer,Iron Pr
Bran for Defence (Q3)
Orthopaedic battery operated drill and reamer system for trauma surgeries
Refined Sunflower Oil (V3) (Defence)
Goods Transport Service – Per Trip based  Service - Vehicles; Platform Truck; 32 FT Truck
PVCP pipe 1.5 Inch,Water Syntax 1000L,15 W Solar Street Led light with Integrated Bty,40 W Solar Pa
Fabrication of A Motorised Balley Screw Jack
CCTV CAMERA,CP PLUS DVR 16,08 PORT GIGA SWITCH,OFC ENCLOSURE,MEDIA CONVERTER,2TB HD,OFC CABLE,OFC J
LV3/ICVS 2815720308605 OIL PUMP ASSY (SB 20-12-00-13)
ICE PITONS SET,SNOW SHOVEL,SNOW GLOVES,EXPEDITION BOOTS,GAITERS,EVACUATION HARNESS,STRETCHER RESCUE
RECHARGEABLE BTY 3.7V,DIODE,RESISTENCE,SUNCTION PIPE,CORE DISC,ADOPTER
STITCHING OF SEATS WITH NEW BLACK RAGZINE,FITMENT OF FOAM SEATS,ADHESIVE CHARGES,WELDING CHARGES,LA
Front Oil Seal,Pressure Plate,Clutch Plate,Eng Mtg Pad,Gear Lever Assy,Driven Disc,Field Coil Assy,
Repair of 29 Brush Cutter Replacement of Spark Plug,Repair of 29 Brush Cutter Replacement of Fuel T
Air Frame,Stack,ELRS Receiver with Antenna,VTX Module with Antenna,Battery Pack,Analog Camera,Prope
Rifampicin 600mg plus Isonizzid 300 mg Tab,Ethambutol Tab 200 mg,Tab Ethambutol 400 mg,Ethambutol T
Egg Fresh,Potato,Onion,Bread,Ice MM,Limequick,Arvi,Beans French or Lobia or Cluster or Broad Beans,
WIRELESS KEYBOARD MOUSE BLACK,HARD DISC DRIVE 2 TB,MOUSE LOGITECH WITH KEYBOARD,HP DRUM UNIT,BTY 12
PTZ IR Enabled Camera
Disc Plate,Pressure plate,Conentri slave,oil filter,Air filter,Fuel filter,U Clamp bush,Shock absor
Hostile Drone Jamming and Tank Protection System for Tank T-90
Lighting Pole or Post and Hardware - Tubular Street Light Poles (V2)
Bty 1 2V 1300Mah AA for PNVB,Bty 1 2V 22Mah AA,Bty 12V CR 123A,Bty 1 2V 2700 mAh AA for RL PNS,Bty 
Oil filter,Engine oil 5W 30,Ultra Coolent,Air filter,Brake hose,Brake pads,Labour cost,Tandem maste
Mother Bd i5,SMPS,Processor fan,Sata cable,Feeding assy,Drum assy,Waste pad,Head,Key bd and mouse,F
Drone jammer,Rf Detector for Drone,Hand Held GPS,Iron folding executive chair two seater,Iron Shoe 
Foot mat,Towel,Cloth Stand,Cloth Basket,Induction Cook Top,Water Pipe,Single Bed Sheet,Pillow,Slipp
Knuckle Bearing,WHEEL BEARING REAR,Pad,Pipe Fuel,Gasket Set,CONE ROLLER FRONT WHEEL BRG INNER
DIGITAL BP CUFF,SUCTION BOTTLE,BP CUFF WITH COVER,BULL NOSE,B P VALVE,B P MACHINE WITH COMPLETE SET
Drone jammer,Rf Detector for Drone,Hand Held GPS,Field Study Chair,Iron Study Table with wooden top
Oil filter,Gasket,Engine oil change,Transmission oil change,Coolant
Hot and Cold AC Voltas,Stabilizer for AC,Wall Fan Havels,Pedestal Fan,Flags Regimental,Visitor Book
Atropine Sulphate 1 ml inj,Lorazepam 2 ml inj,Lignocaine HCL 2 Per inj,Midazolam 5 mg inj,Mannitol 
Drone jammer,Rf Detector for Drone,Iron Peg Table with wooden top,Iron washbasin with mirror,Iron C
Glycopyrrolate 0 point 2 mg 1 ml inj,Atracurium 10 mg per 2 point 5 ml inj,Vecuronium Bromide 4 mg 
Printed File Cover with logo,Register 12 Quire,Register 10 Quire,Register 8 Quire,Register 6 Quire,
Genr set 40 KVA KIRLOSKAR 04.58600.03.0.00,Genr set 40 KVA KIRLOSKAR 04.296.01.0.00,Genr set 40 KVA
CCTV Sys with 4 MP Bullet Camera IR,NVR 32 Channel capacity,Hard Disk Drive 6 TB Capacity,9 U Wall 
High Mast System,LED Solar Light,Installation
LV7 MG CLUTCH RELEASE BRG,LV7 MG PRESSURE PLATE,LV7 MG CLUTCH PLATE,LV7 MG COIL IGNITION,LV7 T 815 
X3 FUEL PIPE,X3 LAMP,X3 NOZZLE,X3 HT COIL,X3 CARBURETOR ASSY,X2 FUEL PIPE,X2 SPARK PLUG WITH HOLDER
Boxing Gloves 10 No,Boxing Gloves 12 No,Punching Pad,Head Guard,Gum Shield,Boxing Bandage
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 160 km from
Haldi Powder,Mirchi Powder,Dhaniya Powder,Jeera,Kalee Mirch,Garam Masala, 100 gm,Chicken Masala, 10
Besan (V2) as per IS 2400 (Q4)
Tiling of outer wall on three sides 60 x 120 cm tiles,Toughened glass work with doors,False Ceiling
Shirting Cloth (Q3)
Full Plate 10.5 inch,Quarter Plate 7inch,Veg Bowl 9cm,Donga or Lid,Salt and Pepper,Napkin Holder,Co
UTNCILS CO 150 MEN SET DEGCHIE 650MM LID,STAINLESS STEEL THERMOS 1 LITRE,UTENSIL COOKING 150 MEN SE
Heptr Weighing Bay Embedded in Hangar Floor
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Admin
EXT FIRE CO2 WATER TYPE 9 LTR CAPACITY,EXT FIRE WATER AIR STORED PRESSURE,BTY SEC PORTABLE LIION SC
green pvcpolythene for tentage,Halogen Light,Globe for wksp entrance,Philips induction HD4928 for O
CCTV Sys with 4 MP Bullet Camera IR,NVR 32 Channel capacity,Hard Disk Drive 6 TB Capacity,9 U Wall 
FLY WHEEL RING,KICK STARTER,RELAY 24 V,RELAY 12 V,SOLENOID SWITCH 12 V,SOLENOID SWITCH,BUSH SET,PRE
PUMP ASSY FUEL,ADAPTER PIPE LEAK OFF,OIL SEAL,HOSE 1 OBLIQUE 4 ID,OIL PUMP ASSY,CHANGE OVER SWITCH,
LV7 STLN WINDOW GLASS RH,LV7 STLN CABIN TILT CYL,LV7 STLN YVEL HYDRAULIC LOCK,LV7 STLN CLUTCH PLATE
LV7 MG OIL FILTER ASSY,LV7 T815 OIL COOLER,LV7 T815 PRESSURE MAGNETIC,LV7 T815 ELECTRO MAGNETIC,LV7
Tyre Stacking Racks
LOGIC CARD,MOTHERBOARD,MAINTENANCE BOX,WIRED KEYBOARD AND MOUSE,INTERNAL DVD WRITER,UPS BTY,WIRED M
Overhauling of winch gear box,Overhauling of auxiliary gear box,Repair of steering gear box,Repair 
stearing columm,stearing bearing,bearing,stearing oil seal,head gasket,hydraulic pipe
Pure Lead Tin Valve Regulated Lead Acid Monobloc Battery 12V 160 AH
gasket set,oil seal,gear counter shaft second,pump assy oil,air cleaner hose,fuel filter paper,valv
Packing polythene,Zip Lock,Packing Tape,Needle,Packing white cloth 42x56,Packing white cloth 30x40,
Cartridge 88A,Bamboo,Fig No 11 Tin Sheet,FS Paper,Fig No 12 Colour Paper
Almond,Muesli 500gm Kellogg,Chyawanprash,Maggi,Biscuits,Jaggery,Nutella,Energy bar
CPU i5 12th Gen,Monitor 24 inch,Keyboard,Mouse,UPS 1 KVA
clutch cable,chain kit,chain wheel with hobs set,speedo cable,speedo drive
Atta as per IS 1155 (Q3)
Cheese Slice,Cheese Slice1,Cheese Slice2,Cheese Cube,Cheese Cube1
Atta as per IS 1155 (Q3)
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
Digital Hearing Aid Programmable Through Software (BTE) Channels - 08
High End Laptop - Notebook,mac os based laptop/notebook
Revolving Search Light (MHA) (Q3)
Drop Arm Barrier (Boom Barrier) (MHA)
High Mast Lighting Tower for large area with LED Flood Lighting System
Cat Part No 10X0540 Gasket Filter for SSL,Cat Part No 10X0788 Head Fuel Filter for SSL,Cat Part No 
SEAL AND SPRING SET,SIDE GEAR BOX SEAL,SHAFT PINION,PINION,FLASHER CHANGE OVER SWITCH,SOLENOID SWIT
Himalayan Pink Rock salt (Q3)
Flight Charges from Jammu to Bangalore,Train ticket charges from Bangalore to Delhi,Train ticket ch
PC,Visualiser,Projection System - one Projector and one Screen,Podium with Integrated Control and A
04 Teacher salary at the rate 25000.00 per month,Books for NDA entrance exam,Books for CDS entrance
High End Laptop - Notebook (Q2)
Atta 5 Kg,Atta 10 Kg,Atta 20 Kg,Atta 25 Kg,Atta 50 Kg
Haldi or Turmeric Powder,Dhania or Coriander Powder,Red Chili or Mirch Lal,Jeera or Cumin Seeds,Kal
wireless heavy duty horse clipper
Construction of Volleyball Court with synthetic Surface and Allied Accessories
Suspension slash Syp Fexofenadine 30 mg slash 5ml coma 60 ml bottle,Levetiracetam 100 mg slash ml c
METALLIC BASE PLATE
DUAL 15 INCH HIGH POWER TWO WAY LOUDSPEAKER,DUAL 18 INCH POWER SUBWOOFER,DUAL CHANNEL 2100W 4 OHMS 
PABX System - EPABX (V2) (Q2)
INJECTOR NOZZLE,PUMP ELEMENT,GASKET CYL HEAD,GASKET CRANK CASE COVER,COVER GASKET CYL HEAD,CR BEARI
X2-MG19-DYNAF-8-35-263-00 PLUG X 10,X2-MG19-DYNAF-8-35-315-00 PLUG X 19
Box Assy Steering Gear,Brg Clutch Release,Brake Cyl,Feed Pump,Dryer with unloader Valve,Assy Clutch
BRAKE BOOSTER FRONT,BRAKE BOOSTER REAR,SOLENOID 24V,SOLENOID 12V,THRUST WASHER,ASSY CLUTCH MASTER C
PTO Pump Assy,Regulator Vehicular Window,Combination Switch,Slave Cyl Assy,Cyl Head Gasket,Assy Cab
Plywood 16mm,Foam Sheet,Plywood 10MM,Plywood 12MM,Anabond Tube,Plywood 19MM,Cutting Wheel Bosch14,A
Coil Assy Ignition,Assy Tail Gate Handle Exterior,Drive Assy,Cyl Barrel,Gasket Set Comp Assy,Assy C
Hose 72Q162020500,Axial Pistan hyd motor TGP01444575,Scrapper Ring CSN029295,Firom unwoven filter 0
1 and Half inch Angle,1 and Half inch Patti,Tyre with Shaft,Hinges 2 Inch,Nut Bolt 2 Inch,GI Elbow 
Centre Bolt,Tie Rod Assy,Thermostat Hose,Fuel Pipe 19 mm,Fuel Pipe 17 mm,Propeller Shaft Rear,Fuel 
All in One PC (V2) (Q2)
Behind the Ear Hearing Aid (Digital)
Bed Side Carpet,Cloth Stand,Mattress,LED 32 Inch Smart TV,Quilt With Cover,Dish TV Free,Water Campe
HOSE,BOLT M10 X 80,FOG LAMP BULB,HOSE 06 BSP HP 280MM B,THROTTLE BODY SPARY,HOSE 1I4 BSP X 525MM
High Power Wiper Motor,Slave Cyl Clutch,Assy Clutch Disc,Assy Clutch Master Cyl,Fuel Pump Motor,Ign
Socks HIMCLOS
Element Oil Filter,Hose 1 ID 80 Long,Mounting Engine Front,Cover Assy Clutch,Field Coil Assy,Fuel F
Title1,Title2,Title3,Title4,Title5
vacuum machine
Printer Repair 1,Printer Repair 2,Repair MFD Drum Head Cartridge Unit and Developer,Printer New Car
Radiator Repaired,Wire Harness Repaired,Wheel Drum Skimming,Radiator Repaired 2,Invertor Repaired
V5/1290-000710, Tripod Fire Control Instrument No. 14 MK
PRESSURE PLATE ASSY,BATTERY CUT OFF SWITCH,ARMATURE ASSY,SOLENOID SWITCH,FIELD COIL ASSY,DUAL BRAKE
CPS head cable,Maintenance box,Pickup assy,UTP cable,16 port switch D link
Strut Assy,Speedometer cable,Oil Seal,Hose Non Metalic,Hose,Flexible Hose Pipe,Elbow Hose 95x100,De
Aluminium Container,Aluminium Container,Kadai Medium,Palta,Jharna,Cooker,Parat Small,Tea Container 
Fuel Fiter MG,Steering Pipe TATA,Rear Brake Booster Kit TATA,Booster Assy TATA,Kilometer Cable TATA
Repair of UPS Card,Replace of pick up roller Brother printer,Replace of pressure roller printer Can
Arterial Blood Gas Analyzer (V2)
Operation and Maintenance Of Electrical Systems/Electrical Installations - Operation and maintenanc
Potato Fresh,Onion Fresh,Garlic (Lassan)
Key Board and Mouse HP,Bty 12V 7AH Exide,SSD 500GB WD,SMPS Intel,Mother Board i5 10 Gen Intel
Custom Bid for Services - Procurement of services and items for printing of IAVC Cards
RAM ASSY,STARTER MOTOR 12V,SHIFTING ROD,FRONT FOG LAMP RH,COVER ASSY CLUTCH,SOLENOID SWITCH
AD Blue Mixture
Repair and Overhauling Service - Camera for CCTV System (V2); CP PLUS; Yes; Buyer Premises
Attendance Register,White envelope,Receipt for LP Medicine 100 pages,Prescription slip Colour Yello
Cover Assy,Clutch Disc Assy,Gear Lever Kit,Assy Pull cable Accel,Wheel Brake Cyl,Assy cable 2200mm,
Acetazolamide 0.25g Tab,Acyclovir Ophth Ointment 3 percent in 5 gm tube,Adapalene 0.1 percent Tube 
BOOSTER BRAKE AND TMC ASSY,HEAD LAMP ASSY RH,HEAD LAMP ASSY LH,TAIL LAMP ASSY RH,TAIL LAMP ASSY LH,
JOINT ASSY UNIVERSAL,CLUTCH CABLE,BRG CLUTCH RELEASE,PAD,BRAKE LINNER,OIL SEAL FRONT HUB,FRONT BUSH
10 Ton Hydraulic jack,Humidity Control device,Computer Repair Kit Pros Kit,Voltage Corrector,Socket
Scanner
Z3 1285-000095 OR 1285-000096 DUPLEXER MIXER DIODE
Fd Toilet (Relocatable)
Repair of RPAV (Remotely Piloted Arial Veh) (Trinetra)
IT HW PROJ
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma; Admin
Selection of Laboratories for Testing of Products/Material - Soil; Buyer to use custom filter to in
Security Manpower Service (Version 2.0) - Healthcare; Unarmed Security Guard
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Manpower Outsourcing Services - Minimum wage - Skilled; Graduate; Admin
Toner Cartridges / Ink Cartridges / Consumables for Printers
Salt Box,Water Cooler,Cooker,Ration Box,Dabbi,Regulator,Lighter,Gas Stove,Tava,Jug,Chakla,Belan,Pat
Monitor 24 inch,Ram 8 GB,SSD,Keyboard with mouse,HDMI cable
Differential overhauling and seal kit replacement service of MPV Casper
Steam Coal (Q3)
Steering Tie Rod End,Ball Joint Assy,Alternator Belt,Air Filter Element,Assy Oil Filter,Assy Kit Li
Stopper Cable,Head Light Bulb Scorpio H7-12V 55W,Fuel On Off Cock,Kick Starter,Speedometer Gear,Spa
Custom Bid for Services - Menu based catering services
Server,Entry and Mid Level Desktop Computer,Online UPS (V2),Line Interactive UPS with AVR (V2),Netw
Professional Training Services (Version 2) - offline; Weekdays
93330-000106 Sheet Cellular,5530-400048 Plywood General purpose,8010-000114 Paint RFU Aluminum,8010
General Service of LBPV Rakshak Plus
Onion Fresh,Garlic (Lassan),Potato Fresh
Wind Screen,Vehicle Speed Sensor GB,Pilot Bearing,Gear fly wheel Ring,Alternator 24 Volts 75 Amps,D
Bacon , Bacon1 , Bacon2 , Ham , Ham1
MULTI GYMNASIUM EQUIPMENT
Rubber Coupling,Fuel Retaining Pipe,Injector Nozzle,De Compressor Cable,Stoper Cable,Mounting Pad,F
LT WIRE,WELDING ROD,STEEL MILD ROUND,SAW BLADE,DUST COVER,BABY FILTER,STEARING ROD CUP COVER,MAIN F
Motherboard for Desktop (Q3)
MOSFET SR 401 of ECM Jx MK II,MOSFET 28100 of ECM Jx MK II,Antenna II of ECM Jx MK II,LED Green of 
hand held gps (Q2) ( PAC Only )
Repair and Overhauling Service - Air Conditioner-IS 1391; Voltas and LG; No; Buyer Premises
Grinding Wheel For Bench Grinder Size 150x25.91x25mm,Wire Brush Wheel For Bench Grinder Size 150x25
Mother Board,Ram,SSD,Power Supply,Monitor Stand,Power Station,Canon Printer
Enamel, Synthetic, Exterior (A) Under Coating (B) Finishing Paint (V3) Confirming to IS 2932,Alumin
Toner Cartridges / Ink Cartridges / Consumables for Printers
Puf Panel 60mm,Plywood 8x4 19mm,plywood 8x4 12mm,Paint white,Paint OG,Pand Sand,Paint Black,Paint B
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Tab Paracetamol 500 mg,Tab Levo Cetirizine 5 mg,Tab Enalapril maleate 10 mg,Tab Asprin 150 mg 75mg,
Match Box,Sago,Chicken Sausages,Ice Cream Powder,Lassi Salted,Ground Nut,Cream Fresh,Walnut without
Solar Light (S&C)
B Veh Shed
VEH RAMP
Store Shelter
flannellette rolls of  cm width
Hepatitis A Vaccine 10ml Inj,Inj Amikacin 500mg vial of 2ml,Inj Benzathine penicillin I.P. 600000 I
LAPTOP 13.6
Genr Set 62.5 KVA with Trolley
PISTON ASSY,PISTON PIN,INJECTOR ASSY,FAN BELT,HEAD GASKET
Bailing Machine,Twin Shaft Waste Shredder,OWC Organic Waste Composter,Incenerator,Push Carts,Meteri
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Female Frisk
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others
Hydraulic Pump 33 PLUS 21CC,Gasket,Filter Element,Filter Engine Oil,Hose 10 BSP HP 600mm B
BEARING CLUTCH RELEASE,MOUNTING ENGINE REAR,JOINT ASSY UNIVERSAL,HORN HIGH TONE,DISC CLUTCH,COVER A
HMG 75 IU Inj,Human Chorionic Gonadotrophin 10000 IU Inj,Human Chorionic Gonadotrophin 2000 IU Inj,
Custom Bid for Services - Hiring of Vehicle
Tab Common Cold containing Cetirizine 5 to 10 mg Paracetamol 500 mg Pseudoephedrine 30 to 60 mg,Tab
REGISTER 3 QR,REGISTER 4QR,COLOUR TAPE HALF INCH,A4 PAPER,FS PAPER,PERMANENT MARKER,WHITE BOARD MAR
AVR 7.5 KVA,FUEL PIPE BIG,BENJO BOLT,NOZZLE,FUSE
CLUTCH DISC DRIVE FRONT,DRIVEN DISC,STTERING HYD BOOSTER REP KIT,DOUBLE SAFETY VALVE,INLET HOSE FOR
Envelope,Pencil,Tape,Stapler Big,Stapler Small,Calculator,Scissors,Clip Board,Carbon Paper,Pen Stan
hand held gps (Q2)
Special Proofed Canvas / Duck as per IS 6803,Special Proofed Canvas / Duck as per IS 6803,Special P
Charge Fire Extinguisher CO2 Gas Cartridge 60 gm (Defence)
Charge Fire Extinguisher CO2 Gas Cartridge 120gm (Defence)
Cotton Newar (V2) conforming to IS 1895,Cotton Newar (V2) conforming to IS 1895,Cotton Newar (V2) c
NETWORK VIDEO SERVER WITH UPS
CCTV CAMERA WITH ACCESSORIES
DUAL BRAKE VALVE,CLUTCH SLEEVE CYL,STAND COMP MAIN,GEAR LEVER,CABLE ASSY SPEEDOMETER,ASSY COMBINATI
OIL SEAL,DOOR LOCK ASSY RH,WIPER TIMER,FAN BELT,SPRING BRAKE ACTUATOR TYPE,AIR FILTER
Amlodipine 10 mg Tab,Carvedilol 10 mg,Diltiazem CD 120 Cap or Tab,Doxophyllin 400 mg Tab,Eye Oint H
Pedestal Fan,SteelFoodContainer,Water Camper 20Ltrs,Nylon Rope 16 MM,Non stick Tawa,Water Dispenser
Commercial Steam Press for Cloth
Plastic Frames,Gypsum Screw 2.5,Waterproof Tape,Cale Tie 4,Lithium Coin Battery 3V
Location Data Device,Modular Fan Sheet 3x3,Modular Fan Sheet 4x3,Modular Fan Sheet 5x3,Modular Fan 
Simulator Remote,PVC Batten three fourths,Soldering Wire 25W,Soldering Wire 40W,PVC Getty 50x8
Feed Pump Assy NM,Pilot Bearing NM,Hose Pipe,Brake Fluid Containor,Linkage Rubber Pipe
Ordinary portland cement grade 43,Coarse sand,20 mm stone aggregates,40 mm stone aggregates,Hardcor
Nozzle,Brake Pad,Head Gasket,Harness Assy,Valve Assy,Pressure Horn Switch
FOG LAMP WITH BULB 24V 60W YELLOW LENS,COVER ELECTRONIC BLINKER GLASS RH,COVER ASSY,LIGHT FOG,PUMP 
Hexa Core iOS 18 Smart Mobile Phone,Octa Core Tablet Ultra Android 14
Liner Shoe KIT,Brake Pad,Ignition Coil,FRONT HUB BEARING,Timing Device Piston,Pressure Protection V
LV7/T-815 (HMV) 442-070-005-244 (Mtrl No 10525009) Motor Engine T3B-928-10/519
LV7/T-815 442-070-990-164 (Mtrl code 10514788) Engine T-3-930.54
13700303Z,24010508,PK0720579,10377101,82800135,140300908,4H03506000,332H7520,13153418Z,14280500900,
Mac Book , laptop
AC Filter,Fuel Pump Assy,Fuel Filter,Coil Assy Ignition,Booster with Master Cyl,Condensor Fan,Stabi
Custom Bid for Services - Outsourcing of scanning, digitization of Record of Service (RoS), creatio
Estimation of Reticulocyte count 100ml,Esbachs Reagent 125ml,Sterile urine container Pack of 100,Di
BIO-RAD Assayed chemistry control Level 2 pack of 12 x 5ml,Erba Protime LS 50 10 x 5ml,Erba Actime 
10298371,10287582,10248230,10307154,10461433
Garlic (Lassan),Onion Fresh,Potato Fresh
SUPPLY ONLY 02 X OR LIVING SHELTER (10 MEN) FEMS WITH CONSTR MATERIAL & ELECTRICAL ITEMS AT SARTHAL
Lemon Pickle 1 KG,Mix Pickle 1 KG,Mango Pickle 1 KG,Garlic Pickle 300 Gms,Ginger Pickle,Coconut Pow
Mirch Powder,Haldi Powder,Dhaniya Powder,Long Sabut,Kali Mirch Sabut,Moti Elachi,Choti Elaichi 8mm,
2 Propanol 45 gm 1 Propanol 30 gm Ethyl hexadecyl dimethyl ammonium ethyl sulphate point 2 gm with 
Water Bowser 4 KL a,Water Bowser 4 KL b,Water Bowser 4 KL for 84 Bde at Rampur c,Water Bowser 4 KL 
Dental Implant with cover screw Grade V Titanium Size Dia 3 point 0X10 point 5mm with Gingival form
CRDS Fire Resistance
Self adhesive leatherette printed having HDHMR back frame support,Design Supply and installation of
Needle file set,Ball peen hammer with handle 450 gm,Screw driver set,Spanner set double ended 6 to7
Hiring of consultancy for preparation of structural drgs for various wk at Pallanwala.
Bullet Proof Gear
Standard Storage Container or Cargo or Container Ships (V2)
Paracetamol 150mg ml 2 ml IV inj,Clobazam 5 mg Tab,Lorazepam 2 mg ml 2 ml inj,Enalapril Maleate 2.5
Rotating Light,SPG Brake Chamber Repair Kit (MSP)
Toilet Brush (V2),Squeegee Washer Wiper Mopper (V2),Toilet Cleaner Liquid (V2) conforming to IS 798
STEEL WIRE ROPE,TWELVE PIN SOCKET,SEAL PLAIN B,DEWATERING VALVE,PALM COUPLING
KIT PAD ASSY,LOWER BALL JOINT ASSY,OIL FILTER,AIR FILTER ELEMENT,ASSY FUEL FILTER THREE PIN,ASSY KI
HOSE FLEXIBLE,ASSY PIPE,WASHER,ASSY SPRING BRAKE ACTUATOR TYPE 16 56,DRIVEN PLATE FOR CLUTCH,RELEAS
INJECTOR COMPLETE
Muffler,Valve Assy,Cover Assy,Clutch Plate,Alternator Assy,Bty Cut Off Switch,Brake Shoe Complete
overhaul kit for maruti gypsy 413W
5780039835216 LIMIT SWITCH,6830 000001 GAS OXYGEN,1714 4731 760 00 797 VOLT METER,IXC KR 12 116 40 
BRAKE DISC,ASSY LINK ARB LH FRONT,CRANK ASSY,GASKET SET,ASSY OIL PUMP,RFF HLA,PISTON,RING PISTON,BE
Accelerator Cable,Clutch Cyl Assy,Sleeve Cyl Kit,Hose Pipe,Accelerator Cable,Fan Belt,Clutch Releas
Haldi,Dhania,Mirchi,Jeera,Jovitri,Kalimirchi,Clonzi,Dalchini,Choti Elachi,Baddi Elachi,Papad,Garam 
HP 2612A Laser Jet Printer Cartridge,Printer Cartridge Samsung,Epson L380 Colour Cartridge All Colo
Tab paracetamol 650 mg,Aceclofenac 100 mg Paracetamol 500 mg Tab,Common Cold Tab Cetirizine 5 10 mg
RISO CV 3230 MASTER,RISO CV 3230 INK,RISO SF 5030 EII A MASTER,RISO SF 5030 INK,A4 75 GSM JK COPIER
Toner Cartridges / Ink Cartridges / Consumables for Printers,cartridge canon 326,canon 78a,brother 
All in One PC (V2),Entry and Mid Level Desktop Computer
Chair Executive,Washing machine top load semi automatic 10 Kgs,Ice Box 60 Ltr,Crompton one and half
ARTICULATION STOP SECONDARY,BOOSTER DIAPHRAM,SHUT OF COCK,PIPE L THREE HUNDRED,PIPE L THREE HUNDRED
Semi Pro V2 Jacket Men with Name,Semi Pro V2 Trouser Men with Name,Pro Shooting Shoes with bag,Pro 
Lock washer,Rubber Hose58ID,Water Cock tab,Wheel cylinder,Delivery Pipe,Air Filter safety,Hgose dia
Electric copper wire 2.5 mm 2 core,Band 25 mm,PVC junction box 25 mm,Tie 12 inch,Tie 10 inch,PVC pi
X2/NK/000213 AVR,X2/NK/000129/EVR,X2/NK/6110-001203/EVR
MASTER CYL POWER UNIT CLUTCH MASTER CYL,FUEL FILTER CUM WATER SEPARATOR WITH W F SENSOR,ARM WIND SC
116TM51661 Gear Driver Ist,116TM03044 Gear Driver IInd,116TM03052 Gear Driver IIIrd,116TM11599 Spac
Divod,Fuel Pump Motor,Copper Washer,Regulator,Hose Pipe one by four Inch,Hose Pipe Half Inch,Hose P
WHEEL BRAKE CYL,SPARK PLUG,SET OF BRAKE DISC PATI,COPPER WASHER,COPPER WASHER,BENJO BOLT,CABLE PULY
02 KVA INVERTOR BATTERY MICROTEK
Fuel Filter,Air filter,Solenoid Switch 12 v,Field Coil 12 V,Chain Sprocket Kit,Clutch Master Cyl As
Glue Stick,Whitener,Highlighter,Paper Pin T Type,Pencil,Colour Flag,Note Stick Pad,File Cover Print
ACECLOFENAC 100 MG plus PARACETAMOL 325 MG TAB,ACEBROPHYLLIN 100MG plus ACETYCSTINE 600MG TAB,Acecl
11 point 7 HP Engine with High Head Water Pump as per relevant IS as per TS,PUF tank 500 ltr,High P
Wind Screen Glass Front with rubber,Wind Shield Glass lh and rh,Oil Filter,Diesel Filter,Oil Filter
speedo cable assy,bulb head lamp,bulb head lamp,bolt r hub,regulator r window,steering kit,fan belt
Supply and fixing of Focus light,Supply and fixing of copper wire 1.5 Sqmm,Supply and fixing copper
Item 1,Item 2,Item 3,Item 4,Item 5
CONSULTANCY FOR ARCHITECTURAL STRUCTURAL DRAWINGS AND PREPARATIO OF DETAILED ESTIMATE
Almirah Med with Shelves,Flowr Hospital Cot,Hospital Bed,Board Notice Hospital,Couch Examination wi
Haldi,Red Chilli Powder,Kasuri Methi,Dhaniya Powder,Emlee,Clove,Jeera Powder,Tej Patta,Hing,Garam M
Haldi,Red Chilli Powder,Kasuri Methi,Dhaniya Powder,Emlee,Clove,Jeera Powder,Tej Patta,Hing,Garam M
Haldi,Red Chilli Powder,Kasuri Methi,Dhaniya Powder,Emlee,Clove,Jeera Powder,Tej Patta,Hing,Garam M
236802062700,0700008035,236801012730,236804052530,340613000140,080202012800,236800010001,1006030203
Extreme Cold Weather Clothing System (HIMCLOS)
Manufacturing and supplying of structural stores for 05 Nos Cook House and Dining Hall,Wall Panels 
Manufacturing and supply of Resin Transfer Moulding Fiberglass Reinforced Plastic three Toilet Cabi
Supply of complete structural stores fixing arrangements sandwich wall panels and complete stores a
Fabrication and supply of complete structural stores for construction of OJL,Wall Panels 50mm thick
Fabrication and supplying of structural stores for ORL 20 Men of size 12000mm x 6000mm,Wall Panel c
Fabrication and supply of structural stores for Bathroom blocks of size 6078mm x 4572mm,Roofing She
Fabrication and supply of complete Structural items of FOL shed of Size 6150 X 3200 X 3000 mm using
Manufacturing and supply of Structural items of FOL shed of Size 4200 X 3200 X 3000 mm using mild S
Fabrication and supply of complete structure of Svl Tower 12 mtr including all necessary fittings f
Manufacturing and supplying of stores for RCC CP as per TS. Cement,Sand,Aggregate 20 mm,TMT Bar 8mm
LV7TMB 6350001140,LV7STLNVF X4704111,LV6MT1 20922998,LV6MT1 4730000014,LV6MT14 2640000048,LV7TMB F0
P1155SWSVLV7MB0010920401,P1155SWVLV7MB0021843601,P1155SWWP15182556D,LV7T816 9903013180,LV7T816 4436
K3/7220-000011 MATS GYMNASIA 185 CM X 185 CM
917 50600 BEARING NEEDLE ROLLER 3DX SUPER CH XXI F,333 Y0140 PIN PIVOT 3DX SUPER CH V J K M,811 800
Biomedical Waste Management Service - Collection, Lifting, Transportation, Treatment, Ways of Dispo
Purified H20 propyln wax glycrne aloemangococoa butr cetyl alc dimethicne stearic disod methyl ZO p
BEARING CONNECTING ROD,TIMING BELT,FIELD COIL ASSY,ARMATURE ASSY 24V,BRUSH GEAR ASSY,DRIVE ASSY,CHA
Tab Amlodipine 2.5mg,Bisoprolol 5 mg Tab,Levetericetam 500 mg Tab,Trimetazidine MR 35 mg Tab,Febuxo
Household Laundry Detergent Powders as per IS 4955
Cotton Yarn Waste (V2) as per IS 5485
Wind Screen Glass,Wiper Motor Assy,Rear Wiper Assy,Radiator Assembly,Window Side Beeding,Seal Water
BRAKE SHOE ASSY,ELECTRIC FAN ASSY,CHANGE OVER SWITCH,FIELD COIL ASSY,ASSY OIL FILTER,ARM ASSY KICK 
Table Flag 6 Inch x 4 Inch duly embroidered with RAJPUT Regiment Crest and Blue, Yellow and Maroon 
ORL WITH TOILET BLOCK
ROOHAFZ HAMDARD
W-10/3510-NIV, WASHING MACHINE 25 TO 30 KG
Z7/ISRAEL-9421-2300-00, Mirror Assy
Flt Controller with GPS,6s 16800mah P42A XT90 Anti Spar1300g,14 AWG wire 05 Mtr Black and Red,ZD 85
ASSY HOSE,COMBINATION SWITCH,RESERVOIR,OIL FILTER,CE BUSH,COMBINATION SWITCH,OIL SEAL,ISOLATOR SWIT
Safety Clip for Lift,Rectifier Assy Electronic,Hose for Air Cleaner,Assy Air Cleaner,Mounting Pad
Motherboard HP,Motherboard Dell,Printer head L3150,Power supply assy L 3150,Pick up roller L 3150,F
TIMING BELT,FAN BELT,TIMING TENSIONER,CLUTCH REL BRG,CLUTCH CABLE,BRG UNIVERSAL JOINT,WHEEL CYL ASS
Chock Cable,Wind shield Glass,Drive Belt,Hand brake parking lever,Projector head light blub
BLDC Motor Test Jig
M SEAL,QUICK FIX,FEVICOL,TAPE INSULATION,ANNABOND RTV SILICON SEALANT,VARISH,HEATX,TAPE ADHESIVE,AB
Entry and Mid Level Desktop Computer,Online UPS (V2),Layer 2 Access Switch (V2),Networking / Server
Repair of Body denting and welding including labour charge,Oil Filter,Fuel Filter,Gear Shifter Top 
Supertructure of Medium living shelter of size 10.66m x 6.12m x 4.40m height with 1.50m wide Verand
Supply of Living Shelter 20 Men as per specification in RFP,Supply of Electrical items for Living S
AIR PRESSURE PIPE,AIR CLEANER HOSE,CLUTCH BOOSTER,EQUILISER KIT,GEAR LEVER KIT,SPARK PLUG,AIR PRESS
Maint & cleaning of store yard of nearby area of store yard, adjancent road area at GE Engr Park Bt
Maint/Painting & preservation of Boat Assualt penumetic light weight & Accessories of ETSR store.
Disconnecting and taking out defective under ground LT cable from trenches pole pipe floor wall etc
Disconnecting and taking out defective under ground LT cable from trenches pole pipe floor wall etc
Disconnecting and taking out defective under ground LT cable from trenches pole pipe floor wall etc
Disconnecting and taking out defective under ground LT cable from trenches pole pipe floor wall etc
Power Generator - DG Set (up to 900 KVA)
S Portable,Shelter P,TEFS 2,F Outer,T Way
Cylinder Pigtail Flexible 2 Ft,Burner Pigtail Flexible 6 or 8 or 10 Ft,Copper Pigtail 2 Ft,Adopter,
Bricks Class B,OPC 43Grade 53 Grade,20mm graded Stone aggregate,40mm graded Stone aggregate,Interlo
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Non-IT Technical,Manpower Outsourcing 
2610-000019 Tyre Pneumatic 7.50
STEEL MILD SHEET H R 2500 1250 3.15MM MATERIAL,STEEL MILD SHEET C R 2500 1250 1.60MM,RUBBER SHEET 2
OUTSTATION Within State Duty Truck upto 7 to 8 Ton Capacity,OUTSTATION Within State Duty Truck upto
Goods Transport Service – Per Trip based  Service - Machinery & Equipment; Open Body LCV Truck; 1
Ignition Switch,Clutch Plate,Brake Booster Rep Kit,Resistance,Drive Assy,Battery Cut Off Switch,Pin
eye drop Lotepredenol etabonate 0.5pct bott of 5 ml,Lignocaine 1pct for intra ocular use vial of 1 
WIPER BLADE CO DRIVER,METAL MAIN BEARING STD,SPARK PLUG,HOSE DN,TURN INDICATOR,BRUSH CARRIER ASSY,S
Transparent tape 2 inch,Transparent tape 1 inch,Brown tape 2 inch,Glue stick 25 gm pack of 10,U Cli
HP Original 12A Toner,Kyocera Original TK 4109 Toner,Canon 925 starter Original Toner,Sumsang MLT D
Stapler pin large 24 6,Green Paper A4,Sketch Pen,Whitener Pen,Multi Colour Tape,Yellow Paper A4,Pen
Manpower Outsourcing Services - Fixed Remuneration - Non-IT Technical; Civil Engineer; Diploma,Manp
Rotary Switch W Wire,Rotary Pump Switch,Steering Pipe,Alternator Repair,Head Light Relay,4 Pin Rela
Goods Transport Service – Per Trip based  Service - Machinery & Equipment; Flatbed Truck; 40 to 8
BENJO UNION 7K,FAN BELT 7K,FUEL FLEXIBLE PIPE LARGE 7K,FUEL PIPE LINE RETURN 7K,RUBBER HOSE 7K,AIR 
Custom Bid for Services - NEWS SCAN
ASSAULT VESTS WITH ARMOUR PLATES
Custom Bid for Services - TOPOGRAPHICAL SURVEY OF LAND / SIDE CLEANING
Malarial antigen PFpLDH Pan pLDH detection of P vivax P falciparum and P vivax P ovale P malariae R
Entry and Mid Level Desktop Computer
Dslr / Compact / Handheld Camcorder Or Video Cameras (V2)
Vehicle mounted focus light (Q3)
Platform Cargo Aerial Delivery for AN-32 Aircraft 1508 mm x 829 mm (Fitted with Aluminium Alloy ('Z
Vitamin B complex with a minimum concentration of Vit B15mg Vit B6 3mg Vit B125mcg therapeutic Tab 
WIRE STRIPPER,E SCREW DRIVER,ALN KEY SET,NOSE PLIER,SIDE CUTTER,FLAT NOSE PLIER,TWIZZER,LEVLER,4 IN
IC DK 124,Motor 6V DC with Pump,Bty 7 point 4 V 4400 MAH,Bty 12V 700 MAH,Toggle Switch,Tubing,Senso
Cart 12 A,Cart 56 A,Cart 2309,Cart 337,HP MFPM 438DN,Brother 3608,Cart 2325,DMP Ribbon Cart1050,Car
Bent rubber Pipe,Rubber Straight Coupling,Bearing Coupling,Clutch Cover,Clutch Plate
Repair/Replacement of Flame proof E/M Fitting Fixture at Armory Bldg
Tablet with M3 Chip Processor
Laptop with M4 Chip Processor
Artemether 80 mg plus Lumefantrine 480 mg Tab,Artesunate 60 mg Inj,Beclomethasone Dipropionate 200 
Atomoxetine 10 mg Tab,Atorvastatin 20 mg Tab,Atropine Sulphate 0.6 mg 1 ml Inj,Azithromycin Dihydra
CHAIN SPROCKET KIT,CABLE COMP SPEEDOMETER,COVER R CYLINDER HEAD SIDE,HORN ASSY HIGH,ARMATURE MOTOR,
Adenosine 3 mgobiliqueml 2 ml Inj,Adrenaline Tartrate 11000 1 ml Inj,Alcoholic Hand Disinfectant Ru
Cab Tilting Oil 220 TS
16 Dihydroxy 2-5 DioxahexaneGluteraldeyde Benzylalkonium chlGluteraldeyde Benzylalkonium chl Alkyl 
Light Weight Running Shoes (V2) (MHA)
Supply of Cook House Cum Dinning Hall as per specification in RFP,Supply of Electrical items for Co
Plain Copier Paper (V3) ISI Marked to IS 14490,Plain Copier Paper (V3) ISI Marked to IS 14490
BOOTS SHORT KNEE RUBBER SIZE 8,SLIPPERS MENS RUBBER BLACK S6,SLIPPERS MENS RUBBER BLACK S9,APRON CO
ROTOR ASSY,RETURN LINE HOSE ASSY,COVER ASSY,FUEL FLAP SOLENOID,BRAKE DISC,ENG COOLING FAN ASSY,WHEE
REPAIR KIT MECH TRANSMISSION,CLUTCH CYL REP KIT,RAM SERVICE KIT,OIL SEAL,OIL SEAL,FRONT WHEEL BRG,G
Pickle , Coconut Powder , Papad
Light Weight Running Shoes (V2) (MHA)
Tactical Knee and Elbow Pad (V2)
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others,Manpower Outsourci
Clotrimazole 1percent wobiliquev IPplus Lignocaine 2percent wobiliquev IP ear drop bott of 10ml,Com
ARMATURE ASSY,FRONT WHEEL BRG,CABLE SPEEDOMETER,ENGINE MOUNTING PAD,CHAIN SPROCKET SET,SPARK PLUG,O
Laying of 2.5 M Wide Running Track (EPDM Material)
Column pipe,Column pipe both,Chlorine Tesing,Brass spidle,Sluice valve,Brass valve,spindle f dia,OT
PVC Copper Cable Single Core and Multi Core Circular Sheathed Cable with Rigid Conductor (V2) as pe
Desktop Computer,Server,Online UPS 5 KVA,24 U Rack,Switch 24 port Giga,Panel for switch with rack,P
Drop Arm Barrier (Boom Barrier) (MHA)
White LED,HT insulation,Switch socket,MCCB Amps,Cable PVC core,Socket P,Recessed LED,CI street ligh
Document Mgt Software OMR Checker,Multi language software Hindi English typing software,Microsoft W
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Instructional Material Output System for training
Mobile Iron Barricades
Cyproheptadine HCl 2 mgobilique5 ml bott of 100 ml,Dabigatran Etexilate 150mg Tab,Danazol 100 mg Ca
Paste Silicone,Metal Putty,Iron Sheet 8x4,Angle Iron 2x2.5,Angle Iron 1x1 Minutes,Square Pipe 2.5x 
Carburator Assy,Ignition Coil,Fuel Filter,Spark plug for bush cutter,Clutch Dog,Hyd Oil Filter,Oil 
Laptop Apple Macbook Air 13 inch
Dough Kneader (V1) (Q2)
Kraft Paper for Packing and Wrapping (V2) as per IS 1397
Household Laundry Detergent Powders as per IS 4955
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Security Gua
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin,Manpower Outsourcin
Etoricoxib 120 mg Tab,Extractum Cepae Heparin Sodium Allantoin gel 20 gm,Fentanyl Citrate 50 mcgobi
Charpoy with hard top FD/MAP-II/01,Chair Writing FD-280
Tactical Knee and Elbow Pad (V2)
Boot High Ankle PU Rubber Sole (Defence)
HALF ENGINE ASSY 4 VALVE MPFI
FPV Camera,Analog Video Transmitter and Antena,Battery,Analog FPV Goggles,FPV Fabrication, Build an
Tie rod end steering,Pump element,Combination switch,Intake hose,Wheel disc,Bearing ball
Levetiracetum 750 mg Tab,Levetiracetam SR 500 mg Tab,Levocarnitine 1 gm amp of 5 ml Inj,Levocarniti
Procurement for Purchase of 01 x LED TV and Zebra Blinds for WIndows
Engine Oil 15W40,Hub Grease LG 278,Brake Fluid DOT4,Throttle Spray,Grease LG 271
Electric Fan,Bush King Pin,Assy Cable Set,Nozzle,Sensor Assy Cam Position,Cold Start Pilot
Football Cup Tournament Prepration,Refreshment League Cum Knockout Matches,Refreshment Finals,Award
Amyl Alcohol bott of 1Ltr,Butyrometer lock stopper for milk test,Cell Clean 50ml Compac with Sysmex
Fevicol SR,Paint RFU Blak,Paint RFU OG,Thinner Antichill,Leather Cloth Black,Plywood for General Pu
Papad Big,Papad Small,Pickle Mango,Pickle Mix,Copra
Custom Bid for Services - 6
I Tape,C Power,Cable P,Insulation,C Vehicle,I Sleeving,B NR,B Sec,Battery L,Battery A,Battery R,B D
KM FLOAT & PAULINE ASSEMBLY
Stainless Steel Bench frame made of SS pipe 48mm,Shade frame of SS pipe 40x40mm, 16 gauge and roof 
Socks (HIMCLOS)
Manpower Outsourcing Services - Fixed Remuneration - Admin; Data Entry Operator; Graduate,Manpower 
Socks HIMCLOS
JEEP (4X4) MILITARY PATTERN MANUAL TRANSMISSION (MT)
Title1,Title2,Title3,Title4,Title5
Item 1,Item 2,Item 3,Item 4,Item 5,Item 6,Item 7,Item 8,Item 9,Item 10,Item 11,Item 12,Item 13,Item
CLUTCH PLATE ASSY,PRESSURE PLATE WITH BRG,KICK STARTER ASSY,TIMING CHAIN KIT,ROCKER,PUSH ROD KIT,BR
Computer test jig with out hard disk,Bty 12 V 130 AH Exide,AC gas nozel 5 mtrs,Earmuff safety premi
Sand for sand blasting 50 microns,Articulating Paper Thickness 20 microns,Plaster of Paris special 
SVGA Rev3 Colour OLED XL Display,Cap 400V 100UF,F 10 LC40 2733,Flash Disk 8GB,Flash Disk 8GB with C
Harpic 500 ml,Acid Bathroom Cleaner,Broom,Phenyl 5 Ltr,Wiper,Cartridge Konica Minolta TN 323,Cartri
Supply and replacement of Canopy,Labour Charge for Canopy fixing,Supply and replacement of engine o
BRAKE DISC,TRUNK LID ASSY DIGGI,BEARING DOUBLE BALL,POWER WINDOW SUB SWITCH,BRAKE SHOE ASSY,AXLE SH
Comprehensive aerial secutity surveillance system (Quadcopter) to include LRF & thermal Camera
CGI Sheet 12 Feet,Rivets,Self Screws,Washers,Iron Squre Pole 1 point 5 into 1 point 5
REPAIR OF CYLINDER HEAD ASSY,REPAIR OF SCORPIO
CLUTCH MASTER CYL,LOCK ASSY GATE SIDE LH,WINDING STARTER GENERATOR,SWITCH ASSY,REGULATOR ENGINE GEN
CLUTCH CYLINDER ASSY,BONNET LOCK,WATER PUMP,GEAR LEVER,DOOR LOCK REAR,FUEL PIPE,FIELD COIL,ARMATURE
Pinion,Wind Shield Glass LH,Piston Ring Set,Fuel Cut off Solenoid 24V,Hose Pipe DKL,Cabin Lifting P
Goods Transport Service – Per Trip based  Service - Household/Office; Closed Body LCV Truck; Load
Ung Betamethasone 0 point 64mg plus Salicylic Acid 30mg Tube of 10gm,Ung Betamethasone dipropionate
HANDLE REGULATOR,DRIVE PINION ASSY,BRUSH CARRIER ASSY,RELAY 12V,STARTER MOTOR 24 VOLT,BRAKE SHOE LI
FEED PUMP,FUSE TP 400,3 TUBE FILTER ASSY,ASSY OIL FILTER,SWITCH 24 V,REGULATOR SR 40,HOSE ASSY AIR 
MRT box 2 x 3,Hydraulic jack 10 Ton,Multimeter Fluke,Welding goggle,Soldering iron weller,De solder
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others,Manpower Outsourcing 
STUD BOLT,DRIVE ASSY,FUEL PUMP MOTOR,ASSY WHEEL CYL,TAPPER ROLLER BEARING REAR HUB OUTER,TAPPER ROL
765 84 SB253 SMOKE INJECTOR,188 60 028SB VALVE,432 40 370 GASKET,432 40 106 PACKING,GOST 8328 75 ET
PROVN OF QTY 08 x STORE SHELTER
Inj Methotrexate 15 mg 1 ml,Amoxycillin 250mg and Clavulanic acid 50mg 300 mg Inj,Inj Benzathine pe
Bulb 12 Volt Casspier,Field Coil Assy TATA,Mirror Fixing Tube Casspier,Fuel Filter LBPV,Knuckle Bus
combat BRS bladder recirculation
Raxine Black,Foam 4x6x3,GAS 134A,LT Wire,DC Wire,WD 40,Fuel Filter Assy,Oil Filter
Silencer (Muffler)
POTATO FRESH,ONION FRESH,GARLIC
4 MEN LIVING SHELTER (RE-LOC PORTA CABIN)
Lidocaine Lignocaine HCl 2 percent with Adrenaline epinephrine 1 80000 1.8 ml cartridge,Noradrenali
11 point 7 HP Engine with High Head Water Pump as per relevant IS as per TS 1,12 point 7 HP Engine 
Paper A4,Paper Legal,Photo Paper,Register 200 Pages,Register 300 Pages,Register 400 Pages,Drawing S
SMA Female to N Male,SMA Female to BNC Male,SMA Female to BNC Female,SMA Female to SMA Female,N mal
N Male Crimp RG 142,DIN Connector LMR 400,SMA Connector RG 142,BNC Connector RG 58,DIN Male to N Ma
Apron set water proof Korean American style,Knife set complete,Masala trolley,Meat mincer,Electric 
Chlorohexidine Disinfectant Mouth Wash Bott Of 500 ml,Clobetasol 0.05 percent and Gentamycin 0.1per
Rotacap LevoSalbutamol 100mcg and Ipratropium 40 mcg Bottle of 30 cap,Bethanechol 25 mg Tab,Chlordi
Amoxycillin 200mg plus Clavulanic acid 28.5mg 30 ml Bott Syp,Lignocaine 2 percent with adrenaline I
Aceclofenac 100mg Tab,Acebrophylline 100mg Tab,Acyclovir 200mg Tab,Alfuzocin 10 mg Tab,Anastrazole 
bonnet shocker,bulb head light,hose assy,oil mist separator,main fuse,timing belt,heating glow plug
GRASS FOR COOLER
Socket 5 Amp,Wall Mounting Fan with electric regulator,Wire 1.5 Sqmm,1.5 sqmm wire,15 Amp Socket,15
4 MP PTZ Camera with 36x Optical Zoom,ANRP Camera,Day Ni Camera,10 TB Hard Disc,1TB Hard Disk,32 Ch
Toggle wooden,CORDAGE Nylon 8mm dia 210mm LG,Valve Air,CORDAGE Nylon 12mm dia 10m LG,Keel assembly,
uick Dispensing Unit (Engine Operated, 3HP Pump Speed 360 rpm)
Epson L805 Ink Btls No 673 - 6 Btls,Cartridge Btls 158A,Cartridge HP 12A,Cartridge Powder,Black Ink
Clutch assy,Clutch release brg,Brake pad assy front,Road spring front main leaf,Gear lever kit,Igni
Oly Plates 28mm,Gym Belts Medium Leather,Frame Rod,Rod Racks,5mm Imported Wire 150 ft,Stainless Dum
Sleeve cyl assy TATA Sumo,Clutch cyl assy TATA Sumo,Pressure pipe line ALS,Pneumatic pipe big,Pneum
Sweeping Broom (V3),Toilet Cleaner Liquid (V2) conforming to IS 7983,Naphthalene (V2) as per IS 539
FAN BELT,ARMATURE ASSY,BRUSH CARRIER PLATE,CONNECTING ROD BEARING,SELF STARTER MOTOR
Salt acid fixing with hardner,Developer X ray films fast to make 9ltr of solution,Titanium oxide bo
352 DIA CLUTCH DISC ASSY 1 POINT 75 SPLINE,PUMP ASSY,MASTER CYL POWER UNIT OBLIQUE CLUTCH MASTER CY
Steel Donga,Spoon,M Tray,M Bowl,Iron Kadhai
Bamboo,Target paper fig 11,Tin sheet,Service book 19 pages,Combat Cloth,Tarpulin
Steel trunk,Drum,welding rod,20ft Pipe 2inch,20ft pipe 1imch,Bread Case
Custom Bid for Services - COMPREHENSIVE ANNUAL MAINTENANCE CONTRACT FOR CT SCAN
405354400122 Pneumatic Valve,2618-4010-6701 Wheel Stud,F-3573815 Lock Bolt,2590-024065 Cable Assy C
Armature Assy,Field Coil Assy,Bush Set,Water pump kit,Rep kit hand brake,Rep kit dual brake valve,W
LO CARD,CONTROLLER CARD,DRIVER CARD,ANTENNA SOCKET,BTY SOCKET MALE
X-4112800 Door Lock RH,2876-3230-07503 Assy Rubber Bushing,2519-2620-7801 Oil Seal Main Shaft,27890
GASKET CYL HEAD,SPARK PLUG,RING SET PISTON,HEAD COMP CYLINDER,SOLENOID SWITCH 12V,BUSH,DOOR MECHANI
Tools SC Metalic,Tools Standard,Scoop H,T Screw,Taps B
Upgradation of Existing AMX 310 CFF Parachute System
PROVN OF QTY 14 x ESS (5KVA SOLAR HYBRID)
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Fuel Filter for BD 80 Size II Dozer,O Ring,Ignition switch for BD 80 Size II Dozer,Oil Filter for B
Grease CIATIM-201 Defence
Grease XG-340
PD Semi Fluid Grease
Mixed Regin
Grease 60230 GR-LM-RAIL OR AFA
Camonet Synthetic fully Garnished
Donga with lid bone china,Rice Bowl with lid bone china,Rice Plate with lid bone china,Baby Spoon,R
Chilli Powder,Coriander Powder,Turmeric Powder,Cumin,Black Pepper,Chicken Masala,Sambar Masala,Cinn
13400701Z,13719501D,13169519D,KR3801402000,333Y6805,332Y2435,335Y2340,332Y6095,333Y6532,4H39902000,
LAPTOP 2025 13.6 INCH WITH M-4 CHIP
vci tablets
Inverter with Bty,Oddy A4 Size Lebel Sheet,Polynet Envelope 11 x 5 Inch,Sheet Protector,Expandable 
U/4925-000409 TRC QF MACH NO 12: EXTCT MK-I
Enamel, Synthetic, Exterior (A) Under Coating (B) Finishing Paint (V3) Confirming to IS 2932,Enamel
Pneumatic Cylinder Assy
See Saw Swing,Merry Go Round,Playground Slide,Jungle Gym,Double Swing,Spring Rider
CA 8310-000044,CA 8310-000007,CE 8405-000068,J1 8305-003920,K3 KND NIV BK 65,CC KND NIV CL1 184
Optical to Ethernet Converter,8 Port Ethernet Switch,PTZ Camera,6 Core Option Fibre,8 Port NVR with
Tablet Albedazole,Tablet multivitamin,Tablet Shelcal,Tablet Cipzox,ORS,Calcitriol Sachet,SPY Albend
GEAR BOX ASSY,CLUTCH DISC ASSY,SEALANT LIQUID GASKET,DRIVE ASSY,COVER ASSY
Automatic water dispenser for dogs
B VEH SHED
Plain Washer,Seal Valve Stem,Seat Spring,Air Filter Element Outer,Gasket Filter,Hose Plain,Fuel Sen
oil s 1004
BTE Digital Hearing Aid Model A1,BTE Digital Hearing Aid Model B1,CIC Digital Heaing Aid Model C1,C
Workshop Maintenance Cleaning Device Heavy Duty Brush Cutter Petrol Engine operated Honda UMK 450 U
VANE PUMP,TD PISTON,HYDRAULIC HEAD,SOLENOID VALVE,CROSS DISE ASSY,AC COMPRESSOR,AUTOMATIC VOLTAGE R
FOOT MATTING COMPLETE SET OF M AND M SCORPIO,SEAT BEAD OF M AND M SCORPIO,IRON ROD 10MM,WELDING ROD
Non Skid Chain (Defence) (Q3)
LV7T 815HMV 482 EG0 401 5,LV7T 815 130 940 010 174,LV7T 815 443 979 572 680,LV7T 815 207 278 305 4,
industrial vacuum cleaner (Q3)
Cement Bag 50 Kg,Mirror Big,Wash Basin,Urinal,European Latrine Seat,Panelling,Light,Wooden Planks
Wooden Scantling,Target Paper 1x1,Target Paper 4x4,Target Paper 8x8,Target tin sheet,Target paper 1
Paper A4,Paper Legal FS,Photo Paper,Register 200 Pages,Register 300 Pages,Register 400 Pages,Drawin
Video Editing software license for 3 years,Photoshop (Photoshop+ Lightroom) for 3 years,Antivirus f
Custom Bid for Services - HIRING OF VEHICLE (LDV)
CAMPLATE,VANE PUMP,HYDRAULIC HEAD,TD PISTON,CROSSED DISC,ROLLER BEAREING,ROLLER PIN,ROLLER WASHER,D
GREASE OKS 250
Ice MM 1,Ice MM 2,Ice MM 3,Ice MM 4,Ice MM 5
Bty 12V 7AH,Keyboard With Mouse,UPS 1 KVA Microtech,Printer Head Epson,Ram DDR III 4 GB,Lan Card
Ice MM 1,Ice MM 2,Ice MM 3,Ice MM 4,Ice MM 5
Antenna of 200W Jammer Ashi,Antenna cable of 200W Jammer Ashi,LM 338 of 200W Jammer Ashi,MOSFET 281
SEA 0W20
Clutch Master Cyl Rep Kit,Pipe Assy Fuel Line,Fuel Feed Pump,Wheel Cyl Rep Kit,Sleeve Clutch Releas
Firewood,Charcoal,Limequick1,Limequick2,Limequick3
Fish Fresh Ponfrat,Fish Fresh Dara,Fish Fresh Surmai,Fish Fresh Singara 1,Fish Fresh Singara 2
4 MP DOME CAMERA,4 MP BULLET CAMERA WITH ACCESSORIES
Custom Bid for Services - Preparation of detailed estimate with yard stick  for Provision of defici
X3 IXC AL 6-65 1 F 3530511 BOLT 5 16 BSF FOR STARTER RING,X3 ND 2990 000513 RING STARTER ENGINE FOR
BRAKE BOOSTER FRONT,BRAKE BOOSTER REAR,SOLENOID 24V,SOLENOID 12V,THRUST WASHER,ASSY CLUTCH MASTER C
LUB OIL FILTER ELEMENT,PIPE OVER FLEW FILTS FUEL TO TANK FUEL,DOWEL BEARING CENTRE,OIL SEAL,RING SE
Recording and Streaming of chat show in two episodes,Refreshment,Banner,Transportation,Boarding Lod
REAR HUB BEARING,FRONT HUB BEARING,DISTANCE BUSH,2 POLE ISOLATOR SWITCH,COVER ASSY,RELEASE BEARING 
Tie Rod End,Drive Lever End,Cable Assy Control,Speedo Cable,Oil Filter,Speed Sensor,Regulator Sr 40
STLN VF 2540 72 0000144 ARM WIND SCREEN WIPER SA OF WIPER ARM,LV7 TATA 2574 5420 9981 SPEEDO CABLE 
AIR FILTER ELEMENT,OIL FILTER,IGNITION WITCH,RETURN SPRING,LOCKING PLATE NUT AND BOLT
paper rim,Pen,Long Register,Glue Stick,Board Marker,Pencil,Attendance Register,Tape Roll,Uniball Pe
Mango Pickle 01 Kg,Carrot Pickle 01 Kg,Lemon Pickle 400 gm,Mix Pickle 01 Kg,Garlic Pickle 400 gm,Co
SUPPLY AND INSTALLATION OF CHINUP BAR AT TRAINING AREA
Diethyl Ether Solvent Bott of 500 ml,Ketamine HCl 50 mg per ml comma 2 ml Inj,Lignocaine HCl 2 perc
Selection of Laboratories for Testing of Products/Material - Soil; Buyer to use custom filter to in
MOTOR GRADER 1,TIPPER 4X4,WHEELED DOZER,10 TON TRUCK MOUNTED CRANE,MOTOR GRADER 2
OIL FILTER ASSY GEN SET,CLAMP GEN SET,FUEL FEED PUMP GEN SET,INJECTOR NOZZLE ASSY,FUEL PIPE GEN SET
Starter Motor,Acture Assy 6 Pin Connector,Gear Flywheel Ring,Fuel Pipe,Crank Pipe
Diluent H 360 pack of 20 ltr,LYSE H 360 pack of 3x500ml,CONTROL H 360 H N L 3x3ml,Glucose XL System
Elevated Security Post with Guard room
Repair and Overhauling Service - cars; TATA MOTORS; No; Service Provider Premises
BRAKE BOOSTER,CLUTCH PLATE STEEL,BRAKE BOOSTER,CONNECTING HOSE DIA 65 300MM,BEARING 30219A,UNIT OF 
AC Gas Filling in SML Ambulance,AC Gas Compressor Repair of SML Ambulance,AC Gas Filling in Safari 
Solution pack for electrolyte analyser Medica easylyte,Printer paper roll for electrolyte analyser,
RING,GASKET,FUSE TP 400,FUSE TP 10,HOSE,PACKING RING,SEAL RING,WASHER PACKING,HOSE 722,HOSE 725,GLA
OIL FILTER RHO,CABLE COMP CLUTCH,BOLT,ASSY MASTER CYLINDER,HOLDER ASSY RECTIFIRE,CLEANER ASSY AIR,C
GEAR SHIFT LEVER,CONNECTING SLEEVE,CONTROL VALVE,BEARING ASSY FRONT,CLEANER ASSY AIR,SWITCH 24 V,FI
CLUTCH PLATE,CYLINDER HEAD GASKET,PUSH ROD,PEDANT TYPE ELECTRIC APM,ROD ASSY STEERING DRAG
X3 IXC RH 001130453 HOSE CONNECTION AIR MAINFOLD AIR FILTER,X3 IXC RH 001600141114 LARGE END BEARIN
Carburetor Assy of 7 KVA gen set for EW Sys,Carburetor cover of 7 KVA gen set for EW Sys,Spark Plug
432 40 037 2 COLLAR,432 40 127 2 COLLAR,765 56 59 OIL SEAL,GOST 397 79 SPLIT PIN 6X12 016,172 32 30
TEP Braided Hose 1,TEP Braided Hose 2,TEP Braided Hose 3,TEP Braided Hose 4,TEP Braided Hose 5
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Food Cover Acrylic,Flask 3 Ltr,Foot Mat,ACR Form,Special BRO,Steel Name Plate Board
CCTV Dome Camera,CCTV Camera Adopter 12V,Nariyal Broom,Broom Sweeping,Phenyl,Black Hit,Dettol Hand 
CCTV Camera 2 point 4 MP Bullet,DVR 16 Channel,Power Supply 12V 10 Amp,Hard Disk 2 TB,CCTV Cable 3 
HOSE PIPE,DOOR LOCK ASSY,SPARK PLUG,KNUCKLE KIT,BULB 12V 21W,WIPER BLADE,PAD SET,OIL SEAL,PRESSURE 
Blood collection bag single with CPDA anticoagulant 49 ml for collection of 350 ml blood made up of
Side Indicator Tata Sumo Amb,Garnish Tata Safari,Cabin Light Tata Sumo Amb,Front Indicator Assy Lt 
Telmisartan 40 mg Tab,POWERHEART G5 Intellisense Adult Defibrillation Pads,Tab Calcium Acetate 667 
LABOR PAIN MANAGEMENT DEVICE,TENS DISPOSABLE ELECTRODE BOX OF 20
KIT LINNING SET WITH RIVITS,COLLANT HOSE,GEAR LEVER REPAIR KIT,VALVE CAP 12 PIECE,THERMISTER,ASSY T
443643034800 PNEUMATIC VALVE,X7448200 STEERING PUMP,2805002769 TUBE HOSE,2540 006515 DOOR MECHANISM
GASKET 175 31 226,HOSE 10MM 40U 10 1 3 13,HOSE 40U 18 13 18MM,HOSE 40U 16 13 16MM,HOSE 40U 12 13 12
CLUTCH BOOSTER,CONTROL VALVE,MAIN BRAKE VALVE,FUEL FEED PUMP,CLUTCH PLATE,VOLTAGE REGULATOR
Development of Distributed Intelligence System
Local Chemist Empanelment Service
Local Chemist Empanelment Service
Lithium Carbonate Prolonged Release 450 mg Tab,Lornoxicam 8 mg Plus Thiocolchicoside 4 mg Tab,Terbi
AIR FILTER,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELE
Samsung galaxy z fold smartphone
TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
Spectrum Analyzers and Vector Network Analyzers
Fuel Cell (For Powering Various Systems)
Door Mat,Fiber IN OUT Tray,Speaker Ahuja Aspire 208,Automatic Air Freshner spray kit,Case Roll 25 L
S550 Hexacopter Auto Pilot Drone with 2 Axis Gimbal Camera
CHDH (Cook House cum Dining Hall) Shelter
RO Water System,Kitchen Exhaust Fan,Bathroom Exhaust Fan,Ceiling Fan,Wall mounted Fan,Desert Cooler
G1 5315-000054 PINS COTTER SPLIT STEEL 2.5 MM X 20 MM,G1 5340-000891 HASPS WITH STAPLES STEEL 125MM
REVERSE LIGHT SWITCH,VALVE BRAKE PNEUMATIC,S A OF HOSE,CLAMP HOSE,ELECT FAN ASSY,SWITCH POWER WINDO
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
PT Uniform ( Sports Shorts ) - Defence
Asphalt Base for out door basketball court,Providing and fixing 8 Layer cushion KDF Material 6000 S
High End Desktop Computer,Computer Printer (V2)
G2 3439-000011 ELECTRODES WELDING STEEL HARD SURFACING,G1 5315-000077 PINS COTTER SPLIT STEEL 2.5 M
ARMATURE ASSY,RESISTANCE,PINION,CABIN GLASS,CHAIN SECONDARY,ASSY FUEL FILTER
Yarn,Gasket Rubber,Joint,Base Plate,Blow Lamp,Rod
P Glue,Rubber Joint,P Leather,S Laundry,Resin,S Liquid,E Starting,Twine S,T Europe,T Rubber,Bunting
RED CHILLI POWDER,HALDI POWDER,DHANIA POWDER,JEERA WHOLE,GARLIC,PAPAD 200 GM,VINEGAR,BESAN,SEMIYA,S
S Angles 5,Steel A 6,Angles 40x6,Angles 55x6,Steel A 65x6,Angles 65x10,Steel A 75x6,Steel A 75x10
I PVC,Lt Wire Red,Wire Navy,Cable,Cord,E Vehicl,Cable Power,Elect Cotton,Cotton Self A,Sleeve
GRADUATED HAND BRAKE VALVE,BALL BEARING,ASSEMBLY SPRING BRAKE ACTUATOR,BEARING BALL,SOLENOID,BUSH F
FLY WHEEL RING,FILTER ASSY,COLLAR ASSY,GEAR LEVER KIT,CALIPER ASSY,DOOR LOCK ASSY LH,TIMING BELT,AC
CUT OUT FUSE 10 AMP,CUT OUT FUSE 15 AMP,CUT OUT FUSE 5 AMP,BUSH,POPPET VALVE REPAIR KIT
NK017 PROCESSOR I5 12GEN,NK00009 FUSER UNIT,NK012 H510 MOTHERBD HDMI,NK000085 RAM DDR4 8GB,NK021 PR
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
PISTON ASSY,PISTON RING SET,CONNCTING ROD BRG,GASKET SET,HESD GASKET,FUEL FILTER,OIL FILTER,AIR FIL
Title1,Title2,Title3,Title4,Title5
BETHANECHOL 25 MG TAB,INDOMETHACIN 25 MG CAP,HYDROCORTISONE 5 MG TAB,SEVELAMER 800 MG TAB,ALFUZOSIN
Computersied Universal Vibration Apparatus.,Single Phase Vapor Absorption Refrigeration Test Rig,Up
NK001265 MS SHEET,2530 001724 PIPE,NK003215 BACK PLATE BOLT,NK003216 SLACK ADJUSTER BOLT,NK003091 P
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Job No CC/3121 Provision Of Office Complex & Store Room for One Battalion and Addition/Alteration C
Television (TV) (V2) (Q2)
Matting Complete suitable for Eritiga Light Vehicle,Stearing Cover suitable for Eritiga Light Vehic
Book1,Book2,Book3,Book4,Book5,Book6,Book7,Cloth,Card
INSTALLATION OF COMPREHENSIVE ACCESS CONTROL SYSTEM
Integrated Slithering Platform
Cam shaft position sensor,Visco clutch assy with fan,Poly v belt,Gear shifting cable,Clutch master 
Field Coil,352 Dia Clutch Cover Assy,Armature Assy,Clutch Release Brg,Clutch Master Cyl Assy,Tfr Ca
COMBAT WEAPONS TRAINING SIMULATOR
Echo Cardiography Scanning Machine (V2)
Solar Security Lights
FRONT WIND GLASS,RADAITOR ASSY,NOZZLE,ASSY HOSE,HAZARD SWITCH
Z7/BEL-1700-002-950-17, Control Box Assembly,Z7/ISRAEL-6406-4500-00, AC Adaptor Digital
Thiocolchiside 4 mg Tab,Tramadol Hcl 50 Mg Cap or Tab,Inj Adrenaline 1 is to 1000 1 Ml,Cyproheptadi
Timer Relay,Master Switch Assy,IGB Shaft Coupling Assy,Fork,Dearation Tank,Filter,Cover Plate,Sendi
Juicer mixer grinder,Rope,Volley ball net,Table cloth blazer,Kero heater PS22G
P Glass,Paper G 30,A P Glass,P Emery,A P Emery,Emery Grit,HD Ultra,Corundum Grit,Paper Grit,Bright 
Processing Station for EW Shelter,Low Cost Receiver,SMA RG58 Crimp,BNC M RG 58 Crimp,TNC M RG 58 Cr
Steel Angles 45x45x6 mm
Camera,NVR,TV,HDD,PC,Cable,Rack,Switch,OTE,OFC,Connector,Junction Box,UPS,Power Cable,Installation
Servicing of Toyota Hilex Vehicle
PS-4 Extreme Duty 10W50-4 Cycle Oil
Steel Angles 40x40x5 mm
Steel Angles 45x45x5 mm
BUSH KING PIN,MAJOR KIT CLUTCH MASTER CYL,FEED PUMP PLUNGER BLUE,DRIVE ASSY,ARMATURE ASSY,ASSY TAND
Paracetamol,Combiflam,Levocetrizine,Avil,Chymoral Forte,Cipzox,Chest N Cold,Pantoprazole,Promethazi
SPEEDO CABLE JIS 4300 LG,ASSY BRAKE SHOE WITH LINING R,OIL FILTER,FILTER FUEL,OIL FILTER CARTRIDGE,
LV7 TMB 2573-5450-9916 FUSE LINK,LV7 ZIL 131-3901259 TYRE PRESSURE GAUGE WITH CASE,Tool Kit CVD-301
Mortin Rat cake,Scotch Brite Antibacterial Scrub Pad,Broom soft Phool Jhadu,Acid for Toilet,Wiper f
INTAKE VALVE SEAL STANDARD,WINDOW DROPPER,3 TUBE FILTER ASSY,CABLE,BOLT,BUSH,ASSY CLUTCH MATER CYL,
GelForRootCanaL,PostExtrationDressing,PulpDevitaliserNonArsenic,AbrasiveMouDiamFG801018,AbrasiveMou
Glysantin G 48,MIL PRF 10924,MIL PRF 32033,MIL PRF 372,MIL PRF 16173,GH 32 GEAR OIL GHE 632,Oil OX 
Ketamine HCl 50 mg per ml of 2 ml Inj,Thiopentone Inj of 0 point 5 g without water for Injection,Bu
AC FAN ASSY,4X4 CABLE,WIPER,KILOMETER GEAR,HEAD GASKET,MUFFLER ASSY,EXHAUST PIPE,MUFFLER CLAMP,WIPE
REGULATOR SR 40,SWITCH 24V,VOLT METER D60,CUT OUT FUSE 10 AMP,CUT OUT FUSE 15 AMP,CUT OUT FUSE 5 AM
G1 5310-001379 WASHERS PLAIN STEEL ZINC PLATED 16MM OD,G1 5315-000094 PINS COTTER SPLIT STEEL 5.0 M
G1 5315-000147 PINS COTTER SPLIT STEEL 2 MM X 50 MM,G1 5315-000186 PINS COTTER SPLIT STEEL 5.5 MM X
ASSY RADIATOR COMPLETE,PISTON RING SET ENG GB-60,OIL SEAL GEAR BOX HAUSING COVER,CONNECTING ROD BRG
Bus above 35 Seater Non AC local duties Garhi, Udhampur military stations for 80 km or 08 hr hill,B
Motorola with power supply 0 db antenna and 30 meters co axial cable,0 db gp antenna and 30 meters 
Z7/R90-5342-000067 ( AL7.150. 10) ACTIVE LASER ROD
Z3-MISC-FC-5720-050-356-10 KIT G PAINT AND HARDNER PU HS LG-SGL
1.5P Active LED Datawall 7.34 feet x 7.34 feet,Wall Mounting Frame for LED Datawall,Video Processor
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Tool Kit CVD-130973530124 NAVTAL LOCK 40mm-5 LEVERS WITH KEYS,Tool Kit CVD-F-4735900 Grease Gun,Too
Fuel Filter,Oil Filter,Fuel Cut Off Switch,3 Pin Shocked,Spark Plug,Fuel Pipe,Ignition Switch,Wheel
Provn of Cook House Dinning Hall Shelter Parts Only FOR TAKSING,Provn of Constr mtrl for Cook House
352 DIA CLUTCH COVER ASSY,FLY WHEEL ASSY,ASSY PRESSURE PLATE O M 330 DIA,AIR PRESSURE PIPE,CARBURAT
Fentanyl Citrate 50mcg ,ml, 2 ml Inj,Fentanyl 50mcg ,ml,10 ml Inj,Pethedine 50 mg, 1 ml Inj,Tramado
Cap Rifaximin 550 mg,Cap Tamsulosin HCl 0.4mg,Cap Vitamin E ,Evion, 200mg,COMPRESSION STOCKING BELO
Oil Aeroshell Fluid 5M or Nycolube 3525
SEWING COTTON THREAD,RIGID SHEET,AC GAS R134A,FEVICOLSR 998,LEATHER CLOTH GREEN,FUEL PIPE FUEL FILT
K6 3510-000088 Washing Machine Fully Automatic
LV6-MT6 12761M70C20 BELT TIMING MPFI,LV6 MT2 4910-000003 GAUGE TYRE PRESSURE MASTER TYPE 70KPA TO,L
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8
Title1,Title2,Title3,Title4,Title5
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Turbocharger Repair kit,Laminated Passenger Door glass,Coolant pipe Hose,Air Dryer Assy,Magnetic va
TENSIONER ASSEMBLY,BRAKE PAD SET,LATCH ASSEMBLY FRONT DOOR RH,LATCH ASSEMBLY FONT DOOR LH,WINDOW RE
Brake pad front,Brake pad rear,Suspension bush kit,Spider bearing,Pressure plate,Release bearing,Fr
Basin,Opener,Rug Horse,Tray Steel,T Soap
G1 5315-000664 NAILS STEEL WIRE ROUND 100 MM X 5.0 MM,G1 5315-000662 NAILS STEEL WIRE ROUND 75 MM X
11345,11320,NIV 01,12238,NIV01,11017,11176,120007,120008
Supply of 12 point 7mm 1 oblic 2 inch Bihexagonal Square Driver socket make Taparia size of as per 
Teak Plywood Sheet,Balli,Nails,Fevicol,Screw,Roof Treatment
Tab Aceclofenac 100 mg,Acebrophylline 100 mg Cap,Tab Acenocoumarol 1 mg ACITROM,Tab Nicoumolone 4 m
hand held gps (Q2)
FP, BODY FLUID CONTROL Part No - 628030,FP, 6C PLUS CELL CONTROL Part No - C07297
LEATHER CLOTH PVC BLACK,FEVICOL SR 998,SHEET CELLULAR,NUT AND BOLT NO 12,NUT AND BOLT NO 14,BENJO B
Clutch Plate,Plate Clutch,ASSY CLUTCH DISC PRESSURE PLATE,ASSY DRIVE SHAFT,Brake shoue,Brake pad,Sl
Wire Cooper Soft Gen Purpose,Paint RFU Black,Paint RFU Syn Red,Anabond,Air Cleaner Hose,Brush Carbo
Cllutch Rel bearing,Armature Assy,Field Coil Assy,Brush Carrier Assy,Hose Pipe,Rubber Hose,Oil Seal
FIELD COIL ASSY,BRUSH CARRIER PLATE,BULB 12V 55W,WIPER BLADE,AIR FILTER ASSY,OIL FILTER ASSY,IGNITI
BALL JOINT KIT SET,BUSHING KIT SET,BUS STABILIZER,RUBBER BUFFER,LINK ROD,ASSY RUBBER BUSHING,RUBBER
Fan Belt,V Belt,Wheel Bearing,Bearing TX,Fuel Pipe Flexible,Fuel Pipe,Coupling Disc,Guage Oil Press
Z1-4920-72-052-5944, Communication Interface Unit (CIU MK II)
Fuel Flexible Pipe,GuageOil Pressure,Assy Fuel Pressure,Fan Belt,Oil Pressure Pipe,Socket Female 26
BRUSHES FLAT PAINT 50 MM TAPERED NYLON M,BRUSHES PAINTS AND VARNISHES FLAT 100 MM,BRUSHES PAINTS AN
M Set,Nail S,Degchie,N Steel 15,Nails S 70
COVER ASSY CLUTCH DIA 260,BEARING ASSY END,ASSY CLUTCH DISC,TIMING BELT,ASSY FUEL FILTER,OIL SEAL,A
Shirts Man's Angola Drab Polywool Modified Pattern 2012
ASSY COMBINATION SWITCH,PLATE SHACKLE INNER,PLATE SHACKLE OUTER,SIREN HORN 12V,FIELD COIL ASSY,ARMA
Boom Cylinder Seal Kit,Ignition Switch,TFR Gear Box Change Over Switch,Pressure Hose,Bearing,S A Ho
AC COMPRESSOR,HOSE,HOSE COOLANT TUBE TO PIPE,DOOR LOCK,ASSY RUBBER BUSHING,RUBBER HOSE UC PIPE
Suji for Defence,Dalia for Defence,Refined Wheat Flour (Maida) (V2) (Defence),Whole Wheat Flour (At
PROCESSOR I7 12TH GEN,MOTHER BOARD I7 12TH GEN,UPS 1KVA,HP WIREDKEYBOARD AND MOUSE,HP WIRELESS KEYB
Repair and Overhauling Service - cars; TATA MOTORS--TATA MOTORS PASSENGER VEHICLES LIMITED; Yes; Bu
Desert Air Cooler
Digital Hearing Aid Model A,Digital Hearing Aid Model B,Digital Hearing Aid Model C,Digital Hearing
Split AC,Stabilizer,AC Stand,Air Cooler,PAD Lock,Bucket Plastic,Mug Plastic,Hot Case Tiffin,Water C
CLUTCH SLAVE CYLINDER,ASSY SPRING BRAKE ACTUATOR,SPRING BRAKE ACTUATOR LH,REPAIR KIT MASTER CYLINDE
Wiper Blade Rear,Wiper Blade Co Dvr,Wiper Blade Dvr,Assy Tail gate gas Balancer,Muffler assy,Bezel 
PRESSURE PLATE ASSY,ASSY CLUTCH DISC PRESSURE PLATE,RELEASE BEARING ASSY,CLUTCH PLATE,CLUTCH BOOSTE
HY DUTY DENT REMOVAL KIT
Bearing,Bolt Wheel Stud,Gasket Cylinder Head,Bearing Assy Front,Hose Stearing Pump to Gear,Assy Fue
Tab Glimepride 0.5 mg,Tab Hydralazine 25 mg,Tab Aspirin 325 mg,Tab Albendazole 400 mg,Tab Azathiopr
Wheat Atta Whole Meal,Flour (Maida),Suji,Dalia
CALCIUM HYPOCHLORITE
Nintedanib 100 mg Soft gelatin cap,Tab Acarbose 25 mg,Tab Telmisartan 20 mg,Carvedilol 6 point 25 m
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
D IFA22 Caffeine Citrate 20 mgml Inj 1ml vial,D IFA22 Salmeterol 25 mcg plus Fluticasone 125 mg MDI
Mirchi Powder,Dhania Powder,Haldi Powder,Sambar Masala,Garam Masala,Meat Masala,Chiken Masala,Birya
Quadcopter Drones,Smart Remote controller,battery,Fast charging Bty Hub,Carry case with spares,Trai
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Paper JK Legal,File Cover Plain Coloured,File Cover White Plain,Epson Ink 003 Black,Glue Stick,Reyn
Pin Pivot,Bolt M-10x90mm,Nut Lock M-10,Mounting Rubber,Disc,Seal Oil,Lock,Rear Bearing Cap Oil,Iner
A4 PAPER,FS PAPER,TAG BIG,BINDER CLIPS BIG,U CLIP STEEL,FLAG 3 COLOUR,CORRECTION FLUID PEN,BOND PAP
ASSY OIL FILTER,ASSY FUEL FILTER,SPIDER BEARING,AIR FILTER BEARING,BEARING,SPACER REAR SHAFT,OIL FI
Banner and hoarding,Caps,mementos,Medals,Incentives to the participants,Photography and video cover
Banner and hoarding,Meals and other refreshments,Lodging during expedition,Photography and video co
Preservation Fluid MIL PRF 6081D GDE 1010/AIR 3516A
Oil Hydraulic PX- 26, Severe Duty, Low Temperature (For breech opening and loading tray operation a
Complete servicing Rakshak plus Maximile FEO 6 L maximile synchro UV 2 l transmission oil kit shock
LV7 STLN P-3710845 BRUSH BOX ASSY,LV7 STLN P-3711145 MAIN TERMINAL SOL,LV7 STLN F-2241600 LOW OIL P
DISPLAY PANEL FOR MILLET TRG SESSION 1 TO 4
Rotary switch of RS Stars V MK II,Filter assembly 6 pin socket of RS Stars V MK II,IC Voltage regul
Wheel bearing rear inner for Rakshak Plus,Wheel bearing rear outer for Rakshak Plus,Rear wheel oil 
8010 000110 PAINT RED OXIDE,8010 007496 PAINT BROWN,8010 007495 PAINT GREEN,8010 007492 PAINT RED S
LV7 STLN F3565215 FRONT HUB NUT LOCK,LV7 STLN P-3701607 JUMP RING PINION,LV7 STLN 2520-72-0473327 S
CARBONATED SOFT DRINKS,Lime Based Soft Drinks
Lub oil temp guage,Lub oil pressure guage,Pannel lamp,Relief valve assy,Inertia brake assy,Hours me
Synthetic Gear Oil 75W85
SLIDING GLASS MG,SIDE GLASS FRAME,DOOR BEEDING REAR,COOLANT HOSE,STEERING OIL BOTTLE,RELAY 24V,OUTE
Metformin 500mg plus Myo-inositol 600mg Tab,Dienogest 2 mg Tab,Clindamycin 100mg plus Clotrimazole 
Z6-ARJ-100130 Fuel Drain Plug Mtrl No 10587597,X3-IXC-MBT ARJUN-100327-V2 O Ring Mtrl No 10594994,Z
ncolssypparacetamolcetirizinephenylphrinehclbottof60ml,ibuprofenplusparacetamolsypbottof60ml,oralul
Mob Airborne Security Apparatus,Battery for Mob Airborne Security Apparatus,Charger for Mob Airborn
Track Chain Nut and Bolt,O ring Box,Hyd Tank Cap,Oil Filter,80 Gear Box Lever Kit,80 Solenoid Switc
REPAIR oblic WORK IS REQUIRED FOR FLT 5 TON SL NO 171072 AT DET EP 1125 FMA JAISALMER,M and L for p
dak folder,wall clock ajanta,dust bin,paper weight,attendance register,good knight rfill with machi
Dental Implant 4 x 11.5 mm,Dental Implant 4.5 x 12 mm,Dental Implant 3.8 x 12 mm,Abutment,Cover scr
Hiring of Excavator 1,Hiring of Excavator 2,Hiring of Excavator 3,Hiring of Excavator 4,Hiring of E
Entecavir 0.5mg Tab,Duloxetine 20 mg Tab,Amisulpride 100 mg,Trimetazidine 35mg MR Tab,Dienogest 2 m
Cornflakes,Custard Powder,Corn flour,Jelly,Otomeal,Horlicks,Raisin Brown,Biscuit,Chocolate,Sago,Lac
Holographic Sight for AK-47
Molygraph Silicon
Potato , Onion , Garlic
Teak Plywood Sheet,Balli,Nails,Fevicol,Screw,Roof Treatment
AIRWAVE OSCILLOMETRY SYSTEM
FAN BELT,SHAFT ASSY PROPELLER NO 1,CHANGE OVER SWITCH,STEERING LOCK,COMMANDER LIGHT ASSY
REPAIR oblic WORK IS REQUIRED FOR FLT 3 TON SL NO 30153 AT GE EP JODHPUR,Parts of vehicle to be rep
SUPPLY OF 01 X LIVING SHELTER (30 MEN) WITH 01 X BATH ROOM (4 C) & 01 X FIELD FLUSH LATRIN
Brake Counter Plate,Brake Friction Plate,Ignition Switch,Oil Filter,Filter Element,Air Filter,Relay
LV7TMB 265429100156,LV7TMB 207829100120,LV7TMB 257329100161,LV7TMB 26258081,LV7STLN F8262500,LV7TMB
Fuser Unit,Maintance Box,Logic Card,Mother Board,Internal DVD Writer,UPS Bty 12V 7.2 AH,Monitor 19 
Isreali Bandage,Axiostate,MOH50 Colour,HP 4E75AA Printer Head,Cartidge,Insulation Tape Large Black,
PUMP ASSY OIL,REGULATOR WINDOW RH,SEAL FRONT OIL 32X47X6,GEAR LEAVER KIT 2.5 TON,ASSY CLUTCH PLATE 
Bearing ball,Roller Brg,Joint Kit,Oil filter,Feed pump,Injector,NRD Valve,Pump Element,Fuel Filter
CLOVE,CORIANDER POWDER,CARDAMOM,CUMIN SEED,RED CHILLI POWDER,MUSTARD,TURMERIC POWDER,TAMARIND,BLACK
Element Air Main,Shim 1.4mm,Seal Pivot Pin,Shim 120 x 60.5x 1.4 Thick,Nipple Grease,Nipple Grease,S
Custom Bid for Services - 1
SUPPLY ONLY 01 X CRDS OR LIVING SHELTER WITH SOLAR PANEL (4 MEN) COLLAPSIBLE & RELOC
LV7 T-815 443-927-113-841 CARBON BRUSH,LV7 T-815 DMD-NK-3080 RESISTANCE OF 18 OHMS 1-2W,LV7 T-815 4
Provn of ESS Genr Set 5 KVA Mini Solar FOR NAB,Provn of ESS Genr Set 5 KVA Mini Solar FOR MAYUM,Pro
OEM Spares for Automobiles (Q2)
Fingerprint and RF Card based Time Attendance and Access Control Solutions,Licence,Lock,Exit Switch
Lamp Assy Combination RH,Lamp Assy Combination LH,Clutch Master Cyl,Solenoid Valve for Diff Lock,Sp
Fuse Box 6 way,Gasket gear cover,Gasket valve cover,Feed Pump 50,Washer spring,Gear Box Seal 50,Bre
50 366 33 STEEL WIRE,4730 000914 M 913602 CONNECTOR 5 8,5420 000270 SUSPENSION PAD SMALL,M 800450 A
Provn of Store Shelter for Shelter parts FOR ALONG,Provn of Store Shelter for Shelter parts FOR GEL
Enalapril Maleate,Verapamil,Tab Nicorandil,Desensitising Paste,Adapalene,Oint Benzyl Peroxide,Calam
Gr Long Life PD 00 OPTIMOL
OEM Spares for Automobiles (Q2)
5 MP Day and Night Full HD IP PTZ Camera with IR Range 100 Mtr,5 MP Day and Night Full HD IP Bullet
PRESERVATION FLUID (AEROSHELL FLUID 2F MIL C6529C TYPE II AIR 1503 B
Glysantin G-48/ Castrol Redicool NF/ AL 001061/01 E Coolant (Anti Freeze) Tk-6-03-010/2 (Proprietar
Oil OM-58
Banana,Mango,Papaya,Mussambies,Pineapple
Base Station
BRAKE SHOE FRONT,LOWER ARM ASSEMBLY,TORSION BAR BRACKET,CLUTCH PLATE,PRESSURE PLATE,UPPER ARM BALL 
Oil OM-16
Grease LG-320
BEARING,CABLE PARKING BRAKE NO 02,CABLE PARKING BRAKE NO 01,CROSS ASSY,PIPE BRAKE NO 08,PIPE BRAKE 
Gate wall 15 mm,Door locking in out clamping set,Binding wire,MCB 32 AMP,Board switch 6 AMP,Socket 
Repair of 1 KVA UPS,Repair of HP Laserjet printer,Repair and servicing of Epson M100,Repair and ser
IGNITION COIL,ARMATURE ASSY,FEED PUMP ASSY,CLUTCH MASTER ASSY,CROSS ASSY YOKE,ASSY VACCUM HOSE FOR 
Earth works,Concrete works,Acrylic synthetic surface and concrete base,Fiber glass board with poles
GR S2 V2202 1,GR S2 V2202 2,GR S2 V2202 3,GR S2 V2202 4,GR S2 V2202 5
WHITE BREAD,WHEATMEAL BREAD,ICE MM
The Future is Faster than you Think,Disrupt or get Disrupted,Wired for War,Super intelligent,Chip W
The Drone Age,50 Battles That Changed The World,The Art of Military Innovation,Professional Militar
Mathematical Modelling Software
011253 Chlorhexidine mouth wash with 0.12 percent sugar, alcohol free, bottle of 450-500 ml in ambe
FUEL FILTER ELEMENT,TRANSMISSION OIL FILTER,OIL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
NIGHT ENABLED QUADCOPTER
Night vision weapon sight (Thermal) / Weapon mounted thermal system as per MHA QRs
NIV 17 Erba Elite 580 Diluent Pkt of 20 ltr for Fully Automatic 5 Part Hematology Analyser,NIV 17 E
PROTECTIVE WK (SUPPLY AND CONSTRUCTION)
NK XGA SWITCHER 4 PORT,NK000054A UNSTRUPTED POWER S 1KVA,NK00006 BTY 12V 7AH,NK000052 KEYBD WITH MO
H3 5530 400082 PLYWOOD GEN PURPOSE,H1 8040 000147 FEVICOL,G2 3439 000149 ELECTRO WELDING ROD,G2 951
Wiper Arm,Suspension Bush Set,Feed Pump,Bty Cut Off Switch,Disc Pad
HOSE COOLANT,FRONT WIND SHIELD GLASS,CLUTCH PLATE,HAND BRAKE CABLE,TAPPER ROLLER BEARING
Chilly as per IS 2322,Spices and Condiments - Turmeric Whole and Ground (V2) as per IS 3576,Spices 
High Pressure Portable Pump for large fire fighting as per IS 12717
Video Sureveillance System in Defence Area
FUEL PUMP ASSY,WHEEL BEARING FRONT,CYL HEAD GASKET,UNIVERSAL JOIN T,CLUTCH PLATE,RELEASE BEARING,OI
Water Pump Assy,Starter Motor,Bty Cutoff Switch,Ram Hydraulic Ram Assy,Clutch Release Bearing,2 Pol
Hose Pipe,Magnetic Switch,Safety Thermo Switch,Armature Assy,Combination Switch 24V,Fuel Water Sepr
Repair Kit Air Dryer,W S Wind Screen Glass,Master Cyl Rep Kit Assy,High Pressure Pipe,Repair Kit fo
Sleeve Cyl Assy,Air Dryer Assy,Pressure Plate,4 X4 Cable,Clutch Master Cyl Assy
Impact Switches,PVC Elbow,PVC Tee,PVC Coupling,PVC Bend
Hooter Assy,Rotary Packing kit,Sleeve Cyl Assy,Clutch Cyl Assy,Cclutch Cyl,Radiator hose,Self Sarte
Wheel Cyl Front,Clutch Cyl Assy,Steering Filter,Pressure Plate,Relay Sarting 24V,Loading Relay
Brake Pad Front,Driven Disc,Field Coil Assy 24V,Brush Carrier Plate,Solenoid Switch,Field Coil Assy
Trail Camera,Solar Panel,Mounting Bracket,Antenna Type,Thermal Imaging Camera
Flag,Tarpauline,Mirror,Light,Wire,Blub,CFL,Grass Cutting Machine
ASSEMBLY INJECTOR,FUEL FILTER,KIT PAD ASSEMBLY FRONT,FRONT DOOR LOCK ASSEMBLY,ALTERNATOR BELT
Emergency lighting and accessories  (PORTABLE EMERGENCY LIGHTING SYSTEM  Tower type  With AC Genset
12 Core Joint Enclosure,12 Core Optical Fibre Cable
PISTON ASSY,PISTON RING SET,COOLANT HOSE,FUEL PIPE 19x19,SLEEVE,BIG END BRG CELL,AIR FILTER,PUSH RO
ARMATURE ASSY 12V,FIELD COIL ASSY 12V,PINION ASSY,SUSPENSION BUSH LINK UPPER,SUSPENSION BUSH LINK L
High End Desktop Computer Type 1,High End Desktop Computer Type 2,1 KVA UPS,5 KVA UPS,Computer Work
Gas Refill and Service of Window AC,Distilled Water 10 Ltr Pack,Raxine Black,Leather File Folders,T
OIL FILTER,CRANK SHAFT SEAL,BEARING,HEAD GASKET SET,JOINT ASSY UNIVERSAL,COIL ASSY IGNITION,TAIL LI
Patient Transfer and OR Table super Absorbent sheet having capacity up to 150 kg size 210 x 80 cmEu
RISPERIDONE 2 MG TAB,SOLIFENACIN 5 MG TAB,MIRABEGRON 50 MG TAB,MIRABEGRON ER 25MG TAB CAP,Spironola
Wiper Motor,Motorised Head Lamp LH,Assy 228 Dia Driven Plate,Assy 228 Dia Clutch,Pad Assy,Assy Filt
Lamy Pen,Lamy Pen Ink,Tactical Gloves,Ivory Sheet,Soluble Marker Pen
Lime,Terracotta,White Paint,Black Paint,OG Paint,Red Paint,Blue Paint,Brown Paint,Turpentine Oil,Pa
EXL LOCI B12 Vitamin B12 kit of 80 tests,Fully Utomated LDL Cholesterol Kit of 120 Tests,Lactate De
ISOLATOR SWITCH,SA HOSE TANK PUMP,OIL FILTER,ASSY CLUTCH MASTER CYL,ASSY PULL CABLE,STARTOR MOTOR,C
Sliding Glass,Laminated Passenger Door Glass,Assy Radiator Pipe with Hose,Pipe TC to IC,Shock Absor
Apple iPhone 16 Pro 512 GB,Apple iPad Pro 11 Inch (M4) 256 GB with Pro Pencil,Apple Mac Book Air 15
Haldi Powder,Mirchi Powder,Dhaniya Powder,Hing,Sabut Jeera,Black Piper,Mutton Masala,Kastoori Maith
BRAKE SHOE ASSY LSV,BRAKE PAD LSV,WIPER BLADE ALS,WIPER BLADE LSV,WIPER LINKAGE TATA,SPRINKLE MOTOR
Z3-LV7-FC-WT-BEL-3845-104-001-6 SELECTION VALVE SET
Digital programmable hearing aid BTE (mild, moderate, Severe hearing loss),Digital programmable hea
Injection Pump PV 12A 9K 9171-1591
WATER SEPRATOR FILTER ELEMENT,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,OIL FILTER ELEMENT,AIR FI
FUEL FILTER,OIL FILTER ELEMENT,ZINC ANODE 1,ZINC ANODE,IMPELLER WATER PUMP
Provn of Security Post Shelter part only FOR MANIGONG,Provn of Security Post Shelter part only FOR 
FUEL FILTER,OIL FILTER ELEMENT,ZINC ANODE 1,ZINC ANODE,IMPELLER WATER PUMP
BA NO 22A-076142P MOTOR CYCLE HERO HF,MOTOR CYCLE HERO HF,MOTOR,CYCLE,HERO,HF,Vech,Moter,Vech,HF
FAN ASSY DC 24V,CAM CHAIN KIT,WHEEL NUT,REGULATOR 24V,WIND SCREEN GLASS FRONT,WIND SCREEN BEEDING F
FD WATER STORAGE TANK 5000 LTR
Thermal Imager Based Night Sight
Auto CPAP Machine with Humidifier
LV7-TATA 2154-8910-6302 Mudguard RH,LV7-TATA 264143700163 Drying and Distri Unit HI PR Voss,LV7-TAT
Crot Set
Conscious Sedation System based on Nitrous Oxide inhalation
50 Pair 0.5mm Unarmd UG cable 2800 mtr AMC for one year,20 Pair 0.5mm Unarmd UG cable 3600 mtr AMC 
SAE AS 8660 (Old No MIL-S-8660)
ASSY STG PIPE BSIII,POWER STG PIPE BSIII,KING PIN BSII,INPUT SHAFT OIL SEAL BSIII,AIR FILTER ELEMEN
BOF-5056653 COUPLING,BOF-6118160 O RING,BOF-N9-8-115X125 O RING,BOF-N9-8-30X35 O RING,BOF-N9-8-55X6
TEFLON,PRESSURE ROLLER,LASER UNIT,INK PUMP ASSEMBLE WITH HEAD CABLE,POWER SUPPLY CARD,WIRED KEYBOAR
Aceclofenac 100 mg Paracetamol 500 mg Tab,Common Cold Tab sinarest,Naproxen 250mg Tab,Etoricoxib 12
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Construction of Synthetic Surface Basketball Court with Fiber Glass bds, Light Poles, Poles and All
Proc of Physiotherapy Chair
WATER HOSE PIPE,AC COMPRESSOR,AC CONDENSOR,AC BELT,ASSEMBLY RECEIVER DRIVER,ASSEMBLY WATER VALVE,BL
Automatic voltage regulator,Charger bty input,Pannel printed circuit board assy,rectifier assy comp
SIRON 24V,BEARING ASSEMBLY FRONT,OIL FILTER ELEMENT,OIL SEAL DRIVE SHAFT,ASSEMBLY TUBE FRONT SIDE
LV7 TATA 2754-4660-0102 STEERING PUMP,LV7 STLN 8030-001186 SEALING COMPOUND ANABOND 673,LV7 STLN VF
G1 5310-003203 WASHERS SPRING DOUBLE COIL STEEL NOMINAL,G1 5310-001417 WASHERS SPRI SING COIL TYPE 
Armature Assy,Field Coil,Brush Holder,Brake Pad,Tantam Master Cylinder,Rear Break Shoe,Coil Assy Ig
AC FAN WITH CONDENSOR,THERMO EXPANSION VALVE,TUBE LIQUID PIPE,ASSEMBLY DISCHARGE HOSE,PU FOAM SEALI
ASSEMBLY BALL JOINT FOR RH,ASSEMBLY BALL JOINT FOR LH,COVER PUSH ROD,HOSE ASSEMBLY AIR FILTER OUTLE
COVER ASSY CLUTCH,DISC CLUTCH,ASSY OIL FILTER,FUEL PRE FILTER ASSY 2 PIN CONNECTOR,ASSY FUEL FILTER
Jelly,Sago,Cornflour,Vermicelli,Chocolate,Custard Powder,Tomato Sauce,Pickle,Orange Squash,Vinegar,
protable laser power & energy meter with detector
Title1,Title2,Title3,Title4,Title5
Z1/5985-012218, Base Antenna Support Assembly Stars-V
Brake Pad Front of Toyota Hilex Vehicle
Atta , Suji , Maida , Dalia , Bran
Antifreeze Additive Eng Oil 1,Antifreeze Additive Eng Oil 2,Antifreeze Additive Eng Oil 3,Antifreez
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
LV7 STLN VF B 5426506 SUB ASSY OF HEAD LAMP AND FDI,LV7 STLN F 7474000 4310-003690 AIR COMPRESSOR,L
Short Term Cab & Taxi Hiring Services - Sedan; Local; 40Kms x 5Hrs,Short Term Cab & Taxi Hiring Ser
LV7-STLN 6220-72-0473323 Head Light Assy High Beam,LV7-STLN 2940-72-0471246 Assy Oil Filter,LV7-STL
LITOL-24
Isoflex Topas NB-52
CLUTCH PLATE,CLUTCH MASTER CYLINDER REPAIR KIT,SLEVE CYLINDER REPAIR KIT,CLUTCH MASTER CYLINDER ASS
LV7 MARUTI 02122M0612A SCREW,LV7 MARUTI 16119M82030 GASKET OIL PUMP,LV7 MARUTI 89031M80000 TANK ASS
WUXGA 3 LCD Laser Projector with 4K Enhancement,ELPLM15 Lens,Ceiling Mount Wall Mount Projector Sta
ROPE STARTING,OIL SEAL SPECIAL TO SUIT,FUEL PIPE,HIGH PRESSURE PIPE ASSY,OIL PRESSURE GAUGE,PIPE FU
Chilly Powder,Turmeric Powder,Coriander Powder,Garam Masala,Chicken Masala,Mustard Seed,Cumin Seed,
Pressure cooker 10ltr,Wick stove,Digital wall clock,Day book register,Pen
KILOMETER GEAR,CLUTCH PLATE,GEAR LEVER BOLT,CLUTCH RELEASE BEARING,PILOT BEARING,REAR DOOR LOCK,HEA
Adhesive Syn Resin Araldite AY 103,Leather cloth Maroon,Leather cloth Green,Talc Sheet,Thinner for 
Red Chilli Powder,Coriander Whole,Turmeric Powder,Jeera,Ajwain,Chicken Masala,Garam Masala,Panner M
Fruit Dried(Raisin Green)
REPAIR KIT AIR COMPRESSOR,HOSE PLAIN,WIPER BLADE WITH ARM,HOSE ENGINE TO RADIATOR,WINDSHIELD GLASS 
AC Busses 40 to 42 seater 1,Extra Kms Local duty 2,Extra Hrs local duty 3,AC Buses 40 to 42 seater 
Custom Bid for Services - SUPPLY, INSTALLATION AND COMMISSIONING OF LIQUID MEDICAL OXYGEN GAS(LMO) 
Sentry Post (Supply, Installation Complete)
Amoxycillin 250 mg Cap,Cefixime 200 mg Tab,Ciprofloxacin 500 mg Tab,Domperidone 10 mg Tab,Aceclofen
Veh Speed Sensor,Relay Emergency Valve,Generator Assy,Brake Cyl,Head Light Upper,Repair Kit for Air
LED DISPLAY BOARD WITH ACRYLIC SHEET MOUNTED ON STAINLESS STEEL FRAME
Repair/Maint Motor Cycle
Sweeping Broom (V3) (Q4)
line matrix printer (Q2)
Smoke Detector Fire Alarm std quality as per buyer Sample,63 AMP Changeover switch as per choice br
SUPPLY AND INSTALLATION OF OBSTACLE IN TRAINING AREA
PIPE EXHAUST CENTRE,SUSPENSION BUSH KIT,TIE ROD END,ASSY UNIVERSAL JOINT,GEAR LEVER KIT,STEERING MT
IMPACT WRENCH,STAR ALEN KEY SET,TAPARIA DR 46 PCS,FILTER WRENCH,GRINDER BOSCH GWC 600,BLACK REFRIGE
ARMATURE ASSEMBLY,ROTOR ASSEMBLY,RELAY 24V,CE BUSH,ARMATURE ASSEMBLY,STARTER KIT SELF,BTY CUT OFF S
Turbocharger Repair Kit,Cover Assy,Assy Kit lined shoe rear brake shoe,Elect Fan Assy,Cam Shaft,Inj
Vitamin D Rapid Quantative Test (Microbion POCT Immunoanalyser)
ARMATURE ASSY,FIELD COIL ASSY,BRUSH GEAR ASSY,FIXING BRAKET ASSY,SOLENOID SWITCH,OIL SEAL,BRAKE PIP
Hydraulic Hose 3 by 4 inch _18_6 Min_19_8 max_ ID WP_21_5 Mpa by 219_2 Kgs by Cm2 SAE 100R2 Type at
LV7 STLN VF DMD-NIV-1034 FEED PUMP REPAIR KIT 9441 037000,LV7 STLN VF 4720-72-0000352 HOSE 4720-014
DUAL BRAKE VALVE,AIR COMPRESSOR REPAIR,MASTER CYLINDER ASSY,DOOR LOCK ASSY RH,DOOR LOCK,ISOLATOR SW
LV7 TATA 312-267-1096 CAP RUBBER PROTECTIVE ON GEAR BOX TOP,LV7 TATA 000-544-0068J MAP READING LAMP
5-0 PTFE monofilament suture,light cured periodontal surgical dressing pack of 4 syringes,bulk fil 
H2 9320 000017 SHEET RUB SOLID BLACK 200CMX100CMX10.0M,G1 5340 000903 HINGES STEEL BUTT 50 MM,G1 53
Repair and Overhauling Service - diesel generators- DG Sets; Kirloskar; Yes; Buyer Premises
Cam Plate,Vane Pump,Roller,Repair Kit,Injector Nozzle,Nozzle,Timing Device Piston,Roller Pin,Gear L
OMALA S4 GX 320 AHS Conveyer Gear Box Oil OMALA S4 GX-320 (Proprietary Product of Shell)
G1 5315-000818 NAILS STEEL WIRE ROUND 50 MM X 3.15 MM,G2 3439-000097 ROD WELDING COPPER 5.00mm,H1B 
Mil - PRF-6083 Hydraulic Fluid Grade (Equivalent Oil recommended by OEM are Hydrauncoil FH-6, C-635
Alovera gel 10 prcnt plus Glycerin 10 prcnt lot 50gm,Cetyl And Stearyl alcohl methyl propyl Hydroxy
LV2 ICVS 2590720256245 765 12 SB224 SHOCK ABSORBER,LV2 ICVS 4720720260274 765 07 24 HOSE,LV2 ICVS 4
CCTV Camera System with Accessories
False Ceiling For VIP Section
Mil - PRF- 32033/ VV-L-800 Preservative Oil, Water displacing Low Temperature (Equivalent Oil recom
Folding Movable Platform for Tools & Heavy Spares
TATA SAFARI GEAR BOX REPAIR,TATA SAFARI SERVICING,TATA SAFARI FUEL PIPE REPAIR,TATA SAFARI AIR PIPE
LV7 T815 CONNECTING HEAD,LV7 T815 PIPE RADIATOR OUTLET,LV7 T815 CLUTCH RELEASE BRG,LV7 T815 ACC CAB
HYDRAULIC CYLINDER HM,BEACONORANGE,CONTROLING DISTRIBUTOR,INDICATOR GLASS,REFLECTION GLASS
Gauze ribbon,Ketac Molar GIC type II GIC,Composite filling instrument double ended 115 730 waldent 
LV6-MT14 2610-000103 Tube Inner Pneu 7.50-20 34-7 LP T B CW,LV6-MT14 2610720308190 Tyre Pneu 14.00R
LV2 ICVS 2590720256245 765 12 SB224 SHOCK ABSORBER,LV2 ICVS 4720720260274 765 07 24 HOSE,LV2 ICVS 4
Evening Primrose Oil 500 mg Tab,Febuxostat 80 mg Tab,Montelukast 10 mg plus Fexofenadine 120 mg Tab
ragulator adapter kit
Gear Wrench Set 6 to 22 mm,Gear Wrench Set 24 To 32 MM,Cutting Plier,T- Handle With 27 Mm Socket,Ra
Alendronic Acid 70mg Tab,Alphaketoanalouge 200mg Tab,Alprazolam 0 Point 25mg Tab,Amiloride 5mg plus
Desktop Computer,Headphone,Speaker 5.1
Wondershare Filmora,Filmore Creative Assets Effect,Render Forest,Adobe Creative Cloud,Doodle maker,
Mineral Water Bisleri,Addidas Quick Dry T Shirt with printing,Dettol Antiseptic Liquid for First Ai
Gabapentin 100 mg Cap,Tab Gabapentin 300 mg plus Methylcobalamin 1500 mcg,Gefitinib 250 mg Tab,Gemf
Stabilizer 10 KVA,Bulb holder,Decor Ladi Rice Hari Warm White 60 Mtr,Decor Ladi Rice Hari Warm Gree
Modification/upgradation of JiG Boring Machine
Holographic Sight for AK-47
Grease Castrol PD00
Cover door sealing,Door regulator handle,Weather strip frt door inner and outer,Weather strip rear 
Dhokla Making Commercial Machine
SUSPENSION BUSH KIT,SILENCER ASSY,DOOR TRIM PANNEL RH,SHOCK ABSORBER ASSY,VEHICLE SPEED SENSOR AGB,
CABLE ASSY COMPLETE,HOSE ASSY,WIPER BLADE,WIPER ARM ASSY,BRAKE HOSE PIPE,DOOR LATCH INNER
software defind radio
3 MP Tilt Camera,Air Grid,Cable,Pole,Installation Commissioning and Configuration of Camera
Light Weight Ground Sheet (TPO Coated)
Boot High Ankle PU Rubber Sole (Defence)
100 Pair 0.5mm Unarmd UG cable 6900 mtr AMC for one year,50 Pair 0.5mm Unarmd UG cable 1898 mtr AMC
Commercial Treadmill Display LED,Commercial Treadmill,Elliptical with Inclination,Spin Bike,Multipr
biometric access consystem
LV7-Maruti 23266M83002 Arm Clutch Release,LV7-Maruti 12810-71C02 Tensioner Assy Timing,LV7-Maruti 1
Rain Cape Multipurpose Disruptive (Poncho) (Defence)
Dextron-II
Glieitmo 805K White
Power Steering Oil 1,Power Steering Oil 2,Power Steering Oil 3,Power Steering Oil 4,Power Steering 
Hose,Bracket,Bushing,Seal Dust,Bolt,O Ring,Hose,Hose,Seal Oil,Rod,Yoke,Lever RH,Lever RH,Rod,Screw,
Toilet FFL (4 Men)
High glossy thermal printing paper roll 110 mm x 18 to 20 mtr for printing USG images (type-5),Non 
TRANSMISSION SYSTEM / FRONT GEAR CASE FLUID (DEMAND DRIVE FLUID)
PS-4 EXTREME DUTY 10W50-4 CYCLE OIL
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5
M3 Chip Tablet 13
BRAKE SHOE LINING,WHEEL CYL ASSY,BRAKE MASTER CYL WITH BOOSTER,STEERING VANE PUMP ASSY,LOCK WASHER,
Hinge for HR Binocular 08X30
PRESSURE CONTROL VALVE
Armature assy,Bush carrier plate,Field coil assy,Bush set,Suspension bush kit
Power Cable Copper 2 point 5 sqmm 2 core,SS Combined Board 15 with box,4 Way board 2 switch 1 Socke
Air Freshener,Antiseptic Liq,Black phenol,Broom Naryal,Broom Soft,Detergent Pdr,Handwash Pauch,Dust
615315008472,619505000228,615360002134,615310021438,5340013922,615315005123,615306011497,6153100213
STORE SHELTER
HMC THK BPASS BMC 1527,BTY 3 POINT 6 11MAH NIMH A11,CAP 0 POINT 6 MPD CAP 600M,CAP 4NX7 250V,CAP 47
Customized AMC/CMC for Pre-owned Products - CAMC OF COMPUTER PRINTER & LAN; CAMC OF COMPUTER PRINTE
Manpower Outsourcing Services - Minimum wage - Skilled; 12th and post graduate; Others,Manpower Out
FAN BELT,HEAD LAMP LEFT HAND 24V,SOLENOID SWITCH,ARMATURE ASSEMBLY,RECTIFIER ASSEMBLY,SPRING BRAKE 
TFT Display
Laptop 16 GB RAM, 512 SSD, Touch Screen with Win 11,Laptop Bag,Notebook with M4 Chip, 16 GB RAM, 51
Unmanned Aerial Vehicle & Payload Systems for Surveillance
Flask 750 ML,Hot Case 1 Ltrs,Dustbin 40 Ltrs,Water Jar 20 Ltrs,In Out Tray,Water Despenser,Peg Tabl
Digital Medical X - Ray Films (V2),Digital Medical X - Ray Films (V2),Digital Medical X - Ray Films
Inj Phenylbutazone 100 ml,In Xylaxin 30 ml,Inj Tribivet 100 ml,Dimethyl sulphoxide LR Grade,Inj Gen
Domestic Plates (V2),Domestic Plates (V2),domestic trays or platters,domestic spoons,Domestic Soup 
Mac M4 Chip Laptop 15 Inch 512 GB,Mac M4 Chip Laptop 13 Inch 512 GB,Mac M4 Chip Laptop 15 Inch 256 
OFFICER JCO LIVING SHELTER
Hand Held Radio UHF with Spare Li Ion battery 2400 mAH and location tracking software for GIS Appli
7 Inch TCD,Coin Cell with Buck Converter,3D Printed Box,Step Down Converter,Solar Panel 12 V 40 Wat
HDMI Cable 4K 20 Mtr,HDMI Cable 4K 15 Mtr,HDMI Cable 4K 1 point 5 Mtr,Pencil Cell 1 point 5 V AA,Pe
Dettol Soap,Broom Soft,Floor Wiper,Harpic,Acid Toilet Cleaner,Coconut Broom,Pocha Cloth,Lizol,Napth
Oil Seal,Needle Bearing,Brake Booster Assy,Gear Speedometer Drive,Bolt with Nut,Gear Box Flange,Clu
CARBONATED SOFT DRINKS,Lime Based Soft Drinks,Packed Juice
LV7 STLN VF P-1303727 SEALING RING,LV7 STLN VF B-5432012 ASSY OF DOOR SHELL LH,LV7 STLN VF 4710-72-
LV7 STLN F-1945450 HOSE 1 ID 80 LONG,LV7 STLN BON00741 EXTERNAL REAR VIEW MIRROR RIGHT,LV7 STLN 803
LV7 STLN 4720-016005 HOSE ASSY NON METALLIC TYRE INFLATOR,LV7 STLN 6220-004485 LIGHT BLACKOUT,LV7 S
LV7 MARUTI 37400M80030 SWITCH ASSY COMBINATION,LV7 MARUTI 2540-006507 ABSORBER ASSY FRONT SHOCK,LV7
LV7 MARUTI 35602M80110 LIGHT ASSEMBLY INDICATOR,LV7 MARUTI 17700M83112 RADIATOR ASSY,LV7 MARUTI 532
LV7 MARUTI 09816M00083 WHEEL WRENCH,LV7 MARUTI 33400M78L00 COIL ASSY IGNITION,LV7 MARUTI 41310M75M0
Manpower Outsourcing Services - Minimum wage - Skilled; Higher Secondary; Finance/Accounts
Ramipiril 2.5 mg Tab,Tab Sacubetril 24 mg Valsartan 26 mg,Cefixime 200 mg Tab,Soft Gelatin cap Anti
50 57 2 RED REFLECTOR,6220-000161 TALE LIGHT,50 669 3 CABLE,NK003042 INDICATOR SCREW,NK002748 INDIC
Ornamental Plants,Printed car diary,Diaries for offices,Packing mtrl for office records,Mats for up
Ignition Coil,Suspension Bush Kit,Siren Amplifier,Siren Assembly,Ignition Coil,Gear Liver Bush,Radi
Counter Unmanned Aerial System (CUAS)
LV2/ICVS 5340015099(765-50-SB805) HANDLE DOOR
LV1/R72 172.52. 021SB BLADE(175-52-021SB)
LV1/R72 172.41. 019SB SHAFT PROPELLER
6850 000017 POWDER CLEANSING,7931 000014 SOAP LAUNDRY,7930 000302 SUPER BRIGHT HD ULTRA,5350 000009
NK002141 TOGGLE SWITCH,1351 2047 CN SOLENOID VALVE,2547 5010 5807 RUBBER HOSE PIPE,NK001351 SIREN,3
Custom Bid for Services - ----
Atta 5 Kg,Atta 10 Kg,Atta 20 Kg,Atta 25 Kg,Atta 50 Kg
Custom Bid for Services - Painting and Preservation of Steel Chesses Double held with GE 583 Engr P
Oil seal for crank shaft rear,Solenoid Operated Valve,Fuel Shut off Solenoid,Filter Assy Oil,Air Fi
Centre drill No one body dia three by sixteen inches plot dia one by six inches length one point se
Repair and Overhauling Service - Repair of Galaxy EPABX System; Galaxy; Yes; Buyer Premises
Evaporative Air Coolers (Desert Coolers) Conforming To IS 3315,Split Air Conditioner Including Gree
Free Style Optimum Neo H Blood Glucose Test Strip,Insulin Disposable For Insulin Pumps set and resr
Microcuvettes for Haemoglobinometer,Hepatitis B surface antigen HBsAg detection ELISA kit of 96 tes
MAHINDRA MAXIMILE SYNTEC F2
Frt Door Beeding LH and RH,Rear Wheel Brg,Kit Brake Pad Assy,Air Filter,Radiator Fan,Clutch M Cyl A
Log Book DG Set at power Houses,Log Book for pump houses,Retail issue Voucher,IAF EO3 inspection fr
Plain Copier Paper (V3) ISI Marked to IS 14490,Plain Copier Paper (V3) ISI Marked to IS 14490,Plain
MT ITEMS 1,MT ITEMS 2,MT ITEMS 3,MT ITEMS 4,MT ITEMS 5,MT ITEMS 6,MT ITEMS 7,MT ITEMS 8,MT ITEMS 9,
Cartridge for printer JET TEC CC388A,Cartridge for printer JET TEC CRG326 CE278A,NPG 51 TONER BLACK
Honey Sucker (Cleaning of Septik Tanks)
Antifreeze Premium Coolant 20 Ltr Bottle,Engine Oil 1 Ltr,Break Fluid Dot 3 1 Ltr,Break Fluid Dot 4
Breathing Bag for OX 10
Ice MM 1,Ice MM 2,Ice MM 3,Ice MM 4,Ice MM 5
Supply Pump,Hydraulic Head 040,Woodruff Key,Positioner,Nozzle
352 Dia Clutch Cover Assy,352 Dia Clutch Plate assy 1.75 Spline,Clutch Master Cyl Assy,Clutch Slave
Driver Amplifier card CH 2 of 40W Jammer Aqua,Two way connector of 40W Jammer Aqua,Directional coup
Repair and Overhauling Service - Vehicle; TATA EICHER; Yes; Service Provider Premises,Repair and Ov
Air Bag Sensor,Ignition Switch,Air Dryer Kit,Gear Lever Kit,Fuel Filter,Oil Filter,Combination Swit
IT Software
LV7-STLN_B1301701_DRIVEN PLATE FOR CLUTCH,LV7-STLN_P4301302_PILOT BEARING,LV7-STLN_F0201410_CLUTCH 
80900125,24100304,81900070,24100205,81900071,82810222,14500001,92615500,24010505,83500074,12304237,
Atta 5 Kg,Atta 10 Kg,Atta 20 Kg,Atta 25 Kg,Atta 50 Kg
CLUTCH RELEASE BEARING,DOOR LOCK REAR,CLUTCH RETURN SPRING,OIL SEAL,THROTTLE GASKET,DOOR STOPPER,WO
352 Dia Clutch Cover Assy,352 Dia Clutch Plate Assy 1.75 Spline,Brush Gear Assy 24V,Wiper Blade fro
Pdr Timpol 100gm,Inj Phenylbutazone sodium salicylate 30 ml,Tincture Benzoin 400ml,Inj Metoclopromi
Honey Sucker (Cleaning of Septic Tanks)
Custom Bid for Services - IT TRAINING
Stud Bolt,Glass Wind Screen,Repair Kit,Hose JS 6X400,Hose JS 8X800,Hose 10x630,Hose 12 MM,Fly Wheel
UNIVERSAL JOINT,IGNITION SWITCH,SPEEDO METER CABLE,HIGH PRESSURE HOSE,ASLY HOSE,ASLY HOSE,ASLY HOSE
SHUT OFF COCK,PALM COUPLING,FUEL PUMP,MANUAL BRAKE VALVE,PINION
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin,Manpower Outsourcin
RETAINER HELICAL COMPRESSION SPRING,NIPPLE GREASE CONICAL,WASHER PLAIN STEEL,PIN,BEARING SLEEVE ROL
CYLINDER LINNER,PISTON,PISTON RING SET,REGULATOR CONTROL ELECTRONIC ENGINE,HYDRAULIC CYLINDER RAM,A
Processor i5 10 Gen Intel,Processor i5 12 Gen Intel,Mother Board i5 12 Gen Intel,Ram 4 GB DDR4 Asus
BRAKE SHOE ASSY,BRAKE PAD,ASSY WINDOW REGULATOR RH,DIFFERENTIAL GEAR KIT,HANDLE REGULATOR GLASS,DRI
NOZZLE,DISTRIBUTOR HEAD,ROLLER,OIL SEAL,BUSH KUNG PIN
NK-IT-00052 LOGIC CARD,NK-IT-00008 GRAPHIC CARD,NK000032 TEFLON,NK000053 PRESSURE ROLLER,NK-IT-0005
Fuel Feed Pump,Cabin Lifting Pipe,Wiper Motor,Wiper Blade,Ignition Switch,Assy Fuel Filter,Water Se
Wheel speed sensor LBPV,Clutch plate TATA,Pressure plate TATA,Clutch release bearing TATA,Release b
Banners for verious events like Repulic Day, Independence Day , Children Day etc,Posters and Banner
POLARIS PREMIUM 50/50 ANTIFREEZE COOLANT
Otorhinolaryngology Clinical Examination Unit with Fiberoptic Endoscope Setup
Lunch,Dinner,Breakfast,Water Bottle,Transportation Charges from Bareilly to Kigam,Lunch,Dinner,Brea
OIL FILTER,CLUTCH KIT,V BELT,SPEEDO METER CABLE,RELAY STARTOR,COMBINATION SWITCH,FUEL FILTER,FLASHE
Panel repair of LED TV 32 Inch,Repair of Refrigerator 1250 Ltr capacity four door steel body,Replac
Banana,Mango Dahsehari,Mango Safeda Mango Neelum Mango Kesar Mango Langra Mango Fazli,Musk Melon,Pa
GLOW PLUG,FUEL WATER SEPARATOR,AIR FILTER ELEMENT,HOSE AIR,ASSEMBLY TURBO CHARGE,WATER PUMP ASSEMBL
Hood Knofe Narrow Blade Right Hand,Hoof Picks wih Brush,Hoof Knife Wide Blade Right Hand,Nail Pulle
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Dual Chamber AICD complete with accessories MRI compatible,Trans catheter dual chamber leadless pac
Modification of Cabinet for Shakti Eqpt in BCP,Avita Cosmos 2nd in 1 Intel for Trg of Comd Post,Clo
GRAR BELT,MICRO CCT VCO,MICRO CIRCULARITY TYPE VCC2803,SEMICONDUCTOR DEVICE TYPE IN5060 400STD,SEMI
Distributor Head,Drive Shaft,Body Housing,Repair Kit,Vane Pump,Timing Device Piston,Cam Plate,Injec
A4 Paper,Ledger Paper,A3 Paper,Sharpner,Eraser,Fevi Stick,Pencil,Highlighter,Cutter Blade Small,Cut
Tranexamic acid plus Mefenemic acid Tab,Evening Primorse oil 1000mg Soft gelatin Tab,Levonogestrol 
SELF STARTOR ASSY AIR COMP,AVR HALF ROUND,CARBON BUSH WITH HOLDER,E V R,SELF STARTOR ASSY 7 5 KVA,O
REAR DOOR LOCK ASSY,WIPER BLADE,WIPER BLADE,PRESSURE PLATE CLUTCH PLATE SET,CLUTCH RELEASE BRG,CLUT
Engine Over Haul of Tata Safari,04x Piston New Required,Valve Grinding,Crank Bearing Broken,Valve G
Piston Ring Set,Piston with Linner,Head Gasket,Solenoid Switch,Connecting Rod
PTZ CAMERAS CCTV,BULLET CAMERA 5MP,10 CHANNAL NVR,2TB HARD DISK,CAT 6 UTB CABLE,POE SWITCH GIGA,4K 
Atta 5 Kg,Atta 10 Kg,Atta 20 Kg,Atta 25 Kg,Atta 50 Kg
STANDALONE CCTV CAMERA,TWO TERABYTE HARD DISK,SIXTEEN CHANNEL NVR,UPS ONE KVA,LED MONITOR TWENTY FO
pickle,tomato sauce,biscuit,vineger,matchbox
Lyzol,Colin,Mop Cloth,Soft Broom,Odonil,Air Pocket,Dusting Cloth,Room Freshner,White Phenyl,Harpic,
Angle iron 2x2 for modification of ALS Recovery,Cutting wheel 4 for modification of ALS Recovery,Cu
Stabilizer Bar,Differential bearing inner,Differential bearing outer,Oil seal hub,Gasket,Accelerato
10558440,10413605,10537019,10308439,10536874,10310437
EC NETS JUTE 5.5 X 4 M LARGE MESH 50 MM
EC NET (JULE) 11 X 8 M LARGE MESH 75 MM
SUN SCREEN LOTION (ECC & E)
Office Shelter Tailor Made
Genr Set 15 KVA Kirloskar 03.922.40.0.00,Genr Set 15 KVA Kirloskar 04.270.01.0.00,Genr Set 15 KVA K
CLUTCH DISC,SUBASSEMBLY OF OIL COOLER,HORN CHANGE OVER SWITCH,ISOLATOR SWITCH,DOOR CATCH INNER,REAR
Genr Set 3.3 KVA Kirloskar BP1.010.10.0.00,Genr Set 3.3 KVA Kirloskar NK,Genr Set 3.3 KVA Kirloskar
CARBONATED SOFT DRINKS,LIME BASED SOFT DRINKS,LIME BASED SOFT DRINKS 1,FRUIT JUICE,FRUIT JUICE 1
VALVE EMERGENCY AIR PRESSURE,SERVO STEERING CYLINDER RV,CIRCUIT BREAKER,CLOSING COCK,SEALING RING I
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
FUEL WATER SEPARATOR,ELEMENT AIR CLEANER,REP KIT MECH TRANSMISSION,V BELT,SPEEDO CABLE,IGNITION SWI
CLUTCH KIT MAJOR,WHEEL KIT,ASLY CLUTCH MASTER CYL,ASLY CABLE COMPLETE,SPPEDO CABLE,FUEL SHOT OFF SO
CPU MODULE
Sit Up Bar with Push Up Bar
Field WSS Desalination Plant (RO Plant) 500 Ltr/Hrs
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7,MTITEMS 8,MTITEMS 9,MTITEMS 1
VII80VN12841 8012843 80 BELT,765 84 SB210 VALVE WITH RELAY,MTO 135 006 TUBE HOUSE,765 50 SB252 LATC
BELT TIMING,BELT V,SPARK PLUG,OIL SEAL,V BELT 1280 MM LONG,BELT V RIBBED,3.2 DIA SPEEDO CABLE,ASSY 
OIL COOLER,GEAR LEVER KIT,OIL COOLER GASKET,SOLENOID SWITCH,INJECTOR ASSY,ACCELERATOR CABLE,WATER P
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Admin,Manpower Outsourcing Ser
9x19MM Machine Pistol
Stacker (Q3)
Sunflower oil,Mustard Oil-IS: 546
Catheter Foleys, Silicon 2 way, 5 ml, Size 16 FG,Disposable surgical rubber gloves size 6.5 pair of
Repair and Servicing of Mahindra Armado BA No 23 F 006709E,Repair and Overhaul of front and rear ax
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Not Required; Others,Manpower Outsourc
Boot Anti Mine Inf (BAMI)
Repair Kit,Cross Assy,Driven Assy,Brush Gear assy,Solenoid switch,Brake Lining With shoe,Gaskit Cyl
COOLING FAN CRIS,ANTENA CRIS,BATTERY 12V LIBRA,ANTENA LIBRA,BATTERY GP 338,SOCKET ANTENA LIBRA
G2 9515 000715 STEEL PLATE CARBON 5000 X 1000 X 5 MM,G2 9520 000033 STEEL ANGLES 35 X 35 X 5 MM,G2 
A1 7720 000040 DRUM SIDE STICK,A1 7720 000024 MOUTH PIECE NO 1 BUGLE MK 1,G1 5310 001647 WASHER SPR
Odonil Room Freshner 270 ml,Dettol Hand Wash,Harpic 1 litre,Broom,Cotton Dusting Cloth,Kent RO wate
Turbo Core,Wheel Hub Nut,Knuckle Bush,Thrust Bearing,Axle Roller Bearing,Booster Pipe,CSC assy,Fly 
Paper Pin T Type,Tape inch Transparent .5 inch,Tape Transparent 1 inch,Battery AA Size,Battery AAA 
Bellows Rubber,Seating Rubber,Cap Rubber,Air Line Seating Rubber,Hose
Self Screw 2 Inch,Self Screw 2.5 Inch,Fevicol,Varnish,Cutter Blade 14 Inch,Paint Red,Paint Yellow,P
Paracetamol with cysteine HCL monohydrate infusion 100mg,Inj tranexamic acid 500mg,Labetalol HCL 5m
Hiring of Earth Moving Equipments, Material Handling Equipments and Cranes (per Hour basis) - As Pe
Short Term Cab & Taxi Hiring Services - Sedan; Local; 80Kms x 08Hrs,Short Term Cab & Taxi Hiring Se
Combination Switch,Front Engine Mounting Pad,Front Brake Hose,Tie Rod,Door Pad Button,Knuckle Bush,
BRAKE SHOE ASSY,REAR HUB CUSH DRIVE RUBBER BLOCK,DRIVE HARDENED STEEL PINION,SOLENOID SWITCH,HOSE E
Construction of Tech Shed room 10 by 15 for wheel balancer eqpt,Sand Work,Cement Work,Stone Work,Ce
CORIANDER SEEDS,CORIANDER POWDER,RED CHILI WHOLE,RED CHILI POWDER,CUMIN SEEDS,CUMIN SEED POWDER,TUR
Repair of Power Suppy Card PSU 48V DC of Matrix Exch 128 Line,Repair of T1E1 card of matrix exchang
RED PAINT,WHITE PAINT,BLACK PAINT,OG PAINT,YELLOW PAINT
Slim DVD Writer,Screen,Plate Unit Wight,SMPS 6 pin,Pressure Roller,Logic Card,MAINT BOX,Drum unit,P
Self starter assy 2.5 Ton,Air filter assy 2.5 Ton,Fan belt MPV,Liquid gasket 2.5 Ton,Wiper blade fo
REAR SPROCKET 38 T,SILENCER ASSY,BRAKE SHOE ASSY,CLUTCH ASSY COMPLETE,BRAKE SHOE ASSY FRT,SIDE STAN
WD 40,THROTTLE BODY CLEANER,TEFLON TAPE,ARMATURE ASSY,FUEL FILTER ASSY,STOP SOLENOID 12V AUTO,FEED 
SUPPLY ONLY 30 X FD SECURITY LIGHTS (SOLAR) AS PER TECH SPECIFICATION AT JANGLOT
Self starter assy 2.5 Ton,Air filter assy ALS,Road spring bolt 2.5 Ton,Bush suspension Marksman,Fro
Chicken Masala 100 gram,Meat Masala 100 gram,Dal Makhni Masala 100 gram,Star Masala 1kg,Chana Masal
SOLDER SOFT,WIRE STEEL MILD,STEEL ANGLE 25X25X3MM,ELECTRIC WELDING ROD 3.15,STEEL PLATE TINNED,STEE
HP Hose,Spark Plug,Relay Main and Fuel,Starter Relay 24V 50A,Assy Cable Complete,Armature,Field Coi
DISTRIBUTOR HEAD,DISTRIBUTOR HEAD,Bearing Bolt,PULLING ELECTROMAGNET,ROLLER,Cam Plate,ROLLER,Govern
Cement Bag 50 Kg Make Abuja Birla ACC Ultratech JK Shree,Sand,PCC Block 300x200x200mm,Vetrified Til
AIR FILTER ELEMENT,ASSY PIPE COOLENT BY PASS,BALL JOINT UPPER,BALL JOINT LOWER,GEAR LEAVER REP KIT,
CABLE ASSY HOOD,SUCTION HOSE ASSY,CLUTCH MASTER CYL,SPIDER BRG,CLUTCH PLATE ASSY,CLUTCH RELEASE BEA
24 port switch,24 port switch with poe,8 port switch,ote,9u rack,ups 1 kva,power strip,cat 6 utp ca
Store shelter Size 10 point 44 m x 6 point 1 m x 4 point 75 m height with 1 point 5 m verandah as p
Solder Soft,Quick Fix,Alcohol Isopropyl,Insulation Tape,Anabond,LT Wire,M Seal,Fuse 10 Amp,Tape adh
COOLING FAN CRIS,ANTENA CRIS,BATTERY 12V LIBRA,COOLING FAN LIBRA,ANTENA LIBRA,ON OFF SWITCH LIBRA,S
Driver card of 40W Jammer Aqua,Final Amplifier card of 40W Jammer Aqua,Antenna of 200W Jammer Ashi,
WIRE STEEL MILD 1 MM,RIVITS AND WASHER,ADHESION RUBBER AND STEEL SR 998,SODA ASH TECH,PAINT RFU BLU
CLIP FRAME OST 3 408 70,GASKET 172 46 067,GASKET 175 40 102,COLLAR 432 40 035 3,GASKET 432 40 089 1
Custom Bid for Services - Comprehensive repair and maintenance to certain lift of bldg DSC, NC-1,NC
THRUST DISC,RINF 50X40,RING 140X 125,PISTON,SPRING,DISC,SECURING RING,SPRING,SETTEING RING,SCREW M 
GA Bucket,Link Arm LH,Link Arm RH,MC Tipping Link,GA Carrier Roller
Manpower Outsourcing Services - Fixed Remuneration - Others; Sweeper; Not Required
Ride on road sweeping machine
CABLE,HOSE,HOSE ASSY,CARBURETTOR ASSY,FILRERING INSERT,OIL FILTER,GLAND SEAL,HOSE
ALCOHOL ISOPROPYL TECHNICAL,BLANCO WHITE,BLEACHING POWDER STABILISHED,BLUE LAUNDRY,CHALK FRENCHTECH
ABSORBER ASSY REAR SHOCK,LOCK ASSY STEERING,FORK HIGH RESERVE SPEED,RECTIFIER ASSY,ARMATURE MOTOR,I
ASSY CLUTCH MASTER CYL,SWITCH 24 V,CARBURRTTOR ASSY,REPAIR KIT PUMPING ASSY,HOSE PREFORMED,HOSE ASS
BLT T 72 SELF STARTER REPAIR,BLT T 72 THREAD MAKING,BLT T 72 FUEL PIPE REPAIR,BLT T 72 AIR PRESSURE
Z6 R72 RELAY ELECTROMAGNET,LV2 RCV MR KIT FOR FILTER,LV1 R 72 HOSE PIPE LINE,LV1 R 72 HOSE 48 MM,LV
Vehicle Washing pump with compressor
Feeding tube size 10 F,Finger Excerciser,Forearm Fracture RS Brace universal size for adult,Functio
Clutch Release Bearing,Control Valve,Cover Assy Clutch,Fuel Pump Assy,Engine Mounting Pad Frt,Nuckl
Baby Spacer Zero Stat for Delivery of Mdi with Transparent Babymask,RIA TUBES,GLUCO STRIPS FOR GLUC
ASSEMBLY OIL FILTER,TIMING BELT,VALVE ASSEMBLY WATER,CLUTCH DISC 310DIA,ASSEMBLY RELEASE CABLE,WHEE
EPS sheet,Repair of doors and windows,Fevicol SR 998,Bolt and nail,Special type grease,Canvas harne
Catgut 40mm1 oblique 2 circle Round Body 90cm No 1 CODE 4259,Catheter Mount,Chemical indicator stri
Plywood 8x4 ft 19mm,Fevicol,Curtain 7 Ft,Double Bed Sheet,Mattress,Wooden Frame
Provn of MT Shed Shelter part only FOR GELEMO,Constr Mtrls for MT Shed FOR GELEMO,A Constr Mtrls fo
Short Term Cab & Taxi Hiring Services - Sedan; Local; 80Kms x 10Hrs,Short Term Cab & Taxi Hiring Se
CF KNDNIVCL2203,CN KNDNIVCL2249,K3 7210-000445,CE 8405-001580,CE KNDNIVCL1-139
LV6MT14 LV6MT14NIV032020FLT TUBE,LV6MT14 2610000321,LV6MT14 BBDNIV032015TUBE,LV6MT14 2610000102,LV6
Modular Work Stations (V2) (Q3)
Repair of deterioration by leakage,deterioration protecting paint,Lubricant,Nylon rope,rotating pro
PVC Panelling,Lights,SR Solutions,Fevicol,Flooring,Touchwood Wooden Polish
ABG Cassette Pkt Of 25,Tegaderm Central line fixer,Tennis Elbow support sizeM,Nitrile Non Sterile G
Non Skid Tile,Cement Bag 50 Kg,Sand,Crusher Cement,Bajri
SLIDING GLASS,WINDOW GLASS RH,TOP GLASS ARMY BUS,SELECTOR SHIFT SHAFT,NEEDLE BEARING,SCRAPER RING
Round body Needle no 09,Sealed Reachargeble Battery Ni MH 3.6V 1000mAh3.6Wh HEINE Made In Germany F
Oil Filter,Water Separator,Stearing Filter,Clutch Booster Kit,Door Beading,Stearing Kit,Turbo Kit,G
Fabrication of Shed Roof Work,Retaining Wall Size Running Length ,30 feet -80 feet -30 feet, Specif
Mirchi Powder,Haldi Powder,Dhaniya Powder,Jeera,Kali Mirch,Long Sabut,Sabut Mirch,Sabut Dhaniya,Eml
Surgical Local Hemostat/sealant 2 Polyethylene Glycols, Dilute hydrogen chloride solution & sodium 
LV2 ICVS 5330720114075 765-10-1408 GASKET,LV2 ICVS 5330720463458 GASKET 765-17-427,LV2 ICVS 765-22S
Wiper,Extendable broom,Bucket with Mug,Toilet Disinfectant cleaner,Liquid hand wash 500ml,Floor Cle
Washing Powder,Harpic 5 ltr Jar,Hand wash 5 ltr Jar,Nimyle Eco Friendly Floor Cleaner Lemon Grass 5
LV7 TMB 000-500-0106J RADIATOR CAP,LV7 TMB 2920-005212 RELAY SOLEHOID ENGINE STARTER ELECTRICAL,LV7
TIMING BELT,FUSE,MAIN BATTERY FUSE KIT,RELAY 40A,BELT TENSIONER,WHEEL CYL ASSY,DOOR LATCH STROME FL
DUAL BRAKE VALVE,GEAR SHIFT LEVER,CONNECTING SLEEVE,CONTROL VALVE,FILTER INSERT,OIL FILTER,CARBULAT
Security Light
Living Shelter 16 Men Porta
Bearing Frt Wheel,Joint Assy Universal,Lock Side Window LH,O Ring Spark Plug,Clutch Pipe,Speed Sens
Supply of stores for Living Shelter 4 Men Porta
Supply of stores for Living Shelter 16 Men Porta
Equilizer Assy,Clutch Booster Assy,Pneumatic Valve,Battery Cut off Switch,Artmature 24V,Self Field 
exhaust manifold gasket,inlet manifold gasket,push tube seal,head gasket,benjo washer 17 no,benjo w
Assembled PC,Desktop PC HP,Laserjet Printer 1000A,Nk,Nk,Nk,PC HP Intel Core i5,Repair of HP Printer
INJECTOR ASSY,Speed Valve Needle,AVR,Diode,Injector Assy Nozzle,Self Starter 12V
REGULATOR,ASSY PIPE HOSE FLEX,CARBURATOR ASSY,FUEL PUMP MOTOR,DISC CLUTCH,COVER ASSY CLUTCH,COMBINA
EP -320
2 MP BULLET CAMERA OR HIGHER,65 INCH MONITOR,16 PORT SWITCH DVR WITH 1 TB HHD,5 KVA ONLINE UPS WITH
Jelly,Sago,Cornflour,Vermicelli,Chocolate,Custard Powder,Tomato Sauce,Pickle,Orange Squash,Vinegar,
Register 100 Pages,Register 200 Pages,Register 300 Pages,Register 500 Pages,Unibal Blue Pen,V7 Blue
Laptop With M4 Chip Set,Tablet with M4 Chip Set,Smartphone
PUMPING SET 06 HP KIRLOSKAR NK,PUMPING SET 06 HP KIRLOSKAR NK,PUMPING SET 06 HP KIRLOSKAR NK,PUMPIN
S Angles 30x3,Angles 30x5,S Angles 25x3,Angles 40x3,Bolt
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 130 km from
DISPOSABLE INSULIN PEN NEEDLES 4MM,DOXYLAMINE SUCCINATE 10 MG USPPlusPYRIDOXINE HYDROCHLORIDE 10 MG
Fuel Hose,Fuel Motor,Cabin Lifting Hose,Air Cleaner Hose,Coolant Hose
LV7-HMV-8x8-AL F1000220-1 P1606651 Clutch Master Cylinder Repair Kit,LV7-HMV-8x8-AL B2H67302 Igniti
LV7-TATA 2614-7000-0135 Assy Tool Box,LV7-TATA 2154-2810-0102 Assy Cable Complete,LV7-TATA 27075424
LV-STLN 6240-72-0468908 Head Light Bulb 55-60W,LV7-STLN 5340-72-0473320 Door Lock Rear Gate,LV7-STL
Belt Waist Synthetic (ICK) (IAF)
Boot High Ankle PU Rubber Sole (Defence)
Development of Multi-mode Communication System
LV7-TATA 2786-1833-9902,LV7-STLN VF X-4001000,LV7-TMB 2530-017910,LV7-STLN 2540-009151,LV7-STLN VF 
Provn of OR Living Shelter 20 Men Shelter Parts Only FOR HOCHE,Provn of OR Living Shelter 20 Men Sh
Sentry Post
power steering oil (dextron-IID)
NIGHT ENABLED QUADCOPTER
ADAPTOR 24V 3AMP,BATTERY 12 VOLT 4500MAH,HOSE PIPE,PRESSURE REGULATOR,OXYGEN PRESSURE
Amplifier 500Watt,Microphone with Lid,Microphone Stand Adjustable,Speaker 220 Watt,Auxiliary Cable 
High Mast Security Light 12 Meter
Upgradation of ZU 23MM Air Defence Gun System to Enhance all Weather Capability
10549754 LV6 MT14 2640 000044 CAP TYRE VALVE TYPE HEAD 880Z TR VC 2,10303024 LV6 MT6 130053110964 H
XLPE Cable for Working Voltages up to and Including 1.1 KV as per IS 7098 (Part 1),XLPE Cable for W
Z6 R90 6150720342863 WIRING HARNESS BRANCHED,Z6 R72 5995-003131 WIRING HARNESS BRANCHED CABLE ASSY 
Catering service (Event Based) - Dinner; Non-Veg; Regular Thali
WELDING HOLDER,WELDING MAGNET SET 6 PCS,BOSCH JIGSAW,STANLEY DRILL BIT 70 PCS,EARTH CLAMP,GCO 220 A
Complete Overhauling of Rotary Pump of 2.5 Ton Veh BA No 17C106672H,Complete Overhauling of EDC Pum
Hyd jack cly BD 80,Hyd piston seal MG,Sheer pin MG,Hyd pipe MG,Hyp Pipe MG
Terlipressin 1mg plus 10ml diluent or0.10mgobiliqueml 10 ml vialobiliqueAmp,Tetanus Toxoid purified
Tab Ovasure-M,Tramadol HCl 50 mg CapobiliqueTab,Tramadol HCl 50 mgobiliqueml Inj 1 ml Amp,Trihexyph
hand held gps (Q2) ( PAC Only )
Fevicol 1 Kg,Nails 1 Inch,Nails 4 Inch,Hinges 6 Inch,Corner Clamp,Plywood,Acrylic Sheet 8x4
Lightening Conductor
G2 9505-000058,H1 A 8010-007501,H1 B 7930-000003,H1 B 6810-000568,H1 CHD-NIV2000-000023,H1 7930-000
HESCO Bastions
A4 Paper,FS Paper,Add Gel Pen V7 Hitech,Add Gel Pen Refill,CD Marker,Calculator,Cmptr Ply Paper,Cor
AIR PRESSURE PIPE,BRAKE SHOE FRONT,FAN BELT,352 DIA CLUTCH DISC ASSY 1.75 SPLINE,CLUTCH COVER 352 D
OUTER HANDLE,AIR CYL REPAIR KIT,WIPER MOTOR ASSY,CLUTCH BOOSTER KIT,FAN BELT,DOOR LOCK ASSY,HANDLE 
PAINT RFU ENAMEL BLACK,PAINT RFU ENAMEL GREEN,PAINT RFU ENAMEL WHITE,THINNER,MUSLIN WHITE,ALCOHOL I
Fan Belt,Combination Switch,Assy Oil Filter,Brake Shoe Rear,AC Filter,Brake Pad,Tail Light Assy,Bra
AIR PELLETS FOR AIR RIFLE AND AIR PISTOL
STARTER MOTOR LUCAS TVS,CYL HEAD GASKET,FUEL FILTER,AIR FILTER,MAIN BRAKE VALVE DUAL BRAKE VALVE,AI
Haldi Powder,Lal Mirch Powder,Garam Masala,Dhaniya Powder,Chicken Powder,Kali Mirch,Zeera,Badi Elai
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Office Space; Batt
Repair/Maint Motor Cycle
POWER STEERING OIL S3 AFT MD3
COVER PILLOW,PILLOW HOSPITAL,WASHERS SPRI SING COIL TYPE B STEEL,WSH SPG SC TY B STL NS 8MM,R POLY 
RUBBER BUFFER,ASSY RUBBER BUSHING,RUBBER HOSE UC PIPE,DOOR GLASS RH,HOSE COOLANT TUBE TO PIPE,HOSE,
Rechargable AA Batteries,Earth Innovation Sonic Sound Rate and Rodent Repellent Device,AA Batteries
Assy Sleeve Cylinder,Bolt,Gear Lever Bush Kit,Weather Strip Door,Rubber Hose,Oil Seal,Rubber Bush
Supply of Living Shelter 30 Men as per specification in RFP,Supply of Electrical items for Living S
Three Jaw Self Centering Chuck with back plate size 250 mm for HMT LB 20 Lathe Medium Lathe Machine
Custom Bid for Services - As per BOQ item No 1 Outsourcing services for Semi Skilled AC operator 01
Bucket Ram Seal Kit,Shim,Fuse 3 Amp 5.5 T,Engine Oil Filter,Rocker Cover Seal,Belt 8PK 1866 MT610,P
RESUC OF AIOS , RESUC OF IAIOS
Air Filter Element Inner,Air Filter Element Outer,Seal Kit for Lift Cyl,Damper,Bearing Ball,Straine
GREASE XG-340
Assy propeller shaft front,Repair kit major clutch master cyl,Knuckle post kit,Knuckle bearing,Clut
SUSPENSION BALL JOINT KIT,STRG BALL ROD LINK,TIE ROD,LINK ROD REAR AND FRONT,RUBBER BUSHING,LINK RO
IEVR,Injector Nozzle,Element,Connector,Filter Air,Eng Packing Kit,Mtg Pad Electrical
ANGLE IRON,PAINT RFU GS BLACK,PAINT WHITE,PAINT OG,PAINT RFU BLACK
Fly Wheel ring,Brake Master Cyl assy,Master cyl rep kit,Air Pressure Pipe,Shifting Lever,Oil Seal r
Calibrator pack Ultra 1 without creatinine for phoxultra ABG mechine(1/pack)
ROD WELDING STEEL MILD,COPPER WASHER 14MM,COPPER WASHER 16 MM,COPPER WASHER 20 MM,COPPER WASHER 30 
LOCK SET RE,SECONDRY FILTER RE,TCI UNIT RE,SPEEDO METER CABLE RE,BRAKE SHOE REAR RE,HEAD LIGHT ASSY
Chicken Eggs , Poultry Alive
TURBO CHARGER REP KIT BSIII,AIR PRESSURE PIPE LARGE BSII,TURBO CHARGER REP KIT MINOR BSII,AIR PRESS
Injector Nozzle,Cylinder Head Gasket,Seal Oil for Extension Shaft Crank Gear,Seal Oil,Eng Overhauli
352 DIA CLUTCH DISC ASSY,ASSY RELEASE BRG,ASSY CABLE COMPLETE,COIL ASSY IGNITION,BRG CLUTCH RELEASE
Architectural & Structural Drawing
G1 5310-001376 WASHERS PLAIN STEEL ZINC PLATED 9MM,G1 5315-000079 PINS COTTER SPLIT STEEL 2.5 MM X 
HOUSING FRICTION CLUTCH,ISOLATOR SWITCH,MAIN BERING SET,CLUTCH RELEASE BRG,SWITCH PUSH,SWITCH ASSY,
FUEL SOLONOID ROTARY PUMP,BULB FOR INDICATOR,RELAY VALVE,ASSY UNIVERSAL JOINT,ASSY WHEEL NUT,HOSE D
Cornflour,Custard Pdr,Sago,Jelly,Ice Cream Pdr,Drinking Chocolate,Tomato Sauce,Vermicelli,Biscuit M
URF 80: 20
Construction Account Book,Measurement Book,White file cover with MES insignia,Compliant slip 400 pa
Oil Seal,Front Hub Oil Seal,Centre Bolt,Master Cyl Repair Kit,Master Cyl Assy,Slave Cyl Assy,Slave 
A4 Paper,Stapler Small,Printed File cover,Swining Thermal Paper Roll use to plotter printer Kiosk m
Armature,Field Coil Assy,Solenoid Switch,Brg Bush Set,Mounting Damper Tfr case,Gasket Cylinder Head
Provision of Solar Street Light
i Pad
Preparation of Base,All weather Acrylic Synthetic Surfaceing Eight layer ultra cushion,Court line m
Carbonated Soft Drink,Carbonated SoftDrink,Lime Based Soft Drink,Lime Based SoftDrink,Lassi
grease lg 320
Pickle,Tomato Sauce,Vinegar,Corn Flakes,Biscuits
CHAIN SPROCKET,HANDLE DOOR INSIDE RH,HANDLE DOOR INSIDE LH,SPEEDOMETER CABLE,GLOW BOX LOCK,FOR LIGH
SLAVE CYLINDER,PUMP ASSY FUEL,O RING SPARK PLUG,SEALING KIT,REPAIR KIT FOR ACCESORIES WIPER,BRG CLU
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11
PRESSURE ROLLER,TEFLON,GEAR SET,POWER SUPPLY CARD,PRINT HEAD,DX FEEDER ASSY,WIC INK PAD,LOGIC CARD,
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Plain Copier Paper (V3) ISI Marked to IS 14490
Stabilizer link bar,Door hinge,Driven shaft assembly,Shock absorber,Clutch driven assy,Pressure pla
OEM Spares for Automobiles (Q2)
ATF Dextron-IID/ Dextron-II
OEM Spares for Automobiles (Q2)
Red Chilly,Turmeric,Coriander Seeds,Black Pepper,Large Cardamom,Clove,Cumin Seeds,Mustard Seeds,Tam
PIPE OIL,SPRING VALVE OUTER,FLEXIBLE PIPE,MICRO FILTER,VOLTAGE REGULATOR,HOSE FILTER AIR TO INLET M
Structure of JCO Living Shelter FEMS,Structure of Officer Living Shelter FEMS,Structure of OR Livin
PUF insulated prefab modular shelter of size 10 point 46 x 6 point 10 mtr including 1 point 5M wide
HYDRAULIC AEROSHELL OIL 41
TERBINAFINE CREAM,THEOPHYLLINE 400 MG TAB,THIOCOLCHICOSIDE 4 MG Tab,THYROXIN 12.5MCG TAB,THYROXINE 
SYP POTASSIUM CITRATE AND CITRIC ACID ORAL SOLUTION 100 ML,SYP TRICHOLINE CITRATE PLUS SORBITOL,SYR
RECOMBINANT HUMAN GROWTH HORMONE 15 IU HGH,SILICON HEEL CUP,SILODOSIN 8 MG PLUS DUTASTEROIDE 0.5 MG
RABEPRAZOLE 20MG PLUSDOMEPERIDON 10MG TAB,RANOLAZINE 500 MG TAB,REPAGLINIDE 0.5 MG TAB,ROSUVASTATIN
Electronic AVR 230V
SPRINKLE MOTOR 12 V TATA,HEAD LIGHT SAFARI,HEAD ASSY MG,HEAD GASKET MG,WIPER BLADE TATA,FAN AC BOLT
Discharge Book combined certificates,Security Training Certificate,Charter Certificate,Proficiency 
Mirchi Powder,Haldi Powder,Dhaniya Powder,Chicken Masal 100 gms pkt,Sabut Dania,clove,Sabut Mirchi,
Etoricoxib 120 mg, Tab,Indomethacin 25 mg Tab,Tramadol HCl 50 mg Tab,Aceclofenac 100 mg Tab,Febuxos
Ordinary portland cement grade 43,Coarse sand,20 mm stone aggregates,40 mm stone aggregates,Hardcor
MT ITEMS 1,MT ITEMS 2,MT ITEMS 3,MT ITEMS 4,MT ITEMS 5
Fast Recovery Diode IN5822,IC Buffer Line Driver SMT 74 FCT 1632,AD 8051 Amplifier,IC DAA CVN 10 Bi
AIR PRESSURE PIPE,SUSPENSION BUSH SET,TIe Rod End,AIR PRESSURE HORN,Gear lever dust cover,ARMETURE 
Cement,Non Skid Ceramic Tiles 300 x 300mm,Non skid ceramic Tiles 600 x 600mm,Gypsum tiles 7mm,Stone
Real Time PCR Kit for Equine Influenza (96 REACTION TEST)
Fruit Juice,Lime Based Soft Drink,carbonate soft Drink
LV2ICVS, NKICVS0027, STARTER PUSH BUTTON,LV2ICVS, NK000241, FLY WHEEL SEAL,LV2ICVS, NKICVS0028, CLU
Apron,Plastic Bucket,Plastic Mug,Mattress,Borosil Bowl,Casserole large,Casserole medium,Casserole s
Room Heater,Kerosene Wick Stove 3 Ltr,Tea Hot Case 5 ltr,Tea Thermos Steel 1 ltr,Water Camper Hot a
Wall Fan,Standing Fan,National Flag,Ord flag,Electric Kettle,TV 32 Inch
Fire Extinguish Ball,Reflector jacket,Batton Light,Fist Aid Kit,Portable Fire Extinguisher,Security
Laminating Machine,Laser Jet Printer,Paper Shedder,Search Light,UPS,Small Plastic Box Transparent F
LAYING OF HIGH QUALTY GRASS TURF,PROVISION OF SPRINKLER SYSTEM,MOTOR CONTROL POST,MARKING OF FOOTBA
Brush Cutter,Computer Revolving Chair,Weighing Machine,Blue Plastic Bin Container Small,Hydraulic H
Repair of rear gate hydraulic system,Paint and denting of inner and outer body,Repair of seat,Inter
OEM Spares for Automobiles (Q2)
Engine Oil Filter,Diesel Filter,Air Filter,Engine Oil Filter,Diesel Filter,Air Filter 35KVA,Overflo
Spine Engines,Batten Nail 0.5 mm,Batten Nail 1 mm,Batten Nail 1.5 mm,Batten Nail 2 mm
Ber Clutch Release,Cable Assy Speedometer,Ring Seal Exhaust Pipe,Brush Gear Assy,Pressure Plate
Pump water,Solenoid Switch,Hand Brake Assy,Field Coil Assy,Solenoid Switch,Rear Brake Booster Assy,
CLUTCH RELEASE BRG,CLUTCH DISC ASSY,CLUTCH COVER ASSY,OIL SEAL COVER REAR END,SEAL N S
HYD HEAD,SUPPLY PUMP,ROLLER PIN,ROLLER BRG,DRIVE SHAFT,PRESSURE CONTROL VALVE,SOLENOID VALVE,TD PIS
Blanket Superior (Defence) (Q2)
AC BELT,STOPPER DOOR,SUSPENSION BUSH KIT,FUEL FILTER,KIT FOR DOJ JOINT BOOT,AC FAN,AC CONDENSOR
AC 1point5 Ton Dual Inverter Super Convertible 6 in 1,Stabilizer V Guard 90v,AC Wall Stand,AC water
Light Weight Running Shoes (V2) (MHA)
Provision of 02 x Split AC Hot & Cold (Laboratory & Minor OT)
PT Uniform ( Sports Shorts ) - Defence
Room Freshener,Hand Sanitizer,Glass Cleaner Colin,Surface Cleaner Disinfectant,Floor Cleaning Solut
PLC based fire alarm system,Online UPS (V2)
Lubricant Artic Weather
Capacitor Assy,Main Board,DC Line Protector,Main Harness,Vicor 24V to 12V DC
Cold Drink (Aerated water)
CABLE COMPLETE FOR TATA 2.5 TON,KNUCKLE BEARING FOR TATA 2.5 TON,KNUCKLE BUSH FOR TATA 2.5 TON,CLUT
DUAL BRAKE VALVE ASSY,STARTING RELAY,IGNITION COIL,CLUTCH CABLE,ACC CABLE
After ME Folder,Weeding Herbicide medicine,Snake repellent powder,Nylon Grass cutting wire,Replacem
M4 CHIP LAPTOPS
GENR SET 5 KVA KIRLOSKAR D8.319.03.0.00,GENR SET 5 KVA KIRLOSKAR 11.203.09.0.00,GENR SET 5 KVA KIRL
LV7 TMB 2786 1599 9966 STARTER MOTOR 24 VOLTS,LV7 MARUTI MAJ 10100M73D00 HALF ENGINE ASSY 4 VALVE M
3253, Accumulator 12V,3160-95-12-150, Servicing Platform,3130-95-00-026.3, Servicing Plateform
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Mattress,Bed sheet,Pillow,Clothing stand,Slipper,Bucket 20 Ltr,Bucket small,Mug,Electric Kettle,Wal
USB Cable,HDMI Cable,Amplifier Cable,Digital Frequency Mapper,RW CD
FOL LEDGER,LOG BOOK,BEETEL PHONE REPAIR,UMBRELLA,REGISTER 100 PAGE,DRAWING SHEET,V7 PEN BLUE,V7 BLU
Insulation Tape,Thread Tape,Abrasives Clotch Emery,Electrodes Welding Rod,Pressure Pipe 22X22,Press
High Pressure Diesel Tank Cleaning Device Wheeled,Leather Hand Gloves,G P Cut of Wheel,4 Chain Hook
MAGAZINE ROUND,SLING ASSEMBLY,SLING ASSEMBLY SMALL ARMS,CORD NYLON PULL THROUGH 1A,BRUSH CLEANING B
TORCH HAND JANTA 300 TL TYPE,GLOVES PROTECTIVE LARGE,GLOVES MT,WAX SHOE MAKERS AND SADDLERS,SHIRTS 
Maintenance Box for EPSON L3150,Developer for Xerox B 1022,Drum for Xerox B1022,DCB for Xerox B1022
CABIN SHOCKER,BEARING ROLLER NEEDLE,BRAKE SWITCH RELAY,PARTS KIT BRAKE CHEMBER,PARTS KIT FOR SPRING
Camera for CCTV System (V3) (Q2)
PETHEDINE 50 MG 1 ML INJ,KETAMINE HCL 50 MG ML 2 ML INJ,Ketamine HCL Inj 50 mg ml 10 ml Vial,NALOXO
Injector Nozzle 2.5 ton,Clutch Cylinder Assy,Sleeve Cylinder Assy,D C Wire 6mm,Door Handle MG Left,
Clutch Master Cylinder Kit,Gear lever KIT,Clutch Cylinder Rep kit,Sleeve Cylinder Rep Kit,Fuel Pipe
Alternator 12V,Starter Motor 12V,Oil Seal,Wheel Valve Tubless Valve,Sensor
Cable,Base A Support,Plug,Dipole,Case Carrying
trail camera
FLUPIRITINE MALEATE 100 MG TAB,MESALAMINE DR 800MG TAB,MIRABEGRON 25MG Plus SOLIFENACIN 5MG TAB,MOM
Patient Slide Board
BEML 220G Air Filter Elements Inner outer,BEML 220G Hydraulic Filter,BEML 220G Bush Pin,BEML 220G o
Tab Donepzile 10mg,Tab Duloxetine 20mg,Tab Dutasteride 0point5mg,Tab Enalapril Meleate 10 mg,Tab En
UTP Cat 6 Cable,eight TB Data Storage Device Hard Disk,NVR 8 Channel,PTZ Camera 360 degree day and 
Kit of Estimation of Albumin 50ml bott 1 box Aspen Company,Antistreptolysin o test latex agglutinat
Isosorbide Dinitrate 10 mg Tab,Itraconazole 100 mg Cap,Ketamine HCl 50 mg per ml 2 ml Inj,Ketoconaz
Behind the Ear Hearing Aid (Digital)
Mispa i2 CRP kit of 30 tests,Mispa i2 D-Dimer kit of 15 tests,Mispa i2 Ferritin kit of 15 tests,Mis
Tropicamide 1per with 5per Phenylephrine eye drops bott of 5 ml,Inj botulinum toxin A 50 units for 
Clindamycin phosphate 1per topical gel Tube of 10 gm,Cyclosporine A micro emulsion 25 mg Cap,Calami
Repair of Injector
FUEL FILTER SPIN TYPE,OIL FILTER,AIR FILTER,FUEL FLEXIBLE PIPE,FUEL FEED PUMP,FAN BELT,AMP METER AC
IGNITION COIL,CLUTCH PLATE,PRESSURE PLATE,RELEASE BRG,PILOT BRG,ENG MTG PAD,CHAIN SPROCKET KIT
2525-5010-5817,1132-3908-453,390-6251,2570-4915-6916,17110-83000,51540M80110,2786-5010-5802,2574-58
Fuel Flexible Pipe,Oil Filter,Meter Elect Frequency,Fuel Filter Top Cover,Hose,Lub Oil Filter Eleme
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6
ABO OBLIQUE RhoD Forward and Reverse Grouping Card Pack of Card 24 Matrix Gel Card,AHG Coombs TestC
DISC BRAKE PAD SET,AC VALVE,OIL FITLER,AC FITLER,SHOCK ABSORBER ASSEMBLY,MUD FLAP,FOG LIGHT ASSEMBL
LEVOCARNITINE 1 GM INJECTION,LEVOSULPIRIDE 25 MG TAB,LIQ PARAFFIN 100 ML BOTT,LITHIUM CARBONATE 300
PT Uniform ( Sports Shorts ) - Defence
Enamel, Synthetic, Exterior (A) Under Coating (B) Finishing Paint (V3) Confirming to IS 2932
Light Weight Running Shoes (V2) (MHA)
DMR Set alongwith Charger for QRT and Incident Mar
Custom Bid for Services - AMC of 42 Numbers of Computer and 28 Numbers of Printers
Steel Shelving Cabinets (Adjustable Type) confirming to IS 3312 (V3),Steel Shelving Cabinets (Adjus
Z7/ISRAEL-K008424C, Servo Amplifier KSA 1
NOZZLE,PLATE CLUTCH,DISC CLUTCH,FLY WHEEL,RELEASE BRG,KIT PAD ASSY FRONT,SYNCHRORING 5TH SPEED,SIDE
HHRS (Hand Held Radio Set) DMR R7 Qty 6 Nos with one spare Bty each set & 1 Pgme cable with SW
Lignocaine Hcl 2percent Without Adrenaline 30 Ml Inj Suitable For Ophthal,Human Insulin Analogue Gl
HALF CLAMP,CAP SCREW DIFFERENTIAL,HYDRAULIC OIL COOLER HOSE,HOSE,SCREW M8 X 50,TIE ROD,ARM,LEVER,DI
DERATION TANK,SPEEDO METER CABLE,ASSY CLUTCH BOOSTER,TENDOM MASTER CYLINDER,PUMP ELEMENT,FLY WHEEL 
Cover Assy Clutch,PAD Set,Radiator Assy,Bearing Frt Wheel,Door Lock Assy
Injector assy with holder,Air compressor assy,Eng Mtg pad,Radiator fan assy,Inlet hose,Clutch brake
Behind the Ear Hearing Aid (Digital),Behind the Ear Hearing Aid (Digital),Behind the Ear Hearing Ai
FRY PAN,KADHAI 05 LTR,KADHAI 03 LTR,PATILA WITH LID,GAS CHULHA WITH LIGHTER,TEA PAN,PRESSURE COOKER
Veh Loc Tracking Device ALS,Sim Subscription 1 Yr ALS,Equipment for installation of vehicle locatio
Two way encrypted Audio Messaging System,Power Supply for two way encrypted Audio Messaging Sys,Mou
Kit Prothrombin Time Test 5 ML,Water Cultrue Kit commercially prepared,Kit Bio Red Contro L1 12 x 5
Tank Mule MK-4 (Defence) (Q3)
Linoleum Sheet & Tiles (V2) Conforming to IS  653
Tent Extendable Frame Supported 4M and 2M Complete with Accessories (V2)
Custom Bid for Services - To Carry Out Soil Investigation for Provision of Training Shed at RVC Mee
OTE,2 by 4 Port POE Switch 01 x UP Link Port,08 Port POE Switch,1 TB Hard Disc,Fiber Cable 2x4 Core
COVER ASSY CLUTCH,DISC CLUTCH,BRG CLUTCH RELEASE,COIL ASSY IGNITION,PLUG SPARK,LINE SHOE ASSY,WHEEL
Engine Mounting Pad,Switch Lock Ignation,Hose Air Pipe,Accelerator Cable,T D Piston,Pressure Contro
Custom Bid for Services - BOQ item No 1 Semi Skilled Electrician per shift of 08 hours       1638  
AP3 Grease
Custom Bid for Services - Developing mobile app for IOS apple Iphone devices for station Ezhimala
DISC COUPLING,ROTARY SWITCH,ROTARY SWITCH,SWITCH PUSH,INDICATOR,FUSE,FUSE,FUSE 2A,FUSE 9A,FUSE 5A,W
COOLING COIL,OIL FILTER,AIR FILTER,FUEL FILTER III PIN,FUEL FILTER II PIN,COMPRESSOR ASSY,CONDENSOR
Honey Sucker (Cleaning of Septic Tanks)
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
HEAD CYL,PISTON RING SET,PISTON RING COMPLETE SET,PISTON,BELT V A 57
Intel Core i5 with 13th Gen for Mini PC,HDMI 2.1 and at least 3 USB port for Mini PC,Ram 16 GB for 
LV7 T 815 CIRCUIT BREAKER,LV7 T 815 SPEEDOMETER CABLE,LV7 T 815 ARMATURE ASSY,LV7 T 815 ELECTRO MAG
MS Frame Box Pipe at Squad Posts with JSW Tin Sheet Covering upper Side
Crystal Glass,Cup and Saucer,Coffee Mug,Quarter Plate,Half Plate,Full Plate,Tea Set,Drinking Glass,
Thunderbeat 9mm 20cms Open Extended Jaw Model No TB - 0920OE-
Field Coil Assy TATA,Carbon Bush Plate TATA,Clutch Plate LBPV,Pressure Plate LBPV,Slave Cylinder Cl
Propeller Shaft Nut Bolt TATA,Oil Sending Unit TATA,Oil Seal,Brake Pad Front LBPV,Needle Bearing,Fl
Supply and Construction of chain link fence 2150 Mtr,MS angle iron fencing post 3.20m long,MS angle
Antenna 136 174 MHZ VS WR 3 1 Max Omni RX Antenna,Transistor Fet N Chan Type UF 28100V,Cable Assy F
Rubber Armoring,Eye Piece,OG Cover,Transistor 6686,Diode 30 06A,Bridge Rectifier,Diode A6T,TR PO2,B
TITLE 1,TITLE 2,TITLE 3,TITLE 4,TITLE 5,TITLE 6,TITLE 7,TITLE 8,TITLE 9,TITLE 10,TITLE 11,TITLE 12,
Toothpaste (V2) as per IS 6356 (Q4)
Z3-LV7-FC-WT-BEL-474 COMPRESSOR MOTOR
Replacement of Garden Light in Walking Plaza at Bathinda Cantt
Repair and Maintenance of Bailey Panel of Bailey Bridge,Repair and Maintenance of Transom of Bailey
Repair and Maintenance of Main Girder of Bridge Assault Float Heavy,Repair and Maintenance of Cross
BRAKE BOOSTER ASSY REAR TATA NEW MODEL,BRAKE M CYL REP KIT OLD MODEL,BRK LIGHT SWITCH,BRUSH SET,BUS
4X4 CABLE TATA OLD MODEL,ACC CABLE TATA OLD MODEL,AIR DRYER REP KIT TATA OLD MODEL,ARMATURE ASSY 12
Cement OPC 43 Grade packed in HDPE bag each 50 Kg wt conforming to IS 8112 - 1989 Make - Birla Gold
Store shelter Size 10.44 m x 6.1 m x 4.75 m height with 1.5 m verandah as per technical secificatio
Store shelter Size 5.22 m x 6.1 m x 4.75 m height with 1.5 m verandah as per technical secification
Annual Maintenance Service - Desktops,  Laptops and Peripherals - Laptop; Dell,Annual Maintenance S
Power Window Machine with mot,Radiator Flexible Hose,Gasket Detent Cover,Retainer Oil Seal,Miniatur
BATTERY FUSE 10A,BATTERY FUSE 5A,FUSE 200A,FUSE 200,FUSE 275A,FUSE HOLDER DPK 1 1,FUSE BOX ASSEMBLY
Atta 5 Kg,Atta 10 Kg,Atta 20 Kg,Atta 25 Kg,Atta 50 Kg
Overhauling of self starter incl replacement of counter teeth gear bentex carbon bush spring and ta
ALTERNATOR ASSY,AVR,KIT COMPLETE,SELF STARTER,CYLINDER HEAD,PISTON RING SET
Killikit set for self starter of five Ton fork lifter,Brass Bush set for self starter of five Ton f
Overhauling of Rotary pump
A3 4020-000198 Rope Nylon Climbing,F1 5120-001582 Spanner Ring Bihex Cut Double Ended Cran,F1 5120-
Self starter assy BOSCH,Pneumatic solenoid valve,Oil filter,Hand brake lever,Brake booster rear,Fue
TOTAL SECURITY,TOTAL PROTECTION,OFFICE SOFTWARE 2021,OFFICE SOFTWARE 2024,OPERATING SYSTEM SOFTWARE
HORN ASSY HIGH TONE,SHOCK ABSORBER FRONT,SHOCK ABSORBER REAR,WATER PUMP,PARTS KIT BRAKE CHAMBER,BRU
Construction of Basket Ball Court with Synthetic Surface, Fiber Glass Boards, Poles, Protection Lay
Aggressive cutter shaver blade for Arthroscopic shaver system,Disposable suture passer for meniscus
Card Assy TX Switch 1 point 2 GHZ,PCB of Bty Charger,Comm Line Prot CKT Panel Elect Circuit,CMOS Bt
Tiles,Anti Skid Tiles,Cement Bags,Sand,Aggregate 20mm,PCC Bricks,Angle 2 ft x1.5 ft,Self Tapping Sc
penumatic valve,door beading,hyd hose assy,air pressure pipe,wiper rope,moniter assy
Milk Made 400gm,Pickle all type 500gm,Tomato sauce 500gm,Chilli Sauce 1Kg,Soups Tomato Mix Veg Chic
gear lever end,gear shifter end,gear shifter,radiator hose,wiper arm,wiper blade
DISC,SOCKET WRENCH NO 17,HYDRAULIC CYLINDER RAM,THRUST PAD MED MOUNTING PAD,PVC CONDUCT PIPE 25 MTR
Drone
chain sprocket set,cabin light,wiper blade front,wiper blade big,wiper blade small,clutch boster as
Haldi Powder Everest,Mirch Powder Everest,Dhaniya Powder Everest,Dal Chini,Ajwain Catch,Badi Ellach
Pinion,steering Lock,Bush,Inner Plate,Push Rod,Regulator Control Electrical,Circuit Breaker,Ignitio
clotrimazole mouth paint 1 pct bottle of 15 ml,cyclosporine a micro emulsion 25 mg cap,Methotrexate
DLF 35RA Engine with Exhaust
Facility Management Service- Manpower based (Version 2) - Residential; TREE TENDING; Unskilled
High End Window Desktop Intel core i7 16 GB RAM,High End Window Desktop Intel core i9 32 GB RAM,M4 
GIS Platform Based Digital Sand Model Room
Flameproof Flood Light 100W,3 Pin Electric Plug 15A,Water Storage Tank Cover,Plywood 12mm thick 7 x
Custom Bid for Services - TECHNICAL TRAINING FOR UPGRADATION OF LEGACY PACKAGE
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
ABSORBER ASSY REAR SHOCK,TANK ASSY WASHER UNIT,AC FILTER,FUEL FILTER,OIL FILTER,BRAKE SHOE SET,AIR 
SLEEVE,BEARING,DOWEL,JET ASSY,TURBO CORE,WATER PUMP ASSY,OIL SEAL,O RING,BRAKE PIPE LINK,ADOPTER BR
Neck Tie,Shut of cock,steel Rope,Red Reflector Tape 120 Mtr,Yellow Reflector Tape 120 Mtr,TRL Relay
Rollers,ROLLERS PIN,VANE PUMP,DISTRIBUTOR HEAD,CROSS DISC,GEAR LEVER KIT,CYLINDER HEAD TOP COVER,HO
FD SECURITY LIGHTS
FD SECURITY LIGHTS
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others
MT Items 1,MT Items 2,MT Items 3,MT Items 4,MT Items 5,MT Items 6,MT Items 7
Search Light,Stamp Pad Medium Violet,Stamp Pad Black,Classik PP Binding Cover A4 Sheet,Carbon Paper
TEFS 4M UNIT F OUTER PV D DYED FABRIC,LNR INR WITH PV DD FABR FOR TEFS 4M UNIT,F OUTER WITH PV DD F
12 V 7 AH Battery,Mother Board H 61,Mother Board H81,Keyboard Mouse Combo,Monitor,DVD Writer
Draw Sheet Disposable,Dressing Medicated adhesive 25 cm x 6 cm in single strip pack,Ear buds Bott o
Disposable sterile surgical gloves S 7.5,Disposable swab stick Pack of 100,Double Lumen Catheter Ca
2816-7230-0175,281683400109,281683400245,286314495801,2880-5890-3519,2880-5890-3517,2786 1599 9802,
Bricks,Cement,Sand,Tile Cutter Blade,Floor Tile 4x2 Feet as per sample,Granite as per sample,Wall t
Lightening Conductor
Refined Sunflower Oil (V2) (Defence)
HOSE AIR CLEANER NO2,HOSE AIR CLEANER NO1,REP KIT FOR WIPER MOTOR,REP KIT DUAL BRAKE VALVE,HOSE RUB
LV7HMV8X8AL, X74953001, ARMATURE STARTER MOTOR,LV7STLN, NKSTLN0002, CLUTCH DRIVE- OVER RUNNING,LV7S
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Healthcare,Manpower 
Oil OM-58
WATER PUMP,OIL SEAL,OIL SEAL 1,SEALING COMPOND,HOSE,CROSS ASSY,ASSY PULL CABLE,WATER TEMP GAUGE,SEA
Antenna 50 OHMS 136 174 MHZ Type GPA 150 Antenna IV,Tablet PC HDD 40 GB 4200 RPM5 V DC Type,Spring 
Multipurpose Portable Programming and Analysis System for training
Cidex OPA 0.55 percent Ortho phthaldehyde,Adapalene 0.1 percent tube of 15 gm,Clindamycin phosphate
Military Standard A I O
High End Desktop Computer (Q2)
LV7/2.5TON(2786-0199-990) NOZZLE,LV7/2.5TON(1466111626) CAMPLATE,LV7/2.5TON(1468336671) DISTRIBUTOR
CRDS OR Living Shelter 4 Men with Solar Panels
Nivia Encounter Shoes,Football Kit Full Sublimation,Basketball Kit,CRT Bails,Football Goalkeeper Gl
Rod Stand,Gym Wire 6mm,Handle Griping Sleeves,Seat Cover,Rod Zig Zag 2 x 4 ft,Rod 3 x 5 ft,Rod 1 x 
NR Sheet Pad 100 Page,Mil Trunks Red Docket 70 Page,Mil Trunks Black Docket 50 Page,Cooler Ducting 
Repair and Overhauling Service - Repair of RPAV (Remoterly Piloted Arial Veh) (Trinetra); Repair of
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
CONSTRUCTION OF SLITHERING PLATFORM WITH ROCK CLIMBING SURFACE SINGLE FACE HIGHT 50 FT plated 14ft 
40mm HDPE for OFC Conduit,Indta 360 Degree Camera,65 Inch Interactive Display,16 Channel 4K NVR wit
Bracket Plate for Chasis,Circuit Breaker bty cut off switch,Repair Kit for main Cyl Clutch,Fuel Fil
DRIVE ASSY,BRUSH CARRIER ASSY,BRUSH SET,KIT BRAKE LINING SET FRONT STD,BRAKE PAD,WIPER BLADE REAR,B
Distributor Head,Injector Nozzle,Engine Mtg Pad,Brake Shoe Assy,Rear Hub Seal
DRIVEN PLATE FOR CLUTCH,CLUTCH RELEASE BEARING,SOLENOID SWITCH ASSY,STEERING MTD COMBI SWITCH,ASSY 
cluth plate assy,gear box oil seal,brake master cyl,combination switch,wiper blade assy,tank set re
CCTV Dash Cam's
Reverse Osmosis based Point of Use Water Treatment System for Drinking Purposes (V3) as per IS 1624
Integration Table with Chain vice
Pull Cable ACC,Solenoid Switch,Cover Assy,Ring Gear,Reserve Water Tank,Switch,Fuel Pump Assy,Flange
ARMATURE ASSY,SOLENOID SWITCH,DRIVE PINION,BEARING TAPPER ROLLER,INJECTOR SEAT GYPSY,SA OF FLY WHEE
Clutch Booster Assy,Spider Brg,K M Cable,4 x 4 Cable,Thermostat Housing,Fuel Fill Up Hose,Thermosta
SYSTEM PROTECTION VALVE KIT,GLOW PLUG TIMMER,FLANG CARBORATOR,BUSH SET,BEARING SET CONNECTING ROD,B
FIRE FIGHTING EQUIPMENTS
3 x 3 inch MS Pipe,Crown Pully 1 Inch,Axle Teeth Pully 6 Inch,Axle Teeth Chain,Teeth Crown 6 Inch,R
Ramp Loader
Custom Bid for Services - SNC OF UNSV INVERTER MANAGER
Smart Map
Active Indoor LED Data wall 8 x 5 feet P 1.86 COB with all accessories and ceiling mount,Online UPS
12A Cartridges,88A Cartridges,166A Cartridges,110A Cartridges,Canon Pixma MG3070S Printer Head Comb
1 x 1 inch MS Pipe,GI Wire Mesh of 4mm wire,Route Mkg Pole 2.4 Mtr,Welding Rod,Cutting Wheel 14 Inc
MOSQUITO BREEDING PROOF DESERT COOLER
Bearing 4 Inch,2mm MS Plate 1 x 2,2 x 1 inch MS Pipe,1 inch MS Flat,GI Wire Mesh of 2mm wire
ASSY FUEL FILTER FOR SAFARI,ASSY OIL FILTER,ASSY AIR FILTER,KIT PRE FILTER,CLUTCH MASTER CYL,CLUTCH
Inj Naloxone 0.4 Mg,HME Filter For Ventilator Circuit,Central Venous Catheter Kit Triple Luman 16g,
Disposable Laparoscopic Port blade less Trocar 5 mm disposable,Disposable Laparoscopic Port blade l
Custom Bid for Services - Job order for repair to vehicle EICHER BA NO- 07D-173270N
PROVISION AND CONSTRUCTION OF VIEW CUTTER (1 KM)
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Commercial; Power 
Cell Pack,Stromatolyser,Cell clean,Cell pack H-560 20 ltr pack,Lyser-1 H- 560,Lyser-2 H- 560,Cell c
Designing Software (V2) (Q2)
Video Laryngoscope (Q3)
Motion Sensor Light (Solar Based)
INTERMEDIATE BRAKE HOSE,EGR JELLY,OIL SUMP,BRAKE SHOE LOCK,MOUNTING SILENCER,GASKET CYLINDER HEAD M
Needle Bearing,Housing,Plate,Field Coil Assy,Coil System,Solenoid Switch,Pole Screw,Clutch Cyl Assy
Clutch Master cylinder assy ALS,Clutch booster ALS,Fuel pipe 19x19 ALS,Fuel Strainer ALS,Fuel feed 
Chilly Powder Mirchi Powder,Turmeric Powder Haldi Powder,Coriander Powder Dhaniya Powder,Coriander 
ROD ASSY CONNECTING,SELF STARTOR ASSY,CLUTCH PLATE,PRESSURE PLATE,LIGHT BLACKOUT,ROTARY SWITCH
Chilly Powder Mirchi Powder,Turmeric Powder Haldi Powder,Coriander Powder Dhaniya Powder,Coriander 
ISOSORBID MONONITRATE 20 MG TAB,Isosorbide Dinitrate 5 mg Tab,KETOROLAC 10 MG TAB,Knee Caps Size L,
ESCITALOPRAM 10 MG PLUS CLONAZEPAM 0.5 MG TAB,ETHAMSYLATE 500 MG Tab,Fenofibrate 160mg TAB,FENOFIBR
CHOLINE SALICYLATE 8PER PLUS LIDOCAINE 2PER DOLOGEL ORAL GEL,CILNIDIPINE 10 MG TAB,CINNARIZINE 25mg
Hair Removal Diode Laser
Intracranial thrombectomy device for stroke,Intracranial Thrombus aspiration device for stroke,PVA 
Z1/5985-012708, Counterpoise Antenna Radial
Z9/MISC-EXIDE-A512-55A LV6/MT4/6140-005340, Battery 12V 55 AH at 20 HRS Rate
SIDE MIRROR LSV,FOG LIGHT ASSY TATA,ROOF LIGHT ASSY TATA,WIPER MOTOR ASSY 24V,DOOR CLUTCH ALS,SPRIN
2 Core 6 MM Coper Wire,LED Light 30 Watt,Electric Gloves,Bed Switch,Holder,Adeptor 48 Volt 5 Amp wi
Upgradation of High Intensity Fitness Training Circuit
H4 8135-000150 Paper Wrapping Reinforced With Hessian Cloth,H4 8115-000522 Boxes Fibre Board Rigid 
Base Work,Edge wall,Roof Fiber,Layer Syenthetic,Volleyball poll,Steel Structure,Lighting Sys,Chain 
Fire Extinguisher Trolley Mounted Mechanical Foam Type 50 Ltrs Capacity
Black Pepper,Chilly as per IS 2322,Large Cardamom (Badi Elaichi) as per IS 13446,Spices And Condime
Dewormer Fenbandazole 3g bds,Dewormer Albendazole,Powder Nagasunt 40gm,Podwder Neosprin,D Mag Spray
Combination switch,Cable assy control,Pump fuel transfer,Speedometer cable,Wiper motor 17w,Tensione
Laundry Service - Commercial/Residential/Transport/Industrial Purpose
Sugar (V2) (Defence) (Q2)
Sharpy light BSM 10R,Par light bisun 3 watt with XLR jack,D Max 512 stan mixture,Pilot make stan,XL
SILICON VACUUM CUP 60MM DIAMETER WITH TUBING,SILICON VACUUM CUP 65MM DIAMETER WITH TUBING
Self Starter Assy,Amp Meter,Volt meter,Hours Meter,Linner Shim,NRD Valve,Door Hinge,Fuel Filter,Fue
Cable Accelerator Lt Ambulance Xenon,Cover Assembly Lt Ambulance Xenon,Driven Plate for Clutch Lt A
Welding Hand Gloves,Measuring Tape Fibre 30mtr Lenght,Goggle Transparent for Cutting,Tool bag,Weldi
Acebrophylline100mg and N-Acetylcysteine 600mg,Alfuzosin 10mg Tab,Amlodipine 2.5mg Tab,Amlodipine 5
LV2/ICVS 765-15-157 BODY
Z7/BEL/180000222218 REFLECTOR ASSY
Jam Td,Tomato Sauce,Orange Squash,Custard Powder,Corn Flour,Cornflakes,Match Box,Horlicks,Lime Squa
Register 300 Pages,Register 200 Pages,Transparent Tape 2 inch,Transparent Tape 1 Inch,Transparent T
Protective PX-2
INJ METHYLCOBALAMINE MECOVIT 500 MG,ISOSORBID MONONITRATE 10 MG TAB,METHYLCOBALAMIN 1500MCG PLUS AL
Air filter,Oil filter,Brake hose,Urea for bolero,wheel alignment wheel balancing of bolero,DEF pump
Clutch assy,Self EGT assy with pinion,Head light bulb,Rear door catch,RR Unite,Combination switch,C
Manpower Outsourcing Services - Fixed Remuneration - Housekeeper; Sweeper; Not Required,Manpower Ou
OIL FILTER ELEMENT,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
Z7-BEL-175000239848 DSRA Protective Covers Mtrl No 10430826,V5-4935-000210 CDRs Sight Control Unit 
Harpic 500 ml,Room freshener,Phenyle 01 Ltr,Toilet Brush,Liquid hand wash 200ml,Broom coconut,Broom
Comprehensive Maintenance Contract (CMC) of ERBA Semi Authomated Biochemistry Analyzer Model EC-5+ 
Autel Robotic Evo Nano & Lite Drone
Preservation MIL PRF-38299
Polaris Premium 50/50 Antifreeze Coolant
Raxine Black,Foam 4x6x3,Foam 1x6x3,Ply wood 12MM,GAS 134A,WD 40,AVR,Fevicol SR 998,Fuel Filter Assy
Chicken (Broiler) Alive
V5-IVE-2167 Driver's Day Periscope (Central) Mtrl No 10442652
Iron sun flame,Water Bottle,water pipe,Water bottle thormous,Bed sheet,Pillow with cover,Blanket do
10569033 LV7 T 816 443 611 195 0 T COUPLING T376516,10321511 LV7 T 815 130 017 231 614 LAYSHAFT GEA
OIL FILTER ELEMENT,TRANSMISSION OIL FILTER,FUEL FILTER ELEMENT,WATER SEPRATOR FILTER ELEMENT,AIR FI
2 MP IP Camera Metal Body,PoE Switch 4 1 Gigabyte Port,LAN Cable,LAN Cable Laying Charge,Camera Pol
Customized AMC/CMC for Pre-owned Products - --; --; Comprehensive Maintenance Contract (CMC); 1; No
Chain Saw 18,Sand Bag,Garden Bench,Indian Style Commode,Milton Water Camper 20 Ltr,Casserole,Milton
ASSY UNIVERSAL JOINT,AIR PRESSURE PIPE,BEARING BUSH CE,ASSY RELEASE BEARING,WIPER BLADE REAR,KIT PA
NIPUN Mine Miniature Model,NIPUN Mine Cut Model,ULKA Mine Miniature Model,ULKA Mine Cut Model,PARTH
Roasted kaju,Kishmish,Rice Basmati Good Quality,Kabuli Chana,Roasted Chana 500gm,Daliya 500gm,Desi 
Structure of Combined Toilet Block,Structure of B Veh Shed,Structure of Combined Toilet Block CTB,S
Customized AMC/CMC for Pre-owned Products - --; --; Comprehensive Maintenance Contract (CMC); 1; No
AC repair kit
Green Fiber Sheet,Iron Pipe,Flex 6 x 4 Ojasvi Ekatees,Photo Framinig,Photo Print with phot Framing,
Customized AMC/CMC for Pre-owned Products - --; --; Comprehensive Maintenance Contract (CMC); 1; No
GASKET SET KIT,NOZZLE,CR BEARING,ROTARY SWITCH,FUEL PIPE BIG,FUEL PIPE 19 BY 19
VMR METER,SEAL KIT,ROTARY SWITCH,FREQUENCY METER,BATTERY LEAD,FUEL GUAGE
CLUTCH PLATE,PRESSURE PLATE,HOSE COOLANT,FRONT WIND SHIELD GLASS,AIR FILTER,STARTER MOTOR 12V
KEYBOARD WITH MOUSE,KEYBOARD AND MOUSE 1,SMPS,USB KEYBOARD WITH MOUSE,HP KEYBOARD AND MOUSE
SEAL FRONT OIL,S A OF PIPE 5 8,UPPER BALL JOINT,THERMOSTATE VALVE,STARTER ASSY REPAIR KIT,AIR CLEAN
LV1-ARJ-R900784029 Corrugated Hose Mtrl No 10612301,LV1-ARJ-R900217733 Flange Complete Unit Mtrl No
Plain Copier A4 Size Paper,Legal size paper 75GSM,Pen V 5,Stapler Large Size,Stapler Pin,Envelopes 
LV7T-815 4X4, 207-902-598-4, INJECTION FUEL PUMP ELECTRIC PUMP,LV7T-815 4X4, NKTATRA00012, HIGH LOW
Battery Diagnostic Station
MAHINDRA MAXIMILE ULTRA COOL
LV7MARUTI, 33310-82010, ROTAR,LV7MARUTI, 15710M83F00, INJECTOR ASSY FUEL,LV7MARUTI, 5340-135143, MO
Annual Maintenance Service - Desktops,  Laptops and Peripherals - Printer (Colour, Laser, Composite
Banana,Mango,Papaya,Mussambies,Pineapple
67571225OH4357 K9BMPNBC GASKET,765711463 K9BMPNBC GASKET,AK150CTY LV1R90 COMPRESSORAVIATIONAK150CAK
5336381401 LV1R90 GASKET17203105P650,5330017028 LV1R90 GASKETDRGNO5405696,1722M02015SB1 LV1R90 GASK
Electric Motor 2 HP with Pump,Starter Panel with on off switch on wooden board,2 Inch insulation pi
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
NOZZLE 8X8 TATRA,NOZZLE ALS,NOZZLE 2.5 TON,WOODRUFF KEY,DRIVE GEAR
Pocker,Binder clip Medium,Finger wetting sponge damper,Pencil,Plastic paper weight,File Cover,Brown
HYDRAULIC HEAD,VANE PUMP,PRV VALVE,TD PISTON,CAM PLATE,CROSS DISC,ROLLER RING
Baclofen 10 mg Tab,Chlorzoxazone 500 mg Diclofenac Sodium 50 mg Paracetamol 325 mg Tab,Amoxycillin 
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6
Budesunide 1 mg Respules,Salmeterol 25 mcg Plus Fluticasone 250 mcg Autohaler,Spacer Device for inh
SEPTOPLASTY SET
J1 5120 001442 SHOVEL HAND ROUND NOSE 1 point 6 KGS,8020000036 BRUSH FLAT 50MM,3 7350 000011 BOWL E
Coolant pipe hose,Brake light switch,Fog light 12 volt,Spark plug,Assy clutch m cyl,Rubber hose VC 
Genr set 2 KVA Honda NK,Genr set 2 KVA Honda NK,Genr set 2 KVA Honda NK,Genr set 2 KVA Honda NK,Gen
Pipe Wrench 24 inch,Plumbing Tools kit for 15mm to 50 mm,Water proof tape 4 inch,GI gate valve 70 m
LV1/ARJ R900768507 (Material No 10482133) Travers Servo Package
Repair and Overhauling Service - built up trucks; TATA MOTORS; Yes; Buyer Premises
ALL IN ONE PC,MULTIFUNCTION PRINTER,SCANNER,KEYBOARD,MOUSE
Regulaor Cotrol Elect,Brush Set,Rectifier Assy,Relay Solenoid,Solenoid Electrical,Change Over Switc
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others,Manpower Outsourci
Volleyball,Volleyball Net,Trophy for Winning Team,Trophy for Runner Up Team,Medal for Winning Team,
ENG MTG PAD,FRONT BRAKE PAD,FUEL FILTER,FUEL PIPE LINE,FUEL PUMP,GEAR BOX OIL SEAL,IAC MOTOR,IGNITI
CHARGER,BATTERY LI-ION,ADAPTER,BATTERY LI-ION BS,BATTERY LI-ION BS1
Red Chilli Powder,Coriander Powder,Turmeric Powder,Cumin Seed,Mustard,Cloves,Cardamom Large,Tamarin
FERROUS BOMB LOCATOR
ASSY LATCH FR DVR LH,COTTER VALVE,SPRING OUT VALVE,SPRING IN VALVE,CAP SEALING,METAL SET THRUST STD
Tech Info Board on Flex Printing 4ft x 3 ft Outgoing Prayer,Tech info Board on Flex Printing 2ft x 
Batteries 9 V,Holder Screw 0.5mm,Holder Screw 0.7mm,Holder Screw 1mm,Tester LED Tube
SPARK PLUG,IGNITION COIL,SUSPENSION BUSH KIT,CLUTCH DISC,BRACKET PEDAL,BRG INPUT,BRAKE SHOE REAR,OI
CARBURATOR ASSEMBLY,PLUG SPARK,FUEL ON OFF COCK,FILTER FUEL,FILTER LUB OIL,BELT VEE AX 43LP 1131 HI
Servo Motors,Gypsum Screw three fourths,Gypsum Screw 1,Gypsum Screw 1.5,Gypsum Screw 2
CONTAINER PORT FOOD 4 PT 5 LTR MK IV,CONTAINER STOVE COOKER OIL 4 AND 6 MEN SET,FLASK THERMOS 0 PT 
Infusion set for insulin pump set of 10 Set Meditronic,LevoSalbutamol syrup 1 mgobilique5ml Bottle 
Epson Ink 0064,Cartridge Lexmark,Cartridge 88A,Cartridge 78,cartridge 12A,Cartridge 79A
Carbon Monoxide Sensor,Smoke oblique Fire Alarm,Solar Lantern,MT SHED electric items as per TS,OFFI
LV6-MT14, 2610-001597 TYRE PNEU 16.00 R20 22PR 173G AT
Sprocket Bearing,Floating Seal Assy,Sprocket Hub,Drive Gear,Bolt Sprocket,Final Drive Gasket,Bearin
Malarial antigen (PF(pLDH) Pan pLDH) detection of P. vivax, P. falciparum and P. vivax, P. ovale, P
25820 012872 PLATE CLUTCH PRESSURELV7HH,22201 GF6 000 DISC CLUTCH FRICTION,12237 GB4 305 GUIDE INLE
Statar Assy,Plug Spark,Pump Assy,Push Rod,Wiper Assy,Hose Pipe,Clutch Assy
Leather Cloth Black,SR 998,Sewing Cotton Thread 165 DTEX x 6 black 1000m t,sheet cellular 25mm thic
Rapid Chloride Permeability Tester
Group Planning Exercise Form,DIPR Form No 156 C Assessors jotting sheet,Set of GTOs Jotting Sheet,W
Auto CPAP Machine with Humidifier
IC 7343 of RS Stars V MK II,IC 3085B of RS Stars V MK II,BMC 1527 of RS Stars V MK II,BMC 1533 of R
Automatic waste Compositing Machine
PAYLOAD AMMUNITION (ANTI PERSONNEL) FOR INFANTARY DRONE
Infantry Combat Drone Rudra 2.0
MOTHER BD H 310,BTY 12 V7AH,RAM DDR IV 8 GB,PICK UP ROLLER,TEFLONE,PREESSURE ROLLER,RAM DDR III 8 G
K - 4 Crash Rated Boom Barrier (Q3)
Asphault Base Flour,Volleyball Court Accrssories with Supply and Fixing,Flood Lighting System,Layer
MOTHER BD H 310,DVD WRITER,BTY 12 V7AH,RAM DDR IV 8 GB,PICK UP ROLLER,TEFLONE,PREESSURE ROLLER,RAM 
Field Coil Assy,Brush Carrier Plate,Radiator Assembly,Fuel Feed Pump,Steering Pipe,Coolent Filter,F
Siren Tata Sumo Amb,Side Mirror Tata Sumo Amb,LED Bar Light Tata Sumo Amb,Self Starter Solenoid Swi
1 set of crank shaft brg 1 to 5,Bearing 6209 2z c3,coupling rubber element,fuse box,fuse box,heater
Wiring work,Connector,SMPS Power,commissioning Charges,Work for PTZ Camera,LED Monitor 19 HDMI Port
Sprocket Bearing for Dozer BD 50,Floating Seal Assy for Dozer BD 50,Sprocket Hub for Dozer BD 50,Dr
OMV 23 HYDRAULIC MOTOR,COMMANDER CONTROL PANEL,SUPER STRUCTURE PANEL,EMERGENCY CONTROL PANEL,WIRING
Custom Bid for Services - Hiring of an Agency for deployment of two resources for Data capturing in
Almirah Large steel with shelves overall size shall be 920 mm x 485 mm x 1985 mm and all as specifi
HDPE Jerrycans (30 Ltrs)
FD WSS SINTEX TANK 500 LTR
Manpower Outsourcing Services - Fixed Remuneration - Healthcare; Dietician; Post Graduate
FD WSS SINTEX TANK 10000 LTR
FD WSS SINTEX TANK 1500 LTR
Harpic 500ml,Lizol 500ml,Soft Broom,Phenyl white 1000ml,Colin glass cleaner 500ml,Dettol hand wash 
Grill fan guard BD 80,Grill fan guarrd BD 80,Grill fan guard BD 80,Grill fan guard BD 80,Grill fan 
Hiring of Transportation for conveyance of youth from various vills to destination and back,Hiring 
Air Compressor,Centre Bolt,Radiator Assembly,Lever Gear Shifting Control,Starter Motor 24V
pickle,tomato sauce,biscuit,vineger,matchbox
Supply and installation of Genr Set 58.5 KVA FOR REDI,Supply and installation of Genr Set 58.5 KVA 
Pin of leg 578002144652009,Left Bracket 578002523652063,Cable B36 578002644352117,Filter 5780026427
12 BORE PUMP ACTION RIFLE (PB)
Fuel Filter Cartridge 10X0620,Air Filter Element Outer 10X472,Loader Arm Bushes End 3B0076,Bucket C
Sanitary Round Register,Noting Sheet,E ticketing Form,Leave Certificate pad,Single Movement order p
printed file cover,printed white file cover,plain file cover,highlighter,whitener,sketch pen,reynol
Tablet , Laptop
533072011544776505432 LV2ICVS GASKET,5315720113846765101009 LV2ICVS GASKET,47207202602747650724 LV2
431072010245676578SB833 LV2ICVS COMPRESSORRECIPROCATING76578SB833,7653881 LV2ICVS GASKET,5330720117
17203105 LV1R72 GASKET,1750303704 LV1R72 GASKET,5405696 LV1R72 GASKET,17503037 LV1R72 GASKET,175401
42400001071 K9T72NBCNBC FILTERFAT100MDRGNOIMGA0006,176310191 LV1R90 GASKET,172321261 LV1R90 GASKET,
Hyd Head,PRV Valve,Vane Pump,Pressure Pump,Front Grill,Assy Turbocharger,Fuel Feed Pump,Ircuit Brea
Mirchi Powder,Haldi Powder,Dhaniya Powder,Dal Chini,Laung,Jeera,Sabut Mirch,Rae,Kali Mirch,Chholi E
Almonds,Cashew,Juice,Fruits,Milk,Black Channa,Desi Ghee,Kishmish,Energy Drink,Anjeer
Hexagon head bolt 384211920110,Timing Belt 21258060180,Cover Plate 240039358126,Plug 240039358323,T
ABST Disc amikcain,ABST Disc Amoxyclav,ABST Disc Ampicilin,ABST Disc Azithromycin,ABST Disc Bacitra
Equalizer,Ram,Hose,Bag,Pressure Plate,Ring,Clutch Plate,Lever Kit,Coil,Silencer,Bolt,Valve,Pressure
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Admin
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Fogging Machine (V2) as per IS 14855 (Part 1)
CPAP,BIPAP,Oxygen Concentrator,Digital Hearing Aid BTE,Wheel Chair Foldable Chromium Plated,Walker 
Dome Camera 2.4 MP,25 x IR PTZ Camera 250 Mts,40 x IR IP Bullet Camera 100 Mtrs,32 ch Network Video
Crawler Hydraulic Excavator (V2)
FLU PANEL WITH RSV DETECTION
Clutch Release Bearing,Universal Joint Assy,Pad,Wabco Clutch Booster,Control Valve Assy,Release Bea
Leather Cloth White,Leather Cloth black,Plywood General Purpose,Electrodes welding steel hard,cable
LV6/MT14, 2610-001575, TYRE CASING 1300 X 530 X533
5 MP Bullet Camera,2MP Bullet Camera,PoE Switch 4 1 Gigabit Port,LAN Cable,LAN Cable laying charge,
Mineral Water,Breakfast comma Launch comma Dinner,Purchasing of necessary medicine for Med Camp,Tra
Winter Route Marker
LV2 ICVS 5330-021360 765-33-56 GASKET,LV2 ICVS 5330400002014 675-05-97 GASKET,LV2 ICVS 533072023418
LV2 ICVS 5360720370452 SPRING FLAT 730-14-267,LV2 ICVS 2510720305501 765-47-658 MUDGUARD VEHICULAR,
MS Plate 6mm 4x8,MS plate 2mm 4x8,Cutting wheel 14 inch,Welding rod,Cutting wheel 4 inch,Source Pip
DISTRIBUTOR HEAD,CAMPLATE,CROSSED DISC,ROLLER RING ASSEMBLY,TIMING DEVICE PISTON,BEARING PIN,REPAIR
KIT BRAKE LINING SET FRONT,SUSPENSION BUSHING KIT,BRAKE PAD,SWITCH BACK LAMP,JOINT ASSY UNIVERSAL,C
TURBO CHARGER,EGR SENSOR,PRIMARY DIESEL FILTER,SECONDARY FILTER,OIL FILTER,AIR FILTER,THERMOSTAE VA
Title1,Title2,Title3,Title4,Title5
W5-AWS-TLV-1840218205004 FILTER ELEMENT-72 MTRL NO 10579619,X2-AWS-15KVA-1840247200040 FUEL FILTER 
HP Cartridge 12A,Cartridge Xerox,Xerox Toner B1025,Cartridge Epson BK 005
Cover Assy Clutch Disc,Clutch Disc Assy,Clutch Release Bearing,Fly wheel assy,Steering Oil Seal Kit
Brake Pad,Clutch Rel Brg,Door Lock LH and RH,Front Wheel Brg,Fuel Filter,Hub Brg,Strut Assy,Drive S
POTATO FRESH , ONION FRESH
Custom Bid for Services - BOQ item No 1 Semi Skilled Electrician per shift of 08 hours          143
Solar Street Light 40w Solar LED,Solar Charger Controller inbuilt 120wp and 12V,60AH Li-Po4 Battery
Clutch r bearing with sleeve,Injector with holder,Fly wheel assy,Tie rod assy,Bush
24 Port Manageable GB 3 Layers Swtich SFP Moudle,16 Port Manageable GB 3 Layers Swtich SFP Moudle,4
DRIVE SHAFT ROTARY PUMP,Supply Pump,CROSS DISC,ROLLER,PIN,ROTAR HYD HEAD ASSY,DRIVE GEAR,ROTARY PUM
Driven Shaft,Brush Gear Assy,Self Bush Set,Assy Clutch Disc 330 Dia,Air Pressure Guage Pipe,Cover T
Micro Circuit MGA 82563,IC Programmed Z8
FPV Drone Simulator
Soil Investigation
PROVN OF QTY 16 x ESS (2KVA SOLAR HYBRID)
Gibco MEM Minimum Essential Medium 1 L,Gibco Antibiotic Antimycotic 100X 100 ml Sol,Molecular grade
UPS Bty 12V 7.2 AH,Key Board and Mouse,SMPS,Printer Head,Maintance Box,Processor I 5,Mother Board,L
SHIM
Processor I 5,Mother Board,Ram DDR IV 4GB,SMPS 450 W,UPS Bty 12V 7.2 AH,CMOS Bty
BTE Digital Hearing Aid
Processor I 5,Mother Board,Ram DDR III 4GB,SMPS 450 W,UPS Bty 12V 7.2 AH
BOROSIL GLASS,ODONIL,HARPIC TOILET CLEANER 700ML,NAPTHELENE BALLS,ROOM FRESHNER,DETTOL HAND WASH,LI
TRANSFER ARM FRAME UPPER
Custom Bid for Services - Local Repair Contract for repairing and re-fitment of Recovery Winch, Rop
CLUTCH PLATE TATA OLD MODEL,COMBINATION SWITCH,DUAL BRAKE VALVE REP KIT,FAN BELT TATA OLD MODEL,FIE
10478561,10443588,10440000,10025681,10451941
False Ceiling and wall Paneling 1600 sqft,Wall Putti and Paint,Lighting and Wire Fitting,AC 2 Ton H
PTZ IP Camera,NVR 32 Channel,Hard Disk,SFTP Cable,RJ 45 Connector,UTP Patch Cord,Media Converter,OF
PTZ CAMERA REPAIR AND MAINTENANCE,IP CAMERA VIDEO RECORDER SIXTEEN CHANNEL REPAIR AND MAINTENANCE,H
CME1 , CME2 , CME3 , CME4 , CME5
T2 1315-001236 NOSE ADAPTER
Manning Operation and Maintenance of Medical Gas Pipeline System at Oncology dept of CH SC,Manning 
AVR,Fuel pipe,Fuel Flexible pipe,Head Gasket,Injector Nozzle,Pump Element,Coupling Rubber Star
Filler Gauge,Tools for Twisting Force Adjusting 0.5mm,Tools for Twisting force Adjusting 100 to 200
H3 5530-400054 PLYWOOD GENERAL PURPOSE WWR-AB-7 PLY 240,H3 5530-400096 PLYWOOD FOR GENERAL PURPOSE 
Back Light Tata Sumo Amb,Front Indicator Assy Tata Sumo Amb,Commander Light Tata Sumo Amb,Tie Rod E
Macbook
Custom Bid for Services - Selection of an firm for engaging 01 x resource for redesign upgrade devp
Total Temperature Management system with whole body blanket
Banana , Pineapple , Pears , Mango
FUEL PRE FILTER ASSY WITH BKT 2 PIN CONNECTOR,ASSY FAN SHROUD,GLOW PLUG,CYL HEAD COVER GASKET,OVER 
Oil Hydraulic PX-26, Servo duty low temperature, ex AVI Oil
A4 Plain Copier Paper,2 Ply Computer Paper Size 10x12x2,Cartridge for printer Brother MFC L27010 TN
RECTIFIER ASSY,RETURN LINE HOSE ASSY,ASSY DRIVE SHAFT,GASKET CYL HEAD,DRIVE ASSY,RELAY ASSY,SHOCK A
UPS 3 KVA INBUILT BTY MICROTEK,D LINK SWITCH 8 PORT,HDMI CABLE 10 MTRS,AIRTEL FIBER 100 MBPS,POWER 
Spark Plug,Combi Switch MS Harness,Speed Sensor AGB,Wiper Blade,Cap Assy Fuel Tank Filler
Custom Bid for Services - As per BOQ item No 1 Outsourcing services for Semi Skilled AC operator 04
LV1/R90 MTO-1-35SB-A VACCUM CLEANER (CONSISTING OF 10 ITEMS)
Z7/ISRAEL-59356-C-01, PWA HOST
1 ORD ITEMS,2 ORD ITEMS,3 ORD ITEMS,4 ORD ITEMS,5 ORD ITEMS
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7,MTITEMS 8,MTITEMS 9,MTITEMS 1
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7,MTITEMS 8,MTITEMS 9,MTITEMS 1
Title1,Title2,Title3,Title4,Title5
Custom Bid for Services - Repair of uncooled HHTI
PACK RECTIFIER,DIODE,GEAR RIM,REP KIT AIR PRESSURE GOVERNOR,REP KIT FOR MAIN CYL CLUTCH,MANNUAL BRA
ELEMENT FUEL FILTER,LUB OIL FILTER,ELEMENT AIR FILTER,SILENCER PIPE,WHEEL MOUNTING,LOAD SOCKET,STAR
1800 10031246 LTC BATTERY 7.2V, 5.5 AH OF INFLUENCE MINE MK-II (ADRUSHY MK-II)
Provn of Fd security light Solar,Provn of Cement Bag of OPC 43 Gde,Provn of Sand,Provn of Aggregate
REP KIT MASTER CYL,FUEL STRAINER,FAN BELT,CABLE ASSY CONTROL REAR,HEAD GASKET,GASKET,BALL BEARING,I
TAFLON 2040,PRESSURE ROLLER,BATTERY 12V 7AH,KEYBOARD AND MOUSE SET,DVD WRITER,MONITER 18 INCH
Prob 1,Prob 2,Heating Element H,Heating Element,Oxygen Flow Meter
MINERAL JELLY
Centre Locking System Repair,AC Repair and Gas refilling,Main Shaft Metal Filling Cutting Balancing
Gasket,Gasket,Gasket,Gasket,GKT,Shock Absorber,Shock Absorber,Gasket 17x200,GKT,Ring Packing,Shock 
FUSER ASSY,TEFLON,SLEEVE,PICKUP ROLLER,MONITOR 21,8 PORT SWITCH,SMPS,FLASH CARD,UPS BTY 12V 7AH,LIT
IGBT CARD,UPS 1 KVA,BATTERY 12V 7AH,PRINTER HEAD,INK PAD
Clutch Master Cylinder Assy,Sleeve Cylinder Assy,Armature Assy,Clutch Plate,Clutch Cylinder Assy,Ca
Cheese Cube , Cheese Slice
BLEACHER
UPS 1 KVA,SMPS,KEY BOARD AND MOUSE WIRELESS,KEY BOARD WITH MOUSE,TEFLON SLEAVE,BTY 12 V 7 AH,MONITO
Differential gear assy,Air dryer rep kit,Suspension kit,Assy rubber bush,Assy fuel filter,Water Sep
AC PIPE,RUBBER HOSE,RUBBER HOSE,RUBBER HOSE,TAIL GATE LATCH SAFARI,BULB H7,ENGINE MOUNTING PAD
Cement Bag 50 Kg,Sand,Wall Panelling,Flooring,Crusher Cement,White Paint
Putti 20 Kg,White Paint,Black Paint,Red Paint,Blue Paint,Green Paint,Brush 2 Inch,Brush 1 Inch
Iron Tin Sheet 10 ft,Iron Angle 1 Point 5 Inch,Welding Rod,Iron Patti 1 inch,Roofing Screw 4 Inch
data wall 12 x 12 92.5 indoor with 4 pipedevice processor,43 inch tv,all in one computer with i5 pr
CABLE COMP CLUTCH,REVOULUTION COUNTER,PROTECTIVE BAG,SWITCH 24 V,RELAY VALVE,NOZZLE,SUSPENTION KIT,
CABLE CLUTCH COMP,BOLT,ASSY MASTER CYLINDER,HOLDER ASSY RECTIFIRE,CLEANER ASSY AIR,DUAL BRAKE VALVE
Automatic System For Pre-treatment and disinfection of Liquid Medical Waste
Rotacaps Tiotropium 18mcg Formeterol 12mcg Fumarate bott of 30 capules,Secnidazole 1 gm Tab,Sodium 
VALL BODY,HOSE,ACC CABLE,NOZZLE,ELEMENT,DELEVERY VALVE,HYDRAULIC PIPE,OIL FILTER ENG,BRAKE FRICTION
Calendula Q 450 ml,Calendula 200 500ml,Arnica mont 30 450 ml,Calcarea sulf 30 500ml,Calcarea flour 
ASSY HOSE,ASSY HEAD LAMP LH 24V,ASSY SIDE INDICATOR LAMP LH 24V,ASSY FRONT FOG LAMP,HOSE HUMP,ZF TA
Paper A4 75 GSM,Paper Legal,12A Toner Cartridge HP LaserJet 1020 Plus,Toner LaserJet Tank 158A Blac
IGNITION COIL,SPARK PLUG,WEATHER STRIP DOOR RK,TIE ROD ASSY,TAIL LIGHT ASSY,DOOR CATCH INNER,LOCK S
DISTRIBUTOR HEAD,NOZZLE TMB,NOZZLE,OIL SEAL,VANE PUMP
88A compatible Toner Black for HP 88A,A4 Paper 75 GSM,166A compatible black laser toner for HP 166A
FOG LIGHT ASSY,JOINT ASSY UNIVERSAL,MOUNTING ENG FRONT,FLOAT VALVE,WIPER BLADE,TEMP SENDING UNIT,OI
Annual Maintenance service - EPABX System,Annual Maintenance service - EPABX System,Annual Maintena
Mobile Record Register as per sample,Register 200 pages,Register 300 pages,Search Light as per samp
Alfuzosin 10 mg Tab,Inj Ferric carboxymaltose 50mg ml 10 ml vial,Inj Human Insulin Analogue Glargin
Lignocaine hcl 2 percent with adrenaline 1 to 80000 volume 30 ml inj,Gel for root canal preparation
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Gel Pen (V3),Gel Pen (V3),Gel Pen (V3),Gel Pen (V3),Gel Pen (V3),Ball Point Pens (V2) as per IS 370
TALC ROLL,MAP CLOTH (18 MTR),BEACON LIGHT,9V BATTERY,AAA BATTERY (PACK OF 10 NOS),AA BATTERY (PACK 
FLASHER SOLID STATE,DOOR LOCK ASSY LH,DOOR LOCK ASSY RH,HOUSING FRICTION,RAM SERVICE KIT,CLUTCH REL
Vehicle Hiring Service - Per Vehicle-Day basis - SUV/MUV; 2020, 2021, 2022, 2023, 2024, 2025; Local
View Cutter 6ft, with MS Pipe structure support and laying and installation
PISTON ASSY STD WITH RINGS PINS,PISTON RING SET STD CLAMP OIL CONTROL,JOINT PUSH ROD SLEEVE RUBBER,
Rope Nylone 32mm,Rope Malina VR 102 cm,Beam Wooden 12 Ft,Coir Mat 5ft Width Brown,Coir Mat 5ft Widt
Customized AMC/CMC for Pre-owned Products - CAMC of Fork Lift Truck; CAMC of 06 X FLTs; Comprehensi
Chicken Eggs (Q3)
RADIATOR ASSY,HOUSING STARTER,REGULATOR ASSY LH,LOCK ASSY GATE SIDE LH,TIE ROD STEERING,PUMP ASSY F
TEA CTC
STAMP PAD INK,CORRECTION PAD,BINDER CLIP 32MM,STAMP PAD BLUE,CPAPER CUTTER,STAPLER HD-10D,FLOOR CLE
Procurement of Multi Purpose Digital Board (Score Board)
Inter Locking Mat 40 mm Heavy Duty,Tightener Heavy Duty,Rope Loop Anchor Iron Heavy Duty,Stop Watch
Bus Hiring Service - Regular Basis - Outstation 24*7; 31-33; Non Deluxe (NDX); 250Kms
Heavy Duty Storage Racks (Q3)
Comprehensive aerial security surveillance system (Quadcopter) to include LRF & thermal camera
Pencil Doms,Blue Ball Pen Montex,Pen black Montex,Blue Pen V7,Blue Pen V5,Red Pen V5,Black Pen V5,H
SAFCO RUBRIC XP 22 Z MOTUL
Hydraulic Oil (Aeroshell-41)
Oil OM-100 Defence
Belt V A57,Pinion 13 Teeth,Solenoid Switch Assy,Fuel Injection Pipe,Cyl Head Gasket,High Pressure P
Cornflakes,Cornflour,CustardPowder,Jelly,Musli,Pickle,TomatoSauce,Bournvita,Horlicks,Protinex,Lacto
SENSOR ASSY,HOSE ASSY AIR FILTER,ASSY UPPER BALL JOINT,HEAD LIGHT ASSY,AIR INTAKE HOSE,ASSY RECEIVE
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - REPAIR OF GEN SET 
Coffee Dispensing Machine (V2) (Q3)
LOADING CONVEYOR
Entry and Mid Level Desktop Computer,Line Interactive UPS with AVR (V2)
Cooling coil assy,Disc brake pad,Fan belt,Clutch plate assy,Clutch rel brg
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - REPAIR OF GEN SET 
HT Coil Assy,PCB Module Assy,Spark Plug,V Belt Aus,Fuel Pipe Line
Ignition cum steering lock,Wiper motor 24V,Fuel water filter seperator,Horn 12V,Door lock LH,Accele
Custom Bid for Services - Repair and replacement of 120 watts street light fittings along with UG C
Triamcinolone Acetate 10 mg ml Inj,Cyclopentolate HCl 1 Percentage Opth soln bottle of 5 ml,Flucona
Item 1,Item 2,Item 3,Item 4,Item 5,Item 6,Item 7,Item 8,Item 9,Item 10,Item 11,Item 12,Item 13,Item
Citicoline 500Mg Tab,Eplerenone 25Mg Tab,Antacid Gel Each 5Ml Dried Aluminium Hydroxide Gel 250 Mg 
Potato Fresh,Onion Fresh,Garlic (Lassan)
Steel Angle Equal Mild,Angle Mild Steel 25x25x3mm,Steel Bar,Welding Rod,Plywood Gen Purpose 18mm,Pl
Split Air Conditioner Including Green AC, Wall Mount Type (V2),Split Air Conditioner Including Gree
Stack,Air Frame,Video Transmitter,FPV Goggle,RC,Battery,ELRS,GPS,Camera,Motors,Propellers,Spacers a
Repair of Dehumidifier
CLUTCH BOOSTER,CLUTCH VALVE,REPAIR KIT FOR MAIN CYL CLUTCH,SPEEDO METER,RESISTOR,HOSE HYDRAULIC,ACC
Power Generator - DG Set (up to 900 KVA),Earthing with each 15 KVA Genr set,Fan Belt,Delivery Valve
Bumper Stopper,Horn Relay Air Pressure,Sub Assy of Hose Pump Tank,Brake Shoe Linning Kit,Assy Pipe,
SPIDER BRG,HORN 12V,WATER PUMP,OIL FILTER,HEAD LIGHT BULB,SPARK PLUG,COIL ASSY IGNITION,HORN ASSY,F
SEAL FRONT OIL,OIL SEAL,BALL BEARING,FUEL RETURN TUBE,OIL SUPPLY TUBE,SLAVE CYL CLUTCH,SOLENOID SWI
Amper Meter,Field Coil Set,Solenoid Switch,Carbon Bush Set,Toogle Switch,Armature Assy,Clutch Assy 
Z1/5999-049290, Accessory Kit Electronic Eqpt, Data
HT ADJUSTABLE WORKBENCH
FIELD ELECT (SOLAR LIGHT)
Grinder High speed for alloy 100463,Micromotor Brushless heavy duty for Dental Lab 100470,Universal
Mini Buff Wheel Rotary Bit in bracket Metal Polishing Buff Small in bracket,Sand Paper Mandrel Pack
Tactical Elbow Pad,Nylon Rope 10 Mtr,Paper Cutter Steel,Thigh Hostler OG,Stand for Camo Net
SUSPENSION KIT,BEARING,KNUCKLE BEARING,SEAL OIL,HEAD LIGNT RELAY,CABLE ASSY,CONTROL LIGHT,CLUTCH SL
Rear View Mirror,RR Unit,Fuel Tank Cap,Spark Plug,Ignition Switch,Hose Pipe,Wiper Blade,Tail Light 
Amn Shelter
Sentry post
Inj Dexmeditomidine 100 mcg per ml 50 ml vial,Inj Rocuronium 10 mg per ml 10 ml vial,Ketamine HCL 5
Cartridge 88A,Cartridge 12A,Toner NPG 87,008 Ink,001 Ink,GT-53 Ink,Ink 774,Cartridge 36 A,Cartridge
Physical Trg Bds,Upgradation of RCP Vehs,Refitting of Crew Shelters,SA Charecteristics Display boar
NAPROXEN 500 MG TAB,NASAL SPRAY CALCITONIN 200IU,NEPHAZOLINEplusCMC ED,Nicorandil 5 mg Tab,NITROFUR
IBUPROFEN GEL TUBE OF 20 GM,INJ ADRENALINE 1COLON1000 1 ML,INJ AVIL PHENIRAMINE 22.75 MG OBILIQUEML
Spirit Level,Line Dori or Fish Line,Hammer Clow,Pipe Wrench 24 Inch,Pipe Wrench 14 Inch,Screw Drive
Prelaminated particle board,Melamine polish,Plywood,Thinner,Plywood,Veneer,Paint,Fevicol,Mirror,SS 
Malathion Tech Grade 95%
MULTI POINT FUEL DISPENSING SYSTEM
Z1/5985-012712, Antenna Element Upper Whip Vehicular*
Z1/5995-020750, Cable Assembly Special Purpose Electric*
View cutter,Glowing board,Platform wooden 8ftx3ft, 3 on each sides,Large PVC containers,Display boa
Procurement of COTS SW
Spike Barrier (V2) (Q3)
Levodopa 150mg plus Carbidopa 37.5mg plus Entecapine 200 mg Tab,Entecavir 0.5mg Tab,Tab Escitalopra
Solenoid switch,Carburetor assy,Injector with holder,Piston assy,Piston bore sleeve,Welding rod,Pis
Goods Transport Service – Per Trip based  Service - Machinery & Equipment; Open Body LCV Truck; 1
Oil Filter 30 KVA Genr Kirloskar 4 RA IV,Oil Filter 30 KVA Genr Greaves 4 YDA II,Oil Filter 30 KVA 
286301995302,2786 0599 9999,278605999801,570107999910,2880-5890-3516,278603999810,502445100148,5855
Living Shelter (6 Men)
MAHINDRA MAXIMILE ELITE
Bench Grinding Wheel 8 inc x 3-14 inc Rough,Bench Grinding Wheel 8 inc x 3-14 inc Fine,Tangles for 
Sedan local 06hr 60 kms,Sedan Local 10hr 100 kms,Sedan local extra kms,Sedan local extra hrs,Premiu
chari (Green),Green Grass (Rajka),Maize Green
Appointment Name Board Acrylic,Photo Gallery Officers,Wall Texture Painting,PVC Mat,Writing Table T
Repair Kit,Flexible Hose Assy,Valve Relay Air Pressure,Nozzle,Yoke Universal Joint,Cross Assy,Sproc
ORD ITEMS 1,ORD ITEMS 2,ORD ITEMS 3,ORD ITEMS 4,ORD ITEMS 5,ORD ITEMS 6,ORD ITEMS 7,ORD ITEMS 8
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7
Influenza Vaccine 0.5 ml Inj,Ketorolac 10 mg Tab,Ketorolac 30 mgobiliqueml 1ml Inj,L Arginine and g
sarson,zira,Imli,Haldi,Kali Mirchi,Dhaniya,Badi elaichi,Lal Mirch,Laung,Lahsun
Methimazole 10 mg Tab,Methotraxate 25 mg Inj,Methotrexate 2.5mg Tab,Methotrexate 20 mg Tab,Methotre
BATTERY SECONDARY PORTABLE LITHIUMION 7
LV1/ARJ R900868520 (Material No. 10480139) Air Supply
Z7/ISRAEL-9421-3520-10, Interface and Drivers CCA
Z7/ISRAEL-110003007, Driver CCA with Capacitor
Z7/ISRAEL-9553-1110-00, Azimuth Resolver & Connector
Office Suite Software (V2) (Q2)
Hexa Blade,Tape Insulation,Anabond Red,Araldite 13 GM,Tape Transparent,Cutting Blade,Electrical Wel
Fevicol SR -998,Paint RFU OG,Thinner Antichill,Adhesive Nitro Cellulose,Alcohol Isopropyl Tech,Seal
Repair / Maintenance of Fork Lifter EM No 05H-8000723L
WELDING ROD 3 15 MM,GAS ACETYLENE,CYL COMPRESSED GAS AC,TAPE THREAD PTFF ROLL,INSUALTION TAPE ELECT
Godrej Lock,Ceramic Qtr Plate,Cup and Saucer Set of 6,Crystal Water Tumbler,Paper and CD Shredder,T
Mounting Engine Front,Cover Assy Clutch,HP Hose LG,Sprocket Final Drive,Element Air Cleaner,Clutch 
Wheel Cylnder Assy,Drying and Distributor Assy,Rear Wheel Bearing,Self Field Coil Assy,Siren 24V,Te
Custom Bid for Services - ----
HP Elite x 360 1040 G11,Hewlett Packard x360 14 inches 2-in-1 Business Laptop,Apple 2025 Mac Book A
Fuel Filter,Oil Filter,Air Filter,Oil Filter,Air Filter,Fuel Filter,Copper Wire 1mm,Tle,Toggle Swit
Aerated Water1,Aerated Water2,Aerated Water3,Aerated Water4,Aerated Water5
ANR HEAD GEAR WITH 2 MTRS CABLE DOR DCH SYSTEM
ICE , ICE1 , ICE2 , ICE3 , ICE4
Piston Assy With Ring,Piston Block,Chain Sprocket Set,Brake Shoe assy,Regulator Assy,Rear View Mirr
HEAD VALVE,RING PISTON ASSY COMPRISING,FUEL PUMP ELEMENT,ELEMENT FUEL FILTER,BANJO BOLT
Reverse Indicator Switch,Field Coil,Hose,Sleeve Cyl Assy,Clutch Master Cyl Assy,Oil Seal,Hose Assy,
CONCRETE BASE,PVC FLOORING,BADMINTON POLES,LIGHTNING WORK,SIDE WALL PANAL,PVC GLASS DOOR
Diclofenac 25 mg per ml 3 ml inj,lorazepam 2 mg per ml 2 ml inj,Dopamine HCl 40 mg per ml 5 ml inj,
CLUTCH PLATE,PRESSURE PLATE,ASSY CLUTCH MASTER CYL,ASSY SLEEVE CYL,ASSY DUAL BRAKE VALVE
Carburetor Assy,Knuckle Bearing,Bolt With Nut,Rubber Coupling,Wheel Bearing 30209,Clutch Assy,Digit
LV7T815 4433320370,LV7T816 9930502890,LV7T815 2073012694,LV7T815 2073012684,LV7T815HMV 2070310934S,
LV7KRZ 256B1350636510,LV7T815 130075062964,LV7TMB 4030000339 10485692,LV7STLNVF B1211802,LV7TATA 40
CLUTCH BOOSTER,STATIONER GASKET,FEED PUMP,REPAIR KIT PUMPING ASSY,REPAIR KIT T,TAIL LIGHT ASSY,ASSY
HOSE 40U 10-13 OR 40U10-7B DIA 10MM,HOSE 40U 12-13 OR 40U12-7 BORE DIA 12 MM,HOSE 14 MM,HOSE 40U 16
Crown wheel and pinion,Pole screw,Connector,Puller fuel pump gear,Assy rubber bush,Assy fuel filter
COVER ASSY CLUTCH,CLUTCH PLATE ASSY,IGNITION SWITCH,COLLANT HOSE,SPIDER BRG,WATER SEPARATOR,FUEL FI
AWH-15
ASSY FUEL PRE FILTER,AIR FILTER ELEMENT,ASSY OIL FILTER,ECU ASSY,GLOW PLUG BERU,MINI RELAY EMS RELA
File cover printed,Paper A4,File Cover Printed White,File cover white,Demand Pad,Register 300 Pages
Tomato Puree
Track Suit with Detachable Hood (MHA)
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma with minimum 03 Years trade experie
PART KIT TRANMISSION
E2IEB USA0005 SCREW DRIVER,43 3040 000008 SHAFT ASSEMBLY FLEXIBLE 17 point 5MM X 7320MM 24FT Drg No
12411613005 TOOTH,12411608005 WEDGE,12090230 2654407 OIL FILTER,12090225 FUEL FILTER WATER SEPARATO
GREASE XG-240
SELF BUSH SET,GOV SHAFT,CONTROL VALVE,TD PISTON,FUEL PUMP MOTOR,CONDENSATE SUMP 4429,BRAKE CYLINDER
Cartridge 166A,Cartridge 88A,Cartridge 12A,Cartridge 137A,Sharp MFD BP 20M24,Epson L 3210 Ink,Epson
Dentin Powder for PFM Build up Shade C3,Base Paste for PFM work,Opaque Paste for PFM work Shade A1,
bofors-nk-24,bofors nk-25,bofors nk-27,bofors nk-26,bofors nk-26,bofors nk-10,bofors nk-30,bofors n
Track Suits (IAF) (Q2)
Tracksuit (Q3)
Peas Dried Green (V2) (Defence)
KEYBOARD AND MOUSE SET,MOTHERBOARD H310,MOTHERBOARD H81,SMPS,IGBT CARD,CONTROLLER INVERTER CARD,TRA
OIL OM-100
Cheese Spread
Cover,D Pin,Cover Hun,Case M,Pin A No 3
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Bus Hiring Service - Short Term - Outstation; 34-36; Non Deluxe (NDX); 300
GASKET CYL HEAD,ASSY CLUTCH MASTER CYL,SPEED SENSOR,REGULATOR,OIL SEAL
COOLANT AVIKOOL R-914
H1A 8010-000244,H1A 8010-007493,H1B 7930-000006,H4 9330-000028,H-2 8305-000063-CASD,H2 4020-000195,
Carbon Bush,Self Heat Rersistant Bone China,Air Dryer and Distributor,Controller Box,Ignition Switc
Night Enabled Quadcopter
CGI Sheet,Outer Facade Work,Inner Facade Works,False Ceiling,Tilling Work,LED Light,Ladakhi Main Ga
SPIDER BRG,DRIVE ASSY,COMPRESSOR PISTON RING,PARTSKIT MECH EQPT,SWITCH ASSY BACKUP LAMP,ROD WIPER L
Entry and Mid Level Desktop Computer
Vidas Anti HIVDUO Ultra 60 Test Kit,Total LgE 60 Test Kit,Vidas Anti HIVDUO Ultra 60 Test Kit,Rapid
Complete Servicing of Engine including washing of vehicle,Dismantling and removing the fuel injecti
Rotational Moulded Polyethylene Water Storage Tanks (V2) conforming to IS 12701,Rotational Moulded 
White - LED Based Solar Street Lighting System
Urea System Pack Kit 5x44 ml 5x11ml Compatible with ERBA EM 200,Creatinine System Pack 5 x 44 ml 5 
KM Head,Repair Kit,Needle Bearing,Door Handle,Oil Seal,Accelerator Cable,T Coupling,Water Pump Assy
Electric Trimmer,Electric Trimmer Rechargeable,Daily Progress Register,Folder File,Talc Sheet,Regis
FAN BELT,FLASHER UNIT NEW MODEL,FUEL FILTER WATER SEPARATOR OLD MODEL,FUEL PIPE LINE OLD MODEL,GEAR
F1 5110-000726 CHISEL FIRMER STRONG 10 MM,F1 5110-000219 KNIFE HACKING STRAIGHT LENGTH 100 X 30 M,F
J950012,AT90112,R46528,19M7932,19M7658,97631003,14M7315,177613,34H312,24M7240,J950010,19M7493,14H10
Standing Fan,Cooler 65ltr,Cooler 180ltr,Mist Fan,Refrigerator 120-210 ltr,Refrigerator 260ltr,Ice B
Water Proof Multi Purpose Rain Poncho with Convertibility as Bivouac (MHA)
Human Insulin Analogue Glargine Inj 100 IU PER ML Recombinent DNA origin 300 IU DISPOSABLE PEN WITH
Battery Secondary Lead Acid MT Type (Defence)
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Main Winch Storage Stand,MWRA Assembly Table,MWRA Stand Alone NO- Load Run Test Jig,MWRA Storage St
Manpower Outsourcing Services - Minimum wage - Highly-Skilled; Diploma; IT-Technical
MS SQL Software,Antivirus,OEM Authorization,Data Migration,OEM Certificate
Solenoid Switch,Pivot Pin Alloy Steel,Pivot Pin Bush,Fan Belt,Throttle Cable,Hydraulic Pipe
hand held gps (Q2) ( PAC Only )
ALLUMINIUM OXYGEN CYLINDER CAPACITY 2000 LITRES WITH VALVE
auto cpap machine with humidifier,bipap machine with humidifier
Almond without Shell (V2) (Defence)
Custom Bid for Services - Painting and Maintenance of x 03 Sentry Posts including Labour
Manpower Outsourcing Services - Minimum wage - Highly-Skilled; Graduate; Healthcare,Manpower Outsou
Coill Assy Ignition,Vane Pump,Fuel Shut Off Solenoid,Assy Clutch Master Cylinder,Spark Plug Champio
CONSTRUCTION OF BASKETBALL COURT WITH FIBRE GLASS BDS & POLES
G2 9505-000058,H1 A 8010-007501,H1 B 7930-000003,H1 B 6810-000568,H1 CHD-NIV2000-000023,H1 7930-000
Goods Transport Service – Per MT per KM Based Service - Food Grains, Food Items; Open Body Taurus
SR 40 24V,BRAKE HOSE,HOSE ASSY FUEL PIPING SYS,RING SET,PISTON RING SET STD
DOOR LOCK ASSY RH,FIELD COIL ASSY,U J KIT ASSY,ASSY CLUTCH MASTER CYL,HEX NUT,BEARING FRT WHEEL,ASS
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Finance/Accounts
Manpower Outsourcing Services - Fixed Remuneration - Healthcare; Audiologist; Educational Qualifica
Selection of Laboratories for Testing of Products/Material - Soil; Soil Testing complete all as spe
Carbonated Soft Drinks (Clear, White, Orange & Black),Lime Based Soft Drinks
Carbonated Soft Drinks (Clear, White, Orange & Black Flavour)
Paint RFU Finish OG,Paint RFU Red Sig,Plywood Gen Purpose 12mm 8x4,Plywood Gen Purpose 18mm,Plywood
Lead Tin Anode
ARMATURE ASSY,FIELD COIL,SOLENOID SWITCH,KNUCKLE BUSH,COVER STEARING KNUCKLE,FAN BELT,SHOCKET FOR E
Clutch Cover Assy 35.56 CM RDC LRV,Poly V Belt,Regulator 3416,Engine Speed Sensor,Ball Joint Assy L
DISC CLUTCH,MOUNTING ENG FRONT,MAJ KIT SLAVE CYL,TANK ASSY FUEL,BEARING BALL,ASSY OIL FILTER,FUEL P
Z7-IZG-1295 IMAGE INTENSIFIER TUBE 18 MM SUPER GEN
LOOM WIRING COMPLETE,INDICATOR FRT,HOSE PIPE,HYDROULIC PIPE,PISTON SEAL,HYDRAOULIC CONT VALVE,OIL F
Genr set 40 KVA Kirloskar HA 494TC NK,Genr set 40 KVA Kirloskar HA 494TC NK,Genr set 40 KVA Kirlosk
FALCO T-01 MAX
Refined Musterd oil 15 kg Tin,Refined Musterd oil 1kg Poly Pouch,Refined Musterd oil 15 kg Tin_1,Re
PROCESSOR I5 12 GEN,PROCESSOR INTEL CORE I5 10 GEN,MONITOR ACER,MOTHERBOARD,KEYBOARD AND MOUSE,UPS 
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Secu
Effluent Water Treatment Plant
LED Luminaire for High Bay Lighting,LED Luminaire for Floodlight (V2) Conforming to IS 10322 (Part 
Engine MountingFront,Engine Mounting Rear,Uj Cross,O Ring,Radiator Cap
Goods Transport Service – Per Trip based  Service - CSD Goods; Goods Carrier; 20 Ton Capacity,Goo
Brake Pad,Assy link RH front,Assy link LH front,Coolant Pipe,Front wind screen weather strip,Valve 
765 17 368 GASKET,765 49 47 GASKET,675 71 381 PACKING RING,765 82 193 GASKET,765 38 81 GASKET,765 5
Dell R250-1U Rack SERVER
PISTON RING SET,BIG END BRG SHELL,OVERHAUL SEAL KIT,GEN SET FUEL INJ PUMP,OIL FILTER ASSY,PUSH ROD 
LED smart TV Samsung 32 Inch,Wall Fan Make Bajaj,Door Curtain,Window Curtain,Table Glass 48 inch x 
TURMERIC,CHILLY,CORINADER,CUMIN,BLACK PEPPER,LARGE CARDAMOM
Acetazolamide 0.25g Tab,Acyclovir Ophth Ointment 3 percent in 5 gm tube,Adapalene 0.1 percent Tube 
REGULATOR VOLTAGE,WD-40 SPRAY,ANABOND LIQUID GASKET,FUEL PIPE,OVER FLOW PIPE
FUEL FEED PUMP,FUEL TANK HOSE,VEHICLE SPEED SENSOR,WINCH SEAL,FUEL PUMP MOTOR,GEAR BOX BEARING,PRIM
LV7 STLN VF 5640 72 0000508 WEATHER STRIP,LV7 STLN VF 4720 016076 HOSE ASSY NON METALIC,LV7 STLN VF
Kit for Triglyceride estimation 100 ml ERBA,Kit for estimation of Bilirubin 240 ml ERBA,Kit for est
PROCUREMENT OF PLANT SPARES
Furea Bolus each containing Nitrofurazone 60 mg and Urea 6 gm,Gauze Absorbent, Folded, 1 cmx100 met
AIR CLEANER REP KIT,INJECTOR NOZZLE,SEAL SET TITLING CYLINDER,BRACKET MOUNTING,LOCK ASSY STEERING,G
Coil Ignition,Hub Brg,Wiper Arm,Suspension Arm,Drive Shaft,Strut Assy,Fuel Filter,Front Wheel Brg,D
NK000090 NUT WITH BOLT 10MM FINE THREAD,NK000091 NUT WITH BOLT 12MM FINE THREAD,NK000093 NUT WITH B
Graphic Card 8 GB RT X 3050,RAM DDR4 16 GB,MONITOR,Printer Head,Keyboard with Mouse,Adoptor Charger
Custom Bid for Services - Annual Maintenance or E-Complaint system
kilometer head assy,brake pad,fuel filter,front hub bearing,hub bearing outer,coolant hose pipe
TABLE GLASS 10 MM WITH BABLING 105 X 240 CM,TABLE GLASS 10 MM WITH BABLING 90 X 200 CM,TABLE GLASS 
Repair and Overhauling Service - Laundry Type Washing Machines / Drying Machines; IFB; Yes; Buyer P
DRUM CANON,BLADE,PRC PRIMARY CHARGER ROLLER,CMOS BTY,DRUM CARTRIDFGE
TEA CTC 500 Gms Pack,Pack TEA CTC 500 Gms,500 Gms Tea CTC Pack,CTC Tea 500 Gms Pack,Pack Tea CTC 50
HbA1C with Calibarator SYSTEM PACK FOR EM 200 2 x 15 ml Oblique 2 x 5 ml Oblique 5 x 0.5 ml,HbA1C C
Jacket,Track Suit,Wind Cheater,T-Shirt,Shoes,Shorts,Towel,Kit Bag,Shoulder Bag,Socks
Front Shocker,Rear Door Lock,Ignition Switch,Fly Wheel Assy,Pressure plate and clutch plate,Clutch 
Tracksuit (Q3)
Cilnidipine10mg and Telmisartan 40mg Tab,Cilnidipine 10mg Tab,Clopidogrel 75 mg Tab,Clobazam 10mg T
Armature 12 v,Fly wheel ring,Field coil 12 v,Brake chamber diaphrm,Bush set,Spider brg,Solenoid swi
RECTIFIER RA 65 LBPV,DUST COVER,G-BOX HOUSING COVER FRT TOP,SOLENOID,PULLEY B GROVE,BEARING-SKF 600
Sugar (V2) (Defence) (Q2)
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Tonsil Artery forcep fine curved jaws 19cm,Tonsil Artery forcep curved laterally 18cm SS,Peritonsil
Tracksuit (Q3)
High Mast Light with Pole
Tracksuit (Q3)
Refined Mustard Oil (V2) (Defence)
Medals (Q4)
Medals-Handicraft,Medals-Handicraft
Solar Street Lighting System (NTPC)
Solar Street Lighting System (NTPC)
computer kiosk (Q3)
Tailoring Tool Kit (YSSY UP Govt.)
PVC molded stool (Q3)
Oil M-3 52 Defence
Shell Turbo-27 Defence
Acid,Broom Soft,Broom Stick,Colin,Detergent Pwdr Tide Double Power,Hand Wash,Hapric Toilet and Bath
Grease LG-320 (Defence)
String: Anti GPS spoofing Project for CTH & CTK Heptr
Electronic Flasher 24V,Clamping Bolt Bty Terminal,Repair Kit for Spring Brake Chamber,4 Way SP Valv
Structural Stores as per TS,Roofing and Wall as per TS,Construction Materials as per TS,Electrical 
Laptop with Mac OS M3 Chip,Tablet Samsung Galaxy S10 Ultra,Smart Mobile iPhone 16 Pro,iPad Pro M4 C
Sterile Packed 3.5 mm Bioabsorbable Anchor with 2 x no. 2 preloaded orthochord or fibrewire suture
CLED Agar with Thymol Blue,Blood Agar baseInfusion Agar,Wilson Blair agar,Kings A medium,Kings B me
Windows 11 Professional Operating System,Microsoft Office Professional,Quick Heal Total Security,PD
High Pressure Pipe,Fan Belt,Disc Rubber for Hole set Coupling,Pipe Lup Oil Pressure Gauge,Hour Mete
Inj Bharglob 16.5percent,Lactare Cap,Letrozole 2.5 mg Tab,Letrozole 5 mg Tab,Levenorgestrel IP 0.15
Assy Master Cylinder,Clutch Disc Pressure Plate,Plate Clutch,Drying and Distri Unit,Clutch Release 
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
Impact Wrench (Q3)
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
Sugar (V2) (Defence) (Q2)
GOC in C ARTRAC Gold Medal,GoC in C ARTRAC silver Medal,Goc in C ARTRAC Bronze Medal,Sword of Honou
Freq Synthesizer,CMOS Bty 3point 6V,CMOS Bty 3V Flat,Flash Disk 8GB,4744A Diode
MICROCIRCUIT MEMORY FPGA 1 PRGMED,MICROCIRCUIT MEMORY FPGA 2 PRGMED,MICRO CCT DGTL TYPE SRAM 551100
LCD MONITOR , METROX CARD
ARMATURE ASSY,HYDRAULIC PIPE,NIPAL,REVERSE LIGHT,ACCELATOR CABLE,SHOCK REP KIT,HYDRAULIC MOTOR GEAR
Monitor HP 24,UPS 1 KVA Luminious,Bty 12V 7AH Exide,SSD 1 TB WD,SMPS Intel,Key Board and Mouse
spark plug NGK B7HS 10,HT Ignition Coil,Carburator Rep Kit,Carborator Throttle Spray,Throttle Shift
Plywood 14 MM,Parade State Register,A4 Paper,Legal Paper,DO Pad Ream,White File Cover,Colour Paper,
Carvedilol 12.5 mg Tab,Chloroxylenol sol Potass Hydroxide 13.6g Chloroxylenol sol 50.5g Oleic Acid7
oil seal,gear box oil seal,oil seal,clutch release bearing,rod spring front,rod spring rear,lock wi
Bromhexine Syp 5 ml containing 4 mg of Bromhexine HCl Bottle of 100 ml,Bupivacaine HCl 5 mgobilique
Chilli powder,Haldi powder,Dhania sabut,Jeera sabut,Star Anise,Garam masala 100 gm,Sambhar masala 1
Laminated Cloth Hessian (Q3)
Cleaning Duster (V3) (Q3)
4720-109-902-51 W2/IWB/HOLLAND PROGRAM SWITCH
CCTV Bullet Camera 4 MP with 12V 1 Amp Adapter,Camera Mount,Waterproofing enclosure,4 MP 150 IR PTZ
Hiring of Agency for IT Projects- Milestone basis
ELECTRONIC DIGITAL SCORING TARGET SYSTEM ALONGWITH LAPTOP AND ACCESSORIES,SHOOTING GOGGLES FOR AIR 
WATER PUMP ASSY,ASSY DRIVE SHAFT,NEEDLE CAGE,RUBBER HOSE,HOSE CLAMP
BUMPER ASSY,CLUTCH REL BRG,BEARING FRONT WHEEL,DISC CLUTCH,COVER ASSY CLUTCH
PHOSPHATE CAOTING,WIRE STEEL,BUSH COUPLING,FAN BELT,BRASS MALE THIMBLE,BRASS FEMALE THIMBLE,LEATHER
CYL LINER ASSY,PISTON RING,OIL FILTER,FUEL FILTER,CYL HEAD ASSY
Provn of Security Post Shelter part only FOR MANIGONG,Provn of Security Post Shelter part only FOR 
Modernisation and Upgradation of 02 x Tech Repair Sections
AVR,AVR for 2.5 KVA,Clamp,Feviquick,Thread tape,M Seal,Tape roll,Anabond liquid gasket,Banjo washer
Key Board Decoder,SVGA REV3 Colour OLED XL Display,Diode 2733,1 GB RAM,Fuse Holder,LM 3842 IC
TMB Assy Spring Brake Actuator Type MSP 16 slace15,MG Cam Shaft,TATA Hose Air Pressure Pipe,Stln TR
VOLTAGE REGULATOR ELECT,BUSH COUPLING,PLYWOOD,SHEET CELLULAR,ROPE STARTER,LEATHER CLOTH BLACK
AMC of Integrated Security and Surveillance System - AMC of Intergrated Security and Surveillance S
LV7/TMB VARICOR ENG O/H KIT,LV7/TMB LAMP HEAD WITH BEZEL
All in One PC (V2),All in One PC (V2)
MURAL PRODUCT
MG 3010 000644 JOINT ASSEMBLY UNIVERSAL,TATA 2752 2520 0106 352 DIA CLUTCH DISC ASSEMBLY,TATA 2752 
CONSTRUCTION OF HOCKEY GROUND
DAH MKIII,RAT TRAP CAGE TYPE,ROLLING PIN,SAND BAGS CUPRAMANIUM PROOFED,DRESSING FIELD COMPRESSED,SC
CLUTCH MASTER CYLINDER BS-III,CLUTCH SLEEVE CYLINDER,ASSEMBLY FRONT FOG LAMP,BEZEL ASSEMBLY FRONT L
Z7/ISRAEL-9902-3210-10, Head Mirror Final Machining
Z7/ISRAEL-016542-A-00, Power Supply Assy
DRIVEN PLATE FOR CLUTCH,WIPER BLADES,SLAVE CYLINDER,CLUTCH MASTER CYL ASSEMBLY,BRAKE SHOE ASSY,SILE
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
A4PAPER,FSPAPER,A3PAPER,A4PHOTOPAPER,A3PHOTOPAPER,REGISTER100PAGES,REGISTER200PAGES,REGISTER300PAGE
False Ceiling,Deep freezer 320 ltr,Photo frame 4 x2 ft,Photo frame 2 x1 ft,Ceiling light 24 W,DO En
Development of upgrade of FPV Drone for Army Unit.
Chicken Sausages,Chicken Sausages 1,Chicken Sausages 2,Chicken Sausages 3,Chicken Sausages 4
UG AMN BKR ARTY
AC,BRACKET AND FASNER,REMOTE CELL,DESERT COOLER,AC INTALLATION CHARGE
Constr of Synthetic Surface Volleyball Courts with poles and allied accessorreis
optic sectra 1G set
RAM ASSY,SPEEDMOTOR SENSOR,SOLENOID SWITCH 12 V,SELF BUSH SET,HYDRAULIC SET,SUPPLY PUMP,ROLLER,ROLL
Desert Air Cooler
Room heater,Computer Table,Table glass,Photo copy machine repair,Cooler big,Cooler small
WHEEL ALIGMENT OF TATA SAFARI JX,WHEEL ALIGMENT OF M AND M SCORPIO,SCHEDULE SERVING OF MAHINDRA SCR
Armature 24V,4x4 cable assy,Suspension bush rear,Link drop assy,Exhaust elbow
BELT VEE ENDLESS INDUSTRIAL A 43 TOP WID,BELT VEE ENDLESS INDUSTRIAL A 57 TOP WID,BELT VEE ENDLESS 
BOLT PLOUGH 0.75 INCH UNFX 70MM,Nut 0.75,Tooth Bucket,Ram Boom Seal Kit,Ram Dipper Seal Kit
Custom Bid for Services - Service and repair of vehicle
Disposable nebulizer mouth piece mask channel tube AND cup,Disposable NIBP Monitoring BP Cuff for A
Chest Drainage system,Coin battery lithium 3V Pack of 5,Cutting body Needle no 9,Disposable Absorba
Adhesive Incise drape 50x45cm,AED Pacing Pads OBS,Bandage, open wove compressed 2.5 cm x 4 metres,B
Bandage crepe 15 cm,Bandage Elastic Adhesive 6 cm x 3 metres unstretched and 56 metres when streche
Adhesive Incise drape 5x15cm,Alcohol swabs 100 pieces in pkt,Baby Tag Pink AND Blue,Bandage T shape
Absorbant suture Vicryl no 6 OBLIQUE 0,Absorbant suture Vicryl no 8 OBLIQUE 0,Adhesive Incise drape
Socket 22mm,Ratchet,Universal,Socket H14,Socket 24mm,Socket HW 10,Extension Rod 9 inch,Allen Key,Ge
Gen Control Unit,Pump Element,Pump Assy,Fuel Pipe,Air Filter,Filter Assy lub oil,AVR,Piston complet
MATING RUBBER CORRUGATED,SHEET CELLULAR 10MM,FUEL FEED PUMP GEN SET,PLYWOOD GENERAL PURPOSE,ELECTRO
Protein Bar
Composite Chocolate Fruit & Nut
ROASTED CASHEW
Chikki Peanut Jaggery
Namkeen Khatta Meetha
Namkeen Aloo Bhujia
Roasted Pista Giri
Millet Based Biscuits
Synthetic Volleyball Court
Tablet Bravecto,SGPT,SGOT,Urea,Injection Ranitidine,Injection Gentamycin,Copper Sulphate
Sleeping Bag (HIMCLOS)
H1C 8030-000016,H5 1080-000004,H1B 8520-000002,H1B 6840-000001,H1B 5350-000008,H1A 8010-007483,H1B 
Kit for estimation of HDL,Kit for estimation of Cholesterol,Kit for estimation of Glucose,Kit for e
Welding Rod 2mm,Gasket,Radiator Hose Pipe,AC Gas,Oil Filter,Rectifier Assy 12V,Regulator Assy 12V,R
Procurement of Display Board
CLUTCH MASTER CYLINDER,WATER SEPARATOR,CIRCUIT BREAKER,HOSE TM,PRESSURE PLATE ASSY,CLUTCH PLATE,CLU
JAVA BLACK WW SW REAR DR MS MINDARI,ASSY TAIL GATE BALANCER COMPLETE LH,ASSY COMBI SWITCH W HORN SW
Sealing lead 15 mm
Structural Stores as per TS,Roofing and Wall as per TS,Construction Materials as per TS,Electrical 
MG-Magnesium pack of 120 test part No 10444963,IRN- Iron pack of 240 Tests Part No. 10444947,UEG DF
Bonavera Count Diluent BCT,Bonavera Count Rinse BCT,Bonavera Count LYSE BCT,Bonavera Count EZ Clean
Leather cloth Green,Hose 24 MM,Hose 38 MM,Hose 42 MM,Hose 32 MM,Hose 30 MM,Hose 28 MM,Adhesive,Stap
Sand
LV7TMB, 1468-336-671, DISTRIBUTOR HEAD,LV7STLN, P-1303456 9430 034720, NOZZLE,LV7TMB, 1467-030-308,
SOLENOID SWITCH,REGULATOR CONTROL ELECTRONIC ENGINE,PRESSURE CONTROL VALVE,FD COIL,VALVE GRADUATED 
WIND SCREEN,ASSY WINDOW REGULATOR,BRAKE PIPE,ASSY HOSE,SUSPENTION BUSHING KIT,BEARING ASSY FRONT,WH
CEMENT BAGS , GRITS (GITTI)
Pilot Bearing,Clutch Plate,Clutch Release Bearing,Tapper Oil Seal Washer Big,Tapper Oil Seal Washer
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Black Tea as per IS 3633 (Q4)
BEARING WHEEL HUB INNER,COMMANDER LIGHT ASSY,OIL SEAL 120X145X15,SPRING PAD,MOUNTING ENGINE FRONT,B
Fabrication of Cope Cage incl Material and Labour Charge
Besan (V2) as per IS 2400 (Q4)
Unmanned Aerial Vehicle (UAV/UAS) as per MHA QR
Handheld Walkie Talkie,Earpiece in build,Charger,Adapter,Waterproof Carrying Case
Split AC 1.5 ton volatas,Deep Freezer,20 ltr Water Camper,20 ltr Camper water,Water Camper
Custom Bid for Services - ----
Tab Paracetamol-650mg,Tab Ibuprofen paracetamol,Tab ZeeCold Paracetamol Phenylephrine Cetrizine,Tab
VC Camera,Tripod Stand,Smart Panel 86 inch,VC Computer,Audio Mixer,VC speakers and Microphone,HDMI 
Printing of Precise AMT,Printing of Precise BMT
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
PIPE LINE,HOSE CONNECTION,GASKET,BRG CLUTCH RELEASE 23266570 COO,GASKET CYLINDER HEAD COVER,DISC CL
Z1/5915-005289, Network Impedance Matching 30-80 MHZ
Vehicle Hiring Service - Per Vehicle-Day basis - Sedan; 2019; Outstation; Hilly; Approx 370 Km Alhi
Panel Mount connector,Power Connector,Sight to PC Cable,Power Switch,Battery Connector,Cable Connec
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - supply and install
Battery Secondary Lead Acid MT Type (Defence)
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Others
TRANSMISSION SYSTEM/ FRONT GEAR CASE (DEMAND DRIVE FLUID)
5W30/5W40/0W40 API CI4 (Winter Grade)
352 DIA CLUTCH DISC ASSY,ASSY RELEASE BEARING,ALTERNATOR 12V,FIELD COIL 12V,SOLENOID SWITCH 12V
Repair of Rajak TWS MR-3 SED00375 (104100001552)
ALL SEASON GREASE OR GREASE CONFORMING TO NLGI NO 2
CHEESE SPREAD,CHEESE CUBE,CHEESE SLICE,SPREAD CHEESE,CHEESE CUBES
Push Buttons,Wall Plug,Round Cover Plate,PVC Tape,Dimmer
Cheese Cube,Cheese Cube1,Cheese Slice,Cheese Slice1,Cheese Slice2
LU unit Pump Pln part No A02807469052,Nozzle Holder with Nozzle part No A4000170921,Bolt Part No CF
PISTON,PISTON RING STD,CONNECTING ROD BEARING,NOZZLE,DAMPER SHIMMY
LV7-TATA_2574-5442-0104_TAIL LIGHT,LV7-T-815_NK001478_STEERING FILTER,LV7-T-815_443 115 187 824_WAT
Resistance,Bush,Tappet Packing,Hose Fuel Small,Hose Fuel Big,Pneumatic Valve,Regulator,Oil Cooler P
Electrodes welding steel,Solder Wire Rosin Cored,Abrasive Cloth Emery,Flux Soldering Paste,Tape Adh
Fuel Pump Bosch,Mounting Eng Rear,Pad,Pressure Control Valve,Distributor Head
DUAL VALVE REP KIT,4 WAY SP RELAY,WHEEL BEARING,WIND SCREEN BEEDING,AIR COMP SEAL KIT,WIND SCREEN G
Gasket Cylinder Head,Fuel Filter,Air Pressure Pipe,Front Door Glass,Over Flow Bleeding Pipe,Sleeve 
Oil Seal,Hose Flexible,Solenoid Switch,Field Coil Assembly,Dual Brake Valve VOSS,Tank Assembly Fuel
Malted Milk Products
SOLAR FLEXIBLE MODULES,BATTERY SET 12V 150 AHC,HYBRID INVERTER,DC POWER CABLES,DCDB BOX,MC4 CONNECT
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Guava Juice (180 ml),Guava Juice (1 ltr)
Mango juice (1 ltr),Mango juice (180ml)
Digestive Candy
Walnut Kernel (Vacuum Sealed)
Roasted Flax Seeds
Egg Fresh
Mango Fruit Drink (in Canned)
HUB BEARING OUTER SKF 580 572,OIL SEAL,DRIVE ASSY,ASSY PULL CABLE ACCELERATOR,TOGGLE SWITCH,SPARK P
MAHINDRA MAXIMILE FEO
Tablet Drontal,Injection Belamyl,Powder Magnesium,Injection Iron,Injection Etophyline,Syringe 10ml
Title 1,Title 2,Title 3,Title 4,Title 5,Title 6,Title 7,Title 8,Title 9,Title 10,Title 11,Title 12,
ms pole,ms fence wire 3.5 km,barded wire,clip for joint,terminal post cap,rail end cup,line post ca
Hose 18MM,Hose 25MM,Hose 10MM,Hose 12MM,Hose 16MM,Hose 18MM,Hose 48MM,Hose 32MM,Hose 38MM,Hose 20MM
COIL ASSY IGNITION,SENSOR ASSY CAM POSITION,VALVE ASSY,AUXLIRY WATER TANK COVER,FIELD COIL ASSY,HAN
Besan (V2) as per IS 2400 (Q4)
SOLUTION RUST REMOVING (TOT ITEM)
ANTI CORROSION INHIBITOR AUTO RUST
GREASE LONG LIFE PD 00 OPTIMAL
Beer bottle holder,Cooker,Dosa Tawa,Kadhai,HB Machine,HB Strips,Accu Check Strips,Accu Check Machin
ANTENNA-10-108MHZ 125W TYPE LB 30108 SF/
Multivitamin Capsules/ Tablets
Pudina Capsules
Isabgol
Rasgulla
Gulab Jamun
Soya Chunks
Honey
Tomato Ketchup
Tomato Puree
Mixed Pickle
Water Pipe,Water Tank,Desert Air Cooler,Plastic Table,Drill Machine,Gate Repair,Finger Print Device
LV1R90, 5331720322383, PACKING RING,G1, NKCW0006, COPPER WASHER 19MM,G1, NKCW0009, COPPER WASHER 11
Hose Mixing in 119778 49040,Hose Drive in 1197780 49080,Hose CWS by Pass 119778 48010,Hose P C Oil 
Hand pump cr 1a 2266,Pneumatic Valve,Bowden Cable,Window dropper,Cab Lifting Electric Control,Maste
Modular Work Stations (V2),Modular Work Stations (V2),Modular Work Stations (V2),Modular Table / Me
Two Canopy Multi Play Station,Triceps Puller,Sky Walker,Back Extension,Sit Up Board,Double Twister 
Power Generator - DG Set (up to 900 KVA),XLPE Cable for Working Voltages up to and Including 1.1 KV
Power Generator - DG Set (up to 900 KVA),XLPE Cable for Working Voltages up to and Including 1.1 KV
Almirah - Handcrafted (Q3)
Public Address System (Q3)
Table Fan / Wall Mount Fan / Ceiling Mount Fan as per IS 555
Glue Stick (V2),Self Adhesive Flags (V2),Pressure Sensitive Adhesive Tapes with Plastic Base (V3) C
Supply and replacement of Synthetic Engine oil,Supply and replacement of Oil Filter,Supply and repl
CLUTCH M CYL ASSY NEW MODEL,CLUTCH M CYL ASSY OLD MODEL,CLUTCH M CYL REP KIT,CLUTCH PLATE NEW MODEL
S A Fuel Hose,Mud Flap Outer,Insul Bush,Laminated Passanger Door Glass,Hose Pipe,Assy Radiator Pipe
Fevicol SR,Leather Cloth Black,Plywood for General Purpose,Sheet Cellular,Sheet Cellular,Paint RFU 
Joint Thick Iron Sheet Covered,Electrodes Welding Steel Mild,Steel Angles,Electrodes Welding Cast I
Cable Electric Copper Conductor,Cable Elect PVC single,Plywood General Purpose,Adhesive Synthetic R
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Air Compressor,Assy Clutch Booster,Injector Assy,Injector Nozzle,KM Sensor
ACCELERATOR CABLE FOR FLT 2 TON,ALTERNATOR ASSY FOR GEN SET,HEAD GASKET FOR TRACTOR SONALIKA,COUPLI
LV7STLN, P-3700820, SOLENOID SWITCH,LV7TATA, L01402000041, BRUSH GEAR ASSEMBLY,LV7STLN, F7X00200, F
Banana,Mango,Papaya,Mussambies,Pineapple
Paracef power,Tissel kit 4 ml,puralbumen power 200 gm,Puralbumen 400 gm,Soln sodium Hypochlorite 5 
Heavy duty trestle,Water pump motor,Water supply pipe,Glass bottle,Stock register
REPAIR KIT AIR COMPRESSOR,TENSIONER BELT,HOSE ENGINE TO RADIATOR,ASSY TAIL LAMP RH,HOSE PLAIN,INJEC
FVICOL SR 998,FIELD COIL ASSY,CARBON BRUSH,AVR,THREAD ROLE,GASKET SET,GASKET CYL HEAD,OIL FILTER,PL
equine hoof glue,equine hoof glue applicator,tar bandage,horse glue tips,large bore infusion set
Bloer Assy,Hyd Head,PRV Valve,Vane Pump,Handle Door Inside Pull,Brake Lining,Speedometer,Nozzle,Noz
1146588 LOADING TROUGH
Black Tea as per IS 3633 (Q4)
ANNABOND,THREAD TAPE,INSULATION TAPE,FEVIQYICK,M SEAL,ARALDITE,BTY TERMINAL,ELCT WIRE COPPER
Ram Assy Hydraulic,Air Filter Element,Oil seal Tfr Case,Weather Strip LH,Weather Strip RH,Solenoid 
WIPER MOTOR 17W,REGULATOR,ENGINE GASKET KIT LOWER,ENGINE GASKET KIT UPPER,ROTOR FINAL ASSY,ASSY SUN
Repair of Cannon LBP 2900 Printer,Repair of Cannon Image Runner IR2525W,Repair of Cannon Image Runn
FPV Drone
Fixing Bracket Assy,Solenoid Switch,Fuel Feed Pump,Repair Kit Piston Ring,Suction Hose Assy,Front B
Rubber Coupling,Starter Rope Assy,Carburator Assy,Steel Angles,Feed Pump
Head Light Bulb,Head gasket,Side Mirror,Tappet gasket,Door rubber,High pressure hose,Side Mirror,Br
REAR VIEW MIRROR,TRANSFER CASE KIT,WINDOW LOCK,CYL ASSY RR WHEEL,FUEL FILTER,HEAD LIGHT BULB,BEARIN
Valve assy IAC Motor,Body assy Throttle,Tank Assy Fuel,Hing Door Rear,Lock assy gate side,Bty Cut O
Head Lamp Water Light,Hose,Brake Valve,Clutch Booster VG 3284,Hose 8X600,Pressure Hose 13,Gasket Cy
Hose Connection,Sid Gear Box Oil Seal,Seal Oil,O Ring,Hose 15 MM,Hose 25 MM,Hose 32 MM,Hose 10 MM
High Pressure Hose,Bearing,Hose,Hand Brake Valve,Inner Bearing,Shaft Assy Propeller,Ring Set,Armatu
BRAKE SHOE REAR FOR HERO HONDA,BRAKE SHOE FRONT FOR HERO HONDA,CARBURATOR ASSY FOR RE,FLY WHEEL RIN
Unmanned Aerial Vehicle (UAV/UAS) as per MHA QR
PS-4 EXTREME DUTY 10W50 4 CYCLE OIL
Oil Filter,Fuel Filter Water Separator,Starting Rope Assy,Valve,Carbonator Assy,Ring Piston,Eng Mgt
PITTONS,ROCK HAMMER,PARACORD 3MM
Hydroxyprogesterone Caproate 500 mgobilique2 ml,Hydroxpropyl Methycellulose USP 0.3 percent w obili
Turmeric,Red Chilli Powder,Corainder Seeds,Cumin Seeds,Black Paper,Large Cardamom,Clove Whole,Musta
Financial regulations part one Vol point one,Delegation of financial powers rules,Army local audit 
Plaintain Green,Brinjal,Lady Finger,Pumpkin,Beans Cluster,Cucumber,Snake Gourd,Tinda,Cabbage,Carrot
LED DISPLAY BOARD (2D) WITH ACP SHEET MOUNTED ON STAINLESS STEEL FRAME SIZE (4 X 4 FT)
Fish Fresh
Potato Grading Machine
Water Storage Tank 1000 ltr capacity,1 HP Water Pump,16 mm PVC pipe line,Fog Nozzle,Water Filter,Ti
Digital telephone binatone,Digital telephone Panasonic,Battery 1 5 AA,Female RJ 45 Connector,Male R
Assy Kit Shoe Rear,Linkage Bush Kit,Assy Oil Filter,Rear Shock Absorber,Air Filter Element,Field Co
Individual First Aid Kit,Pralidoxime 500 mg per 20 ml Inj,Diazepam 10 mg 2 ml Inj,Protamine Sulphat
Drive shaft,Cam plate,Crossed disc,Timing device piston,Governor shaft,Nozzle
Absorber Assy Shock Front,Clutch Release Bearing,Wabco Clutch Booster Alternator F-5P00500,Radiator
Custom Bid for Services - As per BOQ item No 1 Outsourcing services for Semi Skilled Electrician 06
Cylinder head assy,Piston ring set,MCB 63 AMP,Oil filter assy,Oil sending unit,AVR Assy,Water separ
HSS Thread Cutting Tap Set M39 x 1.5 mm,HSS Thread Checking Plug Gauge Go and No Go M39 1.5 mm 6h,D
OIL COOLER PIPE,DOOR GLASS,PRESSURE PLATE,HYDRAULIC HOSE PIPE,GEAR BOOSTER R KIT,DRIVE ASSY,ASSY CL
Bty 12 Volt 7 AH for 1 KVA UPS,Internal DVD writer for PC,Teflon for HP printer 1020 Plus,Wireless 
Grease CIATIM-201
Custom Bid for Services - ----
Polyethylene saloxoena PES-3
Oil OM-58
Grease OKS 480/9480 Defence
NB 52 Oil Kluber Isoflex TOPAS/ Isoflex (R) TOPAS NB 152 Kluber
Solar Inverter with Solar Panels, Batteries, Wiring & Installation
ACCESS CONTROL SYSTEM FOR OFFICE
STARTER MOTOR 12 VOLTS,ASSEMBLY UNIVERSAL JOINT,WINDING FIELD MAIN,BRUSH CARRIER ASSEMBLY,DRIVE ASS
SPEEDOMETER ASSY,REGULATOR ASSY LH,BRAKE DISC,COVER ASSY PRESSURE,OIL FILTER,GEAR ASSY SELF STATER,
Servicing of Air Conditioner,Gas Refilling of Air Conditioner,Panel Repair of Air Conditioner,Repai
Egg Powder (Spray Dried) (V2) (Defence)
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
FUEL TANK CAP,UNIVERSAL JOINT,WIPER BLADE,CLUTCH CABLE ASSY,AIR PRESSURE PIPE,DRIVEN DISC,TIE ROD E
NEEDLE BEARING,SA HOSE STG TO BOX,WIPER BLADE,PRESSURE PLATE ASSY,SLEEVE CYL ASSY,CLUTCH PLATE,WIPE
HYDRAULIC SEAL FOR FLT,REFRIGERANT GAS CANS,WELDING ROD,WIRE ELECTRONIC 15MM,ANGLE IRON 19MM,MS SHE
Inverter as per choic buyer sample brand,15 AMP Socket,Paint for Mod of Lec Hall,Hitex Gum Dendrite
Relay 24V,Rear Brake Shoe,Speedometer Cable,Oil Filter,Pneumatic Valve,Head Cylinder Gasket,Rivalin
5 Part Automated Hematology Analyser (V2)
Custom Bid for Services - CONSULTANCY SERVICES FOR SOIL INVESTIGATION AND PREPARATION OF DETAILED E
Z1, MISC-DCH-2740332020500925, CU 4 PIN MALE CONNECTOR,Z1, MISC-DCH-2740332020500925.1, CU AND UU 4
Electric Fan High Speed Motor Assy,Low Speed Motor Assy,Glove Box Assy,HFL Bolt,Assy Trinary Pressu
ALS INJECTOR OVERHAUL,ALS EDC PUMP OVERHAUL,ALS VALVE GRINDING,ALS FUEL PIPE REPAIR,ALS AIR PIPE RE
LV7 TATA DUAL BRAKE VALVE,LV7 TATA MASTER CYL R KIT,LV7 TATA TANK COOLANT VEHICULAR,LV7 TATA CLUTCH
LV7 MG SPARKING PLUG,LV7 MG MOUNTING PAD,LV7 MG PILOT BRG,LV7 T 815 FUEL FEED PUMP,LV7 T 815 BECONE
LV7 T 815 MAIN BRAKE VALVE,LV7 TMB HOSE,LV7 MG FUEL FILTER,LV7 T 815 CLUTCH VALVE,LV7 T 815 REVOLUT
LV7 MG FUEL FILTER,LV7 STLN CLUTCH MASTER CYL REPAIR KIT,LV7 STLN FUEL CUTT OFF SOLENOID,LV7 TMB HO
LV1 R72 AUTOMATIC PRESSURE REGULATOR,LV7 STLN CLUTCH MASTER CYL REPAIR KIT,LV7 STLN FUEL CUTT OFF S
Car Diary,Register for MT and Water,Register for MT and Water,Baby indent,Register,Attendance regis
Sugar (V2) (Defence) (Q2)
MOTOR FUEL PUMP,SUSPENSION BUSH KIT SET COMP,FRONT WHEEL BRG,Injector Fuel,4ST RELAY,BENDIX DRIVE,C
Soluble Coffee Powder (Refill Packs) (V2) (Defence)
Track Suit,Warm Up Shoes,Towel Hand,Cap,T Shirt,Shorts,Socks,Floater,Inner Stretchable T Shirt and 
Title 1,Title 2,Title 3,Title 4,Title 5,Title 6,Title 7,Title 8,Title 9,Title 10,Title 11,Title 12,
Poly carbonate profile sheet 3 mm clear compact,Poly carbonate profile sheet 2 point 5 mm GI Nail,P
ORL Shelter
Supply of complete structural stores and W2 panels of 3D printed PD including all fixtures,Supply o
Sand,Aggregate 20mm,Ambuja Cement,12 inch Nut Bolt,Tile Cutter Blade,Binding Wire,Iron Saria,SDS Sc
MTITEMS 1,MTITEMS 2,MTITEMS 3,MTITEMS 4,MTITEMS 5,MTITEMS 6,MTITEMS 7,MTITEMS 8,MTITEMS 9,MTITEMS 1
Socket set,Pipe wrench 600 mm,Pipe wrench 300 mm,Nylon Belt 5 Ton,Combination spanner set,C Type sp
Stack(Flight Controller and Electronic Speed Controller)
AIR PRESSURE PIPE LARGE BSIII,SPEEDO METER CABLE BSIII,PNEUMATIC VALVE BSIII,AIR CLEANER HOSE BSIII
Desktop And Application Virtualisation Software
V5 Pen,V7 pen,Uniball Air Pen,File cover printed,File cover Normal,Hauser pen,Sticky pad,Register 2
Printer Sharing Hub,Printer Cable,Logitech Presenter All in One,Air Blower,9V Battery,RJ 45,RJ 45 C
Acetic Acid Ear Drop,Bismuth iodised Paraffin Paste 10 gm,Tube tracheostomy with Double Lumen cuff 
Boric Acid Powder 20 gm,Durapore Adhesive Tape 10cm width,Lacrimal Probe Set Of 4,Paediatric trache
Grommets Shah,Lacrimal Stent silicon,Antifog Solution 6gm,Tube tracheostomy with Double Lumen cuff 
Aluminium Square Surface Celing Light,Door Matt 2x3,Flag Stand,Flag,Iron Stair Case,ACP Board 1x8 F
CANINE SCENTOLOGIX KIT (15 EXPLOSIVES)
Coloured File Cover,Pt II Order Binding,Register,White File Cover,A4 Paper
White Paint,Red Paint,Yellow Paint,Black Paint,Selver Paint,Green Paint,Terracotta Paint,Tarpin oil
Peripherally Inserted central catheter size 1 F,Ram cannula size 1 Green,Ram cannula size 2 Blue,Ra
Boot High Ankle PU Rubber Sole (Defence)
Z1-5961012095010-DIODE SILICON,Z1-59610101724166-DIODE SILICON
13 inch M4 Chip Laptop 512 GB
Plain Copier Paper (V3) ISI Marked to IS 14490,Plain Copier Paper (V3) ISI Marked to IS 14490
Sugar (V2) (Defence) (Q2)
P-1303727,5945-007475,6220-004485,2940-001046,41331M62020,X-7413400,2157-5440-0115,09471M2057,F-828
14 Plus 2-in-1 Laptop 512 GB
Side Hand Rail Plastic Body,PU Bag Asian of 10 Ltr pack,Bituman Tape 4inch wide of 10 Mtr Long,85 x
LED Batten,XLPE Cable for Working Voltages up to and Including 1.1 KV as per IS 7098 (Part 1),XLPE 
HAND PUMP,BRAKE CYLINDER,TURBO CHARGER,BRAKE BOOSTER,CYLINDER HEAD,CYLINDER HEAD GASKET,NOZZLE,CONN
Hand wash containing chloroxylenol Bott of 200mL,Lignocaine Hcl solution 2percent for IV use 50 ml 
Enoxaparin 20 mgobilique0.2ml Inj,Enoxaparin 80mgobilique0.8ml Inj,Ethamsylate 250 mg Tab,Ethamsyla
All in one PC core i9 16 GB RAM,PTZ camera elite FHD premium 20x,Quadro Mic with extension,HDMI Cab
Human Chorionic Gonadotrophin 5000 IU Inj,Ipratropium Bromide Respirator soln 500 mcgobilique2 ml r
WATER SEPARATOR FILTER BOSCH,OIL FILTER 500 ML,FUEL FILTER BOSCH,AIR FILTER BOSCH,AVR 30 KVA,AVR 7.
AC GAS BOTTLE,PHOSPHATE CAOTING METAL,WD 40 SPRAY,M SEAL,ARALDITE,ELECT WELDING ROD
352 DIA Clutch Disc Assy,Clutch Slave Cylinder,Nozzle,Element Oil Filter,Stoper Cable,Head Cylinder
Air Filter,Oil Filter,Hyd Filter,Fuel Filter,Bearing,Hose,Hyd Hose,Head Lamp Assy,Universal Joint,K
Ice Machine Made
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
Fuel Flexible Pipe from Feed pump to fuel,Filter Assy Shorter II 77MM,Spindle Wheel Bearing,Pinion 
FD MOB TOILET TROLLEY MOUNTED (2 CUBICLES)
Epson Printer L 15180,Epson Printer L 4260,Epson Printer L 6580,HP Scan Jet Pro 2600 F 1,Splitter c
Repair of Rajak TMU SR-2 SED 00127
V7 Pen Blue,Transparent Tape 2 Inch,JK Paper 70 GSM,CD Envelope,Cloth Envelope 16x12,Stapler Small,
CHANGE OVER SWITCH,HORN 24V,VANE PUMP,COMBINATION SWITCH,FIELD COIL
Pnumatic Cylinder,Assy Steering Drag Rod,Door Lock LH,Head Light Relay,Head Light Bulb
FEED PUMP,BRUSH PLATE,SOLENOID SWITCH,FIELD COIL ASSY APU,FLY WHEEL RING,GLOW PLUG,ARMATURE
Oil pump Assy,Field coil Assy 24V,Roller Bearing,Drive Assy 24V,Gear Lever Kit,Element Oil Filter,S
Overhaul of auxiliary gear box,Rollar bearing,Input Shaft,Fixed dog clutch,Sliding dog clutch,Speed
Overhaul of steering gear box and rear axle assy,Selector shaft assy,Seal kit turner cover,Worm rac
Overhaul of steering gear box and main gear box,counter shaft,Constant Mesh Gear,Reverse idlear sha
Piston Ring Set,Mtg Pad,Loom Assy Complete,Fuel Filter Element,Oil Filter,Fan Belt,Packing Kit,Cyl 
RAM DDR III 4GB,BTY 12V 7AH,BTY 13.80V 7AH,RAM DDR IV 4GB,TEFLON PAPER
Dexamethasone Sodium Phosphate 4 point 4 mg, Equivalent to Dexamethasone Phosphate 4 mg slace ml 2 
8 Ft Air Curtain with sensor Including Installation
Television (TV) (V2) (Q2)
Goods Transport Service – Per Trip based  Service - Machinery & Equipment; RECOVERY VEHICLE MINIM
DISTRIBUTOR HEAD,VANE PUMP ROTORY VANE PUMP,ROLLERS,CAM PLATE,FUEL TEMP SENSOR,BEARING PIN,NOZZLE,C
AVR ASSY,PISTON ASSY,PISTON RING SET,HEAD GASKET,JOINT FOR PUSH ROD TUBE,OVERHAULING KIT,NOZZLE MAK
Goods Transport Service – Per Trip based  Service - Machinery & Equipment; JCB BACKHOE LOADER FOR
Short Term Cab & Taxi Hiring Services - SUV; Outstation; APPROX 880 KM PER TRIP FROM WALONG/KIBITHU
Sugar (V2) (Defence) (Q2)
Sugar (V2) (Defence) (Q2)
Sugar (V2) (Defence) (Q2)
Goods Transport Service – Per Trip based  Service - Packed Water, Packed Milk, Household/Office, 
LATCH HOOD,COMBINATION SWITCH,CYLINDER HEAD GASKET,REV SELECTOR SHAFT,MASTER CYL POWER UNITCLUTCH M
74 HC 32,IRF 840,Mosfet BLF 242,IC TL 0641,ECG 006C,IAM 82008,IRF 9530,SUB 65 PO6 26,IC 2854 AN FN,
Transistor FET N Chan Type UF 28100V,Antenna 50 OHMS 136 174 MHZ Type GPA 150 Antenna IV,Transistor
TAPER ROLLER BRG,ROTOR ASSY,FD COIL,VALVE RELAY AIR FOOT VALVE ASSY,QUICK RELEASE VALVE,REGULATOR C
Starter Motor Assembly (Q3)
SINGLE ELEMENT FUEL PUMP,ADAPTER JCB,HYDRAULIC PUMP PLATE,HYDRAULIC PUMP REPAIR KIT,RECTIFIER WITH 
Bush Plate,Regulator LH,Maj Repair Kit Air Complete,Gear Lever Kit,Combination Switch,Mud Flap,Spid
Value,Repairing of C Plus charger couroir charges,Star Bit,Aluminium Cutter,MCB Box 6 Way,MCB 16 Am
Haldi Turmeric Powder,Daniya Coriander Powder,Chilli Powder,Sambar Powder,Chicken Masala,Garam Masa
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
AERIAL INTRUDER JAMMER GUN SYSTEM
Custom Bid for Services - Maintenance of General Area Around Store Sheds, Boundary Wall & Store Pli
Custom Bid for Services - Loading Unloading & Shifting of ETSR, Non ETSR & Sector Stores at GE 583 
Custom Bid for Services - Painting and preservation of Bailey Bridge Set No 22 held with GE 583 Eng
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others,Manpower Outs
BUCKET WATER,CLOCK WALL BATTERY OPERATING QUARTZ,HOLDERS SOAP SHAVING MK2,AXES SINGLE BIT FELLING H
Tab Quetiapine 100 mg,Vasopressin 20 unitsobiliqueml Inj 1ml ampoule,Vecuronium Bromide 4mgobilique
Bracket Plate for Chasis,Repair Kit for main Cyl Clutch,Fuel Filter Assy,Hose Dia,Drain Screw
RESISTOR 10K OHM 5 W,RESISTOR 47 OHM 5 W,BNC CONNECTOR,BNC CONNECTOR 10 FEET,GP PCB,LED MAGIFYING G
CLUTCH CYL ASSY,SLEEVE CYL ASSY,HEAD LIGHT ASSY,SPARK PLUG,GEAR LEVER KIT,HOSE ASSY,REPAIR KIT,FAN 
Dhaincha (Sesbania Aculeate) Seed
Z6 R72 6625-72-029-5970 CONTROL INDICATOR BOD-1S-000SB,LV2 ICVS 5330720115456 765-50-2445 PACKING M
PRECISION SCREWDRIVER SET 6 PCS,STANLEY TELECOMMUNICATION TOOL SET 53 PCS,HOT MELT GLUE GUN,STANLEY
Tab Levosulpiride 25 mg,Tab Methylprednisolone 4 mg,Tab Perindopril 8mg,Tab Pramipexole 0.25 mg,Tab
Gear Axel SSL,Solonide Valvw breaks,Heas gaskit SSL,Hose Assy,Banjo Assy,Hose Assy,Break valve Assy
CLUTCH PRESSURE PLATE,FUEL LIFTING PUMP,WINDING FIELD MAIN,CLUTCH VALVE,GEAR RING FLY WHEEL,HOSE TM
Windows 11 Pro 24H2,Microsoft Office 2024 Pro Plus,CORAL Draw Graphics Suite
Weld Mesh Panel for Perimeter Security Fence as per IS 4948
Lignocaine Hcl 2 percent with adrenaline 30 ml,Lignocaine Hcl gelly 2 percent,Tab Paracetamol 50 mg
FUES 50A LIGT BULB,HELOGEN BULB,ELECTRONIC FLASHER UNIT,RELAY ASSY,ELEMENT AIR FILTER,SPARK PLUG,FA
S500 Carbon Fiber Quandcopter Drone Frame Kit,EMAX MT2213 935KV Brushless DC Motor for DroneBlackCa
990-115-005-000 MAGNETIC SWITCH -19024320,990-115-006-000 PRESSURE MAGNET-19024324,F-J106300 DOUBLE
FUES 60A,FUES LINK BLADE C 30A,BULB RL 12V,FLASHER UNIT 24V,ASSY COMBINATION SWITCH,BTY CUT OFF SWI
K9/T72/FF-172-82-091SB Mannual Fire Ext (Mtrl No 10491175)
NK0001 SMPS,Nk00014 KEY BOARD AND MOUSE COMBO,NK0007 INTEL H410AMD MOTHER BOARD FOR DESKTOP,NK00303
Injection Tetanus,Quinapyramine Sulphate,Injection Lignocaine,Povidone Iodine,Needle
3 KVA UPS,USB to LAN Converter,USB to USB Extn 5 mtr,USB to USB Extn 10 mtr,USB to USB Extn 15 mtr,
LV7TATASTORME, 269915400119, SELF STARTER,LV7TATASTORME, 278915400104, CAMSHAFT POSITION SENSOR,LV7
Uncemented THR Ceramic on prosthesis 1 Uncemented fully porous coated acetabular cup 2 Biolox Delta
Handball Court with Synthetic Surface, Goal Post and Allied Accessories
SPIDER BEARING,HEAD LIGHT LED BULUB,WIPER BLADE,DISC CLUTCH,FUEL PUMP ASSY,PRESSURE PLATE,CLUTCH CY
Purchase of Posters and Banners for Tour,Purchase of Kitting Items for Participants,Messing and Mea
Pressure Plate,Release Brg,Cyl Head Gasket,Solenoid Switch,Clutch Plate,Spider Bearing,Armature Ass
Air Dryer,Sleeve Cyl Assy,Pressure Plate,4X4 Cable,Sleeve Cyl
Knuckle brg,Air Dryer Assy,Pressure Plate,Sleeve Cyl Assy,Pressure Plate,Clutch Plate
Lifting Power Motor,Tube Mosquito Killer Blue Colour,Zero Watt Bulb Red,Zero Watt Bulb Green,Zero W
Bush Set,Air tank Pressure Pipe,Knukle Bush,Acc Cable,Knuckle Brg,Fan Belt
Central Brain Motherboard Circuit,Capacitor 2 MFD,Capacitor 2.5 MFD,Capacitor 3.15 MFD,PVC flexible
Combination Switch,Driven Disc,Ros Suspension,Rectifier Plate,Combinanation Switch,Inlet Valve Assy
Chili Powder,Haldi Powder,Garlic,Jeera,Rai,Black Papper,Small Cardamom,Chicken Masala,Garam Masala,
GASKET SET,HAND BRAKE CABLE,ASSY FUEL FILTER,HOSE INTER COOLER OUTLET TO THROTTLE,ASSY WINDOW REHUL
Guardian Link Sensor 4 Medtronic with Bluetooth,Guedels airway size 0,Guedels airway size 00,Guedel
Cheese Cube,Cheese Slice,Cheese Spread,Cheese Spread 1,Cheese Spread 2
Luggage Xray Scanning Machine
Telecommunication Cable - Fully Filled Petroleum Jelly or Absorbent Thixotropic Gel (V2)
Infrared Thermometer,Massage Gun,Aroleap pro
Micro CCT DGTL D27,Micro CCT DGTL D28,Diode SR 5100,Regulator 7812,Main Board
NOVOPEN NEEDLE ALL SIZE,VALCIVIR 500 MG TAB,SODIUM VALPROATE ORAL SOL 200MG 5ML BOTT OF 100 ML,SYP 
M4 Chip Computer
Dash Board Camera,A4 Paper,A3 Paper,Colour Paper all colour,Fevicol half Ltr
RUBBER HOSE AIR INTAKE,LEVER WINDOW DROPPER,REAR VIEW MIRROR RH,STARTER KIT,BEARING REAR,PNEUMATIC 
Hard Sheet 4 mm,Drawing Sheet All Colour,Talc Sheet 100 Mtr,Drawing Roll,Thermacol 1.5 inch,Cutter 
Coir Mat Jute
MINERAL JELLY
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
The Fabricated structure of toilet block 10 Cubicle,Plumbing Itmes,Electrical Items,Sanitary fittin
Plywood 25mm size 8ft x 4 ft,Plywood 8mm size 8ft x 4 ft,Fevicol SR 998,Welding Electrodes,Wood Cut
Release bearing,Air dryer repair kit,S P Valve repair Kit,Thermostst valve New modle,Oil filter old
Welding Rod,Cutting wheel 4 inch,Feviquick 30 ml,WD 40,M Seal,Radium Sticker Reflection strap,Ragzi
Coconut Powder,Papad,Mango Pickle,Mixed pickle,Garlic pickle
Temperator sending unit,Speedometer assy,Fuel pump motor,Eng mounting pad,Universal joint or U J Ki
COVER ASSY,ASSY CLUTCH DISC PRESSURE PLATE,THERMOSTAT,MINOR REP KIT AIR COMPRESSOR,WHEEL CYL REP KI
Provision of soiling and GSB,Provn of RRM Retaining wall,Provn of RRM Retaining wall,Provn of 600 m
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Commercial; Vehicl
NON SKID CHAINS FOR MAHINDRA SCORPIO
Anchored Point Device Setup,High Frequency Tags,Reader Device,Web Based Application,Installation an
Hand Held Thermal Imager
Inj Texableed 20 ml,Inj Frusmide 10ml,Inj Tonophosphan 30 ml,Gloves with full length sleeves pkt of
Servo Press 150
Oil watch
Calibrating Oil ISO 4113
SAE 0W20
Material and labour for asphalt base 30 x 15 mtr,Synthetic all weather acrylic surface ultra cushio
Banana,Mango Dahsehari,Mango Safeda Neelum Kesar Langra Fazli,Pear,Musk Melon,Papaya,Sweet Orange,W
RADIO TRACKING SOFTWARE FOR VERTAL DMR
LV6-MT1,4730-000049,LV6-MT12,2910-000007,LV6-MT14,2640-000048,LV6-MT6,4720-015320,LV6-MT6,F-0331250
Distributor Head,Drive Shaft,Body Housing,Repair Kit,Vane Pump,Timing Device Piston,Cam Plate,Injec
Portable House Containers
Ink Black 003,Ink Colour 003,Cartridge 2365,cartridge 88A,Cartridge 12A
Samsung Galaxy Z Fold 5 12 GB RAM 256 GB,Adopter with Type C Cable,SIM Tray Ejector,Wireless or Wir
PTZ CAMERA,NVR CP PLUS,POE SWITCH CP PLUSH,HARD DISK 1 TB,LED MONITOR 22 INCH,CAT 6 DLINK CABLE 305
LT WIRE,NOZZLE 778,PUMP ELEMENT 104,DELIVERY VALVE 341,NOZZLE 5509,TRANSPARENT TAPE,M SEAL,ANABOND 
Annual Maintenance Service  - Photocopier Machine - Photocopier Machines (Monochrome , Laser , Comp
Unmanned Aerial Vehicle (UAV/UAS) as per MHA QR
Spike Barrier (V2) (Q3)
TYMPANIC MEMBRANE TEMPERATURE MONITOR
RUST CLEANER SPRAY,R22 REG GAS,THROTLE BODY CLEANER,SEALING COMPUND,GASKET FOR CYL HEAD,SEAL OI ID 
JOINT ASSY UNIVERSAL,RING BRG RETAINER,AIR FILTER ELEMENT,COVER ASSY PLATE,SELF STARTER ASSY,RADIAT
Temp Sending Unit,OIL FILTER,FUEL FILTER,Fuel water seperater,AIR FILTER,FUEL STAINER
RUBBER HOSE,OIL SEAL FRONT HUB,SPARK PLUG,AIR FILTER,BRAKE SHOE,GREASE SEAL,BUSH,LENS TAIL LIGHT AS
ACCELERATOR CABLE FOR TATA 2.5 TON 715TC,UNIVERSAL JOINT FOR TATA 2.5 TON 715TC,CLUTCH CYL ASSY FOR
MOUNTING ENGINE FRONT,ASSY CABLE COMPLETE,FUEL FILTER ASSY,AIR FILTER ASSY,FRONT BRAKE PAD,OIL FILT
TEA CTC 500 Gms Pack,Pack TEA CTC 500 Gms,500 Gms Tea CTC Pack,CTC Tea 500 Gms Pack,Pack Tea CTC 50
High End Desktop Computer,All in One PC (V2),Computer Printer (V2),Multifunction Machine MFM (V2),M
Oil filter,Air filter,Washer,Maximile ultra,Maximile elite,Maximile ultracool
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title13,Titl
Toner Cartridges / Ink Cartridges / Consumables for Printers
E CFA RE 01 Budesonide Bp 160 Mcg Formoterol Fumarate 4DOT5 Mcg Dry Powder Multi Unit Dose Inhaler 
All in one,Workstation,Projector Full HD,Visualiser Desktop Document Camera,Switcher HDMI,Switch Ma
Power Generator - DG Set (up to 900 KVA),Power Generator - DG Set (up to 900 KVA),Power Generator -
Closed Circuit Television IP Bullet Camera 5MP,Network Video Recorder 8 channel,Hard Disk Drivers 1
Medicine Storage Bins FPO01 95x102x52 mm,Medicine Storage Bins FPO05 160x115x80mm,Medicine Storage 
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Custom Bid for Services - soil investigation for PM vocational lab at AF II Jamnagar
LV1/R72 229-01-01SB LEFT HAND BLADE UNIT (DRG NO 527 0870 0101)
Clutch Rel Brg,Repair Kit Fuel Pump,Air bag Control Unit,Injector Assy,Coller Assy,Electric Fan Ass
paint white,paint red,paint blue,paint yellow,Fevicol SR 998,Photo frame for calendar,wall paper,Wa
Sugar (V2) (Defence) (Q2)
PILOT BRG,FRONT AXLE SEAL,CALIPER PAD ASSY,INJECTOR ASSY,AIR FILTER,OIL FILTER,FUEL FILTER,ALTERNAT
LV7-T-815 443-332-010-000 Rear View Mirror Special,LV7-HMV-8x8-AL B0T10114 Tarpaulin HMV 8x8,LV7 T-
Fuel Pump Assy,Piston Ring Set,Injector Nozzle,Crank Shaft Bush,Cranck Shaft oil Seal
Hose Pump TE23201,Hose clamp TE20888,Hose Rod TC20962,Hose assy TE23546,Hose TE01926,Hose Fuel TE23
MICROSOFT WINDOW 11 PRO 64 BIT,MICROSOFT OFFICE 2021 PRO PLUS,QUICK HEAL TOTAL SECURITY 10 USER,QUI
WIPER ARM ASSY,WIPER WHEEL BOX ASSY,WIPER BLADE,WIPER LINKAGE,WIPER MOTOR GEAR,MUSIC SYSTEM,SPEAKER
SPIDER BEARING,HEAD LIGHT ASSY,BACK LIGHT ASSY,BRAKE PAD,KEY SET WITH FUEL TANK CAP,CLUTCH BRAKE LE
Cap Carbonyl Iron Zinc Folic Acid,tab Cefuroxime 500mg plus Clavulanic Acid 125 mg,Chlordiazepoxide
Caliper Assy,Steering Rod Assy,Clutch Cable,Bush Carrier Plate,Bulb,Pole Screw,Positioner Assy,RAM 
KIT UJ CROSS,CLAMP,BOLT,OIL FILTER,BEARING,AIR FILTER,PISTON RING SET,PISTON,PIN,PUSH ROD
Material and Labour for conducting soil investigation by drilling boreholes dia 150 mm and depth 10
Smart Phone
HMC THK FLTR Bpass BMC 1532,HMC THK FLTR Bpass BMC 1527,Semiconductor Devices Unitized Dual N and P
VGA to HDMI Connector,RJ 45 Connector,Display to VGA Cable,USB Extension Multi Port,D-link Cat-6 Ca
CLUTCH RELEASE BEARING,NEEDLE ROLLER BEARING,NEEDLE HOUSING,RADIATOR ASSY,MAIN BEARING SET,BRG CON 
Cabin Lifting Pump,Water Tank,Water Pump Hose,Gear Lever Kit,Thermostat Valve,Clutch Cyl Assy,Brake
2.5 sq mm wire copper,10 Sq mm wire Al,6 Sq mm wire Al,Socket 15 Amp,Heater Coil
Hiring of Professionals for Application Development and Maintenance - Development and related roles
Brake Disc Assy,Brake Plate Assy,Hydraulic Filter,Hydraulic pipe,PTO Flange,PTO Oil Seal,Feed pump 
Door Mechanism,Spring Assembly Rear,Cylinder Head Gasket,Feed Pump,Cabin Lifting Pump,Hose Assembly
UPS 1 KVA,PROJECTOR LAMP,LOGIC CARD,DVD WRITER SLIM,DVD WRITER,POWER SUPPLY CARD,FUSER UNIT,LOGIC C
Respiratory Pathogen Panel RTPCR kit with extraction kit
Ventilator Circuit,Yankur suction,Catheter Mount,Disposable Sterilised Bed Sheet,Eye patch,Corn Cap
LV7 TMB 2641 4370 0111 REP KIT DDU,LV7 TMB 2573 4370 0153 GRADUATED HAND BRAKE VALVE,LV7 TMB 2576 4
Rear Sprocket,Rear brake shoe,Front Brake Shoe,Eng Mounting Pad,Clutch Plate assy,Pressure Plate as
Clutch Plate,Brush Carrier Plate,Change Over Switch,Steering Gear Box Repair Kit,Wiper Blade,Regula
ARMETURE ASSY,CLUTCH SALVE CYLINDER,AIR DRYER WITH UNLOADER VALVE,ASSY CLUTCH DISC PRESSURE PLATE,C
Tapper Roller Brg,Clutch Cable,Horn 12V,Brake Pad,Bearing Tapper Roller,Isolator Switch,Solenoid Sw
Bus Hiring Service - Short Term - Outstation; 30-32 SHORT CHASIS BUS NON AC FROM WALONG TO TEZU BOT
Split Air Conditioner Including Green AC, Wall Mount Type (V2),Household Refrigerating Appliances a
Fixed Computer Workstation,Online UPS (V2)
ASUS Vivobook S 14 OLED, AMD Ryzen AI 9 HX 370, 2.0GHz, 24GB RAM, 512GB SSD, 3K OLED 16: 10 120Hz 4
Manpower Outsourcing Services - Minimum wage - Unskilled; Secondary School; Healthcare
BUS HIRING FOR THE MONTH OF APRIL,BUS HIRING FOR THE MONTH OF MAY,BUS HIRING FOR THE MONTH OF JUNE,
BRAKE SHOE,AIR DRYER REP KIT,AIR DRYER ASSY,TANK COOLANT VEHICULAR,ALTERNATOR 24 VOLTS 45 AMP,PISTO
Air Pressure assy,Universal joint,Door Lock Assy,Poly V Belt,Hose Assy
Y3 CVD-5970000440 Tape Insulation Cotton Self Adhesive 1 2,Y3 IYC-0839 Insulation Tape Electrical P
A4 Paper JK copier,White file cover with Logo,Pen Reynolds,Envelop cloth coated file size,Register 
Provn of Op Tr with Interlocking paving blocks with kerb stone FOR GELLING,Constr of 02 x Hume pipe
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Admin
20 KVA UPS,15 KVA UPS,10 KVA UPS,5 KVA UPS,3 KVA UPS,2 KVA UPS,Servo Stabilizer 5 KVA,Servo Stabili
HOSE RADIATOR,HOSE RADIATOR,STARTER KIT,JOINT ASSY UNIVERSAL,SPEEDOMETER CABLE,BRAKE SHOE REAR,GASK
External branding signage boards
Football,Volleyballs as per IS 417:1986,Volleyball Net as per IS 3345
Solar Street Lighting System (NTPC)
TMB Nozzle,TATA Servo Assy,TATA Vacuum Pump Assy,TATA Hose Assy Air Filter Outlet,Tata Assy Latch,T
Fexofenadine Hydrochloride Tab 120 mg,Fluticasone propionate inhaler for paed use 50mcgobiliquedose
NI BP CUFF,BTY 6V 4.5AH,CONNECTOR,NIBP NOSE PIPE,NITROUS OXIDE REGULATOR DOUBLE STAGE,ALLENGER X RA
FULE FILTER ASSY,OIL FILTER,AIR CLEANER ASSY,TIE ROD OUTER,BALL JOINT UPPER,BALL JOINT LOWER,KIT CA
SILENCER ASSY WITH EXHAUST AND TAIL PIPE,IGNITION AMPLIFER,GASKET EXHAUST FLANGE,SLIDING GLASS ARMY
Diclofenac Sodium 50 mgobilique enteric coated Tab,Dicyclomine HCL IP 20 mgplus Paracetamol IP 500 
ALS Ram Assy Hydraulic,TMB Electric Fan Assy,HH Insulator Carburator,MG Relay Main And fuel,TATA So
Diclofenac diethylamine 2.32percent wobiliquev Quick Penetrating Topical Solution30 ml Bottle with 
Steel Angles 75x75x6
UNIBALL PEN BLUE,BLACK BALL PEN DOMS,REYNOLD PEN BLUE,REYNOLD PEN BLACK,REYNOLD PEN RED,SKETCH PEN 
FUEL FILTER,BRAKE SHOE SET,COIL ASSY IGNITION,REAR WHEEL BRG,OIL SEAL HUB,DISTANCE PIECE,ARAMTURE A
Provn of Security Post Shelter part only FOR MENCHUKA,Provn of Security Post Shelter part only FOR 
MULTI GYM,TREADMILL,MULTI PRESS,BICEP CURL,TRICEP PRESS
LV2 ICVS 5365720272132 765-33-15 WASHER FLAT,LV1 R72 172 40 258 BOLT,LV1 R72 432 43 042 BOLT 432-43
Syp Montelukat 4mg Levocetrizine 2.5mg bott of 60ml,Syp NorfloxplusTinidazole bott of 60ml,Syp Oflo
oil 2 t supreme
Repair of Rotary Pump
Green Grass (Rajka) (Q3)
PC Computer,Desktop Visual Presenters,Wireless Cardioids Microphone,Two way PA Speaker,Digital PA S
1132558 PISTON
1015-003302(10549742) WHEEL RIM
Acrylic Polishing Cake,Cotton Buff For Dental Laboratary,Bud Bur Tungsten Carbide for dental labora
EQUALIZER KIT,HYD PIPE,FRONT GLASS,BACK PRESSURE VALVE,MOUTING ENGINE DZIRE,REAR AXLE OIL SEAL,HOSE
AMC of CCTV Cameras
Supply of stores for Bathroom Block 6C,Supply of construction material for Bathroom Block as per st
Focus Light,Iron Pipe 105,Rope 50 mtrs Havells,Car Flag,Silver letter,Cutting Scissor,Spray Pump wi
BALL JOINT KIT,BUSHING KIT SET,BUS STABILIZER,WHEEL BRG,RUBBER HOSE,TIE ROD END,FRONT AND REAR BRAK
CLUTCH MASTER CYL,PRESSURE PLATE,COVER ASSY CLUTCH,ASSY UNIVERSAL JOINT,DRIVE PINION,GEAR BRUSH,AC 
Fuel Filter,Oil Filter,Oil Filter,Brake Pad,Clutch Release Brg,Fuel Motor,Piston Ring Set,Accelerat
Lizol Floor cleeaner 500ml,Harpic 1 ltr,Room Freshener,Red Hit,Black Hit,Domex 1 ltr,Toilet freeshe
730-87-88,520-15-001-04,5330-381927,042-540-2660J,6620-000-050,2573-4370-0153
SIDE INDICATOR ASSY,BTY BOX KEY LOCK,AIR FILTER KEY LOCK,SIDE MIRROR,RADIATOR ASSY
STARTER ASSY BSIII,RECTIFIRE ASSY BSIII,ALTERNATOR BRG BSIII,ROTOR ASSY BSIII,TIE ROD END BSIII,CLU
ELEMENT,NOZZLE,DELIVERY VALVE,O RING,VALVE FUEL SYSTEM DELIVERY VALVE,OIL SEAL OD35XID19XW10
ROTOR ASSY,REGULATOR ASSY,RECTIFER ASSY,BUSH SET,AVR
FLYWHEEL RING BSIII,REGULATOR SR60 BSII,AIR CLEANER HOSE BSII,PNEUMATIC VALVE BSII,MUD FLAP BSII,SU
Main Leaf,Accelerator Cable,Crank oil seal,Driven Disc,Wind Screen glass,Wiper Blade,Oil Filter for
Molded Large Scar Realistic Elephant Head and Rhino Head (4' x 4') with Base (7' x 7') in FRP
Needle Bearing,Sealing Ring Hub,Propeller Shaft Assembly Rear,Slave Cyliner Assembly,Drive Assembly
FUEL FILTER FJ 4A4,CLUTCH BOOSTER REPAIR KIT,REPAIR KIT FOR AIR PRESSURE GOVERNOR,TARPAULINE,REAR V
AC Compressor,AC Gas,Clutch Master Kit,Slave Kit,Clutch Master Kit,Brake Fluid Container,Clutch Pla
Fan Belt,Fuel Filter,Wiper Blade,Pressure Plate,Clutch Plate,Clutch Release Bearing,Ignition Coil
Eco Paper,Highlighter,Transparent Tape,Transparent Tape,Transparent Tape,Brown Tape,Pentonic Pen,Ca
Clutch Master Cylinder Assy,Hose Pipe Upper Radiator,Brake Shoe Assy,Oil Seal Stearing,Air Pressure
A4 Paper 100 GSM,Long roll hand binding A3 Size,Long roll hand binding legal size,Register 300 page
WIPPER MOTOR ASSY BSII,TIE ROD END REP KIT BSII,WIPPER BLADE BSII,CLUTCH MASTER CYL BSII,AIR PRESSU
Garlic Pickle
Mango Pickle
Chilly Pickle
Pineapple Fruit Drink (In Canned)
Laminators (Q3)
Replaces Glass, cover, microscopic, rectangular PV 16442, 22 x 50 mm, made of USP No 1 glass, pkt o
KIT LINE BRAKE SHOE,HAND PRIME PUMP,FLANGE ASSY,SLEAVE ASSY CLUTCH,FLANGE,ASSY BALL JOINT,VALVE THR
2780 5450 0103 ASSY COMBINATION SWITCH,NK002141 TOGGLE SWITCH,6212 0510105 BULB 24V100W,6212 510067
Printer Head,Pick up roller,Logic card,Front panel,Paper feed roller
PUMP ASSY WATER,GASKET CYLINDER HEAD COVER,GASKET EXHAUST MANIFOLD,SWITCH ASSY CHANGE OVER,KNUCKLE 
Dimension Lactate Dehydrogenase Flex LDI 10284483 box of 480 test,Dimension Microalbumin Flex MALB 
Cap Duloxetine HCI 30 mg,Ethambutol 200 mg Tab,Ethambutol 800 mg Tab,Evening Primrose Oil 1 gm Cap,
FIP (MICO-BOSCH) FUEL INJECTION PUMP
HemosIL LA Negative control Kit of 10x1 ml,HemosIL D Dime Controls Kit of 10X1 ml,HemosIL dRVVT Scr
Z1_4295-109-601-71_RF POWER FET D41215S,Z1_4325-101-201-46_MC3372D,Z1_4393-136-601-82_DS 1501WS,Z1_
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Tent Extendable Frame Supported 4M and 2M Complete with Accessories (V2)
Chicken Eggs (Q3)
Colour File Printed 106 I Composite Platoon ASC,White File Printed 106 I Composite Platoon ASC,Regi
Kadhai Iron 20Ltr,Cooker Hawkins,Heavy Duty Mixer Grinder,Palta with wooden Handle,Bhatti Motor,Rol
Biscuit Bourbon
Cookies Cashew
Cup Noodles
GREASE CIATIM 201 (TOT ITEM)
TVS GIRLING DOT 4
LIPREX EP-2 (SERVOCOAT 140 EX IOCL/ CAMEX COMPOUND F EX BPCL/ HYAK-2 EX HPCL)
GREASE OKS 360
Digital Handheld Transceiver Set  (HANDHELD RADIO),Digital  Base / Mobile Transceiver Set  (MOBILE 
Chain Link Security Fence alongwith Accessories
SOLENOID SWITCH,FIELD COIL ASSY,BEARING BUSH CE,BEARING BUSH INTER BKT,ARMATURE ASSY,ASSY CABLE COM
PLATE
Cornflakes,Cornflour,Custard Powder,Pickle,Tomato Sauce,Biscuits,Sago,Vinegar,Horlicks,Oats,Dog Bis
Colour Smoke Grenade
Tomato Puree
CARBURATOR ASSY,FUEL ON OFF COCK,AIR CLEANER FILTER,FUEL PIPE,ELECTRODES WELDING STEEL,THINNER ANTI
LV7-TMB 1466-111-626 Camplate,LV7-TMB 2520-012487 Plate Clutch Disc Clutch,LV7-TMB 2547-0911-0118 A
Erina EP shampoo,Digyton plus syrup,Thrombeat syrup,Gutwell powder,Hepatoglobine Syrup,Salicylic Ac
LV7-TMB 2573-2520-0108 ASSY 310 DIA CLUTCH DISC,LV7-TMB 2786-1599-0113 ALTERNATOR 24 VOLTS 75 AMPS,
Sedan nac 4hrs40Km local,Sedan nac 10hrs80Km local,Sedan nac 12hrs120Kmlocal,SedanPlain Kmoneway Ou
URF PLAIN
Cement,Quick Setting Compound,Sand,Lime,Stone Aggregate 12 point 5 to 20 mm Graded,Bitumen 80 obliq
Desktop And Application Virtualisation Software,Desktop And Application Virtualisation Software
Bullet Proof Security Tower
GEAR SHIFT LEVER ASSY WITH BUSHES,SPARK PLUG,SA OF DRIVEN DISC,GRADUATED HAND BRAKE VALVE,SELECTOR 
NOZZLE,VANE PUMP,SEALING KIT,HOSE,COGGED V BELT 1325MM LONG,EXHAUST BRAKE ASSY,GRADUATED HAND CONTR
Injection Analgin,InjectionTonophasphan,Injection Phenyl Butazone,Injection Meloxicam,Injection Rev
2Propanol 45gm 1Propanol 30gm 500ml bottle with dispenser,Box Denture and appliance,Teeth posterior
Custom Bid for Services - OUTSOURCING OG CONSERVANCY SERVICE AND HIRING OF 6 TON TIPPER FOR COLLECT
Desktop Computer,Monitor,Mouse,Keyboard,DVD Writer
Entry and Mid Level Desktop Computer,Server,Layer 2 Access Switch (V2),Cat 6 Cable for Indoor Use
Weight Belts with weights ( Diving Instruments or Accessories)
Towel Hand Cotton Turkish (IAF)
Portable Water Purifiers or Filters
Sub base basketball Court 94 x 54 Sq Ft,Synthetic 8 Layer Cushion System ITF Approved,LED Flood Lig
SYSCON IC,BATTERY 3.6 VOLT,MIC,SPEAKER,FPGA1
Oil 2T Supreme
PLUG X 1,PLUG X 2,TRANSISTOR 2N 6284
High Mast Lighting Octagonal Tower with Solar Based LED Street Light
Football,Football Goal Post Net as per IS 3345,Decorative Flag
Treadmill (V2),Multi Adjustable Bench (V2),Medicine Ball,Rubberized Weight Dumbbells,Rubberized Wei
Rubberized Weight Plates,Weightlifting Bar and Collars,Rubberized Weight Plates,Rubberized Weight P
Twister - Outdoor Gym Equipment
Skipping Rope (V2) (Q3)
Bathroom or Toilet Mirror (V2) (Q4)
Custom Bid for Services - Suuply and fixing of name board for main gate of HQ CWE Lucknow
Custom Bid for Services - Consultancy for provn of RCC arch gate at OTC AMC under GE (East) Lucknow
Whistle (V2) (Q3)
Sports Trophies (Handicraft),Sports Trophies (Handicraft),Sports Trophies (Handicraft)
Spark Plug,Gasket Cyl Head,Set and Connecting Rod Brg STD,Damper Cabin MTG,Oil Pump Assy,Brg Rear W
CABIN LIFTING PUMP FOR TATRA 815 8X8,AIR DRYER ASSY FOR TATRA 8 X 8,SPRING BRAKE ACTUATOR ASSY 16X1
ACC Cable,Cyl Head Gasket,Pressure Plate,Clutch Plate,clutch Plate,Pressure Plate,Spark Plug,Igniti
Chain transmission 83 IS 2403,Chain Lock IS 2403,Leaf spring EPD 48991,Spring Arming Lug EPD 8423,S
ARMATURE ASSY 12V FOR TATA 2.5 TON,BUSH SET FOR TATA 2.5 TON,KNUCKLE BEARING FOR STLN,ENG MTG PAD F
N-ACETYL CYSTEINE 200MG/ML, 5ML AMPOULE INJ,INJ POLYMIXIN 5 LAC UNITS/VIALS
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
FLEX BANNER,DISPLAY GLASS,MOBILE BOX,PHOTOS WITH FRAME,CORPS SIGN,FORMATION SIGN,STRATEGIC STRIKER 
Ceremonial Horse Gatez with LED lighting,Horse standing Martingale with LED lighting,Horse Head Bri
Mist Air Fan (Q3)
Cutter Large,Cutter Small,Cutter Large Blade,Cutter Small Blade,Pilot Pen,Steel Scale 24 inch,Sketc
Talk Sheet,White Drawing Roll Large,Ivory Hard Sheet,Fevicol,Fevi Stick,Fevi Quick,Flex Quick,Aradi
Manpower Outsourcing Services - Minimum wage - Highly-Skilled; Graduate; Healthcare
URO BAG
armature assy,field coil,solenoid switch,radiator hose,parking light
KEYBOARD AND MOUSE SET,DVD WRITER,UNIT CARE FUSER,MOTHERBOARD H81,WIRELESS KEYBOARD AND MOUSE,PRINT
OIL OM-65
H2_8305-000050_CLOTH BOUNTING INDIA,H2_83005-000064_COTTON WASTE COLOURED,H2_4720-000407_TUBING RUB
Power E,Cable S,Bag,M Hand,Cover
Writing table size 2400x600x750mm as per Trade Pattern,Chair writing as per trade pattern,Chair Vis
Soap Dish - Case,Soap Dish - Case,Bathroom Water Shower (V2),Bathroom Water Shower (V2),Copper allo
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma with minimum 03 Years trade experie
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma with minimum 03 Years trade experie
Hiring of Water Tanker Service - Drinking Water (ISO 10500 Standards); Treated potable water; Any v
Fuel Filter Assy Pri,Fuel Filter Assy Secondary,Oil Filter,Frequency Meter,Piston Assy,Piston Ring,
MAIN SHAFT,COMBI SWITCH,ASSY WINDOW REGULATOR RH,STARTER SOLENOID SWITCH,VALVE BRAKE PNEUMATIC,ASSY
BRAKE LEVER,SIREN 24V,CABIN FAN 24V,TURBO CHARGER,ROOF LIGHT,WIPER BLADE,SIDE INDICATOR,CABIN LIGHT
Desktop And Application Virtualisation Software
Corps of EME Role Vision Mission HD Vinyl printing board with frame,Eqpt display flex Board 6 ft by
Refrigerators 175 Ltr LG or Whirlpool,Wire 1.5 mm,Patrol operated hedge trimmer golf ultral Green l
ARMATURE ASSY,FIELD COIL,BRUSH CARRIER PLATE,SOLENOID SWITCH,BULB 12V 21 5W,BULB 24V 5W,RELAY 24V,B
FABRICATION OF CHINOOK UNDER SLUNG WITH THREE HARD POINTS AKIN TO ORIGINAL HEPTR WITH ACCESSORIES
Ciprofloxacin 0.3percent ear drops of 3mg oblique ml bott of 5 ml Bott,Netcell Merocel Sinus pack 1
Bendix Drive,Armature Assy 24V,Oil Seal,Armature Assy 12V,Power Strg Filter Kit,Brake Pipe Assy,Hig
Neomycin Sulphate Polymyxin B Sulphate and Hydrocortisone Ear Drop Neosporine dash H,Paediatric tra
Faropenam 200mg Tab,Fluticasone Propionate 50 mcg BP Nasal spray,Gentian Violet Solution 30ml,Gelfo
FRONT BRAKE PAD,BRAKE SHOE ASSY REAR,AC FAN BELT,OIL FILTER,FUEL FILTER,AIR FILTER,FRONT SUSPENSION
UNIVERSAL JOINT,Fuel System Hose Pipe Assy - II,OIL SEAL,PROTECTOR OIL SEAL,SENSOR WATER TEMPERATUR
ANNUAL MAINTENANCE SERVICES FOR WATER PURIFICATION AND CONDITIONING SYSTEM (Version 2) - RO Water P
CAM SHAFT BEARING FOR TRACTOR SONALIKA DI 35,ROLLER BEARING FOR TRACTOR SONALIKA DI 35,BEARING END 
ALTERNATOR ASSY 12V LUKAS TVS FOR TATA SUMO GRANDE,FIELD COIL ASSY 24V TVS LUCAS FOR TATA 2.5 TON,S
FLY WHEEL RING,SELF STARTER ASSY 24V,ALTERNATOR ASSY 24V,BRAKE CYL ASSY LH,BRAKE CYL ASSY RH,SPRING
Repair maint of Motorcycle Hero Honda BA No 13A 068072X of AGE EM North under GE North Delhi Cantt,
DRILL BIT,SOLDERING IRON,DRILL MACHINE,GLOVES,BTY RECHARGEABLE 3200 MAH,EMERGENCY LIGHT,T TYPE ALEN
Cyl head gasket,Speedocable rear,Speedocable front,Reverse light switch,Oil seal front hub,Oil seal
JEERA WHOLE 500 GM,HALDI POWDER 1 KG,RED CHILLI POWDER 1 KG,METHI 100 GM,KASURI METHI 100 GM,MUSTAR
Provision of Qty 02 x Living Shelter (OJL wth Drainage)
Dynamo-meter (K-push, K-pull, K-grip)
SOLENOID SWITCH,CLUTCH SELF ASSY,CIRCUIT BREAKER,CLUTCH MASTER CYLINDER,AIR DRYER ASSY,EQUALIZER AS
Custom Bid for Services - Painting and Preservation of Bailey Suspension Bridge Conversion No 2 at 
Spring Mattress,Sheeting, Tickings and Bedsheets (V2) as per IS 175,Cotton Pillow
Curtains (V2) (Q3)
HIRING OF 03 X E1 (6 MBPS) CIRCUIT BETWEEN BAREILLY AND HEMPUR
Disposable Glass,Battery AA Duracell,Battery AAA Duracell,Stapler small,Stapler Medium,Large Size C
Eclairs
Milk Chocolate
Dates/Nuts/Multigrain Bar
Acamprosate 333 mg Tab,Acarbose 50 mg Tab,Acyclovir ophtha Ointment 3 per w per w in 5gm tube,Alpra
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Copper Sector Connectors
2573-3240-7110,8854-4101-1210,2632-2540-0101,2839-4230-0182,2990-9701-7028,2754-2540-0112
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma with minimum 03 Years trade experie
Monthly Basis Cab & Taxi Hiring Services - Hatchback; 1500 km x 260 hours; Local
Manpower Outsourcing Services - Minimum wage - Skilled; Diploma with Minimum 01 Years Trade Experie
Custom Bid for Services - Soil investigation
Arboriculture for the work provision of 50M Swimming Pool at INS Hamla
Thermal Weapon Sight as per MHA QR (V2)
MotorFor Drone Brushmotor,Propellor for Brush Motor Twine Blade,Modular Frame for Drone Plastic,120
FD SECURITY FENCE (VIEW CUTTERS)
AI BASE ACCIDENT PREVENTION SYSTEM
Glue Stick,Permanent Marker fine tip black,Register 300 pages,Register 400 pages,Highlighter pen al
LAMINATED PASSENGER DOOR GLASS,FRONT WIND SHIELD RH,REAR WIND SHIELD LH,BEEDING,SIDE MIRROR REMOTAB
GEAR SHIFT LEVER ASSY WITH BUSHES,SA OF DRIVEN DISC,BLADE ASSY WIPER,IGNITION COIL,SPARK PLUG,BRAKE
Repair of Day Ni Close Circuit Cameras,Repair of IP Camera,Repair of DVR Channel,Repair of 6 Core A
INDOMETHACIN 75MG CAP,NITROGLYCERIN 6.4MG TAB,SILVER SULFADIAZINE OINT,PAROXETINE 12.5MG TAB,CYPROH
Fuel Free Solid Waste Incinerator,Fuel Free Solid Waste Incinerator
Clutch Disc Assy,Field Coil,Flange,Brake Actuator,Swivel Bush King Pin,Kit Rep Maj,Wheel Cyl Rep Ki
Annual Maintenance Service - Desktops,  Laptops and Peripherals - Desktop PC; hp,Annual Maintenance
Electric 4 Wheeler Loader 2000 kg with separate compartment
Assy Slave Cyl,Assy Master Cylinder,4st Solenoid Switch,Field Coil Assy,Brg Bush,Regulator Alternat
Bus Hiring Service - Short Term - Local; 42/44/47 Seater; Non AC with Automatic Door; 41-60 Kms
Starting Rope,Carburetor Assy,Nozzle,Piston,Piston Ring Set,Fuel Pipe 17X17,Fuel Pipe 17X19,Starter
Regulator 24V,Rectifire plate 24V,Clutch plate,Spark plug,Brake pad MG,Clutch release bearing,Fuel 
Navigation Display Sys Size 7 Inch,Horn for Gypsy,Wheel Disk Cover for Gypsy,Only Photo new Gen of 
POLARIS AGL 44OZ
23267 70C00 BEARING CLUTCH RELEASE,09265M15002 BEARING KNUCKLE,2530 014013 TIE ROD,09289 07005 SEAL
Short Term Cab & Taxi Hiring Services - Sedan; Local; 80Kms x 10Hrs,Short Term Cab & Taxi Hiring Se
Turmeric Powder,Coriander Powder,Cloves,Small Cardamom,Large Cardamom,Black Paper,Chilly Powder,Cum
Refilling of Oxygen Cylinder 7000ltr,Refilling of Oxygen Cylinder 1246 ltr,Refilling of N2O Cylinde
IC SMD 74 HC 14,IC SMD 74 HC 00,Gear Belt,IC SMD 317 LB,Mov AC,Mov DC,Chock 1.2 uf 3 amp,Oil Cap 10
Cheese Spread,Cheese Spread1,Cheese Spread2,Cheese Spread3,Cheese Spread4
Wall mounted fan,Fan mounted wall,Desert Cooler,Aqua Guard,Portable fridge
Ambulance Service (Event Based and Short Term) - Type D Advance Life Support Ambulance; Single Stre
ACEBROPHYLLINE 200 MG SR,ACECLOFENAC 100 PLUS SERRATIO 15MG PLUS PCM325MG TAB,ACOTIAMIDE 100MG TAB,
Fabrication and supplying of structural stores for Veh Shed of size 32200 x 8230 x 4000mm using mil
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Store Shelter
Bio - Medical Waste Collection Bags (Biohazard Bags),Bio - Medical Waste Collection Bags (Biohazard
Laundry Service - Commercial/Residential/Transport/Industrial Purpose
Alternator Bty Charger,Insulation Tape Elect Cotton Self,Insulation Tape Electrical pvc,Elect Rod W
ALTERNATOR 24V,WHEEL CYL REPAIR KIT,ASSY OIL FILTER,FUEL FILTER,OIL FILTER,ALTERNATOR BELT
Dise Brake Pad,Washer,Air Cleaner,Brake Drum Gasket,Element Air Refiner,Gasket,Oil Filter,Indicator
Iron Jali,Kabza,Iron blade with cutter machine 4 inches,Iron Pole 20 feet,Iron ring for nut 16 inch
CLUTCH PLATE,CLUTCH BOOSTER,BENDIX PINION,SOLENOID SWITCH,BRUSH GEAR,BUSH SET,FEED PUMP,DC CONVERTE
fluralaner 1000mg chewable tablet> 20-40 Kg
ELECTRONIC FLASHER UNIT,COMBINATION SWITCH,IGNITION SWITCH,BTY CUT OFF SWITCH,REVERSE LIGHT SWITCH,
Football,Volleyballs as per IS 417:1986,Volleyball Net as per IS 3345,Badminton Racket,Cricket Bat,
Ferric Pyrophosphate 30 mg Cap,Homatropine Hydrochloride Soln 2 percent eye drop,Hydrocortisone 5 m
Antacid Gel each 5ml containing driedAluminium Hydroxide gel IP 250mg Magnesium hydroxide NF 250mg 
Electrode Welding Steel Hard Surfacing,Thread Tape,Adhesive Synthetic Araldite,Copper Washer 22 MM,
N1/1015-000639 VALVE ASSY,N1/4730-000142 LUB NUT, 123
Printer Formatter board Make HP Laser Jet 1108,Printer Formatter board Make HP Laser Jet M 202 DW,C
LUB OIL FILTER ELEMENT,ELEMENT FUEL FILTER,FUEL PIPE,ELEMENT MICO PREFILTER FUEL,SLEEVE RUBBER,GASK
ARMATURE ASSY,FIELD COIL ASSY,BRUSH CARRIER PLATE,SOLENOID SWITCH,CLUTCH PRESSURE PLATE AND PTO,RAD
Cartridge 88A,Cartridge 12A,Cartridge 110A,Ink Powder Black 1 Kg,Ink BTD-60BK,Ink BT 5000C,Ink BT 5
Assy Propeller shaft front,Trailer Control Valve,Armature,Bush gear assy,Actuator spring brake,valv
Turbo Super Charger Engine Non air Craft,Bearing Bush,Bush Bearing,C E Bush,Assy propeller Shaft
seal plain,S A Driven Disc,Cover Assy Clutch,Cross Assy,Door lock assy LH,hand brake cable,bearing 
Tail Light Assy,Knuckle Bush,Knuckle Bearing,Spider Bearing,Wiper Blade Assy,Lens Tail Lamp Light A
Liquid Hand Wash,Hexigel,N 95 Mask,Tips Saliva Ejector,Pharmadent painoff,Sterillium,Fixon,Type II 
Visitor Chair,Windows Blinds PS 2002,Fisher Rc4 The Curv GT Ski boot,Classic Height Adjustable Chai
15 inch macbook air, 13inch macbook air, 15 inch ipad air & iphone16 pro
soda making mahcine
Manpower Outsourcing Services - Fixed Remuneration - Healthcare; Psychologist; Masters in Psycholog
Optimux
Jointing Enclosure
ASSY INJECTOR,DOOR LOCK,HAND BRACK ASSY,BUSH ARM,SUSPENSION BUSH KIT,ARM LH,CABLE,BUMPER ASSY,ENG M
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Defence Area; As p
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
Trousers Sleeping Flannel and Trousers Sleeping Cotton - Military Hospital Clothing,Trousers Sleepi
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
Potato , Onion
FXO/FXS
Rear View Mirror,Battery Acid Rubber Pipe,Pressure Pipe 96 Inch,Air Pressure Pipe 22 Inch,Hose Pipe
Automotive Vehicles - Tubes for Pneumatic Tyres (V2) as per IS 13098,Automotive Vehicles - Tubes fo
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Non-IT Technical,Manpower Outsourcing 
Digital Walkie TalkieSets 1,Digital Walkie TalkieSets 2,Digital Walkie TalkieSets 3,Digital Walkie 
Unitary Air Conditioner (Window AC) (V2) as per IS 1391 (Part 1),Unitary Air Conditioner (Window AC
Epson M 200 Printer Cartridge Eco Tank Black and White,Binder Clip Small and Large,Feviquick 12 Gm,
CV Point,CV Point Boot Kit,Small Clamp,Clamp Large,Grease
LV7 T-815 443-612-305-708,LV7 STLN 2540-72-0000645,LV7 TATA 2702-584-0010,LV7 T-815 443-612-302-001
Nails 2 inch,Nails 3 inch,Nails 6 inch,Sand Paper All types,Female Thread and Cap 1 2inch and 3 4 i
ASSY LATCH FR DVR RH,SHOE COMP BRAKE REAR,BRG CLUTCH RELEASE,ASSY MUDFLAP REAR,BALL BEARING,OIL SEA
Bty Eveready 1 5V,Fuses 3A,Fuses 5A,Fuses 10A,Cell 1 5V AA Rechargeable,Insulation Tape,Syringe 2ML
Solar Security Street Lights with Accessories (150W)
Bacon Td , Ham Td
Bendix Drive Assy,Oil Pressure Guage,Seal and Spg Set,Hose 10 MM,Packing Ring 22x30,Air Pressure Pi
Pineapple Orange Fruit Drink (in canned)
Cough Drops
Coconut Water
Orange Juice
Apple Juice
Medicines of Various Types,Transport Charges for Medical Staff & Doctors,Refreshments for Participa
Bricks,Sand,Agg 20mm,Agg 10mm,Agg 63mm,Coarse Sand,Cement,TMT Bar 10mm,TMT Bar 8 mm,Binding Wire,Wh
Gel Pen (V3),Permanent Marker Pen,Double sided tape,Pencil box,Rollerball Pen (V3),Highlighter Pen,
Canon 925 Cartridge,Epson 664 Ink All Colours,Brother TN- 2365 Cartridge,HP 77A Cartridge,HP W1002Y
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Admin
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Bleze Kamekazi Drone
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Electrician tool kit (Q3)
SOFTY ICE CREAM MAKING MACHINE
Red Chili Powder,Turmeric Powder,Coriander Powder,Garam Masala,Chicken Masala,Biryani Masala,Paneer
10444983,10318975,10305526,10347396,10460246,10454824,10460252,10456121
Modifiaction and Repair work at Liquor section of URC
Changeover switch 63 amp,Extention board 6 amp with two socket and two switch,Extention board 16 Am
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Hand Held Search Light (Q2)
PRIMER ASSY,PRESSURE PLATE,CLUTCH PLATE,HEAD LIGHT ASSY RH,HEAD LIGHT ASSY LH
LIGHT BACK UP,ASSY FOG LAMP FRONT YELLOW LENS LH,LIGHT FOG,LIGHT DOME LAMP CAP INTERIOR UNDER LAMP,
Refrigerator 350 ltr,RO water filter 50 ltr,Ceiling fan ceiling,Fan ceiling fan,Ceiling fan ceiling
ROOF LIGHT BSII,SIDE INDICATOR LAMP BSII,TIE ROD END REP KIT BSII,4X4 REP KIT BSII,GEAR LEVER KIT B
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
ALS GEAR BOX REPAIR,ALS VANE PUMP REPAIR,ALS SELF STARTER REPAIR,ALS ALTERNATOR REPAIR,ALS CABIN PI
ALS SYNCHRONIZER GEAR REPAIR,ALS COMPRESSURE REPAIR,ALS FUEL PIPE REPAIR,ALS AIR PIPE REPAIR,ALS CA
ALS ROTARY PUMP OVERHAUL,ALS INJECTOR CLEANING,ALS VALVE GRINDING,ALS FUEL PIPE REPAIR,ALS AIR PIPE
Limequick
Goods Transport Service – Per Trip based  Service - Machinery & Equipment, Vehicles; Flatbed Truc
Soluble Coffee Powder (Refill Packs) (V2) (Defence)
Custom Bid for Services - Annual Maintenance Contract Desktop Printer AND UPS
Turnstile Flap Type Retractable Dual Lane Access with 02 inbuilt RFID card readers,Turnstile Flap T
BTY 12V 7AH,SMPS,OPC DRUM,PAPER PICKUP ROLLER,TAFLON SLEEVE
Ketamine HCl,Bupivacaine HCl,Bupivacaine HCl,Lignocaine HCl,Etomidate 2,Lignocaine HCl,Ephedrine Hy
DRIVE ASSY STLN,DRIVE ASSY,BUSH SET,FLASHER SOLID STATE,RING OIL SEAL INNER,OIL SEAL RING,OIL FILTE
Standalone computer i7 13th Gen 16GB RAM,Work Station i9 13th Gen 32GB RAM,Video conferecing PTZ ca
Data Wall with Processor and accessories with Installation
TV Tray,Telephone cable,Telecome wire,EPABX 16 Channel,Name Plate,Telephone box
AMPLIFIER,WALL SPEAKER,BOX CABLE,MIC,BOX CABLE 90 MTRS
LCD,Mother Board,Arduino board,Relay Module,PSCB,Lithium Bty 12 Volt,Amplifier board,Connector,Cabl
universal joint,Water pump,Wheel cyl assy,Oil seal,Oil seal,Fuel pump,Oil seal,Oil seal,Universal j
Mechanically Woven, Double - Twisted, Hexagonal Wire Mesh Gabions, Revet Mattresses and Rock Fall N
Custom Bid for Services - SOIL INVESTIGATION FOR RECONSTRUCTION OF DEMOLISHED RCC OHT NO 4 BLDG P-1
Providing and fixing outdoor Asphalt Base for synthetic surface volleyball court,Installation of ei
MEDALS FOR PARTICIPANT,RIBBON,MEDALS STICKERS OBIQUE LOGO,TROPHIES,CERTIFICATES,TARGET PAPER FOR AR
Bathing stool plastic,Plastic mug,Pen stand VIP,Chakla,Belan,Steel Dustbin,Water bottle 20 ltr,Acry
Repair of rotary pump and overhauling,Overhauling of rotary pump,Repair of engine head assy,Repair 
Charging adopter,Charger,Rechargeable cell,Angle,Pipe 1 x 1
Panel Board,Clutch Master Cyl,Sleeve Cyl Assy,Universal Joint,KM Sensor,Cabin lifting T
Sticky Notes (V2),Sticky Notes (V2),File/Folder (V3),Sticky Notes (V2),File/Folder (V3),File/Folder
Hose,Hose Flexible Tee To Frt Rear Axle Brk,Hose ,,Hose,,,Welding Rod
Medium Range Anti Drone Detection and Jamming System (Man Portable)
Bran for Defence (Q3)
Repair and Overhauling Service - 1; 1; Yes; Buyer Premises
UPS 1 KVA Luminious,Processor i5 12 Gen Intel,Mother Board i5 12 Gen Intel,Ram 4 GB DDR4 Asus,Ram 8
ASSY WHEEL CYL,BULB 12V,BULB 12V 21W,AIR COMPRESSOR KIT,AIR COMPRESSOR RING,AIR DRYER ASSY,DAMPING 
Kit Spring Brake Act WABCO,DDU Minor Repair Kit,Speedo Meter Gear,Gear Lever End,Wiper Blade,Rear A
Excavation, removal of soil and laying taking down, joining & testing of water pipe
UPS Battery 12 Volts 42 AH
Acrylic display board size 06 ft x 1.6 ft with plinth and 96 x 2.3 inch letters,Acrylic display boa
M & L and taking down for water pipe connections, excavation, removal of soil & connected works
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8
Custom Bid for Services - Annual Maintenance Contract of Digital Franking Machine
Syringe hypodermic catridge type needle 27 G long disposable pkt of 100,Inj lignocaine 2 percent wi
Pin,Pin blade,Ignetation switch,Amp mtr,Carbon bush,Solonide assy,Field coil,Regulator,Starting rel
Impact Wrench half Inch,FRL Janatics half Inch,Coil Hose 8 mm,Impact Socket half Inch,Adapter Coil 
DDU ASSY,ASSY CROSS KIT,CROSS ASSY KIT,CLUTCH MASTER CYL,CLUTCH SLAVE CYL,HOSE CLIP
PDs
Mattress 4 inch 2 layer Single Bed,Tripal plastic 30 ft and 30 ft,Tripal Canvas 15 ft and 15 ft,Vis
Chilly as per IS 2322,Spices and Condiments - Turmeric Whole and Ground (V2) as per IS 3576,Spices 
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Others,Manpower Outsourcing Se
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Others,Manpower Outsourcing Se
G2 3439-000202,D1 3770-000790,G1 5310-001486,D1 3770-001065,CC2 8530-000003,G2 3439-000002,CN KND N
Start Gas Door,Catch Window Lock Back,Handle Assembly Side window,Shim 0506mm dia 65mm AR,Shim 14 m
Tab Griseofulvin 500 mg,Cap Cyclosporine A micro emulsion 25 mg,Inj Bleomycin Sulphate Chloride 15 
Acrifructol Comples P63 Allantoin Alluminium Starch Octenylsuccinate Ascorbyl Palmitate DisodiumPho
Lignocaine HCl 2percent with Adrenaline 1 in 80000 30 ml Inj,Diclofenac 75 mgperml 1 ml Amp Inj,Atr
Annual Maintenance Service  - Photocopier Machine - Photocopier Machine; Ricoh; Neither OEM nor ASP
Annual Maintenance Service - Desktops,  Laptops and Peripherals - All In One PC; Lenovo,Annual Main
Lotion Tacrolimus 0.1 percentage W per V bott of 20 ml,Lotion Halobetasol Propionate 0.05 percentag
IC EL 817 K 21 of Adaptor Base Station,Cap 10 uf 63 V of Adaptor Base Station,IC UC 2845 N of Adapt
NK001,NK002,NK003,NK004,NK005,NK006,NK007,NK008,NK009
Fd WSS RO PLANT (500 LPH)
Toner Cartridges / Ink Cartridges / Consumables for Printers
Wilfit 1,Wilfit 2,Wilfit 3,Wilfit 4,Wilfit 5,Wilfit 6,Wilfit 7,Wilfit 8,Wilfit 9,Wilfit 10,Wilfit 1
Calcium Hypochlorite Granules (65 - 70 %) (V2)
Isolyte P Multi electrolyte injection in 5percentDextrose containingmEqperLitreSodium 23 Chloride 2
Washing Powder,Bathing Shop,Phenol,Brooms Soft,Air Freshner liquid,Liquid Blue colour for cloths,Na
Anti Drone Gun System
Extreme Cold Weather Clothing System (ECWCS) HIMCLOS
Pump Repair
PT Uniform ( Sports Shorts ) - Defence
HHRS Digital Radio Set,HHRS Digital Radio Base Stn,HHRS Digital Radio Repeater Stn,HHRS Accessories
Field Coil,Solenoid Switch,Pole Screw,Oil Filter,Fuel Filter,Oil Filter,Fuel Filter
Banana,Mango Dahsehari,Mango Safeda Mango Neelum Mango Kesar Mango Langra Mango Fazli,Musk Melon,Pa
Manpower Outsourcing Services - Minimum wage - Semi-skilled; ITI; Non-IT Technical,Manpower Outsour
Toner Cartridges / Ink Cartridges / Consumables for Printers
Toner Cartridges / Ink Cartridges / Consumables for Printers
Toner Cartridges / Ink Cartridges / Consumables for Printers
Multifunction Machine MFM (V2) (Q2)
Multifunction Machine MFM (V2) (Q2)
Almirah Med with Shelves,Bath Mat,Chair Easy,Chair Writing,Charpoy MS Rectangular Pipe with Ply woo
Manpower Outsourcing Services - Fixed Remuneration - watch and ward; Watch and Ward; High School
LV1/ARJ-V54801210002 (Material No 10473648) Assy Track Adjuster RH
Socks, Men's Wool (Defence) (Q3)
Boot High Ankle PU Rubber Sole (Defence)
Custom Bid for Services - Repair of veh BA No NYA Chassis No MA3BNC72SRM945344 Maruti Ertiga
Distributor Head,Camplate,Drive Shaft,Nozzle,Injector Assy
COIL ASSY IGNITION,HOLDER ASSY RECTIFIER,SPARK PLUG CHAMPION RC 8 YC,CABLE ASSY ACCELATOR,LENS TAIL
Fuel Filter,Air Filter,Oil Filter,Hose Rubber,Brake Pipe,Rubber Hose Vacuum
LV7-FC-WT-BEL-3845-104-001-68, Selection Valve Set
Z7/ISRAEL-031185-B-00, K / B
Portable Fire Extinguishers (V3) as per BS EN Standards,Portable Fire Extinguishers (V3) as per BS 
LV7 TMB 2574 1511 0104 BRUSH CARRIER ASSY,LV7 TATA L01402000035 ARMATURE ASSY,LV7 TATA L01402000036
Red Chilli Powder,Coriander Whole,Turmeric Powder,Jeera,Ajwain,Chicken Masala,Garam Masala,Panner M
Chest Guard- Gymnastic (Q3)
Boxing Head Guard,Kick / Punching (Bag) - Gymnastics,Boxing Gloves (V2)
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Light Weight Running Shoes (V2) (MHA),Light Weight Running Shoes (V2) (MHA)
Combination Switch,Unloader Valve,Pump Element,Ignition Switch,Rotary Pump,Vane Pump,PRV Rotary
Binocular Loupe 3.5X with LED Headlight
Goods Transport Service – Per KM Based Service - Vehicles, Machinery & Equipment; Open Body LCV T
Brinjal,Cucumber,Lady Finger,Pumkin,Tinda,Bitter Gd,Cabbage,Tomato Ripe,Chillies Green,Coconut Whol
Outdoor Twin Waste Bin (Q3)
Toilet Soap, Liquid (V2) as per IS 4199
SPARK PLUG,CHAIN SPROCKET KIT,ADJUSTER L CHAIN,BALL BEARING 6001,OIL SEAL,SEAT CUSHION,CABLE ADJUST
Curtains (V2) (Q3)
Paper A4 SIZE,Paper Legal Size,Clip board,File Cover printing,File cover white laminated with crust
CLUTCH SLAVE CYLINDER,ASSY UNIVERSAL JOINT,CLUTCH RELEASE BEARING,ASSY CLUTCH DISAK 330 DIA DOUBLE 
OIL SEAL TO HUBS INNER,GASKET VALVE COVER,Assy Vaccum Hose For EGR,Assy Pipe Coolant Bypass,Assy Va
Indicator Assy,Hose Pipe,Fuel Pipe,Oil Filter,Fuel Filter,Cyl Head Gasket,Jointing Sheet Gasket,Wat
MOUNTING RESILIENT,SOLONOID ESOS,VALVE OUT LET,PARKER DIGITAL DISPLAY,FLOOR MAT,MAIN BUCKET HYD PIP
SHITFTING LEVER GEAR BOX,AIR PRESSURE PIPE,HANDLE DOOR INSIDE LH,GASKET HEAD COVER,ASSY CUTCH PLATE
Pickle Mixed,Pickle Garlic,Gari Gola,Pappad Madrasi of 100 gm,Lizzat Pappad of 100 gm
PISTON,PISTON RING SET,BIG END BRG CELL,HEAD GAKET,FUEL PUMP,VALVE SEAL,021 PUMP ELEMENT
Dal Chini MDH,Samber Masala MDH 100 gms,Black Pepper Catch 100gms,Mirch Powder MDH,Sounf Moti MDH,S
coarse aggregate 1,coarse aggregate 2,coarse aggregate 3,fine sand 4,Polythene sheet 5
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Anterolateral plate for distal tibia SS 13 holes,3.5mm distal humerous locking plate Titanium,Dista
Hiring of Consultants - Milestone/Deliverable Based - Consultants for rehabilitation of storm water
SOLENOID SWITCH,HEAD LAMP ASSY,BRANCH PIPE,AIR PIPELINE,DUST SEAL EQPT 141 AND ABOVE,PIPE OF LEFT H
Provision of Additional Infrastructure for Physiotherapy Cell
BULB 12V,OIL FILTER,AC FILTER,KIT FILTER,MOUNTING TER CASE
NK001,NK002,NK003,NK004,NK005,NK006,NK007,NK008,NK009,NK010
Ball Point Pens (V2) as per IS 3705,Ball Point Pens (V2) as per IS 3705,Ball Point Pens (V2) as per
LIVING SHELTER (12 MEN/FEMS)
COOK HOUSE DINING HALL
FD FLUSH LATRINE
GENR SHED
B VEH SHED
BATHING CUBICLE (2/1)
501595 PULLY JOCKEY,158139 ELEMENT LUB OIL FILTER,43828 CLAMP HOUSE,3873576 ELEMENTSUPER LUB OIL,83
Indoor Badminton Court
HESCO BASTION
BRAKE SHOE LINING ASSY REAR,Pad,CYLINDER HEAD GASKET,CHAIN AND SPROCKET KIT,REAR BRAKE SHOE SET,Bal
Ram Rep Kit,Armature,Clutch Plate,Clutch Cyl Assy,Brake Booster R Kit,Clutch Relese Bearing
WD 40,Field Coil Assy,Solenoid Switch,Rep Kit Clutch Booster,Water Seperator,Clutch Master Cyl,Slee
Camplate,PUSHING ELECTROMAGNET,Pump Housing,PRESSURE CONTROL VALVE,Came Plate,Solenoid valve
Title 1,Title 2,Title 3,Title 4,Title 5,Title 6,Title 7,Title 8,Title 9,Title 10,Title 11,Title 12,
PROVN OF QTY 04 x TOILET BLOCK/BATHROOM BLOCK
Clutch Plate 430 GTZ,Belt V Ribbed,Cyl Head Gasket,Retainer Sleeve Seal,Rear Hub Oil Seal,Fan Belt,
Booster MC Assy,Repair Kit MSP 3 49,emister Fan,De-Aeration tank,Relay Emergency Valve,Brkt Fitted 
Clutch Plate,Sleeve Cylinder Rep Kit,Assy Cable Complete,Clutch withdrawal bearing,Hose Pipe,Flange
PINEAPPLE , PEARS , MANGO , BANANA
Oil filter,Fuel filter 5488,Fuel filter,Self bearing,Sleeve cyl kit
Armature Assy,Solenoid Operated Valve,Field Coil Assy,Solenoid Switch,Rotary Switch,Roller,TD Pisto
Camouflage Net (30 x 30)
Sugar (V2) (Defence) (Q2)
Automatic Barrier Gate with Telescopic Boom Arm
Damper pad rear,Cable parking brake No 1,U Bolt LH,U Bolt RH,Centre bolt,Vane pump,Fog light bulb 1
Repair and Overhauling Service - REPAIR OF INTERNAL PCB, RECOFIGURATION OF  SOFTWARE, AND RESETTING
Dried Cow Peas (Lobia) (V2) (Defence)
Deep freezer (Q2)
UPMA MIX (IN SEALED CUP)
Noodles Veg
PANEER READY MADE
DAL MAKHANI
CONNECTING RODS AND BEARING 05MM,O RING,OIL SEAL,PISTON RING SET,CABLE,CHOCK CABLE,PISTON,VALVE,SPA
ARMATURE ASSY,SOLENOID SWITCH,FIELD COIL ASSY,BRUSH CARRIER PLATE,CHANGE OVER SWITCH,SPRING BRAKE A
Gasket oil seal housing,Lock washer,Bolt cyl head,Bush stebiliser mount Suspension kit,Catch assy d
LV7STLN, P-1303456 9430 034720, NOZZLE,LV7STLN VF, 14683760174 AR, DISTRIBUTOR HEAD,LV7STLN VF, 146
Invertor 1650 VA,Thread Tape,Union 25 mm,Union 20 mm,Union 15 mm,Nipple 25 mm,Nipple 20 mm,CP Conne
Sleeping Bag (HIMCLOS)
HP PC with CPU
Diode Positive,Engine Speed Sensor,Regulator Control,Solenoid Switch,2 Pole Isolator Switch,Field C
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Non-IT Technical,Man
Pocha Cloth,Nariyal Jhadu Hard,Hand wash,Handwash Refill,Remote Cell AA,Remote Cell AAA,Lizol,Harpi
WEAVING MACHINE,HANDLOOM WEAVING MACHINE,SEWING MAHCINE,DOOR CURTAINS,WINDOW CURTAIN,PAVOR BLOCK,PV
SKIMMING OF CRANK SHAFT,GRINDING OF CRANK SHAFT,SKIMMING OF HEAD CYL ASSY,REPAIR OF FUEL INJECTION 
Camera Trap / Trail Camera (V2)
LV2 RCV, 765-93SB-232, Float with Rope,LV1 R90, 172-95-264-1 1, Wrench for TITG Bolts of Flanges Co
Earth work in excavation by mechanical means Hydraulic excavator oblique manual means in foundation
Electric Motor and all other speicification as per RFP,Electric Control panel Board and all other s
Superstructure including Foundation B and R Items Electric fittings lighting conductor fire alarm s
ASSY WIPER BLADE,FAN VISCOUS 10 BLADES,ASSY HEAD LAMP WITH HALOGEN BULB RH,WIPER MOTOR 24V,OIL SEAL
KIT BRAKE LINNING BSII,ASSY HOSE PIPE BSIV,SUB ASSY OF HOSE TO TANK MKIV,ELBOW HOSE MKIV,AIR COMPR 
Superstructure including foundation Electric Fittings Fire Alarm System Furniture and Misc items,An
ASSY HOSE MKIV,PARTS KIT TURBO MKIV,SPARK PLUG 413 BSIII,GEAR BOX TOP KIT BSII,CLUTCH MASTER CYL BS
Repair of Tonbo Sight 1,Repair of Tonbo Sight 2,Repair of Tonbo Sight 3,Repair of Tonbo Sight 4,Rep
Seal Water Pump,Hose Front Flexible,Cushion Front,Bearing Pilot,Spring Pipe Exhaust,Tool Kit Ball J
FIELD COIL,FRONT BEARING,HOSE,OIL SEAL SHAFT STRG GEAR WORM SECTOR,HOSE DELIVERY,GASKET,CLUTCH GUAR
TYRE PNEU F-78-15 4PR NYLON RIB AND LUG
TUBE INNER PNEU TYRE F-78-15
Repai rCamera,Repair of NVR,Repair of DisplaySystem,Repair of POE Switch,Repair of Optical Terminal
Sugar (V2) (Defence) (Q2)
Peas Dried Green (V2) (Defence)
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others,Manpower Outs
Biscuit,Namkeen,Juice,Stationary,Prep of Venue,Gifts Prizes,Painting of School Bldg incl Gate,Purch
Malted Milk Food with Cocoa Powder (V1) (Defence)
HUB OIL SEAL,CLUTCH BOOSTER,CONDENSATE SUMP,CIRCUIT BREAKER,WATER PROOF SELF STARTER
Fevi Stick 15 Gm,Pencil Cell AAA,Pencil Cell AA,Pilot Pen V7 Blue,Pilot Pen V5 Blue,Pilot Pen V5 Re
Telescopic Cyl Seal Set,Speedometer Cable,Door Lock RH,Hose With FTG 10x550,Switch Push
CLUTCH MASTER CYLINDER,CLUTCH PLATE ASSY,ECM,FLY WHEEL RING,CIRCUIT BREAKER,SPEEDOMETER HEAD,SELF P
Laptop with Macintosh OS
Spices and Condiments - Cloves, Whole and Ground as per IS 4404,Spices And Condiments - Coriander, 
Oxygen Cylinder,Pulse Oximeter,BP Machine Digital,Infrared Thermometer Digital,First Aid Kit,Tab Am
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Healthcare
Phenyl,Hand wash detol,Collin,Pochha,Harpic,Dusting cloth,Window curtain,Door curtain,Water bottle,
FEVICOL,CONNECTING ROD,BIG END BRG CELL,PISTON ASSY,GASKET,PISTON RING SET,FUEL PUMP ASSY,TUBE ANAB
Emergency Light,Pedestal Fan,Wall Fan,Vertical Cabinet,Inverter,Battery,Inverter Rack,Visitor Table
High Mast Lighting Tower for large area with LED Flood Lighting System
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others
GREASE LG 320
Plaster of paris pkt of 01 kg,Die stone pkt of 01 kg,Plaster dental stone pkt of 01 kg,Articulating
AIR FILTER,DRIVE PINION CLUTCH SET,CLUTCH SET,SONENOID SWITCH,PLATE SELF,RESISTANCE,BEARING NEEDLE,
Oil Servo SAE J1703 DOT-5 Defence
Automotive Vehicles - Pneumatic Tyres for Commercial Vehicles - Diagonal and Radial Ply as per IS 1
CYL CLUTCH RELEASE,CYL CLUTCH MASTER,BUSH,RADIATOR,BEARING ASSY FRONT,OIL SEAL FRONT HUB,LATCH ASSY
ELECTRODES WELDING STEEL ARMOUR 3.15 MM,ELECTRODES WELDING STEEL MILD GENERAL P,ABRASIVES CLOTH EME
PLATE WORK
SWITCH PUSH,BULB 12V 21 5W,LIGHT ASSY INDICATOR FRT DIRECTION,MAJOR REPAIR KIT FOR M CYL,IGNITION R
M2/5935-004519 PLUG AND SOCKET ASSY TAIL LIGHT ASSY,M2/5930-003660 SWITCH ROTARY 8 POLE 2WA
Wiper blade for ALS,Wiper blade for 2.5 Ton,Liquid gasket 2.5 Ton,Brake chamber rear for 2.5 Ton,Br
Moly Coat BR2 Plus
Oil Cutting ZX-1
Red Chili Powder,Turmeric Powder,Coriander Powder,Subjee Masala,Meat Masala,Garam Masala,Chicken Ma
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others
Coriander Powder,Turmeric Powder,Red Chilly Powder,Garam Masala,Chat Masala,Chicken Masala,Sambhar 
Bandage full arm lymphoedema sleeve large,Bandage full arm lymphoedema sleeve small,Bandage full ar
Gr MIL - PRF81322,Oil Hydraulic PX-26 Severe Duty Low Temp
Repair and Overhauling Service - cars; MARUTI SUZUKI INDIA LIMITED; Yes; Service Provider Premises
Wheat Atta Whole Meal,Flour (Maida),Suji,Dalia
Chequered Plywood for Bus Body Building Parts as per IS 3513 (Latest)
Cotton Newar (V2) conforming to IS 1895
Haldi Powder,Red Chilli Powder,Dhania Powder,Jeera,Sabji Masala 100 gm pkt,Meat Masala 100 gm pkt,B
Goods Transport Service – Per KM Based Service - Household/Office; Open Body LCV Truck; 19 FT LCV
BOQ ITEM NO 1,BOQ ITEM NO 2,BOQ ITEM NO 3,BOQ ITEM NO 4,BOQ ITEM NO 5,BOQ ITEM NO 6,BOQ ITEM NO 7,B
LV1-ARJ-5301-024182 HSU Mounting Bolt Mtrl No 10476050,LV1-ARJ-V54801193013 Plug Mtrl No 10475127,L
FILTER FUEL ASSY,PLUG SPARK,DRIVE HARDENED STEEL PINION,WINDING STARTER FIELD COIL,BEARING BUSH,POL
LV1-ARJ-V54801349046 Inner Cap Mtrl No 10612321,LV1-ARJ-V54801063003 Ring Mtrl No 10472463,LV1-ARJ-
Split AC 1 Point 5 Ton,TV 43 Inch,Food Warming Mat,Carpet 5 x 2,White Napkin Cloth
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Baclofen XR 20 mg Tab,Betadine Gargline,Insulin Human Analogue Glargine Inj cart,Insulin Lispro 3ml
Acebrophylline 100 mg Cap,Aceclofenac 200 mg Tab,Ambrisentan 5mg Tab,Amino Acid Tab,Amiodrone HCl 1
Budesonide plus Formeterol Rotacap 200,Budesonide plus Formeterol Rotacap 400,Formeterol plus Momen
LV7 MG 15710M83F00 INJECTOR ASSY FUEL,LV7 MG 15100M830A1 PUMP ASSY FUEL,LV7 STLN P 1310439 COVER AS
read only compact disc cd,read write compact disc cd,read write digital versatile disc  dvd,Compact
Cashew Kernel Whole Raw (Grade-240)
Haldi,Red Chilli,Zeera,Dhania,Imli,Garlic,Mustard Seed,Black Paper,Laung,Cardamom Large
AMC of Integrated Security and Surveillance System - Theft Prevention, Remote Video Monitoring, Out
Hiring of Professionals for Application Development and Maintenance - Data Science and Analytics Ro
Cement,Sand,Aggregate graded 20mm,Aggregate graded 40mm,Aggregate graded 50 to 63 mm,Binding wire,N
Foldable Aluminium Field Cot 6Ft x 2.25Ft x 1.5Ft
All in one PC i7 Window 11 Pro,All in one PC i5 Window 11 Pro,UPS 1000VA Offline,Laser Computer Pri
Foldable Aluminium Field Cot 6Ft x 2.25Ft x 1.5Ft
ASSY RADIATOR,ARMATURE ASSY,FIELD COIL ASSY,PRESSURE CONTROL,VANE PUMP
ALTERNATOR ASSY,HOSE ASSY,AXLE BOOT HOSE,WATER SEPARATOR,FIUEL FILTER
Power Steering oil Dextron II D,Oil 2 T Synthetic Bombarder Inj VES 2 Cycle Oil,SAE 0W20,Oil 15W50,
A 4 PAPER,DVD RW,OMEGA CLIP BOARD,REPAIR RO FILTER PUMP,LEDGER SHEET,SPRING FILE,LEAF,PLASTIC TUB,P
NK001,NK002,NK003,NK004,NK005,NK006,NK007,NK008,NK009,NK010,NK011,NK012
CENTRE PIN,ASSY RELEASE BRG,352 DIA CLUTCH DISC ASSY,CROSS ASSY,COMBINITION SWITCH,ISOLATER SWITCH,
4 Core Copper Cable,1.5 MM 3 Core Copper Cable,1 mm 3 core copper cable,Air Compressure Pipe,Paint 
COBL BURNER CASING MK 2 PLATED FRONT,LENS PAPER BOOK 100 SHT,COBL PUMP WASHER CUP,CONTAINER STOVE C
Assy Auxiliary Water Tank,Universal Joint,Clutch Master Cyl Kit,Sleeve Cyl Kit,Propeller Shaft Nut 
Desktop PC (AIO) i5
BOOKS,COMPUTER,THIN CLIENT WITH MONITOR,CAT 6 CABLE,UPS 1 KVA,8 PORT SWITCH,BOOKSHELVES 4 RACKS,LIB
Bench Workshop Wooden,Rack Magazine,Sofa Single Seater,Table Writing,Almirah Large Steel with Shelv
Light Weight Running Shoes (V2) (MHA)
Foam Mattress (V3) (Q3)
Blanket Barrack and Hospital Blanket (Defence)
ICU Bed (V2) (Q2)
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Annual Maintenance Service  - Photocopier Machine - Photocopier Machines ( Monochrome , Laser , Sep
Refined Mustard Oil (V2) (Defence)
Oil OM-100
BTY 12V 26AH,BRILL PIPE WITH ADOPTER,POWER SUPPLY,POWER CABLE,SUCTION JAR
Injector assy,O ring,Pressure control valve,Light assy indicator,Assy oil Filter,Assy latch front d
BRG CLUTCH RELEASE,RADIATOR ENGINE COOLANT,TAIL LIGHT ASSY,WIPER BLADE CO DRIVER,CHANGE OVER SWITCH
700 40 260 19 GASKET,765 06 261 GASKET,765 06 828 GASKET,765 12 SB224 SHOCK ABSORBER,765 05 724 HOS
Cash Book Public Fund as per sample,Stock indent Register for T and P Comprises of pages 200 as per
Bandage Elastic Adhesive 6 cm X 3 Meters unstretched and 6 meter when stretched,Bandage Triangular,
Levonogestrol 0.10mg plus Ethinylestradiol 0.02mg Tab pack of 21 Low dose OC Pill,Calcium acetate 5
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Supply and fixing of carbon filter,Supply and fixing of sediment filter,Supply and fixing of membra
Modifide Anti Drone Wepon System
Transistor Fet N Chan Type UF 28100V,Transistor Mosfet N Chan Type MRF 166C,Transistor Mosfet N Cha
Retrofit Electric Loader
Calculator,U Clip,Apsara Pencil,Glue Stick,Stapler Big,Kilometer Card,Pental Energy Gel Green,Binde
DISC CLUTCH,COVER ASSY CLUTCH,STEERING PIPE,BONNET MIRROR,MUD FLAP,MUD GUARD,COIL ASSY IGNITION,RAD
Annual Maintenance service-AIR CONDITIONER
AC FILTER,FUEL FILTER,HT LEAD,IGNITION COIL,AIR FILTER,AC FILTER,SPARK PLUG,SPARK PLUG,CLUTCH DISC,
B1 BB-1238 SCABBARD SWORD CAVALRY NO 1MK 1,NSP IBA-0169-NSP SWORD CAV NO 1IP
Manpower Outsourcing Services - Minimum wage - Skilled; Graduate; Admin,Manpower Outsourcing Servic
LEATHER CLOTH BLACK,THREAD COTTON,SHEET CELLULAR,FEVICOL SR998,QUICK FIX,DIODE PLATE
Mupirocin 2 percnt tube of 5gm,Amoxycillin 200mg per 5ml plus clavulanic acid 28 point 5 mg per 5ml
KEY BOARD WITH MOUSE,RAM DDR IV 8 GB,LOGIC CARD,UPS BTY 12V 7 AH,FUSER ASSY,CPU FAN
Repair of RS Motorola Set
Brake Shoe Assy Rear,Brake Shoe Assy Frt,Eng Mtg Pad,Outer Comp Clutch,Fog Light lamp 24 V,Clutch C
Optical Fibre Splicing Machine (V2) as per TEC 88090:2012
Entry and Mid Level Desktop Computer,Line Interactive UPS with AVR (V2)
hydraulic ram,cable assy,Door lock LH,Wheel cyl,Spark plug
Spring Assy Front,Hydraulic Pipe,Brush carrier Plate,Regulator Engine Generator,Disc Clutch,Clutch 
PISTON ASSY,SET and CONNECTING ROD BRG STD,OIL RING,COMPRESSION RING,COMPRESSION RING,VALVE INLET,V
FRONT DOOR PRIMARY SEAL RH,FRONT DOOR PRIMARY SEAL LH,REAR DOOR PRIMARY MOU LH,REAR DOOR PRIMARY MO
CLUTCH PLATE,PRESSURE PLATE,FUEL PIPE,SPRING BRAKE ACTUATOR,FUEL FEED PUMP
INJECTOR ASSY FOR 3.5 KVA GENR,FUEL PUMP ASSY FOR GENR SET 3.5 KVA,AIR FILTER FOR GENR SET 3.5 KVA,
Repair of float cum booster charger Ser No 1015096,Repair of 12 line coral exchange Ser No 09030604
Remotely Piloted Aircraft,Remotely Piloted Aircraft with ECM,4K Ultra High Definition Camera for Re
Electronic AVR,Pannel Control Set DC,Hose,Assy Cyl Head,Fuel Cut Off Soelnoid
Fuel Pump Assy,Slave Cyl Clutch,Roller,Speedometer,Bearing Front Wheel,Gasket Cylinder Head
AVR,Spark plug small,Spark plug Large,Spark plug Medium,Carbon Bush,Fuel pipe,Fuel pipe pump fuel,F
Sprocket,Cussion Pad Rubber,Ignition Coil Assy,Oil Filter,Fuel Filter
Kit Sesal,Door Lock Assy TMX20,Exhaust Pipe,Stop Cable,Hydraulic Hose Pipe
Stud Glass Window,Fuel Pipe,Starter Motor Assy 24V,Starter Ring,Oil Seal Rotary Pump
Drum Unit,SMPS,OPC Drum,Cleaning Blade,PCR,UPS 1KVA,Bty 12V 7AH,Bty 12V 5AH,Mother Board H370
Unmanned Aerial Vehicle & Payload Systems for Surveillance
Combination Switch,Chain and Sprocket Set,Cable Assy Speedometer,Clutch Bearing,Belt Vee,Fan Belt,H
FUEL PUMP ASSY FOR GEN SET 15 7.5KVA,COVER GASKET,BENJO BOLT,ROCKER FOR GEN SET,FUEL FEED PUMP ASSY
OIL FILTER,VANE PUMP,FRONT SHOCK ABSORBER,REAR SHOCK ABSORBER,GEAR LEVER KIT,POWER WINDOW SWITCH,AI
Gasket cyl head,Air dryer,Assy fuel line,Hose,Rep kit spring actuator
Piston Assy,Piston Ring Set,Cyl Head Gasket,Big End Cell,Fuel Pump Assy,Connecting Rod,Injector Noz
Siren,Rear hub oil inner seal,Safety valve,Asm motor,Cyl head gasket
Office Suite Software (V2) (Q2)
Lab reagent
Electric Welding Rod Steel Mild gen purpose,Alcohol Isopropyl,Carbon Tetra Chloride,Electric Weldin
Turmeric,Chilly,Coriander,Cumin Seeds,Black Pepper,Large Cardamom,Cloves,Mustard Seeds,Tamarind,Gar
Protective Px-11
V Belt,Condenser Fan,Air Filter,Spark Plug,Break Pad,Front Headlight
Sugar (V2) (Defence) (Q2)
Armature Assembly,Field Coil 12V,Self Bush,Brake Valve,Clutch Assembly,Isolator Switch 24V,Pressure
Inj Insulin Analogue long acting basal plus long acting GLP 1 analogue in PFS or PFP,Diethyl Ether 
INJ HUMAN INSULIN GLARGINE 300IU PER ML 3ML CART,INJ HUMAN MIXTARD 30 70,INJ INSULIN ISOPHANE OR NP
Goods Transport Service – Per KM Based Service - Household/Office; Pickup Truck; Light Duty
Quick Dispensing Unit (Engine Operated, 3 HP Pump, Speed 360 rpm)
Provn of structure for CTB 8 by 1,Provn of Single items for CTB 8 by 1,Provn of Constr mtrl for CTB
Oil Filter,Disc Pad,AC Belt,Air Filter,Water Pump,Clutch Master Cyl,Fuel Pump,Fuel Filter,Wheel Cyl
thermal gloves (Q3)
Medals-Handicraft (Q3)
External branding signage boards
Rescue Kit / Disaster Management Kit or Accessories
Medicine Kit Bag (Q3)
Medicine Kit Bag (Q3)
HOSE OUTLET,HOSE WATER OUTLET,CLUTCH PLATE,HEAD GASKET,BEARING FRT WHEEL
Fd WSS RO PLANT (2000 LPH)
Paper-based Printing Services - car diary; car diary; As per sample,Paper-based Printing Services -
LV3/ARJ- 0030943004 (Material No 10479948) Filter Cartridge
Z1 DCH, MISC-DCH-27403320250500925, CU 4 PIN MALE CONNECTOR,Z1 DCH, MISC-DCH-2740332020500925.1, CU
Electronic AVR,Carburator Assy,Cock Drain Fuel Tk,Rectifier Assy,Governor
Clutch Plate,Nozzle,Cover Assy Clutch,Assy Clutch Disc Pressure Plate,Assy Clutch Master Cylinder
Esspron E60 non Contact Breath Analyzer with Lcd display type C charging 10 second Rapid result,Ser
Hammer,Ladder,Caliper,Grip Screw,Black tool,Welding,Safety Belt,Safety Helmet,Helmet,Glass Cutter,W
Mix Pickle,Green Chilli Pickle,Mango Pickle,Papad 250gm,Copra Dry Coconut
Replacement parts of printer head Make HP-419 printer
Brick,Cement,Sand,Aggregate 10 20mm,Interlocking tile 80mm,Aggregate 63mm,MS sq pipe 2x2x3mm,MS sq 
Oil Protomac H68 Defence
Wash opaque powder bott of 50 gm,Opaque liquid bott of 250 ml,Opaque classical shade A2 bott of 50 
Wash opaque powder bott of 50 gm,Opaque liquid bott of 250 ml,Opaque classical shade A1 bott of 50 
STEEL FOUNDATION
Pethedine 50 mg 1 ml Inj,Paraffin Liq in bottle of 100 ml,Succinylcholine Chloride 50 mg per ml 2 m
Sugar (V2) (Defence) (Q2)
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin,Manpower Outsourcin
Video Conferencing MCU (Q2)
RAM 4GB DDR-IV,RAM 4GB DDR-III,MOTHER BOARD H-110,DVD WRITER CPU,UPS BTY 12V 7AH,FUSER ASSY,SSD 1 T
DMD CARD,RAM DDR 8GB,PROCESSOR I5,MOTHER BOARD H-110,UPS 1 KVA,UPS BTY 12V 7AH
FRP Bench (Q3)
Rack Steel Adjustable (JSS Specification)
Portable Water Purifiers or Filters
55A ALTERNATOR POLY V ALT,VALVE RELAY AIR FOOT VALVE ASSY,QUICK RELEASE VALVE,FLASHER SOLID STATE,R
ASSY SUNVIOSOR LH,REGULATOR,ARMETURE CLUTCH RELEASE BEARING WITH SLEAVE,ASSY CLUTCH RELEASE BEARING
Custom Bid for Services - ----
Air Freshener Liquid (V2),Household Insecticides (V2),Air Freshener Solid and Gel,Sweeping Broom (V
Kent RO,Matting of classrooms,Tables for staffroom,Biometric Machine,CCTV Camera 4 MP Camera,NVR 16
Ecosprin Tab,Clopidogrel Tab,Atorvastatin Tab,Sublingual Nitrate Tab,Calcium Tab,Vit DTab,Onega Tab
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Jerry Can Plastic 35 Ltrs,Steel Box,Luminous Jacket,Traffic light,Battery Nippo 1.5V D Size
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others,Manpower Outsourci
Inj Rocuronium 10 mg ml 10 ml Vial,Inj Ketamine HCl 50 mg ml vial of 2ml,Inj Thiopentone ampoule of
AMC of Integrated Security and Surveillance System - Theft Prevention, Remote Video Monitoring, Emp
LIFT ARD - Automatic Rescue Device
Courier Service in KG - National; North Zone,Courier Service in KG - National; North Zone,Courier S
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others
Goods Transport Service – Per Trip based  Service - Open Water; Water Tank Truck; Medium Tanker
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin,Manpower Outsourcin
Hiring of Consultants - Milestone/Deliverable Based - Consultancy Service for Analysis, Design and 
TABLE GEERN COLTH,PHOTOPAPER,DUSTER COLTH,DAK FOLDER,WHITE FILE COVER,GLUE STICK,ADOPTER PC,LOCK KE
Solenoid Switch,Starting Relay,Flasher Unit,Rectifire Plate,Pinion,Battery Cut Off Switch,SR-40,Ele
Manpower Outsourcing Services - Minimum wage - Semi-skilled; ITI; Others,Manpower Outsourcing Servi
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others,Manpower Outsourci
AUTO LOADER STRETCHER FOR VEHICLE
ETT flexometallic with cuff size 6.0,ETT flexometallic with cuff size 6.5,ETT flexometallic with cu
ETT flexometallic with cuff size 3.0,ETT flexometallic with cuff size 3.5,ETT flexometallic with cu
Annual Maintenance service - EPABX System
Annual Maintenance service - EPABX System
Cleaning, Sanitation and Disinfection Service - Outcome Based - Entire Mil Area of Mumbai Mil Stati
High End Desktop Computer,Online UPS,Server,Line Interactive UPS with AVR,Layer 2 Access Switch,Dot
Portable Water Purifiers or Filters
Hydrolic pressure testing cleaning and marking of O2 cylinder 200 ltr,Hydrolic pressure testing cle
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others,Manpower Outs
Manpower Outsourcing Services - Minimum wage - Skilled; Graduate; Admin,Manpower Outsourcing Servic
HALDI PDR,MIRCHI PDR,DHANIYA PDR,LONG SABUT,KALI MIIRCH SABUT,MOTI ELACHI,CHOTI ELACHI 8MM,JEERA SA
STARTING PULLY,SPARK PLUG,PIPE FLEXIBLE FUEL TANK TO LIFT PUMP,COCK FUEL TANK 61MM LONG X 16MM,PIPE
ALRENATOR 60A,WATER PROOF FOG HEAD LAMP,IGNITION SWITCH,SWITCH TOGAL,SWITCH PUSH,PART KIT BRAKE VAL
Repair/maint of Central AC System (Chiller/VRF/Ductable/Package)
Clutch disc assembly 352 dia,Alternator 24V,Armature assembly,Starter motor 24V,Sub assembly of dri
Dicyclomine HCl 20mg Inj,Mebeverine HCl 135mg Tab,Pantoprazole 40mg plus Itopride 150mg Tab,Bisacod
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
SPEED SENSOR,DISCHARGE HOSE PIPE,PART KIT HYDRAULIC RAM,SUSPENSION BUSH KIT,AIR FILTER ELEMENT,CARB
Coarinder,Red Chillie powder,Penu Greek 60 gm,Garlic,Mustered seeds,Cadoon Large 75 gm,Cloves,Turme
VANE PUMP,PACKING KIT,NOZZLE,SEALING PLATE,DISTRIBUTOR HEAD
Inj Pheniramine Maleate,Inj Frusemide,Inj Diazepam,Inj Metoclopramide,Lignocaine Jelly,Tab Glucosam
HH CRANK SHAFT REPAIR,HH PISTON BORE REPAIR,HH ENGINE OVERHAUL,HH REAR AND FRONT SHOCKER REPAIR,HH 
X3 SPARKING PLUG,X3 CARBURATOR ASSY,X3 FUEL PIPE,X3 LAMP FITMENT,X3 ELEMENT FUL FILTER,Z1 BACK UP B
Hiring of Earth Moving Equipments, Material Handling Equipments and Cranes (per Hour basis) - As Pe
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
M S STEEL SHEET,STEEL ANGLES 25 X 25 X 3 MM,STEEL BAR ALLOY HOD ROLLED FLAT 30 X 6 MM,MS STEEL SHEE
Serviceing of Mahindra Scorpio incl repair replace of wind shield washer fluid,Element Air Cleaner,
Crimping Tool,SFP Module single Fiber 40 Km,HDMI Splitter 01x in 04 x out,D2 pin plug Mail 2 Pin To
Tomato Puree
LV1 WZT-3, TD50-00-040, Rope TD50-00-040,LV2 ICVS, 4930-002582, Lubricating Gun,LV2 ICVS, KB-05-SB3
ELECT RODES WELDING STEEL MILD GENERAL,REGULATOR VOLTAGE ELECTRONIC,LEATHER CLOTH BLACK,SHEET CELLU
Connector Replacement,Lens Cap Replacement,Shutter Eye Guard Replacement,Dust Cap Replacement,Thumb
Heating Element,Welding Wire,Screw Driver Set,File Set 6 Pc,Circlip Plier Internal,Cutting Plier,Ci
ONE WAY PER KM PLAIN,BOTH WAY PER KM PLAIN,NIGHT HALT,10 HRS OR 80 KMS PLAIN,24 HRS OR 120 KMS PLAI
K6 7330-000080,K6 7350-000342,G2 3439-000016,K3 7210-000018,K1 7320-000023,G1 5315-000817,G1 5315-0
S A WATER PUMP,NEEDLE BRG,PARTS KIT BRG REPLACEMENT MECH EQPT,24 V SOLENOID FOR STARTER,HOSE
TIMING BELT,VACCUM PIPE BOOSTER NRV TO T CONNECTOR,BRAKE LINING KIT STD,ASSY TIE ROD,REAR HUB BEARI
CHANGE OVER SWITCH,FOG LIGHT 12V,LAMPCONVOY NO2 MK5 TO DRG,LAMP FILAMENT 12V 3PT6W BA9S MCCCLEAR,BA
ASSY CLUTCH MASTER CYLINDER,BEARING FRT WHEEL,SHOE BRAKE,MOUNTING ENGINE FRONT,CABLE ASSY CLUTCH,CO
Bat,Thigh Pad,Elbow Pad,Leather Ball Red,Leather Ball Pink,Gloves Batting,Gloves Keeping,Gold Medal
Mother Board Gyga Byte H610,Intel i5 14th Gen Processor,Crucial 16GB RAM,Crucial 500GB SATA SSD,Cru
POLARIS DOT-4 BRAKE FLUID
Kit Estimation of CKMB Erba,Electrolyte Na pluse K pluse CL Spotchem Test kit of 50 test,Troponin T
Tab Aceclofenac 100 plus Paracetamol 325 plus Chloroxazone 250 Tab Hifenac Mr,Tab Acarbose 50 Mg,Ta
Fd Protn Wk Med Gun (S&C)
Semi Integrated Two In One Solar Street Light,Thirty Watt Solar Street Light,Twelve point Eight V T
Samsung LED TV 75 Inch,Fevicol MR 1 ltr,Cap And Can Stand,Used Plate Stand,Veg Non Veg Board
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
HP Dell Desktop PC Keyboard Mouse 13th 14th Gen,HP Dell Desktop PC Keyboard Mouse 14th Gen,Microtek
D IFA RE 26 BT Kit consisting of Blood plasma transfusion set Intra venous cannula 18G cannula fixi
ANPR,RFID,Biometric and Face Recognition,Desktop,UVSS,Desktop
STEEL ROOFING TROUGH 1800MM LONG 2MM THICK AND 27 KG WEIGHT EACH,STEEL ROOFING TROUGH 2400MM LONG 2
Cages size 10 ft x 10 ft made of Wire of Mesh mounted on top of Guns
Haldi Powder,Dhaniya Powder,Mirchi Powder,Garam Masala,Meat Masala,Sabji Masala,Sambar Masala,Choti
CCTV,8 port switch,Network Video Recorder,Hard Disk,Cat 6 UTP Cable,Media Converter,RJ 45 Connector
Assy 310 DIA Clutch Plate,Drive Assy,SPG Brake Chamber Repair Kit,Repair Kit MSP 3 65,Repair Kit 34
shocker assy,suspension bush kit,nut and bolt,bolt hex,self starter assy long
Iron Backlit Board promotional Flex Arch Gate Size 25 Ft x 20 Ft
Calculator,Register No 2,Scale Steel,Feviquick 400mg,Pad Drafting Large,Pad Drafting Small,Stamp Pa
Welding Rod,Aluminum Sheet,Badminton Net,Elastic Rope,Cup Brg with wheel,Wheel,Fiber Sheet 4x4 ft,S
LV7 T 815 433 113 016 000 ALTERNATOR 28OBLIQUE55A 9515 631,LV7 TMB 2751 1540 3402 BEARING BUSH CE,L
Store demanded Joinery,Store demand of electrical,Misc Store Demand Paint,Misc Store Demand Sanitar
OIL FILTER,FUEL PIPE,BUSH FRONT,BUSH REAR,CLAMP FRONT,CLAMP REAR,LINK ROD,LINK ROD FRONT,LINK ROD R
STARTOR MOTOR ASSY,GUIDED VAVLE,WATER PUMP,STUB BOLT,BEARING,HEAD LIGHT RELAY
Refined Sugar conforming to IS 1151
Tea CTC (V2) (Defence) (Q2)
Wheel Bearing inner hub,Caliper Assy,Crank Positioner sensor,Brake Pad,Wind Shield Glass,Hand Brake
BRAKE LINER,GLOW PLUG,BEARING BUSHING,BRUSH HOLDER,DRIVE COMPLETE,FUEL FILTER POWER UNIT,AIR FILTER
SELF ARMATURE,RUBBER DAMPER,SOLENOID SWITCH APU 24V,SINGLE ACTION SOLENOID VALVE,DAMPER POWER PLANT
GLOW TIME RELAY,PISTON ROD SEALING 40 50 X10 5,TOGGLE SWITCH 2 POLE ENVIRONMENTALLY SEAL,TOGGLE SWI
MAGNETIC PICUP,SWITCH OPEN TOGGLE SEALED,NARROW V BELT V BELT 10 X1000,RUBBER DAMPER,SEALING SET AM
Wiper Blade,Assy Oil Filter,Air Filter Element,Bulb Head Lamp,ABS and Hydraulic Motor Assy
KND/NIV/CL1/238 PT UNIFORM S/LARGE
KND/NIV/CL1/238 PT UNIFORM S/LARGE
MICRONEEDLING RF
Inj Ketamine HCl 50 mg obqml 2 ml,Bupivaccaine HCl 5mg obqml 20 ml Inj,Inj Etomidate 2mg obqml 10ml
HIGH END SILENT SUCTION APPARATUS
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Non-IT Technical,Manpower
Shirting Cloth (Q3)
REPAIR OF DESKTOP DELL MOTHER BOARD CARRIED OUT
Loom Wire,Fuel Pump Assy,Nozzle Injector,Nozzle Injector,Fuel Pipe,Wheel,Thinner,Cable Elect 10mm,T
Badminton Racket,Badminton Shuttle Cock (V2) as per IS 415,Volleyballs as per IS 417:1986,Volleybal
Cricket Stumps and Bails,Carrom Board,Basketball Net as per IS 3345,Basketballs,Chess Board,Footbal
Canon Cartridges
OEM Printer Cartridges
Tools and Plant
M and L for seat cover made from high quality foam and PU leather, bucket type fitting complete set
TAPE INSULATION ELECTRICAL,ALCOHAL ISOPROPYL TECHNICAL,CUTTING DISC,COMPRESSED GAS OXYGEN INDUSTRIA
Cellophane paper (Q4)
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Commercial; Vehicl
Hiring of Earth Moving Equipments, Material Handling Equipments and Cranes (per Hour basis) - As Pe
Pressure Pipe,Hose Pipe,Axle Shaft,Hydraulic Pipe,Hub Seal,Bearing Rear Axle,Spider Bearing,Hose Pi
Repair Of Turbo Charger
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Secu
Tent Extendable Frame Supported With Mild Steel Joints and Flooring TPO
Light Weight Running Shoes (V2) (MHA)
IT, NK000926, WASTAGE INK PAD 3110,IT, NK000933, FUSER UNIT 436 NDA,IT, NK000934, UPS CYBER POWER B
Custom Bid for Services - Replacement  parts of ADF unit Make Kyocera 3011i photocopier
Annual Maintenance Service - Desktops,  Laptops and Peripherals - Desktop PC; Acer
URF 75: 25
Z1/5965-003923, Head Set Micro Phone ANR DCH
COVER ASSY,CLIP FR AXLE,WIPER BLADE FRONT 600 DRIVER MS BCS,ASSY OIL FILTER,RUBBER SEAL SEAL HOLDER
Armature 19024318,Pinion 19024305,Rectifying Block,Solenoid Switch,Spring Brake,Relay 12
Fuse link blade c 25A,Fuse link blade c 40A,Oil seal,Gasket oil pump,Body control unit
Driver Disc Clutch plate,Poly V Belt,Slave Cyl Rep Kit Minor,Kit Master Cyl Minor,Clutch master Cyl
WATER BODY,NOZZLE,OVER FLOW PIPE,3 WAY PIPE,FUEL PIPE,OIL FILTER,FUEL FILTER ASSY,BTY LEAD ACID WIT
LV7 TMB 2752 2540 0105 COVER ASSY 1 75 INCH SPINE DIA,LV7 TMB 2654 2910 0194 ASSY CLUTCH MASTER CYL
Steering filter 2.5 Ton,Head lamp bulb 24 V 2.5 Ton,Fuel stainer 2.5 Ton,Knuckle bush 2.5 Ton,Oil s
SEAL SET HOR CYLINDER 2767-009-301-73,FUEL HOSE,FUEL HOSE,GASKET,OIL FILTER,FUEL FILTER 19KVA 100 0
Cover Assy 1.75 Inch Dia,Assy Release Brg 1.75 Dia,352 Dia Clutch 1.75 Spline,Spark Plug,Cable Comp
Clutch master Cyl,Slave Master Cyl,Door Lock RH,Oil Seal,Oil Seal ID 155.73.OD,Cum Fuel Water Seper
INJECTOR REPAIRING AND HIGH PRESSURE PUMP REPAIRING
flags coloured,national flag,flex printing display board red colour size,bathroom mat for ors line,
Paper Legal,Paper A4 Size,Register 200 pages,Register 300 Pages,Register 400 pages,Pencil,Rubber,Sh
Keto diastix bott of 50 strips,Field stain A and B,Stain Leishmans 500 ml Bott,Stain Methylene Blue
Spanner,F Cleaner,W Machine,Brushes,Pliers
D Twist,Spanner,S Screen,Screw Driver,K Board
URF 80: 20
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
dot matrix printers,Online UPS (V2),Barcode Reader Equipment (V2)
Hand Held Jamming System
Asphalt Base for Badminton Court,Synthetic All Weather Surface Badminton Court,LED Flood Light Syst
Demolition brick stone masonry,Demolition reinforced cement concrete,Separating scrapping and clean
ARMATURE,DRIVE PINION,SELF BUSH,SELF FIELD COIL,FUEL COCK
Clutch Master Cyl,Sleeve Cyl Assy,Knuckle Bearing,Pinion Bendix Drive,Baby Filter,Kilometer Cable,R
Gas Filling and Repair
Z1, MISC-DCH-2740332018188925.3, CABLE FOR ANR HEADGEAR WITH 10 PIN MALE CONNECTOR AND 8PIN,Z1, MIS
PAKING,ELECTRIC HORN 24V DC,BRK CYL DIA 100 REPAIR KIT,SPRING 130 3 S443 624 1008,FIELD COIL ASSY,A
Title1,Title2,Title3,Title4,Title5
LV6/MT11, 2540-000019 Chain Assy Tyre Parsons Single Type For Tyre Size 12.00x20
Operation And Maintenance Of Water Supply Systems - Operation and Maintenance,Operation And Mainten
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Not Required; Others,Manpower Outsourc
Bearing Bush CE,Bush,Bearing Bush DE,Pinion,Relay Main,Solenoid Electrical,Regulator Control Elect,
Split Air Conditioner Including Green AC, Wall Mount Type (V2)
All in PC i3 processor 8 GB RAM 512 GB SSD with keyboard mouse,UPS 600 VA,Computer Table,Cushion Ch
Intrusion Monitoring System
Gabapentin 300 mg plus methylcobalamen 500 mcg Tab,Tab Gliclazide 60 mg plus Metformin 500 mg,Tab G
GeneXpert-IV: 4 x 10-Colours Modules Upgradation
Server,All in One PC (V2),All in One PC (V2),Multifunction Machine MFM (V2),Multifunction Machine M
Custom Bid for Services - Soil Investigation
Gasket Set,Bty Lead with Terminal,Rubber Coupling,Sump Gasket,Fan Belt Long,Brake Pressure Pipe,Hos
Chicken Eggs (Q3)
10339376,10332593,10342163,10344244,10344794,10347278,10556778,10339914
Drive Pinion,Rotor Assy,Combination Switch,Mounting Pad Rear,Eng Mtg frt,S A Fuel Hose,Bushing,Rubb
Injector Assembly,Front brake pipe,Exhaust muffler,Pipe Break no 6,Release bearing assembly,Cover a
Sugar (V2) (Defence) (Q2)
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
Provision of Two Server Configuration and Installation of Domain Controller to Client Workstation
Hiring of Earth Moving Equipments, Material Handling Equipments and Cranes (per Hour basis) - As Pe
Light Weight Running Shoes (V2) (MHA)
Full Radius Resector for Arthroscopic Shaver System, Disposal, Presterilised, 3 To 5.5 cm Diameter
D-LINK UTP CABLE CATE 6E,Earth test meter,4 sqmm pvc cable,12V AHC bty,Bosch Tool Kit,Coaxial Cable
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; IT-Technical,Manpower Outsourcing Serv
Refined Sunflower Oil (V2) (Defence)
Refined Mustard Oil (V2) (Defence)
Mechanical Valve Aortic comma Supra Annular 17MM,Mechanical Valve Aortic comma Supra Annular 19MM,M
Mechanical Heart Valve COMMA Rotatable Mitral 23mm,Mechanical Heart Valve COMMA Rotatable Mitral 25
Monthly Basis Cab & Taxi Hiring Services - Sedan; 2000 km x 320 hours; Local 24*7
Z7 5930 -009230 Q-SWITCH ASSEMBLY
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others
Plain Copier Paper (V3) ISI Marked to IS 14490,Plain Copier Paper (V3) ISI Marked to IS 14490,Plain
Sambhar Masala as per IS 1797,Chilly as per IS 2322,Spices and Condiments - Turmeric Whole and Grou
GASKET CYL HEAD,DISC CLUTCH,BRG SET CONNECTING ROD,BRG SET CRANK SHAFT,KIT PAD ASSY FRONT,ASSY KIT 
Jacket Sleeping Flannel - Military Hospital Clothing,Jacket Sleeping Flannel - Military Hospital Cl
Online UPS 10KVA with bty bank,Online UPS 5KVA with bty bank,FCBC,Servo Stabilizer 30 KVA,Power Cab
GLASS PARTITION,COUNTER TOP,ALUMINIUM FRAME,PEBBLE BED,LED VIDEO WALL,CEILLING SPEAKERS,3D RELIEF M
Non Electrical Exercise Support Tool Upper Limb for MI Room
Mixed Pickle 5 Kg,Coconut Powder,Papad Bikaneri,Mango Pickle 5 Kg,Chilly Pickle 5 Kg
Elevated Security Post Galvanised with roof top and side cover,Dimension of Elavated Security Post 
Custom Bid for Services - ----
Apron Locker Cabinet (Q3)
Solenoid Switch,Bush,Field Coil 24 Volt,Bush,Inner Plate,Solenoid Switch,Pinion,Brush Carrier Plate
Portable Label Printer
Bearing,Bulb 12V 6W,Retainer Gasket,Gasket Exhaust Manifold,Strainer,Dozer Seal Kit,Element Filter,
Tea CTC (V2) (Defence) (Q2)
INJECTOR NOZZLE,PUMP ELEMENT,PISTON RING SET,PISTON RING SET,LINER,FUEL FILTER,OIL FILTER,AIR FILTE
Iron Frame 20 Ft and 15 Ft 24Inch x 24 Inch for Gate,Iron Frame for Table,Aerial Recce Svl Device f
TYRE PRESSURE GUAGE,BULB 12V 21W,TERMINAL NEGATIVE,MAIN RELAY,FOG LAMPSWITCH,TAIL LIGHT VEHICULAR,C
Offrs/JCOs Living Shelter (OJL)
FUEL PUMP MOTOR,FUEL PUMP ASSY,ASSY FUEL FILTER 3PIN,ASSY FUEL FILTER 2PIN,PNEUMATIC SOLENOID VALVE
FRONT WND SHIELD,CABIN TILT HYDRAULIC PUMP,DRYING DISTRIBUTION ASSY,AIR COMPRESSOR,KIT PAD ASSY FRO
Bearing Ball,Kit,Housing Filter,Filter,Seal,Universal Joint Assy,Service Kit Dozer,Elbow on bypass 
Repair of Complete Surface,Rapair of Crack Bond for both Handball Court,Paint on both Handball cour
Chain Sprocket set,Indicator Bulb,Chain Sprocket set,Kick starter shaft assy,Brake Master Cyl,Wheel
Equine Hoof Cutter,Hoof Searching Knife,Clencher,Hoof Rasp,Shoe Nail Cutter
Supply and fixing of new window Blinds size 4 ft x 4 ft,Supply and fixing of door handles and door 
BULB 12H7 55W,WIPER BLADE FRONT 600,CYLINDER HEAD GASKET,FLY WHEEL RING,BALL BEARING,PIPE TC TO I C
Locking Plate,Field Coil 12V,Solenoid Switch 12V,Oil Seal,Wheel Cyl Assy 38MM,Wheel Cyl Rep Kit,Inj
CLUTCH PLATE,CONTACTLESS SWITCH 616 213,HYDRAULIC AGGREGATE HA 25 V PUMP,CLUTCH COVER MZF,HOSE 25 3
SPARK PLUG,SPARKING PLUG,SPRING PAD,DISC CLUTCH,MOUNTING ENGINE FRONT,COVER ASSY CLUTCH,BEARING FRT
Clutch Plate Marksman,Pressure Plate Marksman,Clutch Release Bearing Marksman,Bleeder Slave Cyl Mar
Manpower Outsourcing Services - Minimum wage - Unskilled; Not Required; Others,Collection & Disposa
Flex 3 x 4 Feet,Flex 4 x 3 Feet,Flex 4 x 3 Feet 5 Inch,Printed Flex 2 x 3 Feet,Flex 2 x 3 Feet
Havells 2 c 1.5 sqmm,Havells life line sc1.5 Sqmm,Havells Eco pendant holder,Havells 6A Bed Switch 
PIPE FUEL,FUEL FILTER SECONDARY,OIL FILTER SUPER,THREAD TAPE,AIR FILTER,GASKET CYL HEAD,GASKET CRAN
Mokita Brush Cutter,Tripal 18 x 15,Tripal 30 x 24,Rope,Sand Bags,Register 200 Page,A4 Size Paper,Le
MOBIL FILTER,GEAR LEVER,INDICATOR LIGHT ASSY,BOLT 19 INCH,BOLT 13 INCH,BRAKE BOLT WITH NUT,OIL FILE
AIR FILTER ASSY,PINION ASSY SELF,BUSH SET SELF,OIL PRESSURE PIPE,BENJO UNION 19MM,PUMP ELEMENT 15KV
WIPER BLADE,ASSY FRONT FOG LAMP,GEAR LEVER BUSH KIT,BTY CUT OF SWITCH,KNUCKLE BUSH,PULL ACCELERATOR
TABLET (iPAD)
Goods Transport Service – Per Trip based  Service - Food Grains, Food Items; Open Body LCV Truck;
Video Conferencing Camera / Web Camera (V2),Professional Large Format Display,Entry and Mid Level D
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
A4 PAPER,FS PAPER,UNIBALL PEN FINE,PILOT V7,COLOUR FILE COVER WITH PRINTING,WHITE FILE COVER WITH P
PAD CUSHIONING RUBBER,CABLE CONTROL ENGINE STOP,WASHER M.S. 10MM ID 55MM O.D 6.3MM THK,BOLT MACINE 
FUEL PIPE FEED PUMP TO FUEL FILTER,FUEL PIPE FILTER TO FIP,CONNECTING ROD,METER TIME TOTALIZ SP 50 
Repair for Rewinding of Complete Alternator,Repair of Bearing,Repair of Bearing Sleeve,Repair of AV
Rod Spring Assy Frt,Fuel Pipe,Radiator Assy,Bearing Rear,Temperature Elect Gauge,Oil Pressure Switc
NK001,NK002,NK003,NK004,NK005,NK006,NK007,NK008,NK009,NK10,NK11
Dry Film Lubricant Mil O-L 46147A Type 2
3 Pair Round Cable 1.5 Sqmm (16 AWG 1.50 Sqmm),2 core round cable 1.5 Sqmm (16 AWG 1.5 Sqmm)
CONTROL VALVE,NOZZLE WASHER,FUEL FILTER BOWL,OIL SEAL,SPARK PLUG
Fd Elect (Solar Lighting Sys 25 W)
W10 6675-000047 Parallel Rular Common 150MM,B1 1005-008259 Cover Gun Muzzle,B1 1005-007815 Sling As
SPARK PLUG,CLUTCH FAN,WATER PUMP,SUSPENSION BUSH KIT,BRAKE PAD FRT,RELAY MAIN,CLUTCH MASTER CYL,OIL
Hiring of Earth Moving Equipments, Material Handling Equipments and Cranes (per Hour basis) - As Pe
Material and labor for asphalt Base,All Season Synthetic Surfacing,Iron Pole 7 Ft Height 3 inch Dia
Work station with soft board,White Board 3 by 4,Table Glass,Air Purifier,Det Chair,Blinds,Stabilize
SB20 1702 SEALING,765 08 SB358 HOSE ASSY,54 59 107 1 CLIP,520 07 006 05 WASHER,ETY 500 115 COMMON C
Boot High Ankle PU Rubber Sole (Defence)
LV1 R72 172 2M 01 077 1 GASKET,LV1 R72 175 02 034SB 1 GASKET,LV1 R72 4010720355159 CABLE FOR LOG AT
Clutch Master Cylinder,352 Dia Clutch Disc Assy,Pump Water,Drag Link Assy,Cover Assy
Wire Sleeve 10 MM,Wire Sleeve 2 MM,Light Wire 16 MM,Light Wire 10 MM,Tape Insulating,Feviquick Big,
TRANSPORT CHARGES FOR LOCAL CITIZENS,ADVERTISEMENT-PUBLICITY MATERIAL,MEDIA COVERAGE,REFRESHMENT,ST
Fan Belt,Fuel Flexible Pipe 21 x 19,Air Adaptor Kit 6 MM,Air Adaptor Kit 8 MM,Air Adaptor Kit 10 MM
Gloves Examination Small Size,Prevest Denpro EDTA RC Prep sol Gel,Mask Disposable Tieng Type,Novabo
ACC CABLE,CABLE 4X4,SPIDER BEARING,PRESSURE PIPE,WATER PUMP ASSY,AIR PRESSURE PIPE,HUB BELT,SPARK P
Register (V2),Gel Pen (V3),Gel Pen (V3),Rollerball Pen (V3),Rollerball Pen (V3),Highlighter Pen,Sta
Repair and Overhauling Service - Small CCTV Surveillance System (V4); CP PLUS; Yes; Buyer Premises
Fuel Pump Assy,Brake Pad,Bush King Pin,King Pin Upper,King Pin Lower,Taper Brg,Axial Roller Brg,Inj
Hiring of Custom House Agent - Lumpsum Based - Export; Demolitation of Defence building; Demolitati
Providing and fixing outdoor asphalt base for synthetic surface volleyball court,Installation of ei
PRESSURE INJECTOR FOR BAYER MEDRAD IMAXEON SALIENT DUAL HEAD CT CONTRAST POWER INJECTOR 190ML SYRIN
Toner Cartridges / Ink Cartridges / Consumables for Printers
Toner Cartridges / Ink Cartridges / Consumables for Printers
Plain Copier Paper (V3) ISI Marked to IS 14490
Computer Paper (V3) Conforming to IS 12766
Manpower Outsourcing Services - Minimum wage - Skilled; Not Required; Others
ENDOSCOPY CAPSULE FOR CAPSULE ENDOSCOPY ENDOSCOPIC CAPSULE COMPATIBLE WITH SB-3 RECORDER
LV7 STLN VF 6220 72 000403 LIGHT ASSY INDICATOR,LV7 STLN 6240 013624 LAMP INCANDECENT,LV7 STLN 6240
PSA test cards for Finecare Analyzer,HbA1C Rapid Card Quantitative Test kit of 25 Test,T3 Elisa 1X9
Manpower Outsourcing Services - Minimum wage - Semi-skilled; High School; Others
Relugolix 120 mg Tab,BETAMETHASONE 0.1 PERCENT WW CREAM,BETAMETHASONE 0.1 PERCENT PLUS NEOMYCIN 0.5
Microcuvettes for Haemoglobinometer,Hepatitis B surface antigen HbsAg detection ELISA kit of 96 tes
Indoor Direct View LED Video Wall (8ft x 4.5ft),Video Wall Controller/ Processor,Logistic and Fabri
X-1944350,2910-008285,P-1008351,2805-002769,B-290007
Gasket lub cooler,Gasket filter head,Gear lever shifting cont,Magnetic switch-1904320,Bearing,Unit 
CALIPER ASSY DISC BRAKE,DRIVE ASSY,MAJOR REPAIR KIT AIR COMPRESSOR,SOLENOID SWITCH,SPROCKET CAMP CH
Envelopes-Handicraft (Q3)
Manpower Outsourcing Services - Minimum wage - Unskilled; High School; Others
Sports Trophies-Handicraft (Q3)
Phenol (Carbolic Acid) as per IS 538
Toilet Soap, Liquid (V2) as per IS 4199
TAPE INSULATION,M SEAL BIG,ANABOND TUBE,THREAD TAPE,CUTTER BLADE SMALL,BANJO NUT WASHER,CARBURETOR,
Iron Angle,Iron Sheet,Wooden Cabinets,Panelling 18x22,Panel Focus lights,Wall Mounted Fan,Split AC 
Mutton Rogan Josh Canned (Goat/Sheep) (V3) (Defence),Mutton Rogan Josh Canned (Goat/Sheep) (V3) (De
BOQ 1 , BOQ 2 , BOQ 3 , BOQ 4 , BOQ 5
Automated Trail Handling and Winching System for 130MM M-46 Gun System
PRESSURE PLATE,FIELD COIL,FUEL CUT OFF SWITCH,4ST RELAY,IGNITION SWITCH,COMBINATION SWITCH
ELECTRIC SEVEN FUNCTIONAL ICU HOSPITAL BED
DRUMS METAL GALVANISED IRON SHEET WITH 5,ANABOND AL 673 350 GMS,ALCOHOL ISOPROPYL TECHNICAL 6810-00
DX Nikon Lens Black 18mm to 300mm and Ed Vr AF 5,Osaka Camera Flash Speed lite TT990 with 18 to 180
CLUTCH PLATE,PRESSURE PLATE,FUEL PIPE,FAN BELT,FUEL FEED PUMP
2530-72-0471939,2990-72-0466870,2920-005460,2930-72-0466359,B-4383951,F-1939650
Field coil,Drive assy,Clutch Master cyl,Solenoid switch,Clutch plate,Fog light,Bulb fog light,Relay
Hose Connection,Hose Connection,Bolt,Clip Frame,Clip Shaft,Torsion Tape,Clutch Booster,PV RV Assy,H
Sugar (V2) (Defence) (Q2)
Spices And Condiments - Coriander, Whole And Ground (V2) Conforming to IS 2443,Spices and Condiment
Room freshener machine,Air wick Refill,Room Freshener,Collin,Pencil Cell,Pencil Cell,Dusting Cloth,
48 Volt FCBC 25Amp,Battery 12 V 200 AH,Beetel Telephone Caller ID C5l,Multi Meter,Flood light 20W,D
CAT 6 UTP Cable 305 Mtr,Dell Pro Plus Keyboard KB 700,Dell Laser Mouse wired MS 3220,Printer USB Ca
Bits , Pins , R Trough , Knife , Nuts
DRAG LIFTER
Refilling of medical oxygen gas in cylinder jumbo cylinder D type 7000ltr,Refilling of medical oxyg
P-1302318,2530-018172,2930-002922,4730-72-0000764,B-7762010
Refined Sugar conforming to IS 1151
SPEEDO PINION REAR COVER UPPER,ASSY CLUTCH PRESSURE PLATE 310,ASSY RELEASE BEARING 1 75 DIA,ARM ASS
Installation of Security Alarm System incl Siren at New MR Bay
Quadcopter
Cheese Spread 200gms,Cheese Cube 200gms,Cheese Cube 1kgs,Cheese Slice 200gms,Cheese Slice 750gms
Biscuits,Cornflakes,Tomato Sauce,Horlicks,Pickle,Bournvita,Cornflour,Lactogen No 1,Chocolate,Sausag
Transmission System/ Front Gear Case (Demand Drive Fluid) & U Joint Grease
Goods Transport Service – Per KM Based Service - Household/Office; Open Body Taurus; 21 FT Truck
Polaris Premium 50/50 Antifreeze Coolant
Panelling PVC,U Beading,Black Screw 1 inch,Skalling 1.5 x 2 inch,Elfy,Nails 2.5 Inch,Self tapping s
REPAIR OF EXISTING SURVEILLANCE & PREVENTION SYSTEM (CCTV CAMERAS)
RJ 45 Connector,Printer Cable 10 Mtr,Rechargeable Cell,Noval Bty Charger,Thedolite Bty Charger,9 Vo
LV7 STLN VF P 1304856 NOZZLE,LV7 T 815 443 612 015 807 AIR PRESSURE GOVERNOR,LV7 TATA 264143700163 
read only compact disc cd,Eraser,Speed Post Envelope (Large),Compact Disk Cases - CD - DVD Case
Manual Pencil Sharpener (V3),Sticky Notes (V2),Cleaning Duster (V3),Packaging Tape,Packaging Tape,P
Cotton Towelling and Towels (V2) as per IS 7056,Sipper Bottle (V2)
CELLULOSE SPONGE DISPOSABLE PKT OF 5,PVA SPONGE STERILE DISPOSABLE,SF6 GAS VR SURGERY,Paper Roll Fo
Pillow Covers-Handicraft (Q3)
Mist Fan USHA,Disposable Paper Bag Small Size,Disposable Paper Bag Medium Size,Chair Backrest,Pades
Air Pressure Pipe,Door Inner Catch,Rear Hub Sprocket 38 Teeth,Assy Combination Switch,Cylinder Assy
Kitchen Chimney,Tea Container,Imam Dasta,Tray Set,Atta Chalni,Steel Spoon,Borosil Glass,Aluminum Bh
Cover Assy,Cylinder Head Gasket,Gasket kit Oil Sump,Gasket Push ROD Cover,Weather Strip Door,Assy H
675 50 392 PACKING MATERIAL,775 22 38 RING,775 36 25 RING,700 40 260 05 GASKET,700 40 260 8 GASKET,
Dried Cow Peas (Lobia) (V2) (Defence)
AC Water Valve Changement,AC Gas Refilling,AC Coolent Connecter New Fitting,AC Fan belt Changing,Da
HYDRAULIC PUMP WITH PULLING CHAIN FOR ARMT
Bullet Proof Swivel Frame,Gabion Basket,Hesco Basket,Anti Missile Screen
Soldering and Accessories Devices,PVC Saddle Patti,PVC Junction Box,PVC Extension Ring,PVC Cement S
OIL FILTER,AIR FILTER PRIMARY,AIR FILTER SAFETY,HOSE,CYLINDER REPAIR KIT,SPROCKET,BOOM CYLINDER KIT
Chilli Powder,Turmeric Powder,Dhania Powder,Chicken Masala,Meat Masala,Sambar Masala,Chat Masala,Ga
Nebivolol 5mg Tab,Nicorandil 5 mg Tab,Nimodipine 30 Mg Tab,Nintedanib 100 mg Soft Gelatin Capsules,
M S Angle,M S Sheet,Welding Rod,Freviquick 5gm,Throttle Body Spray
Arduino Board,Metal Sensor,Dry Sensor,Wet Sensor,Container,Lithium Bty 12 V
Dispo Syringe 10ml with needle,EDTA Tubes 3 ml,Insulin Disposable syringe 1ml,Dispo syringe 50ml wi
Bathing and Toilet Block structure with Prefab colns,Non skid ceramic floor tiles of size,Looking M
H Smith , Claws , Bags , C Hot , Kettl
Distributor Head,Armature Assy,352 Clutch Cover Assy,Exhaust Brake Solenoid,Cabin Shock Absorber
Drying and distributor unit,Motor assy wiper,Cable assy complete,Combination switch,Fuel pump trans
Ram Rep Kit,Clutch Cyl Assy,Equalizer Rep Kit,Wheel Bolt,Armature Starter Motor,Hose,Break Booster,
FD WSS RO FILTRATION PLANT
battery 12v 7ah,smps,pressure roller,taflon 2040,mouse,ram ddr4 8gb,pci lan card,battery 12v 5ah,pa
CABIN LIFTING PUMP,CLUTCH BOOSTER,PRESSURE VALVE,CLUTCH ASSY,AIR DRYER ASSY,MASTER CYLINDER,COMMAND
Superstructure for 03 x Double Storey Living Shelter 28 Students Capacity of size 24.596M x 11.146M
KY BOARD AND MOUSE COMBO,LOGIC CARD,PICKUP ROLLER,PICKUP ROLLER SET,FUSER ASSY 1020
Inj Esmolol 10 ml,Nor adrenaline Bitartrate 2 mg ml 2 ml Inj,Sodium Bicarbonate amp of 10 ml,Inj Ca
Bty UPS 12 V 7 AH,Monitor LG,Drum Cannon C 3120,Teflon,Pressure Roller 1606,Cleaning Blade 3120,Wir
CHEESE SPREAD
Summatriptan 50mg TAB,Itraconazole 100mg Cap,Chloroquine phosphate 250 mg,Ondansetron 8mg Tab,Folic
Hp 45 Stapler Pin,Envelope 6 x 4inch,Envelope 11 x 4 inch,Envelope 9 x 4 inch,Envelope A4 Size,Ledg
Manpower Outsourcing Services - Minimum wage - Skilled; Secondary School; Admin
Luliconazole 1 percent w w 50gm cream,Betahistine Dihydro Chloride 8mg Tab Vertin,Tab Cinnarizine 2
Manpower Outsourcing Services - Minimum wage - Unskilled; Secondary School; Admin,Manpower Outsourc
AMP Meter,Volt Meter 500V,Volt Meter 300V,Fuel Flexible Pipe 19,Solenoid Switch,Steel Angles 20x20x
Piston Ring Set,Piston Assy Std,Connecting Rod,Overflow Pipe,Main Bearing,Cyl Head Gasket,Oil Pump,
SHOCK ABSORBER,CYL ASSY FRT,BOLT,SEALING RING,NUT,NUT M 14
Maintenance Box T-04DI,Maintenance Box MC-G03,Mother Board with I5 Processor LGA 1151,RMA DDR 4 8GB
REPAIR KIT FOR AIR PRESSURE GOVERNOR,ALTERNATOR,REVERS LIGHT SWITCH,WHEEL CYL REPAIR KIT,OIL SEAL,C
Kit Lining Set Rear,Wheel Brg,Air Filter,Fuel Filter Assy,Flexible Pipe,Clutch Plate,Pressure Plate
Fan belt,Brake shoe assy,Disc Pad,Clutch cyl assy,radiator assy,Oil Filter,Ring Set,Parts Kit Pisto
NK003199 50 POTENTIOMETER,NK003200 SW ROTARY CO-PINBCD 513374-10,NK003201 RASISTANCE 20HM 1W THIN T
INSULATION TAPE ELECT COTTON SELF,FEVI QUICK ADHESIVE 3 GM,NITROGEN GAS PURE,CABLE ELECTRICAL D 3 M
H2 8305-000078,K3 7220-000012,J1 7520-000065,H1C 8110-000017,K3 7210-000027,H4 8135-000095
Z9 RP-6140-MISC-55B24LS-INS-60,Y3 RP-6135-001380,Y3 RP-6145-007490,Y3 RP-6145-000009,Y3 RP-6145-000
CA 8305-000072,F1 5110-000289 1,F1 5120 000060,F1 8020 400002,K6 KND NIV BK 40,H1B 6840-000007,K6 7
Manpower Outsourcing Services - Minimum wage - Unskilled; Secondary School; Others,Manpower Outsour
Title 1,Title 2,Title 3,Title 4,Title 5,Title 6,Title 7,Title 8,Title 9,Title 10,Title 11,Title 12,
Carbonated Soft Drink,Lime Based Soft Drink,Fruit Juice
Refined Sugar conforming to IS 1151
High Density Long Range Movable Lighting System
HEAVYDUTYSEARCHLIGHT,CARRYINGNYLONBAG,ADAPTOR,CHARGINGCABLE,SEALINGSTRAP
Radiator,T Water,Fan E,Pipe,Brake
Reporting Charges HCP,Reporting Charges HAA,Reporting Charges SHAA,Rate per day HCP,Rate per day HA
Portable Field Electrification Solar Set 10kW
Desktop Computer Set,Printer,UPS,Desk with Bench Set,Black Board,Almirah,Plastic Table,Plastic Chai
Hose Assy,Brg Front Axle,Brg RR Wheel,Cyl Head Gasket,Pressure Plate,Air Pressure Pipe
Spider Bearing,Front Axle Tube,Front Hub Seal,Rear Hub Seal,Knuckle Bearing,Ignition Coil Assy,Fuel
Assy Rear Door Latch RH,Tailgate Latch Assy,ASSY FUEL FILTER,ASSY UNIVERSAL JOINT,FLANGE,ALTERNATOR
Refined Sunflower Oil (V2) (Defence)
ROD SPRING ASSEMBLY RIGHT HAND FRONT,SPRING ASSEMBLY RIGHT HAND REAR,PIN SHACKLE,MOUNTING PAD ENGIN
UPS 1 KVA,HDMI SPLITER 4 PORT,HDMI SPLITER 8 PORT,UTP CABLE FOR SERVER,EPSON M100 PRINTER HEAD,EPSO
REFINED SUNFLOWER OIL 15 KG TIN,REFINED SUNFLOWER OIL 1 Liter Pouch,REFINED SUNFLOWER OIL 1 Liter B
Air Filter Element,Assy Fuel Filter Dephi 3xPin,Kit PAD Assy Front,Roller AC Belt Tensioner,Cam Sen
Post It Pad 3X5 3M,File Cover Printed Thick Cardsheet,Pencil,File Covers Ivory Printed,High Lighter
CFW01 31225 Bolt,CFW01 11236 Washer Spring,CFW05 12032 Washer,116FG 11321 Bolt,CFW01 12472 Washer S
Apple Macbook
LV1 R72 155 15 131 BOLT,LV1 R72 5365430002607 OR 5365720330319 BUSHING SPACER,LV1 R72 172 46 050 1 
LV1 R72 53-014B FUEL FILTER DRG NO 53-014-B,LV1 R72 CISV SK 0513 MOUNTING PLATE REAR RH,LV1 R72 155
LMA Proseal 1,LMA Proseal 1 point 5,LMA Proseal 2,LMA Proseal 2 point 5,LMA Proseal 3,LMA Proseal 4
BEARING DRIVE BEVAL,BEARING FRONT AXLE,BEARING REAR AXLE,OIL SEAL REAR,OIL SEAL,SPARK PLUG,GASKET C
550195,550132,562510,562520,562571
Ink Cart for Brother DCP 2441W,Cart 88 A,Cart 12 A,Cannon G 4070,Cannon G 570 all Color
GPS Diagnostic Equipment
Combat Plate Carrier,Triple Magazine Placard,Single Pistol Mag 3 Inch,Grenade Pouch,Wing Pouch,Dump
Readymade Flower S M L,Register 100 To 500 Pages,Note Book 100 Page,Talc Sheet 4 Feet,Drawing Roll
REVERSE LIGHT SWITCH,ASSY WINDOW REGULATOR RH,POLY V BELT,GASKET CYL HEAD 11141M86512,BEARING SET C
CRANK SHAFT GRINDING,MAIN BRG SETTING AND MAKING,VALVE SHEET CUTTING,VALVE TUNNING,VALVE GUIDE FITT
NFSU Cyber KIOSK Ver-3
Malted Milk Food with Cocoa Powder (V1) (Defence)
ENG MTG PAD,STARTING ROPE ASSY,ON OFF COCK,CARBURATOR ASSY,ENGINE MTG PAD,SPARK PLUG,FUEL PUMP ASSY
AUTOMATIC PRESSURE REGULATOR,SHAFT IN THE SET,ELCTROMAGNET EM 26 1C,SENDIMENT DRAIN VALVE,HOSE ASSY
BANJO BOLT,AXUAL ROLLER BRG,FIELD COIL ASSY,HEAD LIGHT ASSY LH,ARMATURE ASSY,TENSIONER ASSY TIMING,
Paper Legal,Register 200 Pages,Talk Sheet,Register 300 Pages,Paper A4,Volley Ball,Basket Ball
FUEL PUMP TRANSFER,VEHICLE SPEED SENSOR GB,WIPER BLADE FRONT 600 DRIVER,DUEL BRAKE VALVE REP KIT,WH
Screw Driver long heavy duty,Bosch Screwdriver Bit Set,Spark Detecting Screwdriver,Soldering Gun,Vo
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Secondary School; Others
Portable Elevated Sentry Post
FD TECH SHELTER MI ROOM
FD TECH SHELTER (BRL TYPE)
MOBILE TOILET
FD FLUSH LATRINE 6/1
BATHING CUBICLE 8/1
CLUTCH PLATE,CLUTCH RELEASE BRG,WHEEL BRG FRONT,KNUCKLE BRG,THROTTLE BODY KIT,TIMING BELT,FAN BELT,
Rental for venue,PA System arrangement,Camera recording lighting and stage arrangement,Flex board o
Almond without Shell (V2) (Defence)
Clam patti,Gasket,Ring Buffer,Gasket,Gasket,Gasket,GKT,GKT,GKT,Ring Packing,Ring Packing,Ring Packi
DISTRIBUTOR HEAD,VANE PUMP,POSITINOER ASSY,CAM PLATE,TD PISTON
DAFC-60%  (Glycol Based Antifreeze Coolant) -Defence
TYRE REMOVAL AND REFITMENT DEVICE,HIGH PRESSURE TANK CLEANING DEVICE,POWER SCREW DRIVER,CUTTING PLI
Bush SPRG Shackle,Filter Assy Fuel,Harness Assy Wiring No 1,Oil Filter Assy,Harness Assy Wiring No 
5 Arm Gold Crystals 38 x 38 x 70 cms,Set of 6 Cortina Dessert Fork Gold,Set of 6 Cortina Dessert Sp
Rectifier Assy,Combination Switch,Armature 12V,Clutch Plate,Coolant Filter
Refined Sugar conforming to IS 1151
Repair and Overhauling Service - RPAV Aerarc Trinetra; RPAV Aerarc Trinetra; No; Service Provider P
Air Filter TATA,Mud Flap STLN,Air Dryer Repair Kit STLN,Radiator Hose Pipe TATA,AnanabOnd,Radiator 
BRANCH PIPE,HOSE,CLUTCH BOOSTER,CLUTCH MASTER CYL,CLUTCH SLAVE CYL,STARTER MOTOR 24 V,INDICATOR LIG
10339540,10332243,10363577,10333453,10449063,10339159,10443074,10323951,10454070,10361227,10451941,
10327371,10325237,10329092,10345478,10362626,10346630,10344995,10327294,10346635,10347150,10337177,
Banana,Mango,Papaya,Mussambies,Pineapple
Cashew Kernels Whole Raw (Grade 240) (V2) (Defence)
DRIVE ASSY STLN,DRIVE ASSY,BUSH SET,FLASHER SOLID STATE,RING OIL SEAL INNER,OIL SEAL RING,OIL FILTE
OIL HYDRAULIC PX-26 EQUIVALENT TO HYDRAUNYCOIL FH-6
Tetracycline 500 mg Tab,Tab Isoniazid 100 mg with Pyridoxine 5 mg,Isoniazid 300 mg Tabpoint,Syp Pyr
Surveillance Quadcopter
Part No NK Nomenclature Stanley Comb Spnr set of 12,Part No NK Nomenclature Socket3 4 inch 43MM,Par
Hand Wash Liquid,Colin,Tissue Paper,Harpic,Phenyle,Mop Cleaning,Wiper cleaning,Odonil,Hit Mosquito,
Natural Cheese (Hard Variety), Processed Cheese, Processed Cheese Spread and Soft Cheese as per IS 
Network Attached Storage (NAS) Device
Repair, Maintenance, and Installation of Plant/ Systems/Equipments (Version 2) - Expdr on Construct
Tea (CTC)
Synthesizer Card with Base,Mosfet 28401,SRAM 128 KX 16,Cap 33 UF 25V SMD,BMC 1526,Bty 11 MAH
LOCK ASSY STEERING,FIELD COIL ASSY,CORD SET HIGH TENSION,SOLENOID SWITCH 12V,SPEEDOMETER ASSY,FUEL 
FLEX BOARD 15X2.5 FEET,FLEX BOARD 8X2.5 FEET,FLEX BOARD 5X7 FEET,CNC MACHINE CASE,LAB NAME PLATE 1X
Repair and Overhauling Service - built up trucks; Ashok leyland; Yes; Buyer Premises
Security Manpower Service (Version 2.0) - Office/Commercial/Institutions/ Residential; Unarmed Secu
Dry Grapes Munnaka,Cashew Nut,Almond without Shell (V2) (Defence)
Beans Dried (Rajmah) (V2) (Defence)
Regulator 12V,Inlet Valve Seal,Pole Screw,Valve Seal,Rotary Switch,Ignition Coil,Fan Belt,Tie Rod E
Dried Cow Peas (Lobia) (V2) (Defence)
Gun Correction Form,Fire Info Form,Fire Order Form,Programme Shoot Form,GPO fire Plan form,Deductio
WHEEL ALIGNMENT & BALANCING AXLE DRIVE SHAFT REPAIR CARRIED OUT,WHEEL ALIGNMENT & BALANCING CARRIED
MULTI DRUG OF ABUSE URINE TESTING KIT AMB BAR BZD COC MOR THC POUCH CONTAINING 01 EACH
NVR 16 Port 4K,PTZ day and Night Vision Camera 36 x Zoom,HDD 6 TB,Cat 6 Armored Cable,8 Port Gigabi
INDOOR GYM WITH SHED
Hiring of Consultants - Milestone/Deliverable Based - Analysis, Design & Preparation of Structural 
Cornflakes,Cornflour,Custard Powder,Jelly,Tomato Sauce,Pickle
Cheese Cube,Cheese Slice,Cheese Spread,Matches Safety,Cornflour,Custard Powder
Supply of materials for protective/ retaining wall
Malted Milk Food
Paper Feed Roller MFD,Head cable Printer,Plotter TM Print Head,Scanner Printer,Print Head Printer,D
Rivet CSK Flat HD Clamp,WASHER SEALING,PLATE INSTRUCTION,NUT CASTELLATED THIN HEX PRECISION STEEL 8
Cut Out with Powder coating radium pasting and installation 5ft x 4ft,Cut Out with Powder coating r
Short Term Cab & Taxi Hiring Services - Sedan; Local; 40Kms x 5Hrs,Short Term Cab & Taxi Hiring Ser
2024-25 Supply of All Terrain Vehicle Bridge (ATV)
Behind the Ear Hearing Aid (Digital)
Unmanned Aerial Vehicle & Payload Systems for Surveillance
High Security Weld Mesh Panels of Size of 12.7 X 76.2 mm along Mesh and Panel size and Weight 2600X
ARF Model 3D NG 78"
GEAR SHIFT BOOSTER,FUEL FILTER,PINION,MECHANISM HANDLE,CLUTCH PLATE ASSEMBLY
Nikon Camera Z6 III
GSL-5A24-115F STARTER ASSY,7050100100 LIGHT SWITCH,3H0435 HOSE ASSY,10X1046 SEAL SHAFT,1040312 BALL
30 KVA 3 Phase Alternator,Pneumatic FRL Filter Regulator Lubricator,Genr Set Drive Gear,100 Amp Cha
Malted Milk Foods with Cocoa Powder (Defence)
RETURN LINE HOSE ASSY FOR ARMY BUS,WHEEL BOX FOR TATA 2.5 TON,ASSY WIPER ARM FOR TATA 2.5 TON,ASSY 
Manpower Outsourcing Services - Minimum wage - Skilled; ITI; Others,Manpower Outsourcing Services -
Toner Cartridges / Ink Cartridges / Consumables for Printers,Toner Cartridges / Ink Cartridges / Co
HOSE LOADER 1,HOSE LOADER 2,HOSE LOADER 3,HOSE LOADER 4,HOSE LOADER 5
Repair/upgradation of toilets
Carbonated Soft Drink,Lime Based Soft Drink,Fruit Juice
Malt Based Foods with Cocoa (Defence)
Repair and Overhauling Service - As per list of ATC; Mixed brands; Yes; Buyer Premises
Welding Rods and Filler Wire for Gas Shielded Arc Welding of Structural Steel as per IS 6419
Bamboo, Tent Pole as per IS 7344
Hydration Pack (Q3)
Hydration Pack (Q3)
Pressure Sensitive Adhesive Plasticized PVC Tapes with Nonthermosetting Adhesive as per IS 7809 (Pa
Piano Type Non Modular Electrical Switch Socket Combination as per IS 3854 and IS 1293,Piano Type N
Molded Case Circuit Breakers (MCCB) as per IS / IEC 60947,LED Luminaire for Floodlight (V2) Conform
Hiring of Consultancy Services - Percentage based - Functional Consultants; Building and Constructi
CLUTCH MASTER CYLINDER,BRAKE PAD,ASSY FUEL FILTER,AIR FILTER ELEMENT,ASSY KIT LINED SHOE,COOLANT PI
FRONT WIND SHIELD,352 DIA CLUTCH DISC ASSY,COVER ASSY CLUTCH,ASSY RELEASE BEARING,BRAKE SHOE ASSY,I
Temperature sensor (Q3)
Syringe Infusion Pump,Volumetric Infusion Pump
LV1/R72 172-41-018SB SHAFT PROPELLER
Rotary pump 2.5 Ton,24V Relay MPV,4 x 4 cable 2.5 Ton,Alternator 2.5 Ton,Vane pump 2.5 ton
Indicator Lamp,Bulb,Knob,Hose,Switch
Fd Coil Assy,Brush Carrier Assy,Brake Shoe Rear,Brake Pad Frt,Speedo Mtr Drive,Ignition Coil,Speedo
Biochemistry Reagent Kit (Close System)
Dearation Tank,Fuel Water Seprator,Wiper Blade,Wiper Blade,Wiper Blade Rear,Gear box oil seal,Kit P
FPV Trainer Drone
Hiring of Consultancy Services - Percentage based - Subject Matter Experts; Forest and Environment;
FIELD COIL,SELF BUSH SET,ALTERNATOR ASSY,SELF STARTER ASSY,ROTOR ASSY
Inj Adalimumab 40 mg / 0.8 ml
CLUTCH PLATE,PRESSURE PLATE,AC FAN ASSY,RELEASE BEARING,NUMETIC VALVE,AIR PRESSURE PIPE
Repair of propeller,Repair of GPS assembly,Repair of 5dbi antenna,Repair of auto pilot,Service char
MacBook Air M4
Res arry 56R,Zener 3216 2.7V 4W,IC DSP TMS 320 VC 550,Display Modem Module,Flex Cable,BC Kit
Sugar (V2) (Defence) (Q2)
SA of Pipe,SA of Pipe,Shim 0.60mm,Shim 0.60mm,Light Assy Indicator,Relay Solid State,SA of Pipe Wat
Wind screen,Silicon paste,Clutch spring,Clutch assy,Exhaust manifold,Hub bering,Bearing,Turbo charg
LV7 TMB 06000 50761 80750 SLIDING GLASS,LV7 TMB 06000 50875 80265 LUMINATED PASSENGER DOOR GLASS,LV
Frame,Drone power connector,Propeller,Motor,Damper
Black Tea as per IS 3633 (Q4)
Black Tea as per IS 3633 (Q4)
Balmerol RG Compound
LAIP A TYPE Y SHAPED OF 75mm X 75mm X 6mm dimension all as per specification attached,LAIP C TYPE O
Hose,Stainer,Hose,Bty Relay,AM Meter,Water temp gauge,Engine oil pressure gauge,Hose,Hose,Hose,Hose
Portable welding machine,Iron cutter balde 4 inch,Iron cutter blade 5 inch,Iron cutter balde 14 inc
Clutch cover assy,Clutch plate assy,Release bearing,Slave cyl assy,Stabilizer linkage bar,Wiper bla
Dry Battery Cell 3 Point 7 Volt 2200mAh,Lithium Battery CR2 3V,Dry Battery AA 1 Point 5Volt,Tape In
Plywood 19mm size 8ft x 4 ft,Plywood 12mm size 8ft x 4 ft,Grinder Wheel 4 inch,Lithium Battery 9 vo
TAPE INSULATION,M SEAL,THREAD TAPE,FEVI QUICK,ANABOND,WD 40
FIRE EXTINGUISHER TYPE 2 KG,FIRE EXTINGUISHER TYPE 6 KG
Haldi powder,Dhania Powder,Mirch Powder,Jeera,Dal Chini,Ajwain,Garam Masala,Chicken Masala,Kasoori 
Talk Roll,Drawing Roll,Graph Paper,Ivory Sheet,V7 Blue,V7 Black,V7 Green,V7 Red,Non Permanent Ohp,P
Chairs for Training Hall,Training Posters,Models for Fresh and fruit items for training hall,White 
165282,210995,211402,231842,2940-20482532,2540009447
AT SHED STRUCTURAL ITEMS
Net replacement of side panels of Water air cooler,Replacement of Capacitor of Water air cooler,Rep
M Sand confirming to IS 383-2016 specification for coarse and fine aggregates free fromadherent as 
BPL C Bed,Valve E 833A,Bty 7 Point 2 V 4400MAH,SPO2 Probe 6 Pin,ECG Card
Clutch slave cyl,Fan belt engine,Slave cyl clutch,relay solenoid eng starter electricals,Relay emer
Flex with printing 10 x 2ft,flex board with frame 10 x2 ft,Star flex priting with frame 10 x8 ft,5 
Malt Based Foods with Cocoa (TEMP) (Defence)
Steel Rope,Red Reflector Tape 120Mtr,Yellow Reflector Tape 120 Mtr,TRL Relay Control Valve,Mud Fap
DAFC-60 (Indigenous),Protective PX-11,URF 80: 20,Oil 2T Synthetic/ Bombardier Injection Oil/VES2 Cy
Outdoor Unlicensed Band RF Radios
Tie Rod End,Self Housing,Brake Pad,Spider Brg,Armature Assy,Brush Gear Assy,Clutch Plate,Pressure P
Dell Desktop Inspiration 14 th Generation i7 Ram 16 GB Storage 512 GB
3110-006355,4720-016164,4820-72-0472252,2930-002930,3110-72-0025322
27891520016,27892012381,28593380010,28704230013,54077220631
Tv & Entertainment Units (Q3)
Fixed Quad Technical Training Drone,Ground Control Station for Fixed Quad Technical Training Drone,
Dry Erase Writing Boards (V3),Wooden Book Case
HP LaserJet 126A
REFINED SUNFLOWER OIL 15 KG TIN,REFINED SUNFLOWER OIL 1 Liter Pouch,REFINED SUNFLOWER OIL 1 Liter B
Microtek Legend 1000VA-24V UPS
OIL 2T SUPREME
Eng Mtg Pad,Relay,Relay 24 V,PTO Fan Belt,Speedo Cable,Fuel Feed Pump,Kit Pad Assy,Brake Pad,Spider
Cyl Barrel,Carburator Assy,Silencer Assy,Chain and Sprocket Kit,Lining Brake Shoe,Brake Shoe Frt,Ca
NOZZLE,NOZZLE PART NO 490,WINDOW DROPPER,CLUTCH DISC,CLUTCH BOOSTER
Glue Stick,Normal Pen Blue,Normal Pen,Fevicol,Colour Flag,Paper Pin,U Clip,Bilder Clip,Bilder Clip,
NAPKIN PAPER,SOFT BROOM,HARD BROOM,HARPIC 500 ML,COLIN 500ML,ODONIL,HANDWASH 200 ML,MORTIN REFIL,RO
Roofing sheet,Sq pipe,3 inch sq pipe,2 inch sq pipe,1.5 inch sq pipe,angle
Bed Sheet Single,Pillow,Pillow Cover,Mattress,Cloth Hanger
Plywood,T Face Veneer,Plywood,Plywood,French Polish,Teak Wood batten,Plywood,Teak Wood beading,Plyw
Interactive panel 75 inch with inbuilt CBT platform,VR Set,Insta 360 degree camera,Standalone AI dr
Soluble Coffee Powder (Refill Packs) (V2) (Defence)
Assy Clutch Disc Pressure Plate,Cover Assy Clutch,Lock Assy Gate Side LH,Clutch Slave Cylinder,Fiel
Specifications, Superstructue of Bathing Cubicle,Paints and Water Supply Items and Staging,Electric
LV1/R72 172.41. 018SB SHAFT PROPELLER
POLARIS AGL 44 OZ
Demolition of P 18 Building taking down copper aluminium points wiringcomplete including fixing and
HOSE,CYL HEAD GASKET,BULB 12 V 55 W,PIPE,BULB HEAD LAMP A 12 V 45 W
Screw Driver Set,Extension Board,Electric Plug 5 Amp,Electric Wires Flexible,Insulation Tape Large,
TEA CTC 500 Gms Pack,Pack TEA CTC 500 Gms,500 Gms Tea CTC Pack,CTC Tea 500 Gms Pack,Pack Tea CTC 50
Title1,Title2,Title3,Title4,Title5,Title6,Title7,Title8,Title9,Title10,Title11,Title12,Title15
Ether Solvent Bottle,Ketamine HCL Inj,Bupivacaine HCL Inj,Bupivacaine HCL Inj,Lignocaine Hcl Inj,Li
K9 T90S NBC EE8-333-030 HANDLE,K9 T72 NBC 175-87-164 3 SCREW,K9 T72 NBC 4240-000107 1 NBC FILTER FA
HP GT 52 Cyan Original Ink Bottle,HP GT 52 Magenta Original Ink Bottle,HP GT 52 Yellow Original Ink
Povidone Iodine 10Percent Oint Tube of 15 20gm,Tranexamic 500mg plus Mefanamic 250 mg Tab,Inj Rabie
Disposable Syringe 50ml,Bandage, Plaster of Paris 10 cm x 3 meters,Bandage, Plaster of Paris 15 cm 
Stainless steel Food Trolley
Manpower Outsourcing Services - Minimum wage - Skilled; High School; Admin
Manpower Outsourcing Services - Minimum wage - Semi-skilled; Not Required; Others
CHICKEN KEBAB
KAHWA
TEA CTC
Engine Mounting Pad,Ring Bearing Retainer,Rear Leaf Assembly,Regulator assembly,Bush Kinf Pin,Drive
Engine Mount front,Assy Kit Lined Shoe rear,Field Coil Assy 24V,Tr Bearing Hub RR Out 580 slace 572
Indent Book,Indent Book PVSM,Duty Cleark register,intake output chart,drug Chart,Investigation Char
Battery Secondary Lead Acid MT Type (Defence)
MT ITEMS 1,MT ITEMS 2,MT ITEMS 3,MT ITEMS 4,MT ITEMS 5,MT ITEMS 6,MT ITEMS 7
INTRA LIPID 20percent,IV Amino Acids inj 10percent100ml,Calcium 9mg plus Calcium gluconate 50mg Inj
LOCAL DUTY Sedan,LOCAL DUTY Sedan,LOCAL DUTY Sedan,LOCAL DUTY Sedan,LOCAL DUTY Sedan,OUTSTATION DUT
BTE HEARING AID MILD, MODERATE, SEVERE HEARING LOSS,RIC HEARING AID MILD MODERATE SEVERE HEARING LO
Annual Maintenance Service - Desktops,  Laptops and Peripherals - Desktop PC; hp,Annual Maintenance
1146123 ARM
Hay Grass (Loose and Bundle) (Q3)
54.0623SBD LV1R72 GASKET,17670041 LV1R72 GASKET,172030121 LV1R72 GASKET,34600SB LV1R72 OILPRIMINGPU
Wind Shield Glass,Hydraulic Head,TD Piston,Brake Shoe Front,Injector Nozzle
TIMING CHEST COVER SEAL BSIII,AIR PRESSURE PIPE MED BSIII,AIR COMPR GASKET BSIII,AIR PRESSURE PIPE 
TU00560168210227019 LV1R72 HOSE40U483BORDIA48MMWALTHK5MM,ADU2016SB LV1R72 AUTOMATICPRESSUREREGULATO
5330720320218OR5330720115697 LV1R72 CORD43211168OR43211169,17503034 LV1R72 GASKET,4720015064 LV1R72
17534033 LV1R72 GASKET,17566021SBA LV1R72 PUMPOILPRIMINGPUMPMODELMZN2,54120861 LV1R72 SEALANDSPRING
Soil Investigation,Boring of soil,Conducting of soil tests,Recommendation of foundation,Submission 

"""

# Step 1: Split into lines
items = data.strip().split('\n')

# Step 2: Count occurrences
counts = Counter(items)

# Step 3: Create Excel file
wb = Workbook()
ws = wb.active
ws.title = "Item Counts"

# Write headers
ws.append(["Item", "Count"])

# Write data
for item, count in counts.items():
    ws.append([item, count])

# Save the Excel file
import os
save_file = os.path.abspath(os.path.join(os.path.dirname(__file__),"xl files")) 
output_file = f"{save_file}/item_counts.xlsx"

wb.save("output_file")