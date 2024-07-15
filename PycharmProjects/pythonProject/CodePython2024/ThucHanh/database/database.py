import sqlite3

class DatabaseManager:
    def __init__(root):
        root.conn = sqlite3.connect('BanHang.db')
        root.cursor = root.conn.cursor()
        root.create_table()

    def create_table(root):
        root.cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                                customer_id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                phone TEXT,
                                email TEXT,
                                address TEXT
                                )''')
        root.conn.commit()

    def add_customer(root, customer_id, name, phone, email, address):
        root.cursor.execute("INSERT INTO Customers (customer_id, name, phone, email, address) VALUES (?, ?, ?, ?, ?)",
                            (customer_id, name, phone, email, address))
        root.conn.commit()

    def update_customer(root, customer_id, name, phone, email, address):
        root.cursor.execute("UPDATE Customers SET name=?, phone=?, email=?, address=? WHERE customer_id=?",
                            (name, phone, email, address, customer_id))
        root.conn.commit()

    def delete_customer(root, customer_id):
        root.cursor.execute("DELETE FROM Customers WHERE customer_id=?", (customer_id,))
        root.conn.commit()

    def search_customer(root, customer_id):
        root.cursor.execute("SELECT * FROM Customers WHERE customer_id=?", (customer_id,))
        return root.cursor.fetchone()

    def close(root):
        root.conn.close()
