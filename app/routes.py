import datetime
from urllib import request
from flask import render_template, flash, redirect, url_for, session
from app import flask_app
from app.login_form import LoginForm
from app.login_database import LoginDatabase
from app.passenger_database import PassengerDatabase
from app.report_form import ReportForm
from app.create_flight_form import CreateFlightForm, ModifyFlightForm
from destinations import DestinationsDatabase
from aircraft import AircraftDatabase
from flight_trip import FlightTrip


@flask_app.route('/index')
@flask_app.route('/')
def index():
    return render_template('index.html', title='Home')

@flask_app.route('/login/', methods=['GET', 'POST'])
def login():

    try:
        if 'username' in session:
            return redirect(url_for('index'))
    except Exception as e:
        print(e)

    form = LoginForm()
    if form.validate_on_submit():
        db = LoginDatabase()
        db.users_db_cursor.execute("SELECT * FROM users WHERE username = (?)", [form.username.data])
        try:
            user = list(db.users_db_cursor.fetchone())
        except:
            flash("Invalid username or password")
            return redirect(url_for('login'))
        if not db.compare(form.username.data, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        session['username'] = form.username.data
        session['role'] = user[3]
        flash('Logged in successfully')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@flask_app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@flask_app.route('/report', methods=['GET', 'POST'])
def report():
    form = ReportForm()
    if form.validate_on_submit():
        db = PassengerDatabase()
        db.c.execute("SELECT first_name, last_name, passport_id FROM " + form.flight_id.data)
        data = db.c.fetchall()
        return render_template('report.html', title='Report', form=form, data=data)
    return render_template('report.html', title='Report', form=form)

#Create Flight
@flask_app.route('/createflight', methods=['GET', 'POST'])
def flight_management():
    form = CreateFlightForm()
    if form.validate_on_submit():
        dest_db = DestinationsDatabase()
        airc_db = AircraftDatabase()
        dest_db.destinations_db_cursor.execute('SELECT time FROM destinations WHERE destination = "{}"'.format(form.destination.data))
        time = dest_db.destinations_db_cursor.fetchone()

        arrival_time = datetime.strptime(time, "HH:mm") + datetime.strptime(form.departure_time.data, "HH:mm")

        FlightTrip.create_flight_trip(int(form.aircraft_id.data), airc_db.get_capacity(form.aircraft_id.data), form.destination.data, datetime.strptime(form.departure_time.data, "HH:mm"), arrival_time)
        flash("Flight has been created")
    return render_template('createflight.html', title='Flight Management', form=form)

# Modify Flight
@flask_app.route('/modifyflight', methods=['GET', 'POST'])
def modify_flight():

    form = ModifyFlightForm()
    if form.validate_on_submit():
        if form.submit.data:
            db = FlightTrip()
            db.flight_trip_db_cursor.execute('SELECT aircraft_id FROM flight_trip WHERE flight_id = "{}"'.format(form.flight_id.data))
            flash("Current plane is: " + db.flight_trip_db_cursor.fetchone())
        elif form.submit2.data:
            db = FlightTrip()
            db.flight_trip_db_cursor.execute('UPDATE flight_trip SET aircraft_id = ? WHERE flight_id = ?', (form.aircraft_id.data, form.flight_id.data))
            flash("Plane has been changed for the Flight")
        return render_template('modifyflight.html', title='Flight Management', form=form)
#Book Flight
