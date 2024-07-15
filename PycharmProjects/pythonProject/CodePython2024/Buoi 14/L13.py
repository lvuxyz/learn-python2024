import sqlite3
from tkinter import *
from tkinter import messagebox, simpledialog

db = sqlite3.connect('student_scores.db')
cursor = db.cursor()
db.execute('''CREATE TABLE IF NOT EXISTS scores
             (id INTEGER PRIMARY KEY AUTOINCREMENT, toan REAL, ly REAL, hoa REAL, van REAL, su REAL, dia REAL, gdcd REAL, note TEXT)''')
db.commit()

def save_student_scores():
    try:
        toan = float(entry_toan.get())
        ly = float(entry_ly.get())
        hoa = float(entry_hoa.get())
        van = float(entry_van.get())
        su = float(entry_su.get())
        dia = float(entry_dia.get())
        gdcd = float(entry_gdcd.get())

        cursor.execute("INSERT INTO scores (toan, ly, hoa, van, su, dia, gdcd) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (toan, ly, hoa, van, su, dia, gdcd))
        db.commit()
        clear_entries()
        messagebox.showinfo("Thành công", "Điểm sinh viên đã được lưu.")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ và đúng định dạng điểm.")

def find_highest_scores():
    cursor.execute("SELECT * FROM scores WHERE toan > 8 OR ly > 8 OR hoa > 8 OR van > 8 OR su > 8 OR dia > 8 OR gdcd > 8")
    highest_scores = cursor.fetchall()
    if highest_scores:
        result = "Sinh viên có điểm cao nhất (trên 8):\n"
        for score in highest_scores:
            result += f"ID: {score[0]}, Toán: {score[1]}, Lý: {score[2]}, Hóa: {score[3]}, Văn: {score[4]}, Sử: {score[5]}, Địa: {score[6]}, GDCD: {score[7]}\n"
        messagebox.showinfo("Kết quả", result)
    else:
        messagebox.showinfo("Kết quả", "Không có sinh viên nào có điểm cao nhất (trên 8).")

def find_lowest_scores():
    cursor.execute("SELECT * FROM scores WHERE toan < 5 OR ly < 5 OR hoa < 5 OR van < 5 OR su < 5 OR dia < 5 OR gdcd < 5")
    lowest_scores = cursor.fetchall()
    if lowest_scores:
        result = "Sinh viên có điểm thấp nhất (dưới 5):\n"
        for score in lowest_scores:
            result += f"ID: {score[0]}, Toán: {score[1]}, Lý: {score[2]}, Hóa: {score[3]}, Văn: {score[4]}, Sử: {score[5]}, Địa: {score[6]}, GDCD: {score[7]}\n"
        messagebox.showinfo("Kết quả", result)
    else:
        messagebox.showinfo("Kết quả", "Không có sinh viên nào có điểm thấp nhất (dưới 5).")

def find_avg_below_5():
    cursor.execute("SELECT * FROM scores")
    all_scores = cursor.fetchall()
    for score in all_scores:
        avg_score = (score[1] + score[2] + score[3] + score[4] + score[5] + score[6] + score[7]) / 7
        if avg_score < 5:
            cursor.execute("UPDATE scores SET note = 'Thi Lại' WHERE id = ?", (score[0],))
    db.commit()
    messagebox.showinfo("Thành công", "Đã đánh dấu 'Thi Lại' cho sinh viên có điểm trung bình dưới 5.")


# Hàm tìm sinh viên có điểm cao nhất và không có môn nào dưới 7
def find_highest_above_7():
    cursor.execute(
        "SELECT * FROM scores WHERE toan >= 7 AND ly >= 7 AND hoa >= 7 AND van >= 7 AND su >= 7 AND dia >= 7 AND gdcd >= 7 ORDER BY toan + ly + hoa + van + su + dia + gdcd DESC LIMIT 1")
    highest_above_7 = cursor.fetchone()
    if highest_above_7:
        result = f"Sinh viên có điểm cao nhất và không có môn nào dưới 7:\nID: {highest_above_7[0]}, Toán: {highest_above_7[1]}, Lý: {highest_above_7[2]}, Hóa: {highest_above_7[3]}, Văn: {highest_above_7[4]}, Sử: {highest_above_7[5]}, Địa: {highest_above_7[6]}, GDCD: {highest_above_7[7]}"
        messagebox.showinfo("Kết quả", result)
    else:
        messagebox.showinfo("Kết quả", "Không có sinh viên nào có điểm cao nhất và không có môn nào dưới 7.")
def find_lowest_below_8():
    cursor.execute(
        "SELECT * FROM scores WHERE toan < 8 AND ly < 8 AND hoa < 8 AND van < 8 AND su < 8 AND dia < 8 AND gdcd < 8 ORDER BY toan + ly + hoa + van + su + dia + gdcd ASC LIMIT 1")
    lowest_below_8 = cursor.fetchone()
    if lowest_below_8:
        result = f"Sinh viên có điểm thấp nhất và không có môn nào trên 8:\nID: {lowest_below_8[0]}, Toán: {lowest_below_8[1]}, Lý: {lowest_below_8[2]}, Hóa: {lowest_below_8[3]}, Văn: {lowest_below_8[4]}, Sử: {lowest_below_8[5]}, Địa: {lowest_below_8[6]}, GDCD: {lowest_below_8[7]}"
        messagebox.showinfo("Kết quả", result)
    else:
        messagebox.showinfo("Kết quả", "Không có sinh viên nào có điểm thấp nhất và không có môn nào trên 8.")

def update_student_scores():
    students_to_update = cursor.execute(
        "SELECT * FROM scores WHERE toan < 5 OR ly < 5 OR hoa < 5 OR van < 5 OR su < 5 OR dia < 5 OR gdcd < 5").fetchall()
    if students_to_update:
        for student in students_to_update:
            num_failed_subjects = sum(1 for score in student[1:8] if score < 5)
            if num_failed_subjects >= 3:
                new_toan = float(entry_toan.get()) if entry_toan.get() else student[1]
                new_ly = float(entry_ly.get()) if entry_ly.get() else student[2]
                new_hoa = float(entry_hoa.get()) if entry_hoa.get() else student[3]
                new_van = float(entry_van.get()) if entry_van.get() else student[4]
                new_su = float(entry_su.get()) if entry_su.get() else student[5]
                new_dia = float(entry_dia.get()) if entry_dia.get() else student[6]
                new_gdcd = float(entry_gdcd.get()) if entry_gdcd.get() else student[7]

                cursor.execute(
                    "UPDATE scores SET toan = ?, ly = ?, hoa = ?, van = ?, su = ?, dia = ?, gdcd = ? WHERE id = ?",
                    (new_toan, new_ly, new_hoa, new_van, new_su, new_dia, new_gdcd, student[0])
                )
                db.commit()
                messagebox.showinfo("Thành công", "Điểm sinh viên đã được cập nhật.")
                clear_entries()
    else:
        messagebox.showinfo("Thông báo", "Không có sinh viên nào có 3 môn đều thi lại.")

def delete_student_scores():
    student_id = simpledialog.askinteger("Xóa sinh viên", "Nhập ID sinh viên cần xóa:")
    if student_id:
        cursor.execute("DELETE FROM scores WHERE id = ?", (student_id,))
        db.commit()
        messagebox.showinfo("Thành công", "Điểm sinh viên đã được xóa.")
    else:
        messagebox.showinfo("Thông báo", "Không có ID sinh viên được nhập.")

def clear_entries():
    entry_toan.delete(0, END)
    entry_ly.delete(0, END)
    entry_hoa.delete(0, END)
    entry_van.delete(0, END)
    entry_su.delete(0, END)
    entry_dia.delete(0, END)
    entry_gdcd.delete(0, END)


# Tạo cửa sổ và các thành phần giao diện
window = Tk()
window.title("Quản lý điểm sinh viên")
window.geometry("720x480")

label_toan = Label(window, text="Toán")
label_toan.place(x=20, y=20)
entry_toan = Entry(window)
entry_toan.place(x=120, y=20)

label_ly = Label(window, text="Lý")
label_ly.place(x=20, y=60)
entry_ly = Entry(window)
entry_ly.place(x=120, y=60)

label_hoa = Label(window, text="Hóa")
label_hoa.place(x=20, y=100)
entry_hoa = Entry(window)
entry_hoa.place(x=120, y=100)

label_van = Label(window, text="Văn")
label_van.place(x=20, y=140)
entry_van = Entry(window)
entry_van.place(x=120, y=140)

label_su = Label(window, text="Sử")
label_su.place(x=20, y=180)
entry_su = Entry(window)
entry_su.place(x=120, y=180)

label_dia = Label(window, text="Địa")
label_dia.place(x=20, y=220)
entry_dia = Entry(window)
entry_dia.place(x=120, y=220)

label_gdcd = Label(window, text="GDCD")
label_gdcd.place(x=20, y=260)
entry_gdcd = Entry(window)
entry_gdcd.place(x=120, y=260)

button_add = Button(window, text="Thêm", command=save_student_scores)
button_add.place(x=50, y=400, width=100, height=25)

button_highest = Button(window, text="Điểm cao nhất", command=find_highest_scores)
button_highest.place(x=200, y=400, width=100, height=25)

button_lowest = Button(window, text="Điểm thấp nhất", command=find_lowest_scores)
button_lowest.place(x=350, y=400, width=100, height=25)

button_avg_below_5 = Button(window, text="Đánh dấu thi lại", command=find_avg_below_5)
button_avg_below_5.place(x=500, y=400, width=100, height=25)

button_highest_above_7 = Button(window, text="Điểm cao nhất >7", command=find_highest_above_7)
button_highest_above_7.place(x=50, y=450, width=120, height=25)

button_lowest_below_8 = Button(window, text="Điểm thấp nhất <8", command=find_lowest_below_8)
button_lowest_below_8.place(x=200, y=450, width=120, height=25)

button_update = Button(window, text="Sửa 3 môn thi lại", command=update_student_scores)
button_update.place(x=350, y=450, width=120, height=25)

button_delete = Button(window, text="Xóa sinh viên", command=delete_student_scores)
button_delete.place(x=500, y=450, width=100, height=25)

window.mainloop()
