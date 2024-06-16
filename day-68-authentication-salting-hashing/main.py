from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError
import pathlib
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
db_folder = str(os.path.join(pathlib.Path(__file__).parent.resolve(), 'instance')).replace('\\', '/')
if not os.path.exists(db_folder):
    os.mkdir(db_folder)
db_uri = f'sqlite:///{db_folder}/users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(
            request.form['password'],
            method='pbkdf2:sha256',
            salt_length=8
            )
        new_user = User(
            name = request.form['name'].capitalize(),
            email = request.form['email'],
            password = hashed_password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('secrets'))
        except IntegrityError:
            flash('A user with that email is already registered in the system, try to log in instead')
            db.session.rollback()
        
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_email = request.form['email']
        login_password = request.form['password']

        assumed_user = db.session.execute(db.select(User).where(User.email==login_email)).scalar()

        if assumed_user:
            if check_password_hash(assumed_user.password, login_password):
                login_user(assumed_user)
                return redirect(url_for('secrets'))
            else:
                flash('Incorrect Password, please try again')
        else:
            flash('Email not found, please try again')

    return render_template("login.html")


@app.route('/secrets', methods=['GET', 'POST'])
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static' , 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
