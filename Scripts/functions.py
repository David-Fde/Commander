import pandas as pd
import os

PlainText_Decklists = r"..\Datos\PlainText_Decklists"
Datos = r"..\Datos"


# https://tugbucket.net/tests/salvation/mtg_sets/ Pagina para descargar las colecciones en texto plano.

def PlainTextToExcel(respuesta):
    if respuesta == "1":
        os.system("cls")
        lista = os.listdir(PlainText_Decklists)
        contador = 1
        for e in lista:
            print(f"Opción{contador}: {e}")
            contador += 1
        opcion = int(input("Opción: ")) -1
        df = pd.read_excel(f"{Datos}\Decklists.xlsx", header=None)
        f = open(PlainText_Decklists + f"\{lista[opcion]}","r+")
        text = f.read()
        text = text.splitlines()
        for e in range(len(text)):
            text[e] = text[e].rstrip()
            if text[e][0] != "1":
                contador = 0
                while contador < int(text[e][0]):
                    text.append(f"1 {text[e][2:]}")
                    contador += 1
                text.remove(text[e])
        df[f"lista[{opcion}].split('.')[0]"] = text
        df.to_excel(f"{Datos}\Decklists.xlsx", index=False)
        input("Press enter to close")
    return


'''    name = input('Nombre de coleccion: ')
    url = r"..\Datos\Plain_text_new_set.txt"
    url_destino = r"..\Colecciones"'''
 

def DecklistExcelToPlainText():
    column = [str(input("Nombre del Comandante: "))]
    Excel_Decklists = f"{Datos}\Decklists.xlsx"
    df = pd.read_excel(Excel_Decklists, usecols=column)
    lista = []
    lista.append(column[0])
    for e in df[column[0]]:
        lista.append(e)
    with open(PlainText_Decklists + f"\{column[0]}.txt", "w") as output:
        for item in lista:
            output.write(str(item))
            output.write("\n")
    return