import turtle as t

turtle = t.Turtle()


def move_forwards():
    turtle.forward(20)


def move_backwards():
    turtle.backward(20)


def move_left():
    turtle.left(20)


def move_right():
    turtle.right(20)


def clear_screen():
    turtle.reset()


screen = t.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
