from tkinter import *
from PIL import Image, ImageTk
import os
import pickle

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

def Update_database():
  os.system("Update_Database.py")

def Seeker(event=None):
  name=name_var.get()
  name_var.set("")

  try:  
    search_text.delete('1.0', END)
    result = b[f"{name}"]
    for e in result:
      if len(e) > 79:
        search_text.insert(END, e.replace("'","")[:78] + "\n")
        search_text.insert(END, " " + e.replace("'","")[78:])
      else:
        search_text.insert(END, e.replace("'","") + "\n")

  except:
    search_text.delete('1.0', END)
    search_text.insert(END, "Card not found")


root = Tk()
root.title("Mtg App")
root.geometry('1000x500')
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
bottomframe.place(relx=0.17, rely=0.6, anchor=CENTER)
textframe = Frame(frame, relief='raised', borderwidth=2)
textframe.place(relx=0.34, rely=0.8, anchor=CENTER)
loading_frame = Frame(frame, relief='raised', borderwidth=2)
loading_frame.place(relx=0.1, rely=0.17, anchor=CENTER)
search_text = Text(textframe, width=79, height=10)
loading_text = Text(loading_frame, width=15, height=1)


Button(top_frame, text='Update Database', command=Update_database , width=20, height=2, bg="#fae4b3", relief=RIDGE).pack(side=TOP)
submit_btn = Button(bottomframe,text = 'Submit', command = Seeker)
Label(bottomframe, text='Enter Card Name: ', width=14).pack(side=LEFT)
entrada = Entry(bottomframe,textvariable = name_var, font=('calibre',10,'normal')).pack(side=LEFT)
root.bind('<Return>', lambda event=None: submit_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly.

search_text.pack()
loading_text.pack()
submit_btn.pack(side=RIGHT)

root.mainloop()