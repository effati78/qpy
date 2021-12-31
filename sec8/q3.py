# سوال سه

import turtle

def NestedSquare(tDocsTurtle,side, delta):
    if side < delta:
        return 
 
    tDocsTurtle.penup()
    tDocsTurtle.goto(-(side-delta)/2, -(side-delta)/2)
    tDocsTurtle.pendown()
    
    for i in range(4):
        tDocsTurtle.forward(side)
        tDocsTurtle.left(90) 

    NestedSquare(tDocsTurtle,side-delta,delta)
    
t = turtle.Turtle()
NestedSquare(t,1200,60) 
turtle.exitonclick()
