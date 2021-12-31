# سوال چهار

import turtle

def draw(t, radius, jd, step = 3):  
    t.circle(radius, jd, steps = step) 

turtle.setup(640, 480)
pen = turtle.Turtle()
pen.hideturtle()
pen.pensize(1)  

for i in range(22):
    draw(pen, 1 + i * 7, min(180, i * 60))

turtle.exitonclick()