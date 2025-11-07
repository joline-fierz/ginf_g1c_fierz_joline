import random
import turtle 

d = random.randrange(10, 26)
starke = random.randrange(1, 6)
x1 = random.randrange(-100, 101)
x2 = random.randrange(-100, 101)
x3 = random.randrange(-100, 101)
y1 = random.randrange(-200, 176)
y2 = random.randrange(-200, 176)
y3 = random.randrange(-200, 176)
farbe_1 = "red"
farbe_2 = "green"
farbe_3 = "blue"
turtle.pensize(starke)
turtle.pu()
turtle.goto(x1, y1)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(x2, y2)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(x3, y3)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(x1, y1)


