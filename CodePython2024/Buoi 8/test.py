'''from turtle import *

# Thiết lập màn hình
window = Screen()
window.bgcolor("lightgreen")  # Màu nền xanh nhạt
control = Turtle()
control.speed(1)  # Tốc độ vẽ chậm hơn để dễ quan sát

# Vẽ thân xe
control.penup()
control.goto(-100, 0)
control.pendown()
control.color("red")  # Màu đỏ cho thân xe
control.begin_fill()
control.forward(200)
control.left(90)
control.forward(60)
control.left(90)
control.forward(200)
control.left(90)
control.forward(60)
control.left(90)
control.end_fill()

# Vẽ cửa sổ
control.penup()
control.goto(-70, 30)
control.pendown()
control.color("black")  # Màu đen cho cửa sổ
control.setheading(0)
for _ in range(2):
    control.forward(100)
    control.left(90)
    control.forward(40)
    control.left(90)

# Vẽ bánh xe trước
control.penup()
control.goto(-80, -30)
control.pendown()
control.color("gray")  # Màu xám cho bánh xe
control.begin_fill()
control.circle(20)
control.end_fill()

# Vẽ bánh xe sau
control.penup()
control.goto(80, -30)
control.pendown()
control.color("gray")  # Màu xám cho bánh xe
control.begin_fill()
control.circle(20)
control.end_fill()

# Kết thúc
window.mainloop()'''
from turtle import *

# Thiết lập màn hình
screen = Screen()
screen.bgcolor("lightgray")  # Màu nền xám nhạt

# Tạo đối tượng Turtle
stick_figure = Turtle()
stick_figure.speed(1)  # Tốc độ vẽ chậm để dễ quan sát
stick_figure.pensize(3)  # Đặt kích thước viết là 3 pixel

# Vẽ đầu
stick_figure.penup()
stick_figure.goto(0, 100)
stick_figure.pendown()
stick_figure.color("black")  # Màu đen cho người que
stick_figure.circle(20)

# Vẽ thân
stick_figure.penup()
stick_figure.goto(0, 80)
stick_figure.pendown()
stick_figure.left(90)
stick_figure.forward(100)

# Vẽ tay trái
stick_figure.right(135)
stick_figure.forward(50)

# Vẽ tay phải
stick_figure.penup()
stick_figure.goto(0, 80)
stick_figure.pendown()
stick_figure.right(45)
stick_figure.forward(50)

# Vẽ chân trái
stick_figure.penup()
stick_figure.goto(0, -20)
stick_figure.pendown()
stick_figure.right(45)
stick_figure.forward(50)

# Vẽ chân phải
stick_figure.penup()
stick_figure.goto(0, -20)
stick_figure.pendown()
stick_figure.left(90)
stick_figure.forward(50)

# Kết thúc
screen.mainloop()