from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.all_squares = []
        self.create_snake()
        self.head = self.all_squares[0]

    def create_snake(self):
        for positions in STARTING_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        # square.goto(x=-20*index, y=0)
        square.goto(position)
        self.all_squares.append(square)

    def extend(self):
        self.add_segment(self.all_squares[-1].position())

    def move(self):
        for j in range(len(self.all_squares) - 1, 0, -1):
            # self.all_squares[j].goto(self.all_squares[j-1].xcor(), self.all_squares[j-1].ycor())
            self.all_squares[j].goto(self.all_squares[j-1].position())
        # if self.all_squares[0].xcor() == 280:
        #     self.all_squares[0].goto(-280, self.all_squares[0].ycor())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def snake_reset(self):
        for squares in self.all_squares:
            squares.goto(1000, 1000)
        self.all_squares.clear()
        self.create_snake()
        self.head = self.all_squares[0]
