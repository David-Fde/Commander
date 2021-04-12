import tkinter as tk
import pickle
import os

with open(r'..\Datos\Mtg_Database.pickle', 'rb') as handle:
    b = pickle.load(handle)

def find():
  name=name_var.get()
  name_var.set("")
  
  text.insert('1.0', name) 
  text.pack(side=tk.BOTTOM)
  

#to create a window
root = tk.Tk()

root.geometry("600x400")

name_var=tk.StringVar()

#root window is the parent window
fram = tk.Frame(root)

name_label = tk.Label(fram,text='Busqueda:').pack(side=tk.LEFT)

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))


#adding of single line text box
edit = tk.Entry(fram) 
  
#positioning of text box
edit.pack(side=tk.LEFT, fill=tk.BOTH, expand=1) 
  
#setting focus
edit.focus_set() 
  
#adding of search button
butt = tk.Button(fram, text='Find')  
butt.pack(side=tk.RIGHT) 
fram.pack(side=tk.TOP)

#text box in root window
text = tk.Text(root) 

butt.config(command=find)

root.mainloop()

