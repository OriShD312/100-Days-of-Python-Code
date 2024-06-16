from flask import Flask, render_template
from wtforms import PasswordField, SubmitField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "app_secret_key"

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password must be at least 8 characters long")])
    submit = SubmitField(label="Login")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            print(form.email.data)
            return render_template('/success.html')
        else:
            print("FAIL")
            return render_template('/denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
