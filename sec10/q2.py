# import package
import turtle

pen = turtle.Turtle()

pen.fillcolor('green')
pen.begin_fill()
for i in range(6):
    pen.forward(75)
    pen.left(60)
pen.end_fill()

pen.seth(-185)
pen.forward(255)

pen.fillcolor('blue')
pen.begin_fill()
def draw(rad):
    for i in range(2):
        pen.circle(rad,90)
        pen.circle(rad//2,90)

pen.seth(-45)
draw(110)
pen.end_fill()

turtle.exitonclick()