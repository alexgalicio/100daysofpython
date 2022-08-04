import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
color_list = [(211, 160, 84), (188, 175, 33), (172, 50, 71), (195, 70, 37), (229, 208, 111), (232, 72, 38),
              (149, 30, 46), (126, 165, 193), (66, 34, 55), (210, 133, 163), (212, 68, 111), (55, 49, 107),
              (59, 83, 149), (41, 39, 68), (51, 134, 95), (113, 182, 158), (142, 32, 27), (56, 164, 185),
              (46, 158, 104), (80, 52, 35), (152, 203, 219), (229, 166, 183), (89, 102, 176), (235, 172, 162),
              (172, 207, 183), (182, 183, 217)]

turtle.hideturtle()
turtle.penup()
turtle.speed('fastest')
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

numbers_of_dots = 100

for _dot_count in range(1, numbers_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)

    if _dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()
