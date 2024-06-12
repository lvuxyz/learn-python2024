from tkinter import *
window = Tk()
window.title("vudz")
window.geometry("700x400")

def them_ten():
    ten = entry_ten.get()
    listbox.insert(END, ten)
    entry_ten.delete(0, END)

def clear():
    listbox.delete(0, END)

label_nhapten = Label(window, text="Hay nhap ten cua may vao day")
label_nhapten.place(x=20, y= 40)

entry_ten = Entry()
entry_ten.place(x=200, y=40)

button_add = Button(window, text="add", command=them_ten)
button_add.place(x=400, y=40)
button_clear = Button(window, text="clear", command=clear)
button_clear.place(x=400, y=80)

listbox = Listbox()
listbox.place(x=500, y=40)
window.mainloop()