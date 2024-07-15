from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

root.title("vu dep trai hihi")
root.geometry("500x350")


my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 18))

my_label = tb.Label(text="vai lon",bootstyle = "success" )
my_label.pack(pady=10)

my_button = tb.Button(text="hello world", width=30,
                      bootstyle = "success",
                      style="success.Outline.TButton")
my_button.pack(pady=40)

root.mainloop()
