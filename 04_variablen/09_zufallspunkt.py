import turtle

d = 10 # Die Variable d speichert den Int (kurz für Integer) 10.
starke = 2
farbe_1 = "red" # Die Variable farbe_1 speichert den String "red"
farbe_2 = "green"
farbe_3 = "blue"
turtle.pensize(starke)
turtle.pu()
turtle.goto(50, 0)
turtle.pd()
turtle.pencolor(farbe_1)
turtle.dot(d)
turtle.goto(100, 0)
turtle.pencolor(farbe_2)
turtle.dot(d)
turtle.goto(75, 175)
turtle.pencolor(farbe_3)
turtle.dot(d)
turtle.goto(50, 0)
