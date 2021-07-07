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

contador = 0

# Tratamiento de la imagen de background
def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = background_image.resize((new_width, new_height))
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
    for widget in reimpresiones_frame1.winfo_children():
        widget.destroy()
    reimpresiones_frame1.pack_forget()
    for widget in reimpresiones_frame2.winfo_children():
        widget.destroy()
    reimpresiones_frame2.pack_forget()

# Conexion con la api de Scryfall
def Seeker(event=None):
    
    clear()
    
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
    mylist = Listbox(root, yscrollcommand = scrollbar_reimpresiones.set)
    for e in range(len(reimpresiones_json['data'])): # Recorre la longitud de la lista del número de reimpresiones de la carta
        img_reimpresion_url = reimpresiones_json['data'][e]['image_uris'].get('normal') # Obtiene la url de la imagen
        precio_eur, precio_eur_foil = (reimpresiones_json['data'][e]['prices'].get('eur'), reimpresiones_json['data'][e]['prices'].get('eur_foil')) # Obtiene los precios de la api de skcryfall           
        # ¡¡¡¡Mirar la forma dinamica de ejecutar esta parte!!!!
        if e <= 13:    
            x = Button(reimpresiones_frame1, text = reimpresiones_json['data'][e]['set_name'], command = partial(pintar_imagen, img_reimpresion_url)).pack() # Linka la url de la imagen a un boton que al clickarlo la pinta en pantalla  
            Label(reimpresiones_frame1, text=f"Eur: {precio_eur} // Eur Foil: {precio_eur_foil}").pack() # Muestra los precios debajo del boton de reimpresion
            mylist.insert(END, x)
            mylist.pack()
            scrollbar_reimpresiones.config( command = mylist.yview )
        elif e > 13 and e <= 30:
            Button(reimpresiones_frame2, text = reimpresiones_json['data'][e]['set_name'], command = partial(pintar_imagen, img_reimpresion_url)).pack() # Linka la url de la imagen a un boton que al clickarlo la pinta en pantalla  
            Label(reimpresiones_frame2, text=f"Eur: {precio_eur} // Eur Foil: {precio_eur_foil}").pack() # Muestra los precios debajo del boton de reimpresion
        elif e > 30 and e <= 46:
            Button(reimpresiones_frame3, text = reimpresiones_json['data'][e]['set_name'], command = partial(pintar_imagen, img_reimpresion_url)).pack() # Linka la url de la imagen a un boton que al clickarlo la pinta en pantalla  
            Label(reimpresiones_frame3, text=f"Eur: {precio_eur} // Eur Foil: {precio_eur_foil}").pack() # Muestra los precios debajo del boton de reimpresion
        elif e < 46:
            Button(reimpresiones_frame4, text = reimpresiones_json['data'][e]['set_name'], command = partial(pintar_imagen, img_reimpresion_url)).pack() # Linka la url de la imagen a un boton que al clickarlo la pinta en pantalla  
            Label(reimpresiones_frame4, text=f"Eur: {precio_eur} // Eur Foil: {precio_eur_foil}").pack() # Muestra los precios debajo del boton de reimpresion
        


# Definicion de los parametros de inicio de la APP  
root = tk.Tk()
root.title("Mtg App") #Titulo
root.geometry('1500x800') # Tamaño de la pantalla
#root.attributes("-fullscreen", True) # Pantalla completa sin modo ventana
root.state('zoomed') # Pantalla completa modo ventana
name_var=StringVar()
scrollbar_reimpresiones = Scrollbar(root)
frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)

# Imagen de background
background_image = Image.open(r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Images\Background.png")
photo = ImageTk.PhotoImage(background_image)

# Labels
label = Label(frame, image=photo)
label.bind('<Configure>', resize_image)

# Frames
top_frame = Frame(frame, relief='raised', borderwidth=2)
bottomframe = Frame(frame, relief='raised', borderwidth=2)
textframe = Frame(frame, relief='raised', borderwidth=2)
reimpresiones_frame1 = Frame(root, relief='raised', borderwidth=2)
reimpresiones_frame2 = Frame(root, relief='raised', borderwidth=2)
reimpresiones_frame3= Frame(root, relief='raised', borderwidth=2)
reimpresiones_frame4= Frame(root, relief='raised', borderwidth=2)

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
reimpresiones_frame1.place(relx=0.25, rely=0.4, anchor=CENTER)
reimpresiones_frame2.place(relx=0.35, rely=0.4, anchor=CENTER)
reimpresiones_frame3.place(relx=0.50, rely=0.4, anchor=CENTER)
reimpresiones_frame4.place(relx=0.60, rely=0.4, anchor=CENTER)
exit_button.place(relx=0.95, rely=0.95, anchor=CENTER)
submit_btn.pack(side=RIGHT)

# Inicia la APP
root.mainloop()