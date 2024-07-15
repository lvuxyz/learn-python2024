from tkinter import *
from googletrans import Translator
from PIL import Image, ImageTk
window = Tk()
window.title("Google dịch của Vũ đẹp trai")
window.geometry("720x480")

def phien_ra():
    chu = entry_box.get()
    t = Translator()
    translation = t.translate(chu, src="en", dest="vi")
    ket_qua = translation.text
    list_box.insert(END, ket_qua)
    entry_box.delete(0, END)

def clear():
    list_box.delete(0, END)

load = Image.open('background.png')
render = ImageTk.PhotoImage(load)
img = Label(window, image=render)
img.image = render
img.place(x=0, y=0)

entry_box = Entry()
entry_box.place(x=350, y=100)

button_an = Button(window, text="Dịch", command=phien_ra)
button_an.place(x=350, y=140, width=100, height=25)

button_xoa = Button(window, text="Clear", command=clear)
button_xoa.place(x=450, y=140, width=100, height=25)

list_box = Listbox()
list_box.place(x=350, y=170)


window.mainloop()
