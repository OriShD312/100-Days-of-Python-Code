import random
from flask import Flask

correct_guess = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def homepage():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media4.giphy.com/media/IsfrRWvbUdRny/200.webp?cid=790b7611huiuegogn5o3auhkjpj0cj2gyb7hv0geb2jb7ju5&ep=v1_gifs_search&rid=200.webp&ct=g>'


@app.route("/<int:number>")
def guess_page(number):
    if number > correct_guess:
        return '<h1 color=purple>Too high! Try again</h1>' \
               '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
    elif number < correct_guess:
        return '<h1 color=red>Too low! Try again</h1>' \
               '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'
    else:
        return '<h1 color=green>You found me!</h1>' \
               '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'


if __name__ == "__main__":
    app.run(debug=True)
