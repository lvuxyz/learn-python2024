from tkinter import *

window = Tk()
window.geometry("720x480")
window.title("Form")

def them_vao_danh_sach():
    name = entry1.get()
    gender = select_name.get()
    full_entry = f"{name}, {gender}"
    list_box.insert(END, full_entry)
    ghi_vao_tep(full_entry)

def ghi_vao_tep(entry):
    with open("names.txt", "a") as file:
        file.write(entry + "\n")

def hien_thi_noi_dung_tep():
    with open("names.txt", "r") as file:
        content = file.read()
        print(content)

label1 = Label(window, text="Enter their name: ")
label1.place(x=200, y=50)

entry1 = Entry()
entry1.place(x=300, y=50)

label2 = Label(window, text="Select Gender ")
label2.place(x=200, y=100)

select_name = StringVar(window)
select_name.set("Male/Female")
nameList = OptionMenu(window, select_name, "Male", "Female")
nameList.place(x=300, y=100)

list_box = Listbox()
list_box.place(x=300, y=150)

button_click = Button(window, text="Add to List", command=them_vao_danh_sach)
button_click.place(x=200, y=340)

display_button = Button(window, text="Display File Content", command=hien_thi_noi_dung_tep)
display_button.place(x=350, y=340)


window.mainloop()
