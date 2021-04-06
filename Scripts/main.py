import functions
import os

respuesta = ""

while respuesta != "3":
    if respuesta == "1" or respuesta == "2":
        os.startfile(r"App.bat")
        functions.answer_menu(respuesta)        
    else:
        respuesta = functions.menu()