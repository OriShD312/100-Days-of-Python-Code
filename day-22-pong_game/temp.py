from turtle import Turtle
TURTLE_SIZE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.snake_size = 3
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for coord in STARTING_POSITIONS:
            self.add_segment(coord)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def add_segment(self, position):
        part = Turtle("square")
        part.penup()
        part.color("white")
        part.goto(position)
        self.snake.append(part)


    def move(self):
        for part in range(len(self.snake) - 1, 0, -1):
            self.snake[part].goto(self.snake[part - 1].pos())
        self.snake[0].forward(TURTLE_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
