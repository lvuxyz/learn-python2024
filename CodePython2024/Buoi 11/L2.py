from tkinter import *
import random

window = Tk()
window.title("cua vu")
window.geometry("720x480")

def cau_hoi():
    global num1, num2, correct_answer
    num1 = random.randint(10, 50)
    num2 = random.randint(10, 50)
    label_hien_thi_cau_hoi.config(text=f"{num1} + {num2} = ")
    correct_answer = num1 + num2

def kiem_tra_ket_qua():
    try:
        user_answer = int(entry_nhap.get())
        if user_answer == correct_answer:
            result_label.config(image=anh_dung)
        else:
            result_label.config(image=anh_sai)
    except ValueError:
        result_label.config(text="Vui lòng nhập một số nguyên")

anh_dung = PhotoImage(file="meomeolike.png")
anh_sai = PhotoImage(file="meomeokhoc.png")

label_hien_thi_cau_hoi = Label(window, text="")
label_hien_thi_cau_hoi.place(x=20, y=10)

label_hien_thi_nhap = Label(window, text="Nhập kết quả vào đây:")
label_hien_thi_nhap.place(x=20, y=50)

entry_nhap = Entry(window)
entry_nhap.place(x=20, y=80)

button_check = Button(window, text="Check kết quả", command=kiem_tra_ket_qua)
button_check.place(x=20, y=120)

button_cau_moi = Button(window, text="Câu mới", command=cau_hoi)
button_cau_moi.place(x=150, y=120)

result_label = Label(window)
result_label.place(x=20, y=150)

cau_hoi()

window.mainloop()
