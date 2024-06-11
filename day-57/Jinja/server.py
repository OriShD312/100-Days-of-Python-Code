import datetime
from flask import Flask, render_template
from pip._vendor import requests

CREATOR_NAME = "Ori Shahar"
CURRENT_YEAR = datetime.datetime.now().strftime("%Y")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", year=CURRENT_YEAR, name=CREATOR_NAME)

@app.route("/guess/<name>")
def mystic(name):
    params = {"name": name}
    gender = requests.get(url='https://api.genderize.io', params=params).json()["gender"]
    age = requests.get(url='https://api.agify.io', params=params).json()["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/dbc9fa5c2f51e61d5b23"
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts, post_num=num)

if __name__ == "__main__":
    app.run(debug=True)
