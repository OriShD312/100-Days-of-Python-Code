from turtle import Turtle
NORTH_EAST = 45
NORTH_WEST = 135
SOUTH_WEST = 225
SOUTH_EAST = 315

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.up_down = True
        self.left_right = True
        self.move_y = 10
        self.move_x = 10
        self.game_speed = 0.02

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.game_speed *= 0.8

    def reset(self):
        self.game_speed = 0.02
        self.home()
