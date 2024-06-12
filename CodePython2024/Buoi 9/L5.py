from tkinter import *
def convert_miles_to_km():
    miles = float(entry.get())
    km = miles * 1.6093
    result_label.config(text=f"{miles} miles = {km:.2f} km")

def convert_km_to_miles():
    km = float(entry.get())
    miles = km * 0.6214
    result_label.config(text=f"{km} km = {miles:.2f} miles")

window = Tk()
window.title("vudz")
window.geometry("300x300")
entry_label = Label(window, text="Enter distance:")
entry_label.pack()

entry = Entry(window)
entry.pack()

miles_to_km_button = Button(window, text="Miles to Km", command=convert_miles_to_km)
miles_to_km_button.pack()

km_to_miles_button = Button(window, text="Km to Miles", command=convert_km_to_miles)
km_to_miles_button.pack()

result_label = Label(window, text="")
result_label.pack()
window.mainloop()