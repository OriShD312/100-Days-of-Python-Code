from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snek = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snek.up, "w")
screen.onkey(snek.down, "s")
screen.onkey(snek.left, "a")
screen.onkey(snek.right, "d")

playing = True

while playing:
    screen.update()
    time.sleep(0.05)
    snek.move()

    # Detect collision with food
    if snek.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snek.extend()

    # Detect collision with wall
    if snek.head.xcor() > 295 or snek.head.xcor() < -295 or snek.head.ycor() > 295 or snek.head.ycor() < -295:
        scoreboard.reset()
        snek.reset()

    # Detect collision with self
    for segment in snek.snake[1:]:
        if snek.head.distance(segment) < 10:
            scoreboard.reset()
            snek.reset()

screen.exitonclick()
