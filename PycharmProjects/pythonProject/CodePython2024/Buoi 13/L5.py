import sqlite3

conn = sqlite3.connect('BookInfo.db')
c = conn.cursor()

year = input("Nhập năm: ")

c.execute('''SELECT Title, PublishedDate 
             FROM Books
             WHERE PublishedDate > ?
             ORDER BY PublishedDate''', (year,))

books = c.fetchall()

if books:
    print(f"Sách được xuất bản sau năm {year}:")
    for book in books:
        print(f"{book[0]} - {book[1]}")
else:
    print(f"Không tìm thấy sách được xuất bản sau năm {year}.")

# Đóng kết nối
conn.close()