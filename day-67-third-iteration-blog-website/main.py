from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
import os
import pathlib


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config['CKEDITOR_PKG_TYPE'] = 'full'
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
db_folder = str(os.path.join(pathlib.Path(__file__).parent.resolve(), 'instance')).replace('\\', '/')
if not os.path.exists(db_folder):
    os.mkdir(db_folder)
db_uri = f'sqlite:///{db_folder}/posts.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

class NewPostForm(FlaskForm):
    post_title = StringField(label='Post title', validators=[DataRequired()])
    post_subtitle = StringField(label='Post subtitle', validators=[DataRequired()])
    post_author = StringField(label='Post author', validators=[DataRequired()])
    post_bg_img_url = StringField(label='Post background image', validators=[DataRequired()])
    post_body = CKEditorField('Post content', validators=[DataRequired()])
    submit = SubmitField(label='Submit Post')

with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id==post_id)).scalar()
    print(requested_post)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=['GET', 'POST'])
def new_post():
    form = NewPostForm()
    if form.validate_on_submit():
        post_title = form.post_title.data
        post_subtitle = form.post_subtitle.data
        post_author = form.post_author.data
        post_bg_img_url = form.post_bg_img_url.data
        post_body = form.post_body.data
        new_post = BlogPost(
            title = post_title,
            subtitle = post_subtitle,
            date = date.today().strftime('%B %d, %Y'),
            body = post_body,
            author = post_author,
            img_url = post_bg_img_url,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html', form=form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    form = NewPostForm(
        post_title = post_to_edit.title,
        post_subtitle = post_to_edit.subtitle,
        post_author = post_to_edit.author,
        post_bg_img_url = post_to_edit.img_url,
        post_body = post_to_edit.body,
    )
    if form.validate_on_submit():
        post_to_edit.title = form.post_title.data
        post_to_edit.subtitle = form.post_subtitle.data
        post_to_edit.body = form.post_body.data
        post_to_edit.author = form.post_author.data
        post_to_edit.img_url = form.post_bg_img_url.data
        db.session.commit()
        return redirect(url_for('show_post', post_id=post_id))
    return render_template('make-post.html', form=form)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
