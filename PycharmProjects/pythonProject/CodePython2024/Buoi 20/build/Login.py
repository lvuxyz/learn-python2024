from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\hello1love\PycharmProjects\pythonProject\CodePython2024\Buoi 20\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def connect_db():
    """Connects to the SQLite database."""
    return sqlite3.connect('BanHang.db')

def login(username, password):
    """Checks username and password against the database."""
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM Users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

def attempt_login():
    """Attempts to login user using entered credentials."""
    username = entry_login.get()
    password = entry_pass.get()
    user = login(username, password)
    if user:
        messagebox.showinfo("Login Successful", "Bạn đã đăng nhập thành công!")
    else:
        messagebox.showerror("Login Failed", "Tên đăng nhập hoặc mật khẩu không chính xác!")

window = Tk()
window.geometry("1320x690")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=690,
    width=1320,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(990.0, 345.0, image=image_image_1)

canvas.create_text(
    930.0, 250.0, anchor="nw",
    text="Xin chào!", fill="#FFFFFF",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    761.0, 318.0, anchor="nw",
    text="Hãy nhập thông tin cá nhân của bạn và\ntiến hành đăng nhập nhé <3",
    fill="#FFFFFF", font=("Itim Regular", 30 * -1)
)

canvas.create_text(
    213.0, 102.0, anchor="nw",
    text="Đăng nhập", fill="#000000",
    font=("Itim Regular", 40 * -1)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(300.0, 270.0, image=entry_image_1)
entry_login = Entry(
    bd=0, bg="#F0F0F0", fg="#000716", highlightthickness=0
)
entry_login.place(x=140.0, y=240.0, width=320.0, height=58.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(300.0, 390.0, image=entry_image_2)
entry_pass = Entry(
    bd=0, bg="#F0F0F0", fg="#000716", highlightthickness=0, show="*"
)
entry_pass.place(x=140.0, y=360.0, width=320.0, height=58.0)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_login = Button(
    image=button_image_2, borderwidth=0, highlightthickness=0,
    command=attempt_login, relief="flat"
)
button_login.place(x=178.0, y=480.0, width=240.0, height=60.0)

canvas.create_text(
    357.0, 431.0, anchor="nw",
    text="Quên mật khẩu", fill="#229EE4",
    font=("Itim Regular", 20 * -1)
)

canvas.create_text(
    88.0, 198.0, anchor="nw",
    text="Tài khoản :", fill="#000000",
    font=("Itim Regular", 30 * -1)
)

canvas.create_text(
     94.0, 312.0, anchor="nw",
    text="Mật khẩu:", fill="#000000",
    font=("Itim Regular", 30 * -1)
)

window.resizable(False, False)
window.mainloop()
