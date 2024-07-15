import tkinter as tk
import sqlite3

window = tk.Tk()
window.title("Test Scores")
window.geometry("720x480")

conn = sqlite3.connect('TestScores.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS scores (
        name TEXT,
        score INTEGER
    )
""")

def add_score():
    name = name_entry.get()
    score = score_entry.get()
    if name and score:
        c.execute("INSERT INTO scores VALUES (?, ?)", (name, int(score)))
        conn.commit()
        name_entry.delete(0, tk.END)
        score_entry.delete(0, tk.END)

def clear_entries():
    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

def close_window():
    conn.close()
    window.destroy()

# GUI elements
name_label = tk.Label(window, text="Enter student's name:")
name_label.place(x=10, y=20)

name_entry = tk.Entry(window)
name_entry.place(x=150, y=20)

score_label = tk.Label(window, text="Enter student's grade:")
score_label.place(x=10, y=80)

score_entry = tk.Entry(window)
score_entry.place(x=150, y=80)

add_button = tk.Button(window, text="Add", command=add_score)
add_button.place(x=60, y=150)

clear_button = tk.Button(window, text="Clear", command=clear_entries)
clear_button.place(x=120, y=150)

exit_button = tk.Button(window, text="Exit", command=close_window)
exit_button.place(x=180, y=150)

window.mainloop()
