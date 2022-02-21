from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

score = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect food collision using distance function
    if snake.head.distance(food) < 15:
        # print("collided")
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.scoreboard_reset()
        snake.snake_reset()

    for square in snake.all_squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.scoreboard_reset()
            snake.snake_reset()


screen.exitonclick()
