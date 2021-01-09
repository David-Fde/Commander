from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import os

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://tugbucket.net/tests/salvation/mtg_sets/")
url_destino = r"..\Colecciones"
downloaded_sets = []

for e in os.listdir(url_destino):
    downloaded_sets.append(e.split(".xlsx")[0])

try:
    search_set = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "set"))
    )
except:
    driver.quit()
    
long_list = driver.find_element_by_id("longlist")
continue_button = driver.find_element_by_id("startbutton")

x = search_set.text
x = x.replace(":","")
x = x.replace("/","")

sets_list = x
sets_list = sets_list.split('\n')

for e in sets_list:
    if e not in downloaded_sets:
        search_set.send_keys(e)
        long_list.click()
        continue_button.click()
        time.sleep(10)

        elemento = driver.find_element_by_id("setJustGot")
        text = elemento.text
        text = text.split('\n')

        df = pd.DataFrame()
        try:
            df[f'{e.split(" ")[0]}'] = text
            df.to_excel(f"{url_destino}\{e}.xlsx", index=False)
        except:
            df[f'{e.split(" ")[0]}'] = text
            df.to_excel(f"{url_destino}\{e.split(' ')[-1]}.xlsx", index=False) 
        
driver.quit()