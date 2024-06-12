from tkinter import *
import csv

def check_integer():
    value = entry.get()
    if value.isdigit():
        listbox.insert(END, value)
        entry.delete(0, END)
    else:
        entry.delete(0, END)

def clear_list():
    listbox.delete(0, END)

def save_to_csv():
    numbers = listbox.get(0, END)
    with open("numbers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(numbers)

root = Tk()
root.title("Integer Checker")

entry_label = Label(root, text="Enter a number:")
entry_label.pack()

entry = Entry(root)
entry.pack()

check_button = Button(root, text="Check", command=check_integer)
check_button.pack()

clear_button = Button(root, text="Clear List", command=clear_list)
clear_button.pack()

save_button = Button(root, text="Save to CSV", command=save_to_csv)
save_button.pack()

listbox = Listbox(root)
listbox.pack()

root.mainloop()