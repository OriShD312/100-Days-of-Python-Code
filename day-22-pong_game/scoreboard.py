from turtle import Turtle
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = {"left player": 0, "right player": 0}
        self.hideturtle()
        self.goto(0, 200)
        self.color("white")
        self.show_score()

    def update_score(self, player):
        self.score[player] += 1
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"{self.score['left player']}    {self.score['right player']}", False, align="center", font=FONT)
