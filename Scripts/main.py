import functions
import os

os.system("cls")
print("1. Añadir Deck a la base de datos" +"\n" + 
      "2. Actualizar Base de datos" + "\n" + 
      "3. Actualizar un set" + "\n" +
      "4. Analizar deck" + "\n" + 
      "5. Buscador de Cartas" + "\n")

respuesta = input("Opción: ")

if respuesta == "1":
    os.system("cls")
    functions.PlainTextToExcel(respuesta)
elif respuesta == "2":
    os.startfile(r"Update_Database.py")
    functions.UpdatePickleDatabase()
elif respuesta == "3":
    os.startfile(r"Update_one_set.py")
    functions.UpdatePickleDatabase()
elif respuesta == "4":
    os.startfile(r"Deck_Statistics.py")
    functions.UpdatePickleDatabase()
elif respuesta == "5":
    os.startfile(r"Buscador.py")
    functions.UpdatePickleDatabase()
else: 
    input("Pulsa para cerrar")