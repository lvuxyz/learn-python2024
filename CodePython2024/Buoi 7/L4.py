from turtle import *
window = Screen()
control = Turtle()
control.speed(500)

control.begin_fill()

control.color("red")
control.forward(50)
control.left(90)
control.forward(200)
control.left(90)
control.forward(50)
control.left(90)
control.forward(200)
control.left(90)
control.end_fill()
control.penup()
control.goto(-100, 80)
control.pendown()

control.begin_fill()
control.color("red")
control.forward(250)
control.left(90)
control.forward(50)
control.left(90)
control.forward(250)
control.left(90)
control.forward(50)
control.end_fill()

control.penup()
control.goto(-300, 80)
control.pendown()

control.begin_fill()
control.color("green")
control.circle(30)
control.end_fill()

control.penup()
control.goto(-300, -80)
control.pendown()

control.begin_fill()
control.color("green")
control.circle(30)
control.end_fill()

control.penup()
control.goto(-400, 25)
control.pendown()

control.begin_fill()
control.color("green")
control.forward(50)
control.left(90)
control.forward(250)
control.left(90)
control.forward(50)
control.left(90)
control.forward(250)
control.end_fill()

control.penup()
control.goto(0, -300)
control.pendown()

control.begin_fill()
control.color("yellow")
control.right(120)
control.forward(50)
control.right(90)
control.forward(250)
control.right(90)
control.forward(50)
control.right(90)
control.forward(250)
control.end_fill()

control.penup()
control.goto(250, -300)
control.pendown()

control.begin_fill()
control.color("yellow")
control.right(30)
control.forward(50)
control.left(90)
control.forward(250)
control.left(90)
control.forward(50)
control.left(90)
control.forward(250)
control.end_fill()

window.mainloop()