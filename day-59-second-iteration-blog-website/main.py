from flask import Flask, render_template, request
from pip._vendor import requests
from smtplib import SMTP

RECEIVER_EMAIL = "YOUR EMAIL"
RECEIVER_PASSWORD = "YOUR PASSWORD"

app = Flask(__name__)
blog_url = "https://api.npoint.io/c5f5befb0727a34587b8"
all_posts = requests.get(url=blog_url).json()

@app.route("/")
def homepage():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def get_about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        email = request.form["email"]
        message = request.form["message"]
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=RECEIVER_EMAIL, password=RECEIVER_PASSWORD)
            connection.sendmail(from_addr=email,
                                to_addrs=RECEIVER_EMAIL,
                                msg=f"""Subject: I need help\n\n
                                Name:{name}
                                Email: {email}
                                Phone Number:{phone}
                                Message: {message}"""
                                )
    return render_template("contact.html")

@app.route("/blog/<int:num>")
def get_post(num):
    return render_template("post.html", post=all_posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)
