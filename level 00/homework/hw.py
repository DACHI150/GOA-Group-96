from turtle import *


#we want to paint a house

#step 1: draw a square


width(7)
speed(30)

color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(140,140)

pendown()
color("brown")
left(120)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)

penup()
goto(153,159)
pendown()
forward(15)

penup()
goto(145,152)
left(90)
pendown()
forward(20)

penup()
goto(20,160)
pendown()

right(90)
forward(20)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(26)

penup()
goto(33,160)
pendown()
left(90)
forward(20)
penup()
goto(25,152)
pendown()
left(90)
forward(20)




exitonclick()