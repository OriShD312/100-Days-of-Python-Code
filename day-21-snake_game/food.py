import random
from turtle import Turtle
FOOD_SIZE = 0.5
SCREEN_BOUNDS = 280

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(FOOD_SIZE, FOOD_SIZE)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-SCREEN_BOUNDS, SCREEN_BOUNDS), random.randint(-SCREEN_BOUNDS, SCREEN_BOUNDS))
