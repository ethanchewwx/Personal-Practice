from turtle import Screen
from paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
line = Line()

scoreboard_r = Scoreboard()
scoreboard_r.goto(50, 250)
scoreboard_r.print_score()

scoreboard_l = Scoreboard()
scoreboard_l.goto(-50, 250)
scoreboard_l.print_score()

paddle_r = Paddle(380, 0)
paddle_l = Paddle(-380, 0)

ball = Ball()

screen.listen()
screen.onkeypress(fun=paddle_r.up, key="Up")
screen.onkeypress(fun=paddle_r.down, key="Down")
screen.onkeypress(fun=paddle_l.up, key="w")
screen.onkeypress(fun=paddle_l.down, key="s")

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()
    # screen.update()
    time.sleep(ball.starting_sleep)

    if (ball.xcor() > 360 and ball.distance(paddle_r) < 50) or (ball.xcor() < -360 and ball.distance(paddle_l) < 50):
        ball.bounce_paddle()

    if ball.xcor() > 390:
        scoreboard_l.update_score()
        ball.ball_reset()
        screen.update()
        time.sleep(1)

    if ball.xcor() < -390:
        scoreboard_r.update_score()
        ball.ball_reset()
        screen.update()
        time.sleep(1)

    if scoreboard_r.score == 10:
        scoreboard_r.game_over("R")
        is_game_on = False
    elif scoreboard_l.score == 10:
        scoreboard_r.game_over("L")
        is_game_on = False

screen.exitonclick()
