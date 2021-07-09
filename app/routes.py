from datetime import datetime, timedelta
from flask import render_template, flash, redirect, url_for, session
from app import flask_app
from app.login_form import LoginForm, RegisterForm
from app.login_database import LoginDatabase
from app.passenger_database import PassengerDatabase
from app.report_form import ReportForm
from app.flight_form import CreateFlightForm, ModifyFlightForm, BookFlightForm
from app.destinations_database import DestinationsDatabase
from app.aircraft_database import AircraftDatabase
from app.flight_trip import FlightTrip


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

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db = LoginDatabase()
        db.new_user(int(form.staff_id.data), str(form.username.data), str(form.password.data), str(form.role.data))
        flash("User registration complete!")
    return render_template('register.html', title='Register a new user', form=form)

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
        vals = form.departure_time.data.split(':')
        arrival_time = datetime.strptime(time[0], "%H:%M") + timedelta(hours=int(vals[0]), minutes=int(vals[1]))
        arrival_time = "{:d}:{:02d}".format(arrival_time.hour, arrival_time.minute)
        departure_time = datetime.strptime(form.departure_time.data, "%H:%M")
        departure_time = "{:d}:{:02d}".format(departure_time.hour, departure_time.minute)

        ft = FlightTrip()
        ft.create_flight_trip(form.flight_id.data, form.aircraft_id.data, airc_db.get_capacity(form.aircraft_id.data), form.destination.data, departure_time, arrival_time)
        flash("Flight has been created")
    return render_template('createflight.html', title='Create Flight', form=form)

# Modify Flight
@flask_app.route('/modifyflight', methods=['GET', 'POST'])
def modify_flight():

    form = ModifyFlightForm()
    if form.validate_on_submit():
        if form.submit.data:
            db = FlightTrip()
            db.flight_trip_db_cursor.execute('SELECT aircraft_id FROM flight_trip WHERE flight_id = "{}"'.format(form.flight_id.data))
            return render_template('modifyflight.html', title='Flight Management', form=form, data=db.flight_trip_db_cursor.fetchone()[0])
        elif form.submit2.data:
            db = FlightTrip()
            db.flight_trip_db_cursor.execute('UPDATE flight_trip SET aircraft_id = ? WHERE flight_id = ?', (form.aircraft_id.data, form.flight_id.data))
            flash("Plane has been changed for the Flight")
    return render_template('modifyflight.html', title='Modify Flight', form=form)
#Book Flight

#Book Flight
@flask_app.route('/bookflight', methods=['GET', 'POST'])
def book_flight():
    form = BookFlightForm()
    if form.validate_on_submit():
        db = PassengerDatabase()
        db.add_passenger(str(form.flight_id.data), str(form.passport_id.data), str(form.first_name.data), str(form.last_name.data), str(form.dob.data))
        flash("Passenger has been added to list")
    return render_template('bookflight.html', title='Passenger flight booking', form=form)
