from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 32, "bold")
GAMEOVER_FONT = ("Courier", 48, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()

    def print_score(self):
        # self.goto(-50, 250)
        self.write(arg="{}".format(self.score), move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def game_over(self, player):
        self.goto(0, 0)
        self.write(arg="GAME OVER. {} WINS!".format(player), move=False, align=ALIGNMENT, font=GAMEOVER_FONT)
