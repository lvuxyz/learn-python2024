import mysql.connector

# Kết nối đến MySQL server
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Tạo cursor
cursor = mydb.cursor()

# Tạo database
cursor.execute("CREATE DATABASE IF NOT EXISTS library_management")

# Sử dụng database vừa tạo
cursor.execute("USE library_management")

# Tạo bảng books
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    publication_year INT,
    available BOOLEAN DEFAULT TRUE
)
""")

# Tạo bảng borrowings
cursor.execute("""
CREATE TABLE IF NOT EXISTS borrowings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    user_name VARCHAR(255) NOT NULL,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(id)
)
""")

# Tạo bảng user_requests (cho yêu cầu số 6)
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    request_content TEXT,
    request_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Commit các thay đổi
mydb.commit()

# Đóng kết nối
cursor.close()
mydb.close()

print("Database và các bảng đã được tạo thành công.")