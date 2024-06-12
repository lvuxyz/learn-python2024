from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Form của Vũ DZ")
window.geometry("720x480")


def hien_thi_thong_tin():
    ten = entry_ten.get()
    tuoi = entry_tuoi.get()
    dia_chi = entry_dia_chi.get()

    if ten and tuoi and dia_chi:
        thong_tin = f"Tên: {ten}\nTuổi: {tuoi}\nĐịa chỉ: {dia_chi}"
        list_box.insert(END, thong_tin)
        messagebox.showinfo("Thành công", "đã thêm thành công")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin")


label_ten = Label(window, text="Tên:")
label_ten.place(x=10, y=50)

entry_ten = Entry(window)
entry_ten.place(x=100, y=50)

label_tuoi = Label(window, text="Tuổi:")
label_tuoi.place(x=10, y=100)

entry_tuoi = Entry(window)
entry_tuoi.place(x=100, y=100)

label_dia_chi = Label(window, text="Địa chỉ:")
label_dia_chi.place(x=10, y=150)

entry_dia_chi = Entry(window)
entry_dia_chi.place(x=100, y=150)

button_hien_thi = Button(window, text="Hiển thị thông tin", command=hien_thi_thong_tin)
button_hien_thi.place(x=10, y=290, width=120, height=25)

list_box = Listbox(window)
list_box.place(x=300, y=50, width=400, height=300)

window.mainloop()
