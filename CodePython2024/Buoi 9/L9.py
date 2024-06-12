from tkinter import *
import csv

def display_people():
    listbox.delete(0, END)
    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, age = row
            listbox.insert(END, f"{name} ({age})")

root = Tk()
root.title("People List")

display_button = Button(root, text="Display People", command=display_people)
display_button.pack()

listbox = Listbox(root)
listbox.pack()

root.mainloop()