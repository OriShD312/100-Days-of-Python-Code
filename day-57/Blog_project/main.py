from flask import Flask, render_template
from pip._vendor import requests

app = Flask(__name__)

all_posts = requests.get(url="https://api.npoint.io/dbc9fa5c2f51e61d5b23").json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    return render_template("post.html", post=all_posts[blog_id-1])

if __name__ == "__main__":
    app.run(debug=True)
