import functions
import os

print("1. Convertir texto plano a Excel" +"\n" + 
      "2. Convertir Decklist a texto plano" )

respuesta = input("Opción: ")

if respuesta == "1":
    os.system("cls")
    print("1. Convertir Decklist: " + "\n" +
          "2. Convertir Colección: ")
    respuesta = input("Respuesta: ")
    functions.PlainTextToExcel(respuesta)
if respuesta == "2":
    functions.DecklistExcelToPlainText()
else: 
    input("Pulsa para cerrar")
input("Pulsa para cerrar")