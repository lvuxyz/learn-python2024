import sqlite3

conn = sqlite3.connect('BookInfo.db')
c = conn.cursor()

author_name = input("Nhập tên tác giả: ")

c.execute('''SELECT Books.Title, Books.PublishedDate, Authors.Name
             FROM Books
             INNER JOIN Authors ON Books.AuthorID = Authors.ID
             WHERE Authors.Name = ?''', (author_name,))

books = c.fetchall()

with open('books.txt', 'w', encoding='utf-8') as f:
    for book in books:
        book_info = '---'.join([str(item) for item in book])
        f.write(book_info + '\n')

if books:
    print(f"Đã lưu danh sách sách của tác giả {author_name} vào file 'books.txt'.")
else:
    print(f"Không tìm thấy sách của tác giả {author_name}.")

conn.close()