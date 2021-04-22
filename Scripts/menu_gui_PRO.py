import tkinter as tk
import os 
import pickle
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from PIL import Image, ImageTk

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

root = tk.Tk()
root.title("Mtg App")
topframe = tk.Frame(root)
middleframe = tk.Frame(root)
bottomframe = tk.Frame(root)
text = tk.Text(bottomframe, width=120, height=10)
name_var=tk.StringVar()

def Update_database():
  os.system("Update_Database.py")

def Seeker(event=None):
  name=name_var.get()
  name_var.set("")

  try:  
    text.delete('1.0', tk.END)
    result = b[f"{name}"]
    for e in result:
      text.insert(tk.END, e + "\n")
    
  except:
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Card not found")

# Labels
name_label = tk.Label(middleframe, text = 'Enter Card Name: ', font=('calibre',10, 'bold'))
name_entry = tk.Entry(middleframe,textvariable = name_var, font=('calibre',10,'normal'))

# Buttons
actualizar_btn=tk.Button(topframe,text = 'Update Database', command = Update_database)
submit_btn=tk.Button(middleframe,text = 'Submit', command = Seeker)
root.bind('<Return>', lambda event=None: submit_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly.

# Background

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    label.config(image=photo)
    label.image = photo  # avoid garbage collection

frame_image = tk.Frame(root, relief='raised', borderwidth=2)
frame_image.pack(fill=tk.BOTH, expand=tk.YES)
frame_image.pack_propagate(False)

copy_of_image = Image.open(r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Scripts\Background.png")
photo = ImageTk.PhotoImage(copy_of_image)

label = tk.Label(frame_image, image=photo)
label.place(x=0, y=0, relwidth=1, relheight=1)
label.bind('<Configure>', resize_image)

# Pack
topframe.pack(side=TOP)
middleframe.pack()
bottomframe.pack()
actualizar_btn.pack(side=LEFT)
name_label.pack(side=LEFT)
name_entry.pack(side=LEFT)
submit_btn.pack(side=LEFT)
text.pack(side=BOTTOM)

root.geometry("1100x250")

root.mainloop()