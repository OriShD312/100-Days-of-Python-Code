from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login_page():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]
        return f"<h1>Your name is {name} and your password is {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
