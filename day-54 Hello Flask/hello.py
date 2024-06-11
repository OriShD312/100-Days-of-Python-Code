from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def bolden():
        return f'<b>{function()}</b>'
    return bolden


def make_emphasis(function):
    def italic():
        return f'<em>{function()}</em>'
    return italic


def make_underlined(function):
    def underline():
        return f'<u>{function()}</u>'
    return underline


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"


@app.route("/bye")
def say_bye():
    return '<h1>Bye!</h1>' \
           '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTJncDlleTZvZmF5aXRhazR5dHFtNW1odHE1eW01bzByMDBtZG4xdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Bht33KS4YXaHS5ABOP/giphy.gif" width=200px>'

if __name__ == "__main__":
    app.run(debug=True)
