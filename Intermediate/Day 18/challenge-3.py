import turtle as t
import random

turtle = t.Turtle()
colors = ["azure4", "brown3", "DarkOrchid2", "cyan", "DodgerBlue", "chartreuse", "DarkOrange4"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for shape_sides in range(3, 10):
    turtle.color(random.choice(colors))
    draw_shape(shape_sides)

screen = t.Screen()
screen.exitonclick()
