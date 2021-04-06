import functions
import os
import pandas as pd
import os
import pickle

PlainText_Decklists = r"..\Datos\PlainText_Decklists"
Datos = r"..\Datos"

def PlainTextToExcel():
    lista = os.listdir(PlainText_Decklists)
    contador = 1
    for e in lista:
        print(f"Opción{contador}: {e}")
        contador += 1
    opcion = int(input("Opción: "))
    opcion -= 1
    df = pd.read_excel(f"{Datos}\Decklists.xlsx", header=0)
    f = open(PlainText_Decklists + f"\{lista[opcion]}","r+")
    text = f.read()
    text = text.splitlines()
    if text[0][1] == " ":
        for e in range(len(text)):
            text[e] = text[e].rstrip()
            if text[e][0] != "1" or text[e][0] != 1:
                contador = 0
                while contador < int(text[e][0]):
                    text.append(f"1 {text[e][2:]}")
                    contador += 1
                text.remove(text[e])
        for e in range(len(text)):
            text[e] = text[e][2:]
    df[lista[opcion][:-4]] = text
    df.to_excel(f"{Datos}\Decklists.xlsx", index=False)
    input("Pulsa una tecla para cerrar")
    return

 

def ExcelToPlainText():
    column = [str(input("Nombre del Comandante: "))]
    Excel_Decklists = f"{Datos}\Decklists.xlsx"
    df = pd.read_excel(Excel_Decklists, usecols=column)
    if column in df.columns:
        lista = []
        lista.append(column[0])
        for e in df[column[0]]:
            lista.append(e)
        with open(PlainText_Decklists + f"\{column[0]}.txt", "w") as output:
            for item in lista:
                output.write(str(item))
                output.write("\n")
    return




def UpdatePickleDatabase():
    Mtg_Database = {}
    decklist = pd.read_excel(r"..\Datos\Decklists.xlsx")
    database = pd.DataFrame()
    columnas = []
    lista_total = []

    for filename in os.listdir(r"..\Datos\Database by set\Set with text box\Xlsx sets"):
        if filename.endswith(".xlsx"):
            df2 = pd.read_excel(f"..\Datos\Database by set\Set with text box\Xlsx sets\{filename}")
        database = pd.concat([database,df2], axis=1)

    database = database.fillna(0)

    for e in database.columns:
        columnas.append(e)

    for columna in columnas:
        for ind in database.index:
            if database[f'{columna}'][ind] != 0:
                lista_total.append(database[f'{columna}'][ind])

    for e in lista_total:
        key = e.split("[")[0][2:].split("',")[0].strip()
        value = e.split("[")[1][:-2].split("',")
        if key[-1] == ",":
            Mtg_Database.update({key[:-2]:value})
        else:
            Mtg_Database.update({key:value})

    with open(r'..\Datos\Mtg_Database.pickle', 'wb') as handle: # Save mtg Database in .pickle format.
        pickle.dump(Mtg_Database, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
        
def menu():
    os.system("cls")
    print("1. Actualizar Base de datos" + "\n" + 
          "2. Buscador de Cartas" + "\n"
          "3. Salir" + "\n"
          )

    respuesta = input("Opción: ")
    
    return respuesta

def answer_menu(respuesta):
    lista_respuestas = ["1","2"]
    while respuesta in lista_respuestas:
        if respuesta == "1":
            os.startfile(r"Update_Database.py")
            functions.UpdatePickleDatabase()
        elif respuesta == "2":
            os.startfile(r"Buscador.py")
            functions.UpdatePickleDatabase()
        elif respuesta == "3":
            exit()
def update_database():
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
    set_by_name = r"..\Datos\Database by set\Set by name"
    set_with_text_box = r"..\Datos\Database by set\Set with text box"
    new_list = []
    downloaded_sets = []
    newest_sets = []
    json_database = {}
    numbers = [1,16,31,46,61,76] # This list is to get the 6 newest sets from skryfall, the data got from skryfall has a set name each 15 positions.

    for e in os.listdir(r"..\Datos\Database by set\Set with text box\Xlsx sets"): # Make a list with the allready downloaded sets in the folder.
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

    def Datadownload(entrada, url):
        for e in sets_list: 
            if e not in downloaded_sets or e.split("(")[0][:-1] in newest_sets: # Get a new set only if it is not in the downloaded_sets folder or if it is one of the 4 newest sets.
                search_set.send_keys(e)
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

    Datadownload(long_list, set_by_name)
    Datadownload(text_spoiler, set_with_text_box)

    driver.quit()

def buscador():
    import pickle
    import os

    lista = ["Y","y","S","s","Yes","Si","yes","si"]

    check = "Y"

    with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
        b = pickle.load(handle)

    while check in lista:

        entrada = str(input("Busqueda: "))
        print("\n")
        try:
            print(b[f"{entrada}"])
        except:
            print("Carta no encontrada")
        print("\n")
        check = str(input("¿Buscar otra carta? Y/N  "))
        os.system("cls")
        
    else:
        exit()

respuesta = ""

while respuesta != "3":
    if respuesta == "1" or respuesta == "2":
        answer_menu(respuesta)        
    else:
        respuesta = menu()
