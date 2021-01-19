import functions
import os

os.system("cls")
print("1. Añadir Deck a la base de datos" +"\n" + 
      "2. Convertir Excel a texto plano" + "\n" +
      "3. Actualizar Base de datos" + "\n" + 
      "4. Actualizar un set" + "\n")

respuesta = input("Opción: ")

if respuesta == "1":
    os.system("cls")
    functions.PlainTextToExcel(respuesta)
elif respuesta == "2":
    functions.ExcelToPlainText()
elif respuesta == "3":
    os.startfile(r"Update_Database.py")
    functions.UpdatePickleDatabase()
elif respuesta == "4":
    os.startfile(r"Update_one_set.py")
    functions.UpdatePickleDatabase()
else: 
    input("Pulsa para cerrar")