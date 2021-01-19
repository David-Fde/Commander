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