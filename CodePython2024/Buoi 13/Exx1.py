import sqlite3

with sqlite3.connect("testdata.db") as db:
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Names (
        ID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        SurName TEXT NOT NULL,
        PhoneNumber TEXT
    )''')

    table_name = input("Nhập tên bảng: ")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    table_exists = cursor.fetchone()
    '''first_name = input("Nhập FirstName: ")
    sur_name = input("Nhập SurName: ")
    phone_number = input("Nhập PhoneNumber: ")

    # Thực thi truy vấn INSERT
    cursor.execute("INSERT INTO Names (FirstName, SurName, PhoneNumber) VALUES (?, ?, ?)",
                   (first_name, sur_name, phone_number))

    print("Đã thêm dữ liệu vào bảng Names.")

    # Commit thay đổi
    db.commit()'''

    if table_exists:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]
        print(f"Số hàng trong bảng {table_name}: {count}")
    else:
        print(f"Bảng {table_name} không tồn tại trong cơ sở dữ liệu.")

