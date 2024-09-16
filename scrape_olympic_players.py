from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

def get_data(driver, all_player_set):
    try:
        print("-----Scrapping Data-----")
        player_details = []
        all_players = driver.find_elements(By.CLASS_NAME, "emotion-srm-1xycdp4")
        for item in all_players:
            print("Extractimg Items")
            all_player_set.add(item.text)
        print(all_player_set)
        for player in all_player_set:
            player_list = player.split("\n")
            player_details.append(player_list)
        return player_details
    except Exception as e:
        print(e)

# Initialize the web driver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://olympics.com/en/paris-2024")
time.sleep(5)

button = driver.find_element(By.XPATH, '//button[text()="Yes, I am happy"]')
button.click()

print("Cookei accepted")

# Go to the medals page
try:
    main_div = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hxilJZ")))
except Exception as e:
    print(e)
try:
    parent_nav = main_div.find_element(By.TAG_NAME,"nav")
    # print(parent_nav)
except Exception as e:
    print(e)

try:
    child_navs = parent_nav.find_elements(By.TAG_NAME,"nav")
    # print(child_navs)
except Exception as e:
    print(e)

for nav in child_navs:
    anchors = nav.find_elements(By.TAG_NAME, "a")
    for anchor in anchors:
        print(anchor.text)
        if 'MEDAL TABLE' in anchor.text:
            anchor.click()
            break

anchor = driver.find_element(By.LINK_TEXT, "MEDALLISTS")
anchor.click()
driver.maximize_window()

time.sleep(5)

# Scrape the data
details = []
all_player_set = set()

# Scrolling the page
total_hight = 137184
scroll_hight = 500
current_scroll = 0
while current_scroll < total_hight:
    res = get_data(driver, all_player_set)
    # details.append(res)
    details.extend([item for item in res if item not in details])
    driver.execute_script(f"window.scrollBy(0,{scroll_hight})","")
    current_scroll += scroll_hight
    time.sleep(5)

# Close the driver
driver.close()

# Creating thecsv file
columns = ["Country","Player Name","Gold","Silver","Bronze","Total Medals"]
df = pd.DataFrame(details, columns = columns)
df.to_csv("Olympic_players_data.csv", index=False)
 