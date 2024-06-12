from turtle import *
window = Screen()
control = Turtle()
control.speed(100)
control.pensize(5)

def binh_hoa():
    control.color("black", "yellow")
    control.begin_fill()
    control.forward(80)
    control.left(90)
    control.forward(10)
    control.right(20)
    control.forward(60)
    control.left(40)
    control.forward(50)
    control.right(30)
    control.forward(70)
    control.left(100)
    control.forward(110)
    control.right(-100)
    control.forward(70)
    control.left(-30)
    control.forward(50)
    control.right(-40)
    control.forward(60)
    control.left(-19.5)
    control.forward(10)
    control.end_fill()
binh_hoa()

control.penup()
control.goto(-50, 300)
control.pendown()

control.begin_fill()
control.color("pink")
for i in range(9):
    control.circle(40, 100)
    control.right(60)
control.end_fill()

control.penup()
control.goto(-30, 310)
control.pendown()

control.begin_fill()
control.color("yellow")
for i in range(9):
    control.circle(30, 100)
    control.right(60)
control.end_fill()

control.penup()
control.goto(9, 340)
control.pendown()

control.begin_fill()
control.color("red")
control.circle(20)
control.end_fill()

control.penup()
control.goto(30, 180)
control.pendown()

control.begin_fill()
control.color("green")
control.right(180)
control.forward(70)
control.end_fill()


window.mainloop()