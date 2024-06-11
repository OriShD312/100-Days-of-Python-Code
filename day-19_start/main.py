import random
import turtle as t

colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
width = 500
height = 400
x_start = -0.9 * width / 2
y_positions = [-0.8 * height / 2, -0.5 * height / 2, -0.2 * height / 2,
               0.2 * height / 2, 0.5 * height / 2, 0.8 * height / 2]

all_turtles = []
is_race_on = False
scr = t.Screen()
scr.setup(width, height)
user_racer = scr.textinput("Pick racer", "Choose the color of the turtle you think is going to win")

for t_index in range(0, 6):
    new_turtle = t.Turtle("turtle")
    new_turtle.speed(6)
    new_turtle.penup()
    new_turtle.color(colors[t_index])
    new_turtle.goto(x_start, y_positions[t_index])
    all_turtles.append(new_turtle)

if user_racer:
    is_race_on = True

while is_race_on:

    for racer in all_turtles:
        rand_dist = random.randint(50, 100)
        racer.forward(rand_dist)
        if racer.xcor() > 0.8 * width / 2:
            is_race_on = False
            if user_racer == racer.pencolor().lower():
                print("Your turtle won!")
                break
            else:
                print(f"The {racer.pencolor()} turtle won, try again")
                break

scr.exitonclick()
