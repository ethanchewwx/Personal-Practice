from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.width(5)
        self.color("white")
        self.penup()
        self.goto(x=0, y=295)
        self.setheading(270)
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)