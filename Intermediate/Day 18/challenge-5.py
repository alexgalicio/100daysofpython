import turtle as t
import random

turtle = t.Turtle()
turtle.speed('fastest')
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


while True:
    turtle.color(random_color())
    turtle.circle(100)
    turtle.left(5)
    if turtle.heading() < 1:
        turtle.hideturtle()
        break

screen = t.Screen()
screen.exitonclick()
