import turtle as t
import random

turtle = t.Turtle()
colors = ["azure4", "brown3", "DarkOrchid2", "cyan", "DodgerBlue", "chartreuse", "DarkOrange4"]

directions = [0, 90, 180, 270]
turtle.speed(0)
turtle.pensize(10)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    for _ in range(200):
        turtle.forward(30)
        turtle.setheading(random.choice(directions))
        turtle.color(random_color())


random_walk()

screen = t.Screen()
screen.exitonclick()
