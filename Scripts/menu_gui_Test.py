import tkinter as tk
import os 
import pickle
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from PIL import Image, ImageTk

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

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = bg.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)

    image_label.config(image=photo)
    image_label.image = photo  # avoid garbage collection

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

root = tk.Tk()
root.geometry("1000x500")
root.title("Mtg App")
photo = tk.PhotoImage(file = r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Scripts\Background.png")
name_var=tk.StringVar()


# Labels
image_label = tk.Label(root, image=photo)
image_label.place(x=0, y=0, relwidth=1, relheight=1)
image_label.bind('<Configure>', resize_image)

name_label = tk.Label(root, text = 'Enter Card Name: ', font=('calibre',10, 'bold'))
name_label.pack(pady=20,padx=20)
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.pack(pady=20)

frame = tk.Frame(root, relief='raised', borderwidth=2)
frame.pack(fill=tk.BOTH, expand=tk.YES)
frame.pack_propagate(False)


text = tk.Text(frame, width=120, height=10)
text.pack(pady=1)


# Buttons
actualizar_btn=tk.Button(frame,text = 'Update Database', command = Update_database)
actualizar_btn.pack(pady=20)
submit_btn=tk.Button(frame,text = 'Submit', command = Seeker)
submit_btn.pack(pady=20)
root.bind('<Return>', lambda event=None: submit_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly. 

root.mainloop()