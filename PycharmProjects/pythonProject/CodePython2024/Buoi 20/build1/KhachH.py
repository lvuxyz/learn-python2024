from pathlib import Path
from tkinter import ttk
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Khởi tạo cửa sổ chính
window = Tk()
window.geometry("1440x1024")

# Đường dẫn tới thư mục assets
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hello1love\PycharmProjects\pythonProject\CodePython2024\Buoi 20\build1\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Kết nối cơ sở dữ liệu
conn = sqlite3.connect('BanHang.db')  # Sửa lại đường dẫn cho phù hợp
cursor = conn.cursor()



def show_customers():
    # Hàm thêm khách hàng
    def add_customer():
        cursor.execute("INSERT INTO Customers (name, phone, email, address) VALUES (?, ?, ?, ?)",
                       (entry_ten_khach.get(), entry_SDT.get(), entry_email.get(), entry_dia_chi.get()))
        conn.commit()
        update_display()

    # Hàm sửa khách hàng
    def edit_customer():
        selected_item = tree.selection()[0]
        customer_id = tree.item(selected_item)['values'][0]
        cursor.execute("UPDATE Customers SET name=?, phone=?, email=?, address=? WHERE customer_id=?",
                       (entry_ten_khach.get(), entry_SDT.get(), entry_email.get(), entry_dia_chi.get(), customer_id))
        conn.commit()
        update_display()

    # Hàm xóa khách hàng
    def delete_customer():
        selected_item = tree.selection()[0]
        customer_id = tree.item(selected_item)['values'][0]
        cursor.execute("DELETE FROM Customers WHERE customer_id=?", (customer_id,))
        conn.commit()
        update_display()

    # Hàm tìm kiếm khách hàng
    def search_customer():
        for i in tree.get_children():
            tree.delete(i)
        cursor.execute("SELECT * FROM Customers WHERE name LIKE ?", ('%' + entry_search.get() + '%',))
        for row in cursor.fetchall():
            tree.insert('', 'end', values=row)

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        640.5,
        186.5,
        image=entry_image_2
    )
    entry_ma_khach = Entry(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_ma_khach.place(
        x=563.0,
        y=179.0,
        width=155.0,
        height=13.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        640.5,
        254.5,
        image=entry_image_3
    )
    entry_ten_khach = Entry(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_ten_khach.place(
        x=563.0,
        y=247.0,
        width=155.0,
        height=13.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        640.5,
        326.5,
        image=entry_image_4
    )
    entry_SDT = Entry(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_SDT.place(
        x=563.0,
        y=319.0,
        width=155.0,
        height=13.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        638.5,
        381.5,
        image=entry_image_5
    )
    entry_email = Entry(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_email.place(
        x=561.0,
        y=374.0,
        width=155.0,
        height=13.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        959.5,
        185.5,
        image=entry_image_6
    )
    entry_dia_chi = Entry(
        bd=0,
        bg="#F0F0F0",
        fg="#000716",
        highlightthickness=0
    )
    entry_dia_chi.place(
        x=882.0,
        y=178.0,
        width=155.0,
        height=13.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_add = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=add_customer,
        relief="flat"
    )
    button_add.place(
        x=476.0,
        y=426.0,
        width=114.0,
        height=38.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_edit = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=edit_customer,
        relief="flat"
    )
    button_edit.place(
        x=670.0,
        y=426.0,
        width=114.0,
        height=38.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_delete = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=delete_customer,
        relief="flat"
    )
    button_delete.place(
        x=845.0,
        y=422.0,
        width=114.0,
        height=38.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_search = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=search_customer,
        relief="flat"
    )
    button_search.place(
        x=1193.0,
        y=426.0,
        width=114.0,
        height=38.0
    )

# Cấu trúc giao diện người dùng
canvas = Canvas(
    window,
    bg = "#F9F9F9",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    156.0,
    512.0,
    image=image_image_1
)

canvas.create_text(
    115.0,
    938.0,
    anchor="nw",
    text="Ngô Long Vũ",
    fill="#000000",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    112.0,
    962.0,
    anchor="nw",
    text="20210463@eaut.edu.vn",
    fill="#000000",
    font=("Itim Regular", 15 * -1)
)

canvas.create_rectangle(
    348.0,
    132.9999999944157,
    1372.0000019036233,
    136.0,
    fill="#D0C8C8",
    outline="")

canvas.create_rectangle(
    13.0,
    134.9718323162731,
    301.99981672200374,
    138.0,
    fill="#D0C8C8",
    outline="")

canvas.create_rectangle(
    12.996337890625,
    510.0140380859375,
    302.0032958984375,
    511.0140380859375,
    fill="#D0C8C8",
    outline="")

canvas.create_rectangle(
    348.0,
    552.0,
    1372.0,
    553.0,
    fill="#D0C8C8",
    outline="")

canvas.create_rectangle(
    13.0,
    916.0,
    302.0069580078125,
    917.0,
    fill="#D0C8C8",
    outline="")

canvas.create_text(
    37.0,
    27.0,
    anchor="nw",
    text="Quản Lý Dịch Vụ Chăm Sóc Máy Tính",
    fill="#000000",
    font=("Itim Regular", 30)  # Positive font size
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_in_bc = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("in bao cao clicked"),
    relief="flat"
)
button_in_bc.place(
    x=1295.0,
    y=104.0,
    width=77.0,
    height=24.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_quan_ly_kh = Button(
    window,
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=show_customers,
    relief="flat"
)
button_quan_ly_kh.place(
    x=47.0,
    y=264.0,
    width=217.0,
    height=41.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_quan_ly_bao_cao = Button(
    window,  # Replace 'frame' with your actual frame variable
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("quan ly bao cao clicked"),
    relief="flat"
)
button_quan_ly_bao_cao.place(
    x=47.0,
    y=374.0,
    width=217.0,
    height=41.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_quan_ly_san_pham = Button(
    window,  # Replace 'frame' with your actual frame variable
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("quan ly san pham clicked"),
    relief="flat"
)
button_quan_ly_san_pham.place(
    x=47.0,
    y=209.0,
    width=217.0,
    height=41.0
)

button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_quan_ly_don_hang = Button(
    window,  # Replace 'frame' with your actual frame variable
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("quan ly don hang clicked"),
    relief="flat"
)
button_quan_ly_don_hang.place(
    x=47.0,
    y=319.0,
    width=217.0,
    height=41.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    57.0,
    961.0,
    image=image_image_2
)

canvas.create_rectangle(
    349.0,
    159.0,
    1088.0,
    520.0,
    fill="#FFFFFF",
    outline="")

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    718.0,
    339.0,
    image=image_image_3
)

canvas.create_text(
    801.0,
    180.0,
    anchor="nw",
    text="Địa Chỉ",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

canvas.create_text(
    395.0,
    365.0,
    anchor="nw",
    text="Email",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1244.0,
    339.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    652.0,
    185.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    652.0,
    254.0,
    image=image_image_6
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1244.5,
    254.5,
    image=entry_image_1
)
entry_search = Entry(
    bd=0,
    bg="#F0F0F0",
    fg="#000716",
    highlightthickness=0
)
entry_search.place(
    x=1155.5,
    y=235.0,
    width=178.0,
    height=37.0
)

canvas.create_text(
    1136.0,
    189.0,
    anchor="nw",
    text="Tìm kiếm",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    652.0,
    324.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    652.0,
    382.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    968.0,
    185.0,
    image=image_image_9
)

canvas.create_text(
    387.0,
    184.0,
    anchor="nw",
    text="Mã Khách",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

canvas.create_text(
    387.0,
    247.0,
    anchor="nw",
    text="Tên Khách",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

canvas.create_text(
    387.0,
    314.0,
    anchor="nw",
    text="Số Điện Thoại",
    fill="#000000",
    font=("TimesNewRomanPSMT", 15 * -1)
)

def create_treeview(window):

    # Định nghĩa Treeview
    tree = ttk.Treeview(window, columns=('ID', 'Name', 'Phone', 'Email', 'Address'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Name', text='Tên Khách')
    tree.heading('Phone', text='Số Điện Thoại')
    tree.heading('Email', text='Email')
    tree.heading('Address', text='Địa Chỉ')
    tree.place(x=400, y=600, height=340, width=980)

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


window.resizable(False, False)
window.mainloop()
