from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os
import pyautogui
import functions

PATH = r"C:\Program Files (x86)\chromedriver.exe" # Path to chrome driver, needed for use selenium in chrome.
driver = webdriver.Chrome(PATH)
driver.get("https://tugbucket.net/tests/salvation/mtg_sets/")
set_by_name = r"..\Datos\Database by set\Set by name"
set_with_text_box = r"..\Datos\Database by set\Set with text box"
json_database = {}

#pyautogui.hotkey('win', 'm') # Minimize all windows.

try: # Wait until there is a set displayed in tgbucket.
    search_set = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "set"))
    )
except:
    driver.quit()
    
long_list = driver.find_element_by_id("longlist")
text_spoiler = driver.find_element_by_id("spoilerlist")
continue_button = driver.find_element_by_id("startbutton")
set_to_update = str(input("Nombre de la colección: "))
search_set.send_keys(set_to_update)

# Get rid of non accepted icons.
def DeleteNonAcceptedIcons(x):
    x = x.replace(":","")
    x = x.replace("/","")
    return x

set_to_update = DeleteNonAcceptedIcons(set_to_update)
sets_list = DeleteNonAcceptedIcons(search_set.text)
sets_list = sets_list.split('\n')

def Datadownload(entrada, url, set_to_update):
    for e in sets_list: 
        if e == set_to_update: # Get a new set only if matches the input.
            entrada.click()
            continue_button.click()
            time.sleep(10)
            df = pd.DataFrame()
            
            if entrada == long_list:
                elemento = driver.find_element_by_id("setJustGot")
                text = elemento.text
                text = text.split('\n')

                try:
                    df[f'{e}'] = text
                    df.to_excel(f"{url}\Xlsx sets\{e}.xlsx", index=False) # Export the new set to excel.
                    df.to_csv(f"{url}\Txt sets\{e}.txt", header=None, index=None) # Export the new set to txt.
                except:
                    df[f'{e.split(" ")[0]}'] = text
                    df.to_excel(f"{url}\Xlsx sets\{e.split(' ')[-1]}.xlsx", index=False) # Export the new set to excel.
                    df.to_csv(f"{url}cc\{e.split(' ')[-1]}.txt", header=None, index=None) # Export the new set to txt.

            elif entrada == text_spoiler:
                try:
                    elemento = driver.find_element_by_class_name("text-grid-inner")
                    text = elemento.text
                    text = text.split('\n')
                    dictionary = {}
                    
                    for grq in elemento.find_elements_by_class_name("grq"):
                        dictionary.update({(grq.text.split("\n")[0]) : grq.text.split("\n")[1:]})
                    df[f"{e}"] = dictionary.items()
                    df.to_excel(f"{url}\Xlsx sets\{e}.xlsx", index=False) # Export the new set to excel.
                    df.to_csv(f"{url}\Txt sets\{e}.txt", header=None, index=None) # Export the new set to txt.
                except:
                    pass

    functions.UpdatePickleDatabase()
                
Datadownload(long_list, set_by_name, set_to_update)
Datadownload(text_spoiler, set_with_text_box, set_to_update)

driver.quit()