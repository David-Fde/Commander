from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
import pyautogui
import pickle

PATH = r"C:\Program Files (x86)\chromedriver.exe" # Path to chrome driver, needed for use selenium in chrome.
driver = webdriver.Chrome(PATH)
driver.get("https://tugbucket.net/tests/salvation/mtg_sets/")
driver2 = webdriver.Chrome(PATH)
driver2.get("https://scryfall.com/sets")
set_by_name = r"..\Datos\Database by set\Set by name"
set_with_text_box = r"..\Datos\Database by set\Set with text box"
skryfall_list = []
newest_sets = []
pickle_database = {}
sets_database = []
numbers = [1,16,31,46] # This list is to get the 4 newest sets from skryfall, the data got from skryfall has a set name each 15 positions.
with open(r'..\Datos\downloaded_sets.txt', 'rb') as handle:
    sets_database = pickle.load(handle)
pyautogui.hotkey('win', 'm') # Minimize all windows.

search_set2 = driver2.find_element_by_id("js-checklist") # Goes to skryfall and get a list of all sets ordered by date.
for e in search_set2.text.split("\n"):
    try:
        skryfall_list.append(e)
    except:
        pass
driver2.quit()
    
for x,y in enumerate(new_list): # Filter the skryfall set list to only keep the 6 newest sets.
    if x in numbers:
        newest_sets.append(y)
        
for e in newest_sets:
    if e not in sets_database:
        sets_database.append(e)
        with open(r'..\Datos\downloaded_sets.txt', 'wb') as fp:
            pickle.dump(sets_database, fp)
try: # Wait until there is a set displayed in tgbucket.
    search_set = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "set"))
    )
except:
    driver.quit()
    
text_spoiler = driver.find_element_by_id("spoilerlist")
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
for x,y in enumerate(skryfall_list): # Filter the skryfall set list to only keep the 6 newest sets.
    if x in numbers:
        newest_sets.append(y)
sets_database = [] # Borrar despues de ejecutar (Sirve para rellenar la base la primera vez)
for e in sets_list: # Get a new set only if it is not in the downloaded_sets folder or if it is one of the 4 newest sets.
    if e not in sets_database: #or e in newest_sets
        search_set.send_keys(e)
        text_spoiler.click()
        continue_button.click()
        time.sleep(10)
        try:
            elemento = driver.find_element_by_class_name("text-grid-inner")
            text = elemento.text
            text = text.split('\n')      

            for grq in elemento.find_elements_by_class_name("grq"):
                pickle_database.update({(grq.text.split("\n")[0]) : grq.text.split("\n")[1:]}) 
        except:
            pass

with open(r'..\Datos\pickle_database.pickle', 'wb') as handle:
    pickle.dump(pickle_database, handle, protocol=pickle.HIGHEST_PROTOCOL) # Se guarda toda la base de datos en formato .pickle

driver.quit()