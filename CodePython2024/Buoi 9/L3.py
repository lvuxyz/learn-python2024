from tkinter import *
window = Tk()
window.geometry("500x500")

total = 0
def tinh_tong():
    global total
    so = int(entry1.get())
    total += so
    entry2.delete(0, END)
    entry2.insert(0, f"{total}")
    entry1.delete(0, END)
def clear_di():
    global total
    total = 0
    entry2.delete(0,END)
    entry2.insert(0, "")


label1 = Label(window, text="Enter a numbers: ")
label1.place(x=10, y=40)

label2 = Label(window, text="Answer = ")
label2.place(x=10, y=80)

entry1 = Entry()
entry1.place(x=150, y=40)

entry2 = Entry()
entry2.place(x=150, y=80)

button_add = Button(window, text="Add", command=tinh_tong)
button_add.place(x=300, y=40)

button_clear = Button(window, text="Clear", command=clear_di)
button_clear.place(x=300, y=80)
window.mainloop()
