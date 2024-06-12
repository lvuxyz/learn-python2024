from tkinter import *

window = Tk()
window.title('Hello World')
window.geometry('800x800')
anh = PhotoImage(file="vu.png")
label_anh = Label(window, image=anh)
label_anh.place(x=200, y=220)

def show_ten():
    name = name_entry.get()
    entry_show.delete(0, END)
    entry_show.insert(0, f"Hello, {name}!")

name_entry = Entry()
name_entry.place(x=30, y=200)

entry_show = Entry(window)
entry_show.place(x=30, y=250)

button = Button(window, text="Press Me", command=show_ten)
button.place(x=30, y=170)

window.mainloop()
