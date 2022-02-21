from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x_position, y_position)

    def up(self):
        if self.ycor() < 230:
            new_y = self.ycor() + 20
            current_x = self.xcor()
            self.goto(current_x, new_y)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            current_x = self.xcor()
            self.goto(current_x, new_y)

# starting_positions_player = [(380, 20), (380, 0), (380, -20)]
# starting_positions_comp = [(-390, 20), (-390, 0), (-390, -20)]


# class Paddle:
#
#     def __init__(self):
#         self.all_squares = []
#         self.create_paddle_player()
#         # self.create_paddle_comp()
#         self.head = self.all_squares[0]
#         self.end = self.all_squares[-1]
#
#     def create_paddle_player(self):
#         for position in starting_positions_player:
#             square = Turtle(shape="square")
#             square.color("white")
#             square.penup()
#             square.goto(position)
#             self.all_squares.append(square)
#
#     def up(self):
#         if self.head.ycor() < 280:
#             for i in range(len(self.all_squares)):
#                 self.all_squares[i].setheading(90)
#                 self.all_squares[i].forward(20)
#
#     def down(self):
#         if self.all_squares[-1].ycor() > -280:
#             for i in range(len(self.all_squares) - 1, -1 , -1):
#                 self.all_squares[i].setheading(270)
#                 self.all_squares[i].forward(20)
#
