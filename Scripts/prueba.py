import tkinter as tk
from PIL import Image, ImageTk
from urllib import urlopen
from io import BytesIO, StringIO

root = tk.Tk()

URL = "http://www.universeofsymbolism.com/images/ram-spirit-animal.jpg"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(StringIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tk.Label(image=photo)
label.image = photo
label.pack()

root.mainloop()