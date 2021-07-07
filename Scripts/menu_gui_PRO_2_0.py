from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk 
from PIL.ImageTk import PhotoImage
import os
import pickle
import functions
import time
import requests
import urllib
import io
from functools import partial # Permite pasar al command de un boton una funcion personalizada

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    database = pickle.load(handle)

# Tratamiento de la imagen de background
def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

# Tratamiento de la imagen obtenida desde la url
def ImgFromUrl(url):
    global image
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((300, 400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    return image

def pintar_imagen(url, event=None):
    panel = Label(frame, relief='raised', borderwidth=2, image=ImgFromUrl(url), compound=None) # Muestra la imagen de la carta elegida por pantalla
    panel.place(relx=0.111, rely=0.4, anchor=CENTER)

def clear():
    for widget in reimpresiones_frame.grid_slaves():
        widget.destroy()

# Conexion con la api de Scryfall
def Seeker(event=None):
    test_frame=reimpresiones_frame.grid_slaves()

    print(test_frame != "")
    print(type(test_frame))
    if reimpresiones_frame.grid_slaves() != "":
        for widget in reimpresiones_frame.grid_slaves():
            widget.destroy()
        reimpresiones_frame.pack_forget()   

    name=name_var.get()
    name_var.set("")
    url = "https://api.scryfall.com/cards/named?fuzzy=" + name.replace(" ","+") # Obtiene la url de la carta introducida por el usuario

    # Pintar Imagen
    r = requests.get(url) # Obtiene los datos desde Scryfall
    imagen_url = r.json().get('image_uris').get('normal') # Busca en los json la url de la imagen de la carta introducida por el usuario
    pintar_imagen(imagen_url)

    # Reimpresiones
    reimpresiones_url = r.json()['prints_search_uri']
    reimpresiones_json = requests.get(reimpresiones_url).json()
    posy = 0.0
    for e in range(len(reimpresiones_json['data'])):
        posy += 0.03
        img_reimpresion_url = reimpresiones_json['data'][e]['image_uris'].get('normal')
        Button(reimpresiones_frame, text = reimpresiones_json['data'][e]['set_name'], command = partial(pintar_imagen, img_reimpresion_url)).pack()  

# Definicion de los parametros de inicio de la APP  
root = tk.Tk()
root.title("Mtg App") #Titulo
root.geometry('1200x700') # Tamaño de la pantalla
#root.attributes("-fullscreen", True) # Pantalla completa
name_var=StringVar()
frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

# Imagen de background
copy_of_image = Image.open(r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Scripts\Background.png")
photo = ImageTk.PhotoImage(copy_of_image)

# Labels
label = Label(frame, image=photo)
label.bind('<Configure>', resize_image)

# Frames
top_frame = Frame(frame, relief='raised', borderwidth=2)
bottomframe = Frame(frame, relief='raised', borderwidth=2)
textframe = Frame(frame, relief='raised', borderwidth=2)
reimpresiones_frame = Frame(frame, relief='raised', borderwidth=2)

# Botones
submit_btn = Button(bottomframe, text = 'Submit', command = Seeker)
Label(bottomframe, text='Search for a Card: ', width=14, height=2).pack(side=LEFT)
entrada = Entry(bottomframe,textvariable = name_var, font=('calibre',10,'normal')).pack(side=LEFT)
root.bind('<Return>', lambda event=None: submit_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly.
exit_button = Button(frame, text="Exit", width=10, command=root.destroy)

#Posicion de los elementos
label.place(x=0, y=0, relwidth=1, relheight=1)
top_frame.place(relx=0.1, rely=0.1, anchor=CENTER)
bottomframe.place(relx=0.111, rely=0.1, anchor=CENTER)
textframe.place(relx=0.34, rely=0.8, anchor=CENTER)
reimpresiones_frame.place(relx=0.25, rely=0.4, anchor=CENTER)
exit_button.place(relx=0.95, rely=0.95, anchor=CENTER)
submit_btn.pack(side=RIGHT)

# Inicia la APP
root.mainloop()