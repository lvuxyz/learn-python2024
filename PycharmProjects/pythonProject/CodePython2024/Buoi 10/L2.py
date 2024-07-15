import math
from tkinter import *
from turtle import RawTurtle, ScrolledCanvas, TurtleScreen
from tkinter import messagebox

window = Tk()
window.title("app cua vũ dz")
window.geometry("720x480")

def tinh_toan():
    try:
        a = int(entry_nhap_a.get())
        b = int(entry_nhap_b.get())

        tong = a + b
        hieu = a - b
        tich = a * b
        thuong = a / b if b != 0 else "Lỗi: chia cho 0"

        giai_thua_a = math.factorial(a)
        giai_thua_b = math.factorial(b)

        list_box.delete(0, END)
        list_box.insert(END, f"Tổng của {a} và {b} là: {tong}")
        list_box.insert(END, f"Hiệu của {a} và {b} là: {hieu}")
        list_box.insert(END, f"Tích của {a} và {b} là: {tich}")
        list_box.insert(END, f"Thương của {a} và {b} là: {thuong}")
        list_box.insert(END, f"Giai thừa của {a} là: {giai_thua_a}")
        list_box.insert(END, f"Giai thừa của {b} là: {giai_thua_b}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")


def giai_phuong_trinh():
    try:
        a = float(entry_nhap_a.get())
        b = float(entry_nhap_b.get())

        if a == 0:
            if b == 0:
                result = "Phương trình vô số nghiệm"
            else:
                result = "Phương trình vô nghiệm"
        else:
            x = -b / a
            result = f"Nghiệm của phương trình {a}x + {b} = 0 là: x = {x}"

        list_box.delete(0, END)
        list_box.insert(END, result)

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

def tinh_hang_dang_thuc():
    try:
        a = int(entry_nhap_a.get())
        b = int(entry_nhap_b.get())
        c = int(entry_nhap_c.get())

        identity1 = a**2 - b**2
        identity2 = (a + b)**2
        identity3 = (a - b)**2
        identity4 = a**2 + b**2

        list_box.delete(0, END)
        list_box.insert(END, "Hằng đẳng thức:")
        list_box.insert(END, f"1. a^2 - b^2 = (a + b)(a - b) = {identity1} = {a + b}({a - b})")
        list_box.insert(END, f"2. (a + b)^2 = a^2 + 2ab + b^2 = {identity2} = {a**2 + 2*a*b + b**2}")
        list_box.insert(END, f"3. (a - b)^2 = a^2 - 2ab + b^2 = {identity3} = {a**2 - 2*a*b + b**2}")
        list_box.insert(END, f"4. a^2 + b^2 = (a + b)^2 - 2ab = {identity4} = {(a + b)**2 - 2*a*b}")

    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

def ve_tam_giac():
    control.reset()
    control.begin_fill()
    control.color("red")
    for _ in range(3):
        control.forward(100)
        control.left(120)
    control.end_fill()


def ve_may_tinh():
    control.reset()
    control.begin_fill()
    for i in range(4):
        control.color("yellow", "red")
        control.forward(100)
        control.left(90)
    control.end_fill()

    control.penup()
    control.goto(10, 10)
    control.pendown()

    control.begin_fill()
    for i in range(4):
        control.color("white")
        control.forward(80)
        control.left(90)
    control.end_fill()

    control.penup()
    control.goto(40, 0)
    control.pendown()

    control.begin_fill()
    control.color("black")
    control.right(90)
    control.forward(10)
    control.left(90)
    control.forward(20)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.end_fill()

    control.penup()
    control.goto(40, -10)
    control.pendown()

    control.forward(10)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(40)
    control.left(90)
    control.forward(10)
    control.left(90)
    control.forward(10)

    control.penup()
    control.goto(-20, 0)
    control.pendown()

    control.forward(40)
    control.right(90)
    control.forward(100)
    control.right(90)
    control.forward(40)
    control.right(90)
    control.forward(100)

    control.penup()
    control.goto(-20, 20)
    control.pendown()

    control.right(90)
    control.forward(40)

    control.penup()
    control.goto(-20, 40)
    control.pendown()

    control.forward(40)
    control.right(90)

    control.penup()
    control.goto(-30, 30)
    control.pendown()

    control.begin_fill()
    control.color("black")
    control.circle(3)
    control.end_fill()
    control.hideturtle()

def thoat_chuong_trinh():
    window.quit()


label_nhap_a = Label(window, text="Nhập số a: ")
label_nhap_a.place(x=10, y=20)

label_nhap_b = Label(window, text="Nhập số b: ")
label_nhap_b.place(x=10, y=50)

label_nhap_c = Label(window, text="Nhập số c: ")
label_nhap_c.place(x=10, y=80)

entry_nhap_a = Entry(window)
entry_nhap_a.place(x=100, y=20)

entry_nhap_b = Entry(window)
entry_nhap_b.place(x=100, y=50)

entry_nhap_c = Entry(window)
entry_nhap_c.place(x=100, y=80)

list_box = Listbox(window, width=50, height=10)
list_box.place(x=400, y=20)

button_tinh_toan = Button(window, text="Tính toán", command=tinh_toan)
button_tinh_toan.place(x=10, y=120, width=100, height=25)

button_phuong_trinh = Button(window, text="Giải phương trình", command=giai_phuong_trinh)
button_phuong_trinh.place(x=120, y=120, width=120, height=25)

button_hang_dang_thuc = Button(window, text="Hằng đẳng thức", command=tinh_hang_dang_thuc)
button_hang_dang_thuc.place(x=250, y=120, width=120, height=25)

button_tam_giac = Button(window, text="Vẽ tam giác", command=ve_tam_giac)
button_tam_giac.place(x=10, y=160, width=100, height=25)

button_may_tinh = Button(window, text="Vẽ máy tính", command=ve_may_tinh)
button_may_tinh.place(x=120, y=160, width=120, height=25)

button_thoat = Button(window, text="Thoát", command=thoat_chuong_trinh)
button_thoat.place(x=250, y=160, width=100, height=25)


canvas = ScrolledCanvas(window)
canvas.place(x=10, y=200, width=300, height=200)

screen = TurtleScreen(canvas)
control = RawTurtle(screen)

window.mainloop()
