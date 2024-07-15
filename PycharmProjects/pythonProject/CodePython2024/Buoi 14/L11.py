from tkinter import *
import sqlite3

window = Tk()
window.geometry("400x200")
window.title("Login")

def save_to_database():
    id_name = entry_id.get()
    password = entry_pass.get()

    conn = sqlite3.connect('Login.db')
    cursor = conn.cursor()

    # Creating table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS login_data
                    (id_name TEXT PRIMARY KEY, password TEXT)''')

    # Inserting data into the table
    cursor.execute('''INSERT INTO login_data (id_name, password)
                    VALUES (?, ?)''', (id_name, password))

    conn.commit()
    conn.close()

def exit_login():
    window.destroy()

label_login = Label(window, text="Login")
label_login.place(x=150, y=10)

label_id = Label(window, text="ID Name: ")
label_id.place(x=10, y=40)

label_pass = Label(window, text="Password: ")
label_pass.place(x=10, y=80)

entry_id = Entry(window)
entry_id.place(x=100, y=40)

entry_pass = Entry(window, show="*")
entry_pass.place(x=100, y=80)

login_button = Button(window, text="Login", command=save_to_database)
login_button.place(x=180, y=120)

login_exit = Button(window, text="Exit", command=exit_login)
login_exit.place(x=100, y=120)

window.mainloop()
