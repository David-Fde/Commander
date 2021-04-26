# Import module
from tkinter import *

def resize_image(event):
    new_width = event.width
    new_height = event.height

    image = bg.resize((new_width, new_height))
    photo = PhotoImage(image)

    label1.config(image=photo)
    label1.image = photo  # avoid garbage collection

# Create object
root = Tk()

# Adjust size
root.geometry("1000x500")

# Add image file
bg = PhotoImage(file = r"C:\Users\dfernandez\Documents\Proyectos_Python\Commander\Scripts\Background.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0, relwidth=1, relheight=1)
label1.bind('<Configure>', resize_image)

label2 = Label( root, text = "Welcome")
label2.pack(pady = 50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )

# Add buttons
button1 = Button(frame1,text="Exit")
button1.pack(pady=20)

button2 = Button( frame1, text = "Start")
button2.pack(pady = 20)

button3 = Button( frame1, text = "Reset")
button3.pack(pady = 20)

# Execute tkinter
root.mainloop()
