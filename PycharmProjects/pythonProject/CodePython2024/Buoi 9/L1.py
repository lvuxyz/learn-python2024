from tkinter import *
window = Tk()
window.title("vudz")
window.geometry("300x300")

def nhap_vao():
    name = entry.get()
    label_vao = Label(window, text= f"hello {name}", bg="red", fg="green")
    label_vao.place(x=150, y=80)

label_ten = Label(window, text="Enter your name: ")
label_ten.place(x=40, y=40)

entry = Entry()
entry.place(x=150, y=40)

button_nhap = Button(window, text="click here", command=nhap_vao)
button_nhap.place(x=40, y=80, width=100, height = 25)




window.mainloop()