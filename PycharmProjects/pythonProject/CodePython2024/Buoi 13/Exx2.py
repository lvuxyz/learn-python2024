import sqlite3


def delete_from_names():
    # Kết nối đến cơ sở dữ liệu
    with sqlite3.connect("testdata.db") as db:
        cursor = db.cursor()

        # Hiển thị các dòng trong bảng Names để người dùng có thể xác định dữ liệu cần xóa
        cursor.execute("SELECT ID, FirstName, SurName, PhoneNumber FROM Names")
        rows = cursor.fetchall()

        if not rows:
            print("Bảng Names hiện đang trống.")
            return

        print("Danh sách các hàng trong bảng Names:")
        for row in rows:
            print(f"ID: {row[0]}, FirstName: {row[1]}, SurName: {row[2]}, PhoneNumber: {row[3]}")

        # Nhập ID của hàng cần xóa từ người dùng
        row_id = int(input("Nhập ID của hàng cần xóa: "))

        # Thực thi truy vấn DELETE
        cursor.execute("DELETE FROM Names WHERE ID=?", (row_id,))

        if cursor.rowcount == 1:
            print(f"Đã xóa hàng có ID {row_id} từ bảng Names.")
        else:
            print(f"Không tìm thấy hàng có ID {row_id} để xóa.")

        # Commit thay đổi
        db.commit()


# Gọi hàm để thực hiện xóa dữ liệu
delete_from_names()
