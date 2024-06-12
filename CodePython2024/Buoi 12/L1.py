from tkinter import *
from tkinter import messagebox
import math

window = Tk()
window.geometry("720x480")

def giai_phuong_trinh_bac_nhat():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            if b == 0:
                result_label.config(text="Phương trình vô số nghiệm")
            else:
                result_label.config(text="Phương trình vô nghiệm")
        else:
            x = -b / a
            result_label.config(text=f"Nghiệm của phương trình: x = {x}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def giai_phuong_trinh_bac_hai():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            giai_phuong_trinh_bac_nhat()
        else:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                result_label.config(text="Phương trình vô nghiệm")
            elif delta == 0:
                x = -b / (2 * a)
                result_label.config(text=f"Phương trình có nghiệm kép: x = {x}")
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                result_label.config(text=f"Nghiệm của phương trình:\nx1 = {x1}\nx2 = {x2}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

label_nhap_a = Label(window, text="Nhập số a:")
label_nhap_a.place(x=10, y=50)
entry_a = Entry(window)
entry_a.place(x=100, y=50)

label_nhap_b = Label(window, text="Nhập số b:")
label_nhap_b.place(x=10, y=100)
entry_b = Entry(window)
entry_b.place(x=100, y=100)

label_nhap_c = Label(window, text="Nhập số c:")
label_nhap_c.place(x=10, y=150)
entry_c = Entry(window)
entry_c.place(x=100, y=150)

button_tinh_bac_nhat = Button(window, text="Tính phương trình bậc nhất", command=giai_phuong_trinh_bac_nhat)
button_tinh_bac_nhat.place(x=10, y=200)

button_tinh_bac_hai = Button(window, text="Tính phương trình bậc hai", command=giai_phuong_trinh_bac_hai)
button_tinh_bac_hai.place(x=200, y=200)

result_label = Label(window, text="")
result_label.place(x=10, y=250)

window.mainloop()
