import pandas as pd
import os

PlainText_Decklists = r"..\Datos\PlainText_Decklists"
Datos = r"..\Datos"

def PlainTextToExcel(respuesta):
    if respuesta == "1":
        os.system("cls")
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
                if text[e][0] != "1":
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
    elif respuesta == "2":
        os.system("cls")
        name = input('Nombre de coleccion: ')
        url = r"..\Datos\Plain_text_new_set.txt"
        url_destino = r"..\Colecciones"
        df = pd.DataFrame()
        f = open(url,"r+")
        text = f.read()
        text = text.split('\n')
        df[f'{name}'] = text
        df.to_excel(f"{url_destino}\{name}.xlsx", index=False)
        print(f"{name} añadida a la base de datos.")
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