import sqlite3

conn = sqlite3.connect('BookInfo.db')
c = conn.cursor()

c.execute('SELECT Name, PlaceOfBirth FROM Authors')
authors = c.fetchall()

print("Danh sách tác giả và nơi sinh:")
for author in authors:
    print(f"{author[0]} - {author[1]}")

place_of_birth = input("Nhập nơi sinh để tìm kiếm sách: ")

c.execute('''SELECT Books.Title, Books.PublishedDate, Authors.Name
             FROM Books 
             INNER JOIN Authors ON Books.AuthorID = Authors.ID
             WHERE Authors.PlaceOfBirth = ?''', (place_of_birth,))

books = c.fetchall()

if books:
    print(f"\nSách của tác giả sinh tại {place_of_birth}:")
    for book in books:
        print(f"{book[0]} - {book[1]} - {book[2]}")
else:
    print(f"Không tìm thấy sách của tác giả sinh tại {place_of_birth}.")

conn.close()