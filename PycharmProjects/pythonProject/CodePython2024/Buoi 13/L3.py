import sqlite3

# Kết nối đến cơ sở dữ liệu (tạo mới nếu chưa tồn tại)
conn = sqlite3.connect('BookInfo.db')
c = conn.cursor()

# Tạo bảng Authors
c.execute('''CREATE TABLE Authors
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                Name TEXT,
                PlaceOfBirth TEXT)''')

# Chèn dữ liệu vào bảng Authors
authors = [('Jane Austen', 'England'),
           ('Leo Tolstoy', 'Russia'),
           ('Gabriel Garcia', 'Colombia')]

c.executemany('INSERT INTO Authors (Name, PlaceOfBirth) VALUES (?, ?)', authors)

# Tạo bảng Books
c.execute('''CREATE TABLE Books
                (BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                AuthorID INTEGER, 
                Title TEXT,
                PublishedDate TEXT,
                FOREIGN KEY(AuthorID) REFERENCES Authors(ID))''')

# Chèn dữ liệu vào bảng Books
books = [(1, 'Pride and Prejudice', '1813-01-28'),
         (1, 'Sense and Sensibility', '1811-01-01'),
         (2, 'War and Peace', '1869-01-01'),
         (2, 'Anna Karenina', '1877-01-01'),
         (3, 'One Hundred Years', '1967-06-05')]

c.executemany('INSERT INTO Books (AuthorID, Title, PublishedDate) VALUES (?, ?, ?)', books)

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Cơ sở dữ liệu BookInfo đã được tạo thành công!")