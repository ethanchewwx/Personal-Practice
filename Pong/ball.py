from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.starting_sleep = 0.05
        self.speed(1)
        self.setheading(random.randint(0, 359))

    def move(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.setheading(360 - self.heading())
            self.starting_sleep *= 0.9
        self.forward(10)

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.starting_sleep *= 0.9
        self.forward(10)

    def ball_reset(self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 359))
        self.starting_sleep = 0.1
