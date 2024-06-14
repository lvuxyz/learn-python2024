import sqlite3
from tkinter import *
from tkinter import messagebox

db = sqlite3.connect('student_info.db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, age INTEGER, class TEXT, student_id TEXT PRIMARY KEY, year INTEGER, achievement TEXT, hobby TEXT, note TEXT)''')
db.commit()

def save_student():
    name = entry_name.get()
    age = entry_age.get()
    class_name = entry_class.get()
    student_id = entry_msv.get()
    year = entry_learnyear.get()
    achievement = entry_thanhtich.get()
    hobby = entry_sothich.get()
    note = entry_note.get()

    try:
        cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, age, class_name, student_id, year, achievement, hobby, note))
        db.commit()
        clear()
        messagebox.showinfo("Thành công", "Thông tin sinh viên đã được lưu.")
    except sqlite3.IntegrityError:
        messagebox.showerror("Lỗi", "Mã sinh viên đã tồn tại. Vui lòng kiểm tra lại.")

def update_student():
    name = entry_name.get()
    age = entry_age.get()
    class_name = entry_class.get()
    student_id = entry_msv.get()
    year = entry_learnyear.get()
    achievement = entry_thanhtich.get()
    hobby = entry_sothich.get()
    note = entry_note.get()

    cursor.execute("UPDATE students SET name = ?, age = ?, class = ?, year = ?, achievement = ?, hobby = ?, note = ? WHERE student_id = ?", (name, age, class_name, year, achievement, hobby, note, student_id))
    db.commit()
    messagebox.showinfo("Thành công", "Thông tin sinh viên đã được cập nhật.")

def delete_student():
    student_id = entry_msv.get()

    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    db.commit()
    clear()
    messagebox.showinfo("Thành công", "Thông tin sinh viên đã được xóa.")

def clear():
    entry_name.delete(0, END)
    entry_age.delete(0, END)
    entry_class.delete(0, END)
    entry_msv.delete(0, END)
    entry_learnyear.delete(0, END)
    entry_thanhtich.delete(0, END)
    entry_sothich.delete(0, END)
    entry_note.delete(0, END)

window = Tk()
window.title("Đăng nhập thông tin cá nhân")
window.geometry("720x480")

label_name = Label(window, text="Họ tên")
label_name.place(x=20, y=20)
entry_name = Entry(window)
entry_name.place(x=120, y=20)

label_age = Label(window, text="Tuổi")
label_age.place(x=20, y=60)
entry_age = Entry(window)
entry_age.place(x=120, y=60)

label_class = Label(window, text="Lớp")
label_class.place(x=20, y=100)
entry_class = Entry(window)
entry_class.place(x=120, y=100)

label_msv = Label(window, text="Mã sinh viên")
label_msv.place(x=20, y=140)
entry_msv = Entry(window)
entry_msv.place(x=120, y=140)

label_learnyear = Label(window, text="Năm học")
label_learnyear.place(x=20, y=180)
entry_learnyear = Entry(window)
entry_learnyear.place(x=120, y=180)

label_thanhtich = Label(window, text="Thành tích")
label_thanhtich.place(x=20, y=220)
entry_thanhtich = Entry(window)
entry_thanhtich.place(x=120, y=220)

label_sothich = Label(window, text="Sở thích")
label_sothich.place(x=20, y=260)
entry_sothich = Entry(window)
entry_sothich.place(x=120, y=260)

label_note = Label(window, text="Ghi chú")
label_note.place(x=20, y=300)
entry_note = Entry(window)
entry_note.place(x=120, y=300)

button_add = Button(window, text="Thêm", command=save_student)
button_add.place(x=50, y=400, width=100, height=25)

button_update = Button(window, text="Sửa", command=update_student)
button_update.place(x=200, y=400, width=100, height=25)

button_delete = Button(window, text="Xóa", command=delete_student)
button_delete.place(x=350, y=400, width=100, height=25)

button_clear = Button(window, text="Xóa thông tin nhap", command=clear)
button_clear.place(x=500, y=400, width=100, height=25)

window.mainloop()
