from turtle import Turtle


class PlayingSurface(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(390, 300)
        self.color("white")
        self.hideturtle()
        self.pensize(5)
        for _ in range(4):
            if _ % 2 == 0:
                self.right(90)
                self.forward(600)
            else:
                self.right(90)
                self.forward(780)

    def net(self):
        self.penup()
        self.setheading(90)
        self.goto(0, -308)
        self.color("white")
        for _ in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
