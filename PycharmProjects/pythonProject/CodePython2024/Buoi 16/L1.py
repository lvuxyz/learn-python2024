'''import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Univer"
)

mycursor = mydb.cursor()

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        major VARCHAR(255),
        point VARCHAR(255),
        note VARCHAR(255)
    )
""")

students = [
    ("Ngô Vũ", 20, "Khoa học máy tính", "A", "Có"),
    ("Trung Dũng", 22, "Toán học", "B", "Không"),
    ("Tiến Đạt", 21, "Vật lý", "C", "Có"),
    ("Quang Thắng", 23, "Hoá học", "A", "Không"),
    ("Huy Chiến", 20, "Sinh học", "B", "Có")
]

sql = "INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)"

for student in students:
    mycursor.execute(sql, student)

mydb.commit()
mycursor.close()
mydb.close()'''
import mysql.connector

def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Univer"
    )
    if mydb.is_connected():
        return mydb
    return None

def close_connection(connection, cursor=None):
    if cursor:
        cursor.close()
    if connection:
        connection.close()

def create_table():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS students ("
            "id INT AUTO_INCREMENT PRIMARY KEY, "
            "name VARCHAR(255), "
            "age INT, "
            "major VARCHAR(255), "
            "point VARCHAR(255), "
            "note VARCHAR(255))"
        )
        close_connection(connection, cursor)

def them_sinh_vien(name, age, major, point, note):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "INSERT INTO students (name, age, major, point, note) VALUES (%s, %s, %s, %s, %s)"
        val = (name, age, major, point, note)
        cursor.execute(sql, val)
        connection.commit()
        print("Sinh viên mới đã được thêm vào.")
        close_connection(connection, cursor)

def cap_nhat_sinh_vien(id, name, age, major, point, note):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "UPDATE students SET name = %s, age = %s, major = %s, point = %s, note = %s WHERE id = %s"
        val = (name, age, major, point, note, id)
        cursor.execute(sql, val)
        connection.commit()
        print(f"Sinh viên có ID {id} đã được cập nhật.")
        close_connection(connection, cursor)

def xoa_sinh_vien(id):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM students WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        connection.commit()
        print(f"Sinh viên có ID {id} đã được xóa.")
        close_connection(connection, cursor)

def truy_van_tat_ca_sinh_vien():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)
        close_connection(connection, cursor)

def truy_van_sinh_vien_theo_ten_hoac_chuyen_nganh(name=None, major=None):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM students WHERE"
        conditions = []
        val = []
        if name:
            conditions.append("name = %s")
            val.append(name)
        if major:
            conditions.append("major = %s")
            val.append(major)
        if conditions:
            sql += " " + " OR ".join(conditions)
            cursor.execute(sql, tuple(val))
            result = cursor.fetchall()
            for row in result:
                print(row)
        else:
            print("Bạn cần cung cấp ít nhất tên hoặc major.")
        close_connection(connection, cursor)

def sap_xep_sinh_vien_theo_ten():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students ORDER BY name")
        result = cursor.fetchall()
        for row in result:
            print(row)
        close_connection(connection, cursor)

def tim_sinh_vien_theo_ten(name):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM students WHERE name = %s"
        val = (name,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        for row in result:
            print(row)
        close_connection(connection, cursor)

def xoa_sinh_vien_co_ghi_chu():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "DELETE FROM students WHERE note = %s"
        val = ("có",)
        cursor.execute(sql, val)
        connection.commit()
        print("Tất cả sinh viên có note là 'có' đã được xóa.")
        close_connection(connection, cursor)

def truy_van_sinh_vien_theo_tuoi(age):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "SELECT * FROM students WHERE age = %s"
        val = (age,)
        cursor.execute(sql, val)
        result = cursor.fetchall()
        for row in result:
            print(row)
        close_connection(connection, cursor)

def truy_van_diem_cao_nhat_va_thap_nhat():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(CAST(point AS SIGNED)) AS highest_score, MIN(CAST(point AS SIGNED)) AS lowest_score FROM students")
        result = cursor.fetchone()
        print(f"Điểm cao nhất: {result[0]}, Điểm thấp nhất: {result[1]}")
        close_connection(connection, cursor)

def cap_nhat_diem_sinh_vien(id, new_score):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        sql = "UPDATE students SET point = %s WHERE id = %s"
        val = (new_score, id)
        cursor.execute(sql, val)
        connection.commit()
        print(f"Điểm của sinh viên có ID {id} đã được cập nhật.")
        close_connection(connection, cursor)

def tinh_tong_diem():
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT SUM(CAST(point AS SIGNED)) AS total_score FROM students")
        result = cursor.fetchone()
        total_score = result[0]
        print(f"Tổng điểm của tất cả sinh viên: {total_score}")
        close_connection(connection, cursor)

# Chạy chương trình
create_table()

while True:
    print("\nChọn một tác vụ:")
    print("1. Thêm sinh viên mới")
    print("2. Cập nhật thông tin sinh viên")
    print("3. Xóa sinh viên")
    print("4. Truy vấn tất cả sinh viên")
    print("5. Truy vấn sinh viên theo tên hoặc major")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Tìm kiếm sinh viên có cùng tên")
    print("8. Xóa toàn bộ sinh viên có note là 'có'")
    print("9. Hiển thị danh sách sinh viên có cùng tuổi")
    print("10. Tìm sinh viên có điểm cao nhất và thấp nhất")
    print("11. Thay đổi điểm của một sinh viên")
    print("12. Tính tổng điểm của tất cả sinh viên")
    print("13. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-13): ")

    if choice == "1":
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        major = input("Nhập chuyên ngành của sinh viên: ")
        point = input("Nhập điểm của sinh viên: ")
        note = input("Nhập ghi chú của sinh viên: ")
        them_sinh_vien(name, age, major, point, note)

    elif choice == "2":
        id = int(input("Nhập ID của sinh viên cần cập nhật: "))
        name = input("Nhập tên mới của sinh viên: ")
        age = int(input("Nhập tuổi mới của sinh viên: "))
        major = input("Nhập chuyên ngành mới của sinh viên: ")
        point = input("Nhập điểm mới của sinh viên: ")
        note = input("Nhập ghi chú mới của sinh viên: ")
        cap_nhat_sinh_vien(id, name, age, major, point, note)

    elif choice == "3":
        id = int(input("Nhập ID của sinh viên cần xóa: "))
        xoa_sinh_vien(id)

    elif choice == "4":
        truy_van_tat_ca_sinh_vien()

    elif choice == "5":
        name = input("Nhập tên sinh viên (hoặc bỏ trống nếu không muốn tìm kiếm theo tên): ")
        major = input("Nhập chuyên ngành của sinh viên (hoặc bỏ trống nếu không muốn tìm kiếm theo chuyên ngành): ")
        truy_van_sinh_vien_theo_ten_hoac_chuyen_nganh(name if name else None, major if major else None)

    elif choice == "6":
        sap_xep_sinh_vien_theo_ten()

    elif choice == "7":
        name = input("Nhập tên sinh viên: ")
        tim_sinh_vien_theo_ten(name)

    elif choice == "8":
        xoa_sinh_vien_co_ghi_chu()

    elif choice == "9":
        age = int(input("Nhập tuổi sinh viên: "))
        truy_van_sinh_vien_theo_tuoi(age)

    elif choice == "10":
        truy_van_diem_cao_nhat_va_thap_nhat()

    elif choice == "11":
        id = int(input("Nhập ID của sinh viên cần thay đổi điểm: "))
        new_score = input("Nhập điểm mới: ")
        cap_nhat_diem_sinh_vien(id, new_score)

    elif choice == "12":
        tinh_tong_diem()

    elif choice == "13":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")