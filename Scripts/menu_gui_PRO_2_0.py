from tkinter import *
from PIL import Image, ImageTk 
from PIL.ImageTk import PhotoImage
import os
import pickle
import functions
import time
import requests
import urllib
import io

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    database = pickle.load(handle)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

def ImgFromUrl(url):
    global image
    with urllib.request.urlopen(url) as connection:
        raw_data = connection.read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((300, 400), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(im)
    return image

def Seeker(event=None):
  name=name_var.get()
  name_var.set("")
  url = "https://api.scryfall.com/cards/named?fuzzy=" + name.replace(" ","+")
  r = requests.get(url)
  imagen_url = r.json().get('image_uris').get('normal')
  panel = Label(frame, relief='raised', borderwidth=2, image=ImgFromUrl(imagen_url), compound=None)
  panel.place(relx=0.111, rely=0.4, anchor=CENTER)
  
root = Tk()
root.title("Mtg App")
root.geometry('1200x700')
root.attributes("-fullscreen", True)
name_var=StringVar()
frame = Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=BOTH, expand=YES)
frame.pack_propagate(False)


copy_of_image = Image.open(r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Scripts\Background.png")
photo = ImageTk.PhotoImage(copy_of_image)

label = Label(frame, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

top_frame = Frame(frame, relief='raised', borderwidth=2)
top_frame.place(relx=0.1, rely=0.1, anchor=CENTER)
bottomframe = Frame(frame, relief='raised', borderwidth=2)
bottomframe.place(relx=0.111, rely=0.1, anchor=CENTER)
textframe = Frame(frame, relief='raised', borderwidth=2)
textframe.place(relx=0.34, rely=0.8, anchor=CENTER)


submit_btn = Button(bottomframe, text = 'Submit', command = Seeker)
Label(bottomframe, text='Search for a Card: ', width=14, height=2).pack(side=LEFT)
entrada = Entry(bottomframe,textvariable = name_var, font=('calibre',10,'normal')).pack(side=LEFT)
root.bind('<Return>', lambda event=None: submit_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly.
exit_button = Button(frame, text="Exit", width=10, command=root.destroy)
exit_button.place(relx=0.95, rely=0.95, anchor=CENTER)

submit_btn.pack(side=RIGHT)

root.mainloop()