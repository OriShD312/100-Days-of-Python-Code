import turtle
import pandas
from screenwriter import ScreenWriter

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_guesses = []
writer = ScreenWriter()

while len(correct_guesses) <= 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="Insert State name").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        all_states.remove(answer_state)
        correct_guesses.append(answer_state)
        writer.write_xy(data[data.state == answer_state])

df = pandas.DataFrame(all_states)
df.to_csv("States to learn.csv")
