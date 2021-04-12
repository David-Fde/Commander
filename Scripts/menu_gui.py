import tkinter as tk
import pickle
import os

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

def find():
  name=name_var.get()
  name_var.set("")

  try:
    text.delete('1.0', tk.END)
    text.insert(tk.END, b[f"{name}"])
  except:
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Carta no encontrada")

root = tk.Tk()
root.title("Mtg App")
text = tk.Text(root)
name_var=tk.StringVar()
name_label = tk.Label(root, text = 'Busqueda: ', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = find)

name_label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)
text.grid(row=3,column=1)

root.mainloop()