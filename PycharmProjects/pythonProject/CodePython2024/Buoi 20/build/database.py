import sqlite3

# Tạo kết nối đến cơ sở dữ liệu SQLite
conn = sqlite3.connect('BanHang.db')
cursor = conn.cursor()

# Tạo các bảng cần thiết
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL UNIQUE,
  role TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products (
  product_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT,
  price REAL NOT NULL,
  stock INTEGER NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
  customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT UNIQUE,
  address TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
  order_id INTEGER PRIMARY KEY AUTOINCREMENT,
  customer_id INTEGER,
  order_date DATE NOT NULL,
  status TEXT NOT NULL,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS OrderDetails (
  order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id INTEGER,
  product_id INTEGER,
  quantity INTEGER NOT NULL,
  price REAL NOT NULL,
  FOREIGN KEY (order_id) REFERENCES Orders(order_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
''')

print("Các bảng đã được tạo thành công.")

# Thêm dữ liệu vào các bảng
cursor.executemany('''
INSERT INTO Users (username, password, email, role) VALUES (?, ?, ?, ?);
''', [
    ('admin', 'admin123', 'admin@example.com', 'administrator'),
    ('user', 'user123', 'user@example.com', 'customer'),
    ('manager', 'manager123', 'manager@example.com', 'manager')
])

cursor.executemany('''
INSERT INTO Products (name, description, price, stock) VALUES (?, ?, ?, ?);
''', [
    ('Laptop', 'Laptop cao cấp, màn hình 15 inch', 1500.00, 10),
    ('Mouse', 'Chuột không dây', 25.00, 50),
    ('Keyboard', 'Bàn phím cơ', 75.00, 30)
])

cursor.executemany('''
INSERT INTO Customers (name, phone, email, address) VALUES (?, ?, ?, ?);
''', [
    ('Nguyễn Văn A', '0123456789', 'vana@example.com', 'Hà Nội'),
    ('Trần Thị B', '0987654321', 'thib@example.com', 'TP HCM'),
    ('Lê Văn C', '0912345678', 'vanc@example.com', 'Đà Nẵng')
])

cursor.executemany('''
INSERT INTO Orders (customer_id, order_date, status) VALUES (?, ?, ?);
''', [
    (1, '2023-06-20', 'Pending'),
    (2, '2023-06-21', 'Shipped')
])

cursor.executemany('''
INSERT INTO OrderDetails (order_id, product_id, quantity, price) VALUES (?, ?, ?, ?);
''', [
    (1, 1, 2, 1500.00),
    (1, 2, 1, 25.00),
    (2, 3, 1, 75.00)
])

# Lưu thay đổi và đóng kết nối
conn.commit()
conn.close()

print("Dữ liệu đã được thêm thành công vào tất cả các bảng.")
