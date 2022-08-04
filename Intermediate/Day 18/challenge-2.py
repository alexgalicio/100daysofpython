import turtle as t

turtle = t.Turtle()
for _ in range(15):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = t.Screen()
screen.exitonclick()
