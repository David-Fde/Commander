import functions
import os

os.system("cls")
print("1. Convertir texto plano a Excel" +"\n" + 
      "2. Convertir Excel a texto plano" )

respuesta = input("Opción: ")

if respuesta == "1":
    os.system("cls")
    print("1. Convertir Decklist: " + "\n" +
          "2. Convertir Colección: ")
    respuesta = input("Respuesta: ")
    functions.PlainTextToExcel(respuesta)
elif respuesta == "2":
    functions.ExcelToPlainText()
else: 
    input("Pulsa para cerrar")