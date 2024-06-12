import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

"""cursor.execute('''CREATE TABLE BookInfo
(Name TEXT NOT NULL,
PlaceOfBirth TEXT)''')
"""

newName = input("Nhap name cua ban: ")
newPlaceOfBirth = input("Nhap placeofbirth cua ban: ")
cursor.execute("""INSERT INTO BookInfo (Name, PlaceOfBirth)
VALUES (?, ?)""", (newName, newPlaceOfBirth))


"""cursor.execute('''CREATE TABLE BookAndData
(BookID INTEGER PRIMARY KEY,
Title TEXT NOT NULL,
Author INTEGER NOT NULL,
DatePublished INTEGER)''')
"""
'''newID = int(input("Nhap id cua ban: "))
newTitle = input("Nhap Title cua ban: ")
newAuthor = int(input("Nhap Author cua ban: "))
newDate = input("Nhap DatePublished cua ban: ")
cursor.execute("""INSERT INTO BookAndData (BookID, Title, Author, DatePublished)
VALUES (?, ?, ?, ?)""", (newID, newTitle, newAuthor, newDate))'''

db.commit()
