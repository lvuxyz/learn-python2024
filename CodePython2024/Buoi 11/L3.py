from tkinter import *

window = Tk()
window.geometry("720x480")
window.title("form cua vu dz")

def doi_mau():
    mau = select_name.get()
    if mau == "Blue":
        window.configure(background="blue")
    elif mau == "Red":
        window.configure(background="red")
    elif mau == "Yellow":
        window.configure(background="yellow")
    elif mau == "Black":
        window.configure(background="black")
    elif mau == "Green":
        window.configure(background="green")

select_name = StringVar(window)
select_name.set("Chon mau sac")
nameList = OptionMenu(window, select_name, "Blue", "Red", "Yellow", "Black", "Green")
nameList.place(x=340, y=120)

button_click = Button(window, text="Click to do", command=doi_mau)
button_click.place(x=340, y=240)

window.mainloop()
