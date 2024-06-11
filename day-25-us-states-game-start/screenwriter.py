from turtle import Turtle


class ScreenWriter(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_xy(self, df):
        self.goto(int(df.x), int(df.y))
        self.write(df.state.item())
