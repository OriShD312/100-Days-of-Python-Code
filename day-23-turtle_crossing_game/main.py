from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time


player_score = 0

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

p = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(p.move_up, "w")

playing = True
while playing:
    time.sleep(0.05)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if p.is_at_finish_line():
        p.beginning()
        car_manager.lvl_up()
        scoreboard.increase_lvl()

    for car in car_manager.all_cars:
        if car.distance(p) < 20:
            playing = False
            scoreboard.game_over()


screen.exitonclick()
