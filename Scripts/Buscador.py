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