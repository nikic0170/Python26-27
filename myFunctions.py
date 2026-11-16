
import turtle
bob = turtle.Turtle()

#define triangle() fn
def triangle(dist):
    sides = 3
    angle = 360/sides
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)

#define square() fn
def square(dist):
    sides = 4
    angle = 360/sides
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)

#define pentagon() fn
def pentagon(dist):
    sides = 5
    angle = 360/sides
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
        
def circle(radius, border_color, fill_color):
    bob.pencolor(border_color)
    bob.fillcolor(fill_color)
    bob.begin_fill()
    bob.circle(radius)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
