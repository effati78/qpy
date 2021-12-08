# سوال دو

import turtle

t = turtle.Turtle()
r = 20
for i in range(11):
    t.circle(r * i)
    t.up()
    t.sety((r * i) * (-1))
    t.down()

turtle.exitonclick()
