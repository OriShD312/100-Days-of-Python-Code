from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
import pathlib
import os

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db_folder = str(os.path.join(pathlib.Path(__file__).parent.resolve(), 'instance')).replace('\\', '/')
if not os.path.exists(db_folder):
    os.mkdir(db_folder)
db_uri = f'sqlite:///{db_folder}/books.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    Author: Mapped[str] = mapped_column(String(250), nullable=False)
    Rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

all_books = []

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.Rating)).scalars()
    return render_template('index.html', book_list=all_books)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Book(
            Title=request.form['title'],
            Author=request.form['author'],
            Rating=request.form['rating'],
        )
        db.session.add(book)
        db.session.commit()
        all_books.append(book)
        return redirect('/')
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)

