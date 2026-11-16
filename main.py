from myFunctions import *
from random import *
turtle.colormode(255)
turtle.bgcolor("black")

bob.speed(0)

for number in range(11):
    triangle(100)
    bob.right(95)

bob.penup()
bob.goto(-200,100)
bob.pendown()

bob.pensize(1)
bob.color("light blue")
for number in range(15):
    square(75)
    bob.right(95)

bob.penup()
bob.goto(220,-100)
bob.pendown()

bob.pensize(1)
bob.color("darkblue")
for number in range(15):
    pentagon(120)
    bob.right(95)

bob.penup()
bob.goto(220,-100)
bob.pendown()
bob.pensize(1)
bob.color("light blue")
for number in range(15):
    square(75)
    bob.right(95)

bob.penup()
bob.goto(400,-400)


bob.pendown()
bob.color("lightgreen")
for number in range(15):
    pentagon(120)
    bob.right(95)

bob.penup()
bob.goto(-300,300)
bob.pendown()
bob.color("green")
for number in range(15):
    pentagon(120)
    bob.right(95)

bob.penup()
bob.goto(-300,300)
bob.pendown()
bob.pensize(1)
bob.color("light green")
for number in range(15):
    square(75)
    bob.right(95)


bob.penup()
bob.goto(220,-100)
bob.penup()
bob.goto(200,300)
bob.pendown()
bob.color("violet")
for number in range(15):
    pentagon(120)
    bob.right(95)

bob.pendown()
bob.color("light pink")
for number in range(15):
    square(75)
    bob.right(95)

bob.penup()
bob.goto(-400,-400)
bob.pendown()
bob.color("purple")
for number in range(15):
    pentagon(120)
    bob.right(95)
bob.penup()
bob.goto(-400,-400)
bob.pendown()
bob.color("violet")
for number in range(15):
    pentagon(120)
    bob.right(95)
bob.penup()
bob.goto(400,-400)
bob.pendown()
bob.color("green")
for number in range(15):
    pentagon(120)
    bob.right(95)


import turtle
bob = turtle.Turtle()

n = 10
angle = 30

bob.speed(0)
for times in range (300):
    r = randint(255,255)
    g = randint (255,255)
    b = randint(255,255)
    border = "white"
    fill = (r,g,b)
    x = randint(-500,500)
    y = randint(-500,500)
    radius = randint(1,3)
    circle(radius, border, fill)
    jump(x,y)
