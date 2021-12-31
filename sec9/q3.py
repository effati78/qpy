# Exam
# سوال سه

import turtle

ws = turtle.Screen()
pen = turtle.Turtle()
pen.fillcolor('yellow')
pen.begin_fill()

for i in range(8):
	pen.forward(100)
	pen.left(45)

pen.end_fill()
turtle.exitonclick()