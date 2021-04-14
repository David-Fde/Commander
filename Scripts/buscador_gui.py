import tkinter as tk
import pickle
import os

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

def find(event=None):
  name=name_var.get()
  name_var.set("")

  try:
    text.delete('1.0', tk.END)
    text.insert(tk.END, b[f"{name}"])
  except:
    text.delete('1.0', tk.END)
    text.insert(tk.END, "Card not found")

root = tk.Tk()
root.title("Mtg App")
text = tk.Text(root, width=20, height=2)
name_var=tk.StringVar()
name_label = tk.Label(root, text = 'Search: ', font=('calibre',10, 'bold'))
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = find)
root.bind('<Return>', lambda event=None: sub_btn.invoke()) # Click submit by pressing Enter using lambda to doing it continuosly.

name_label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
sub_btn.grid(row=2,column=0)
text.grid(row=3,column=1)

root.mainloop()