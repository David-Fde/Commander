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
    search_set = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "set"))
    )
except:
    driver.quit()

for e in search_set.text:
    if e not in downloaded_sets:
        long_list = driver.find_element_by_id("longlist")

        continue_button = driver.find_element_by_id("startbutton")

        long_list.click()
        for e in search_set.text:
            if e == entrada:
                search_set.send_keys(e)
                break
        continue_button.click()

        time.sleep(10)

        elemento = driver.find_element_by_id("setJustGot")
        text = elemento.text
        text = text.split('\n')

        driver.quit()

        df = pd.DataFrame()

        df[f'{e.split(" ")[0]}'] = text
        df.to_excel(f"{url_destino}\{e.split(' ')[0]}.xlsx", index=False)