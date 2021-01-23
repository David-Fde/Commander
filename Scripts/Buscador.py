import pickle
import os

contador = "Y"

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

while contador == "Y":

    entrada = str(input("Busqueda: "))
    print("\n")
    print(b[f"{entrada}"])
    print("\n")
    contador = str(input("¿Buscar otra carta? Y/N  "))
    os.system("cls")