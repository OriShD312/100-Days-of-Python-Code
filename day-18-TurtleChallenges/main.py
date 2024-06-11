import turtle as t
from random import *

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


tim.speed(0)

for theta in range(0, 361, 5):
    tim.setheading(theta)
    tim.color(random_color())
    tim.circle(100)

scr = t.Screen()
scr.exitonclick()
