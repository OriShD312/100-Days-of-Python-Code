from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    location_url = URLField('Cafe Location on Google Maps(URL)', validators=[URL()])
    open_time = StringField('Opening Time e.g. 8:30AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:00PM', validators=[DataRequired()])
    coffee_rate = SelectField(label='Coffee Rating', choices=['✘' if i==0 else '☕' * (i) for i in range(6)], validators=[DataRequired()])
    wifi_rate = SelectField(label='WiFi Rating', choices=['✘' if i==0 else '💪' * (i) for i in range(6)], validators=[DataRequired()])
    socket_rate = SelectField(label='Power Socket Availabilty', choices=['✘' if i==0 else '🔌' * (i) for i in range(6)], validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    new_cafe = []
    if form.validate_on_submit():
        print("True")
        new_cafe.append(form.cafe_name.data)
        new_cafe.append(form.location_url.data)
        new_cafe.append(form.open_time.data)
        new_cafe.append(form.close_time.data)
        new_cafe.append(form.coffee_rate.data)
        new_cafe.append(form.wifi_rate.data)
        new_cafe.append(form.socket_rate.data)
        with open('100 Days of Code Python\day-62\cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_file.write('\n')
            csv.writer(csv_file).writerow(new_cafe)
        return redirect('cafes')
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('100 Days of Code Python\day-62\cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
