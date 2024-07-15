from tkinter import *
import csv

def add_person():
    name = name_entry.get()
    age = age_entry.get()
    if name and age.isdigit():
        with open("people.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, age])
        name_entry.delete(0, END)
        age_entry.delete(0, END)

root = Tk()
root.title("Add Person")

name_label = Label(root, text="Name:")
name_label.pack()

name_entry = Entry(root)
name_entry.pack()

age_label = Label(root, text="Age:")
age_label.pack()

age_entry = Entry(root)
age_entry.pack()

add_button = Button(root, text="Add", command=add_person)
add_button.pack()

root.mainloop()