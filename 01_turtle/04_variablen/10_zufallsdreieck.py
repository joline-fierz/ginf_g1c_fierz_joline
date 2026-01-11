import turtle
import random as rd

d = rd.randrange(10, 26)
starke = rd.randrange(1, 6)

x_1 = rd.randrange(-100, 101)
x_2 = rd.randrange(-100, 101)
x_3 = rd.randrange(-100, 101)
y_1 = rd.randrange(-200, 176)
y_2 = rd.randrange(-200, 176)
y_3 = rd.randrange(-200, 176)

farbe_1 = "red"  # Die Variable farbe_1 speichert den String "red".
farbe_2 = "green"
farbe_3 = "blue"
turtle.pensize(starke)
turtle.pu()
turtle.goto(x_1, y_1)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(x_2, y_2)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(x_3, y_3)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(x_1, y_1)