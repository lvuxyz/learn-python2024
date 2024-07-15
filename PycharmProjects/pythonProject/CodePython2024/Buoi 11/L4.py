from tkinter import *

window = Tk()
window.geometry("720x480")
window.title("form cua vu dz")

def add_name():
    name = entry1.get()
    gioitinh = select_name.get()
    list_box.insert(END, f"{name}", f"{gioitinh}")


label1 = Label(window, text="Enter their name: ")
label1.place(x=200, y=50)

entry1 = Entry()
entry1.place(x=300, y=50)

label2 = Label(window, text="Select Gender ")
label2.place(x=200, y=100)

select_name = StringVar(window)
select_name.set("M/F")
nameList = OptionMenu(window, select_name, "Nam", "Nu")
nameList.place(x=300, y=100)

list_box = Listbox()
list_box.place(x=300, y=150)

button_click = Button(window, text="Add a list", command=add_name)
button_click.place(x=200, y=340)

window.mainloop()
