from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 14, "bold")
GAMEOVER_FONT = ("Courier", 32, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.print_score()

    def update_score(self):
        # self.clear()
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(arg="Score: {0} High Score: {1}".format(self.score, self.highscore), move=False, align=ALIGNMENT, font=FONT)

    def scoreboard_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("highscore.txt", mode="w") as file:
            file.write(str(self.highscore))
        self.score = 0
        self.print_score()
