import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

"""cursor.execute('''CREATE TABLE Names
(ID INTEGER PRIMARY KEY,
FirstName TEXT NOT NULL,
SurName TEXT NOT NULL,
PhoneNumber TEXT)''')"""

newID = input("Nhap ID cua ban: ")
newFirstName = input("Nhap FirstName cua ban: ")
newLastName = input("Nhap Surname cua ban: ")
newPhone = input("Nhap phone cua ban: ")
cursor.execute("""INSERT INTO Names (ID, FirstName, SurName, PhoneNumber)
VALUES (?, ?, ?, ?)""", (newID, newFirstName, newLastName, newPhone))

db.commit()