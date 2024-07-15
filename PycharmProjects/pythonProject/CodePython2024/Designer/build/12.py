from tkinter import *
from tkinter import ttk
import sqlite3

# Khởi tạo cửa sổ chính
window = Tk()
window.geometry("1440x1024")
window.configure(bg="#F9F9F9")

def create_treeview(window):

    # Định nghĩa Treeview
    tree = ttk.Treeview(window, columns=('ID', 'Name', 'Phone', 'Email', 'Address'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Tên Khách')
    tree.heading('Phone', text='Số Điện Thoại')
    tree.heading('Email', text='Email')
    tree.heading('Address', text='Địa Chỉ')
    tree.pack(pady=10)

    return tree

# Tạo Treeview
tree = create_treeview(window)

# Kết nối cơ sở dữ liệu
conn = sqlite3.connect('BanHang.db')  # Sửa lại đường dẫn cho phù hợp
cursor = conn.cursor()

# Hàm cập nhật dữ liệu hiển thị
def update_display():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM Customers")
    for row in cursor.fetchall():
        tree.insert('', 'end', values=row)

# Khởi động cập nhật giao diện ban đầu
update_display()

window.resizable(False, False)
window.mainloop()
