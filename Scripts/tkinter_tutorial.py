import tkinter
window = tkinter.Tk()

# to rename the title of the window
window.title("GUI")

# pack is used to show the object in the window
#label = tkinter.Label(window, text = "Hello World!", font=("Arial Bold",20)).pack()

txt = tkinter.Entry(window,width=10)
txt.grid(column=1,row=0)

def clicked():
  res = "Welcome to " + txt.get()
  tkinter.Label.configure(text=res)

bt = tkinter.Button(window, text="Enter", command=clicked)
bt.grid(column=2,row=0)

window.geometry("350x200")

window.mainloop()