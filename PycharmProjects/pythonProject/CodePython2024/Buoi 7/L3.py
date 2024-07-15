from turtle import *

window = Screen()
control = Turtle()
control.color("green")

control.begin_fill()

control.left(40)
control.forward(140)
control.circle(70, 210)
control.right(140)
control.circle(70, 210)
control.forward(140)

control.end_fill()


control.penup()
control.goto(130, 0)
control.pendown()

control.color("pink")
control.begin_fill()
control.left(80)
control.forward(133)
control.circle(70, 214)
control.right(140)
control.circle(70, 214)
control.forward(133)
control.end_fill()

window.mainloop()