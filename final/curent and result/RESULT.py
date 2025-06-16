from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import traceback
import time
import json
from selenium.common.exceptions import TimeoutException
from datetime import datetime as ds
from time import sleep

from datetime import date
today = date.today()
from selenium.common.exceptions import NoSuchElementException
import pyodbc
import pyodbc
import pandas as pd

def sql_udate(status, L_Placeholder, tender_id_to_update):
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\\SQLEXPRESS;"
            "DATABASE=gem_tenders;"
            "Trusted_Connection=yes;"
        )
        cursor = conn.cursor()

        # Serialize list into JSON string
        L_Placeholder_str = json.dumps(L_Placeholder)

        update_query = """
            UPDATE tender_data
            SET status = ?, L_Placeholder = ?
            WHERE tender_id = ?
        """

        cursor.execute(update_query, status, L_Placeholder_str, tender_id_to_update)
        conn.commit()
        print(f"Updated tender_id {tender_id_to_update} successfully.")
        cursor.close()
        conn.close()
    except:
        return print(f"faild:{tender_id_to_update}")    

def gem_funtion(elements_list):
    driver = webdriver.Edge()
    driver.get('https://bidplus.gem.gov.in/all-bids')
    wait = WebDriverWait(driver, 10)
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, "bidrastatus")))
    checkbox.click()
    sleep(2)
    for element in elements_list:
        time.sleep(1)
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'searchBid')))
        search.clear()
        search.send_keys(element)
        search.send_keys(Keys.RETURN)
        
        try:
            card_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'card')))
            if card_elements:
                pass
            else:
                continue
            for card in card_elements:
                if element == card.find_element(By.CLASS_NAME, 'bid_no_hover').text:
                    if "Technical Evaluation" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        sql_udate("Technical Evaluation", None, element)
                        
                        break
                    if "Bid Award" in card.find_element(By.CLASS_NAME, 'text-success').text  or "financial evaluation" in card.find_element(By.CLASS_NAME, 'text-success').text:
                        main_window = driver.current_window_handle

                        try: 
                            view_bid_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='View BID Results']")))
                            view_bid_button.click()
                            
                            
                        except: 
                            view_bid_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='View RA Results']")))
                            view_bid_button.click()
            

                        wait.until(EC.new_window_is_opened)
                        all_windows = driver.window_handles
                        new_window = [w for w in all_windows if w != main_window][0]
                        driver.switch_to.window(new_window)
                        time.sleep(5)

                        evaluation_texts = ['financial evaluation', 'ra evaluation', "evaluation"]
                        clicked = False
                            

                        for text in evaluation_texts:
                            xpath = f"//h4[@class='panel-title']/a[contains(translate(normalize-space(.), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '{text}')]"

                            try:
                                link = WebDriverWait(driver, 1).until(
                                    EC.element_to_be_clickable((By.XPATH, xpath))
                                )
                                driver.execute_script("arguments[0].scrollIntoView(true);", link)
                                driver.execute_script("arguments[0].click();", link)
                                print(f"✅ Clicked element with text containing: {text}")
                                clicked = True
                                break
                            except TimeoutException:
                                print(f"❌ Timeout for text: {text}")

                        if not clicked:
                            print("❌ No matching evaluation link found.")
                        
                        time.sleep(2)

                        try:
                            table_element = driver.find_element(By.XPATH, "//label[contains(text(), 'List of Sellers Qualified Financially')]/following::table[1]")
                        except NoSuchElementException:
                            elements = driver.find_elements(By.CLASS_NAME, "technical_eligible")
                            if len(elements) == 1:
                                table_element = elements[0]
                            else:
                                print("Could not do")
                                table_element = None  
                        
                        rows = table_element.find_elements(By.XPATH, ".//tbody/tr")
                        table_data = []
                        for row in rows:
                            cells = row.find_elements(By.TAG_NAME, "td")
                            row_data = [cell.text.strip() for cell in cells]
                            table_data.append(row_data)

                        new_arr = []
                        for arr in table_data:
                            price_str = arr[3].replace('`', '').strip()  
                            new_arr.append([arr[1], price_str])



                        sql_udate("Bid Award", new_arr, element)
                        print(f"done:{element}")
                        driver.close()
                        driver.switch_to.window(main_window)

        except Exception as e:
            print(f"error in gem id:{element}")
            traceback.print_exc() 

    driver.quit()

    
import threading
def Main(item_list):
    try:
        
        threads = []
        
        max_threads = 5
        for elements in item_list: 
            while True:
                threads = [t for t in threads if t.is_alive()]
                if len(threads) < max_threads:
                    break
                
                time.sleep(0.5)

            t = threading.Thread(target=gem_funtion, args=(elements,))
            t.start()
            threads.append(t)
                
    except:
        traceback.print_exc() 


conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=gem_tenders;"
    "Trusted_Connection=yes;"
)

query = "SELECT * FROM tender_data WHERE id >= 23944 AND id <=24256;"
df = pd.read_sql(query, conn)

filtered_df = df[
    (df['status'].isnull() | (df['status'] == 'null')| (df['status'] == ''))
    # (df['L_Placeholder'].isnull() | (df['L_Placeholder'] == 'null')| (df['L_Placeholder'] == ''))
]
# for know 

tender_ids = filtered_df['tender_id'].tolist()

total_entries = len(tender_ids)
print(f"Total entries where live is 'no': {total_entries}")

def split_into_parts(lst, n):
    k, m = divmod(len(lst), n)
    return [lst[i*k + min(i, m):(i+1)*k + min(i+1, m)] for i in range(n)]






















raw_text = """  
GEM/2024/B/5682036
GEM/2024/B/5524276
GEM/2024/B/5486304
GEM/2024/B/5454145
GEM/2024/B/5458604
GEM/2024/B/5367152
GEM/2024/B/5076138
GEM/2024/B/5074655
GEM/2024/B/4896619
GEM/2024/B/4530127
GEM/2024/B/4777963
GEM/2023/B/4324622
GEM/2023/B/3814969
GEM/2023/B/4047184
GEM/2023/B/3817986
GEM/2023/B/4027762
GEM/2023/B/4000787
GEM/2023/B/3896183
GEM/2023/B/4016922
GEM/2023/B/3988151
GEM/2023/B/3987994
GEM/2023/B/3960160
GEM/2023/B/3808769
GEM/2023/B/3947819
GEM/2023/B/3927153
GEM/2023/B/3927062
GEM/2023/B/3916901
GEM/2023/B/3861391
GEM/2023/B/3895981
GEM/2023/B/3895944
GEM/2023/B/3858161
GEM/2023/B/3848537
GEM/2023/B/3816284
GEM/2023/B/3816092
GEM/2023/B/3803873
GEM/2023/B/3802680
GEM/2023/B/3800180
GEM/2023/B/3785028
GEM/2023/B/3792859
GEM/2023/B/3792848
GEM/2023/B/3727364
GEM/2023/B/3741761
GEM/2023/B/3743952
GEM/2023/B/3730654
GEM/2023/B/3684037
GEM/2023/B/3713607
GEM/2023/B/3710981
GEM/2023/B/3700378
GEM/2023/B/3699453
GEM/2023/B/3695707
GEM/2023/B/3687045
GEM/2023/B/3686841
GEM/2023/B/3681107
GEM/2023/B/3669910
GEM/2023/B/3670418
GEM/2023/B/3670464
GEM/2023/B/3643054
GEM/2023/B/3668314
GEM/2023/B/3666711
GEM/2023/B/3657846
GEM/2023/B/3657529
GEM/2023/B/3654574
GEM/2023/B/3481496
GEM/2023/B/3634216
GEM/2023/B/3605192
GEM/2023/B/3566897
GEM/2023/B/3618556
GEM/2023/B/3618485
GEM/2023/B/3508857
GEM/2023/B/3589920
GEM/2023/B/3570388
GEM/2023/B/3567657
GEM/2023/B/3567015
GEM/2023/B/3585895
GEM/2023/B/3510611
GEM/2023/B/3555586
GEM/2023/B/3555535
GEM/2023/B/3552271
GEM/2023/B/3549736
GEM/2023/B/3549801
GEM/2023/B/3549605
GEM/2023/B/3542817
GEM/2023/B/3526669
GEM/2023/B/3531778
GEM/2023/B/3493200
GEM/2023/B/3529879
GEM/2023/B/3515497
GEM/2023/B/3520363
GEM/2023/B/3522419
GEM/2023/B/3509189
GEM/2023/B/3509021
GEM/2023/B/2981567
GEM/2023/B/3157094
GEM/2023/B/3394493
GEM/2023/B/3315775
GEM/2023/B/3162820
GEM/2023/B/3244935
GEM/2023/B/3214069
GEM/2023/B/3191338
GEM/2023/B/3089110
GEM/2023/B/3048825
GEM/2023/B/3058082
GEM/2023/B/3000004
GEM/2023/B/3039415
GEM/2023/B/3028357
GEM/2023/B/3009651
GEM/2023/B/2948532
GEM/2022/B/2909382
GEM/2022/B/2900742
GEM/2022/B/2811013
GEM/2022/B/2835175
GEM/2022/B/2809505
GEM/2022/B/2692023
GEM/2022/B/2622857
GEM/2022/B/2594976
GEM/2022/B/2592739
GEM/2022/B/2529473
GEM/2022/B/2524299
GEM/2022/B/2487900
GEM/2022/B/2483610
GEM/2022/B/2479705
GEM/2022/B/2455103
GEM/2022/B/2196376
GEM/2022/B/2396267
GEM/2022/B/2345581
GEM/2022/B/2374603
GEM/2022/B/2335435
GEM/2022/B/2286388
GEM/2022/B/2312540
GEM/2022/B/2274959
GEM/2022/B/2271553
GEM/2022/B/2229967
GEM/2022/B/2252791
GEM/2022/B/2201339
GEM/2022/B/2172587
GEM/2022/B/2154347
GEM/2022/B/2083691
GEM/2022/B/1921597
GEM/2022/B/1833181
GEM/2022/B/1830412
GEM/2022/B/1829593
GEM/2022/B/1829211
GEM/2022/B/1818994
GEM/2021/B/1802013
GEM/2021/B/1796153
GEM/2021/B/1796232
GEM/2021/B/1781483
GEM/2021/B/1772940
GEM/2021/B/1772594
GEM/2021/B/1740596
GEM/2021/B/1732639
GEM/2021/B/1699601
GEM/2021/B/1674452
GEM/2021/B/1676004
GEM/2021/B/1655112
GEM/2021/B/1587893
GEM/2021/B/1604831
GEM/2021/B/1509160
GEM/2021/B/1502051
GEM/2021/B/1400978
GEM/2021/B/1347323
GEM/2021/B/1344023
GEM/2021/B/1300231
GEM/2021/B/1024417
GEM/2020/B/826272
GEM/2020/B/830021
GEM/2020/B/830200
GEM/2020/B/765371
GEM/2020/B/725933
GEM/2020/B/760579
GEM/2020/B/686119
GEM/2020/B/677194
GEM/2020/B/675544
GEM/2020/B/644680
GEM/2020/B/668361
GEM/2020/B/661548
GEM/2020/B/661511
GEM/2020/B/660793
GEM/2020/B/617476
GEM/2020/B/613295
GEM/2019/B/426719
GEM/2019/B/344692
GEM/2019/B/309907
GEM/2019/B/290820
GEM/2019/B/290645
GEM/2019/B/273293
GEM/2019/B/268044
GEM/2019/B/268215
GEM/2019/B/260220
GEM/2023/B/4189006
GEM/2023/B/4143988
GEM/2023/B/4105209
GEM/2023/B/4069365
GEM/2023/B/4105343
GEM/2023/B/4116127
GEM/2023/B/4189131
GEM/2023/B/4144711
GEM/2023/B/4188965
GEM/2023/B/3685069
GEM/2023/B/4069632
GEM/2023/B/3528708
GEM/2023/B/4142035
GEM/2023/B/3757875
GEM/2023/B/3612371
GEM/2023/B/3008420
GEM/2023/B/4149925
GEM/2023/B/3187588
GEM/2023/B/3061272
GEM/2023/B/3855944
GEM/2023/B/3940295
GEM/2023/B/3630373
GEM/2023/B/4131320
GEM/2023/B/3863595
GEM/2023/B/4118376
GEM/2023/B/3675466
GEM/2023/B/3866761
GEM/2023/B/3844160
GEM/2024/B/4455173
GEM/2023/B/3161326
GEM/2023/B/3405047
GEM/2021/B/1655153
GEM/2024/B/4491191
GEM/2023/B/4017865
GEM/2023/B/3478606
GEM/2023/B/3614058
GEM/2023/B/3658007
GEM/2023/B/3613992
GEM/2023/B/3542005
GEM/2023/B/3741459
GEM/2023/B/3657873
GEM/2022/B/2556537
GEM/2022/B/2411842
GEM/2023/B/3856747
GEM/2022/B/2551581
GEM/2022/B/2320429
GEM/2022/B/2395866
GEM/2022/B/2551416
GEM/2023/B/3531563
GEM/2022/B/2457715
GEM/2022/B/2457570
GEM/2022/B/2084736
GEM/2022/B/2762603
GEM/2022/B/2093666
GEM/2022/B/2556107
GEM/2023/B/4106483
GEM/2022/B/2090779
GEM/2022/B/2260068
GEM/2022/B/2508415
GEM/2023/B/3546927
GEM/2023/B/3299466
GEM/2023/B/4058345
GEM/2023/B/3896972
GEM/2023/B/4158477
GEM/2023/B/3707596
GEM/2023/B/3830833
GEM/2022/B/2416368
GEM/2023/B/3904373
GEM/2022/B/2375937
GEM/2022/B/2401964
GEM/2022/B/2312870
GEM/2022/B/2488126
GEM/2022/B/2434670
GEM/2023/B/3722889
GEM/2023/B/3791844
GEM/2022/B/2475582
GEM/2023/B/3722447
GEM/2023/B/3586078
GEM/2023/B/4200564
GEM/2023/B/3740556
GEM/2023/B/3893099
GEM/2023/B/3723290
GEM/2022/B/2698697
GEM/2022/B/2430191
GEM/2023/B/3922552
GEM/2022/B/2435566
GEM/2023/B/3511516
GEM/2022/B/1968672
GEM/2023/B/3769542
GEM/2023/B/3021421
GEM/2023/B/3761557
GEM/2023/B/3827247
GEM/2023/B/3890734
GEM/2022/B/2536267
GEM/2022/B/2655453
GEM/2023/B/3761538
GEM/2020/B/599275
GEM/2023/B/3687612
GEM/2022/B/2872873
GEM/2023/B/3765669
GEM/2023/B/3788595
GEM/2023/B/3982827
GEM/2022/B/2475949
GEM/2023/B/4011731
GEM/2023/B/3785226
GEM/2023/B/3847509
GEM/2023/B/3929924
GEM/2022/B/2500793
GEM/2023/B/3741425
GEM/2022/B/2087105
GEM/2022/B/2416927
GEM/2023/B/4003532
GEM/2022/B/2511699
GEM/2023/B/3634182
GEM/2023/B/3662060
GEM/2022/B/2433365
GEM/2023/B/3788549
GEM/2023/B/3810110
GEM/2023/B/3732102
GEM/2023/B/3896234
GEM/2023/B/3717503
GEM/2023/B/3573617
GEM/2022/B/2479678
GEM/2023/B/3498851
"""

# tender_ids = raw_text.strip().split('\n')
tender_ids = set(tender_ids)
tender_ids = list(tender_ids)

split_arrays = split_into_parts(tender_ids, 4)


Main(split_arrays)
