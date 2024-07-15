from tkinter import *

window = Tk()
window.title("Variable")
window.geometry("720x480")

def check_number():
    number = entry_box.get()
    if number.isdigit():
        list_box.insert(END, number)
        entry_box.delete(0, END)
    else:
        entry_box.delete(0, END)

def clear_listbox():
    list_box.delete(0, END)

label_enter = Label(window, text="Enter a number: ")
label_enter.place(x=10, y=20)

label_list = Label(window, text="List: ")
label_list.place(x=10, y=60)

entry_box = Entry()
entry_box.place(x=150, y=20)

list_box = Listbox()
list_box.place(x=150, y=60)

button_add = Button(window, text="Add to List", command=check_number)
button_add.place(x=350, y=20)

button_clear = Button(window, text="Clear List", command=clear_listbox)
button_clear.place(x=350, y=60)

window.mainloop()
