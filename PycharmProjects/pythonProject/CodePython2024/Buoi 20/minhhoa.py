import tkinter as tk
from tkinter import ttk

def show_home():
    for widget in right_frame.winfo_children():
        widget.destroy()
    ttk.Label(right_frame, text="Đây là trang chủ").pack(pady=20)

def show_customers():
    for widget in right_frame.winfo_children():
        widget.destroy()
    ttk.Label(right_frame, text="Quản lý khách hàng").pack(pady=20)
    ttk.Button(right_frame, text="Thêm Khách Hàng", command=add_customer).pack(fill='x')
    ttk.Button(right_frame, text="Sửa Thông Tin Khách Hàng", command=edit_customer).pack(fill='x')
    ttk.Button(right_frame, text="Xóa Khách Hàng", command=delete_customer).pack(fill='x')

def add_customer():
    print("Thêm khách hàng")

def edit_customer():
    print("Sửa thông tin khách hàng")

def delete_customer():
    print("Xóa khách hàng")

def add_donhang():
    print("them don hang")
def show_donhang():
    for widget in right_frame.winfo_children():
        widget.destroy()
    ttk.Label(right_frame, text="Quan ly don hang").pack(pady=20)
    ttk.Button(right_frame, text="Them don hang", command=add_donhang).pack(fill='x')




root = tk.Tk()
root.title("Ứng dụng Quản lý")
root.geometry("500x350")

left_frame = ttk.Frame(root, width=200, height=500, relief=tk.RIDGE)
left_frame.pack(side="left", fill="y")

right_frame = ttk.Frame(root, width=600, height=500, relief=tk.RIDGE)
right_frame.pack(side="right", fill="both", expand=True)

# Buttons for navigation in the left frame
ttk.Button(left_frame, text="Trang Chủ", command=show_home).pack(fill='x')
ttk.Button(left_frame, text="Quản Lý Khách Hàng", command=show_customers).pack(fill='x')
ttk.Button(left_frame, text="Quan ly don hang", command=show_donhang).pack(fill='x')
root.mainloop()
