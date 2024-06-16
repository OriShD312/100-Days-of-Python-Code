import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, inspect
from sqlalchemy.exc import IntegrityError, OperationalError
import os
import pathlib

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
db_folder = str(os.path.join(pathlib.Path(__file__).parent.resolve(), 'instance')).replace('\\', '/')
if not os.path.exists(db_folder):
    os.mkdir(db_folder)
db_uri = f'sqlite:///{db_folder}/cafes.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random')
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return random_cafe.to_dict()

@app.route('/all')
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route('/search')
def search_cafe():
    loc = request.args.get('loc').capitalize()
    result = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    cafes_from_location = result.scalars().all()
    if cafes_from_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_from_location])
    return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location"})

# HTTP POST - Create Record
@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    empty_fields = []

    for field_name, value in request.form.items():
        if value == '' and field_name != 'coffee_price':
            empty_fields.append(field_name)
            
    if empty_fields:
        return jsonify(response={'Bad Request':f'The following fields were left empty: {", ".join(empty_fields)}'})

    new_cafe = Cafe(
        name = request.form['name'],
        map_url = request.form['map_url'],
        img_url = request.form['img_url'],
        location = request.form['loc'],
        seats = request.form['seats'],
        has_toilet = bool(request.form['toilet']),
        has_wifi = bool(request.form['wifi']),
        has_sockets = bool(request.form['sockets']),
        can_take_calls = bool(request.form['calls']),
        coffee_price = request.form['coffee_price'],
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={'Success':'Successfully added new cafe'})
    except IntegrityError as e:
        return jsonify(response={'Error':'Cafe name already in list'})

# HTTP PUT/PATCH - Update Record
@app.route('/update-price/<cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get('new_price')
    if Cafe.query.filter_by(id=cafe_id).first():
        cafe_to_update = db.get_or_404(Cafe, cafe_id)
        if new_price:
            cafe_to_update.coffee_price = new_price
            db.session.commit()
            return jsonify(response={'Success':f'Price for {cafe_to_update.name} updated successfully'})
        else:
            return jsonify(response={'Error':'No valid price or id inputted'}), 404
    return jsonify(response={'ID Error':'The ID entered is not present in the database'}), 404
    

# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def remove_cafe(cafe_id):
    api_key = request.args.get('api-key')
    if api_key == 'TopSecretAPIKey':
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify({'Success':'Entry successfully removed from database'})
        return jsonify({'ID Error':'The ID entered is not present in the database'}), 404
    return jsonify({'Authorization Error':'Sorry, that is not allowed. Make sure you have the correct API key'}), 403

if __name__ == '__main__':
    app.run(debug=True)
