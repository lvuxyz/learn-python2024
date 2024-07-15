from turtle import *
window = Screen()
control = Turtle()

control.begin_fill()
for i in range(4):
    control.color("yellow","red")
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
control.goto(300, 100)
control.pendown()

window.mainloop()
