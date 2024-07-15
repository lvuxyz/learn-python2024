from tkinter import*
import random
window = Tk()
window.geometry("300x300")

def nhap_so():
    so = random.randint(1,6)
    label_random.config(text=f"so ra random la {so}", bg="red")

label_random = Label(window, text="")
label_random.place(x=50, y=100)

button = Button(window, text="Roll", command=nhap_so)
button.place(x=50, y=50, width=100, height=25)

window.mainloop()