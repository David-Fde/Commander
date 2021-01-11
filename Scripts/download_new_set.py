from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os

PATH = r"C:\Program Files (x86)\chromedriver.exe" # Path to chrome driver, needed for use selenium in chrome.
driver = webdriver.Chrome(PATH)
driver.get("https://tugbucket.net/tests/salvation/mtg_sets/")
driver2 = webdriver.Chrome(PATH)
driver2.get("https://scryfall.com/sets")
url_destino = r"..\Colecciones"
new_list = []
downloaded_sets = []
newest_sets = []
numbers = [1,16,31,46] # This list is to get the 4 newest sets from skryfall, the data got from skryfall has a set name each 15 positions.

for e in os.listdir(url_destino): # Make a list with the allready downloaded sets in the folder.
    downloaded_sets.append(e.split(".xlsx")[0])

search_set2 = driver2.find_element_by_id("js-checklist") # Goes to skryfall and get a list of all sets ordered by date.
for e in search_set2.text.split("\n"):
    try:
        new_list.append(e)
    except:
        pass
driver2.quit()

for x,y in enumerate(new_list): # Filter the skryfall set list to only keep the 6 newest sets.
    if x in numbers:
        newest_sets.append(y)

try: # Wait until there is a set displayed in tgbucket.
    search_set = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "set"))
    )
except:
    driver.quit()
    
long_list = driver.find_element_by_id("longlist")
continue_button = driver.find_element_by_id("startbutton")

# Get rid of non accepted icons.
x = search_set.text
x = x.replace(":","")
x = x.replace("/","")
sets_list = x
sets_list = sets_list.split('\n')

for e in range(len(newest_sets)): # Get rid of non accepted icons.
    newest_sets[e] = newest_sets[e].replace(":","")
    newest_sets[e] = newest_sets[e].replace("/","")

for e in sets_list: # Get a new set only if it is not in the downloaded_sets folder or if it is one of the 4 newest sets.
    if e not in downloaded_sets or e.split("(")[0][:-1] in newest_sets:
        search_set.send_keys(e)
        long_list.click()
        continue_button.click()
        time.sleep(10)

        elemento = driver.find_element_by_id("setJustGot")
        text = elemento.text
        text = text.split('\n')

        df = pd.DataFrame()
        try:
            df[f'{e}'] = text
            df.to_excel(f"{url_destino}\{e}.xlsx", index=False)
        except:
            df[f'{e.split(" ")[0]}'] = text
            df.to_excel(f"{url_destino}\{e.split(' ')[-1]}.xlsx", index=False) # Export the new set to excel.
        
driver.quit()
