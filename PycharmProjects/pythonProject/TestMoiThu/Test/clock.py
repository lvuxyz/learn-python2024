from tkinter import *
from tkinter.ttk import *
from time import strftime
window = Tk()
window.title("Đồng hồ của vũ dz")
def clock():
    string = strftime('%I:%M:%S:%p')
    label.config(text=string)
    label.after(1000,clock)
label=Label(window, font=("Digital-7",100), background='black', foreground='green')
label.pack(anchor='center')
clock()

window.mainloop()