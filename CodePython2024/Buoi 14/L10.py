from tkinter import *

window = Tk()
window.geometry("720x480")
window.configure(bg='yellow')

label_welcome = Label(window, text="WELCOME TO MY PROGRAM", font=("Arial", 30), fg='purple')
label_welcome.place(x=130, y=40)

button_view = Button(window, text="View", fg='purple', bg='violet')
button_view.place(x=50, y=200, width=100, height=25)

button_add = Button(window, text="Add", fg='purple', bg='violet')
button_add.place(x=450, y=200, width=100, height=25)

button_delete = Button(window, text="Delete", fg='purple', bg='violet')
button_delete.place(x=50, y=300, width=100, height=25)

button_update = Button(window, text="Update", fg='purple', bg='violet')
button_update.place(x=450, y=300, width=100, height=25)

button_exit = Button(window, text="Exit", fg='purple', bg='violet')
button_exit.place(x=250, y=400, width=100, height=25)

window.mainloop()
