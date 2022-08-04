import turtle as t

turtle = t.Turtle()
for _ in range(4):
    turtle.right(90)
    turtle.forward(100)

screen = t.Screen()
screen.exitonclick()
