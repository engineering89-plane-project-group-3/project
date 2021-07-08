from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from app.destinations import DestinationsDatabase
from app.aircraft import AircraftDatabase
from app.flight_trip import FlightTrip

def tuple_maker(list):
    temp = []
    for i, x in enumerate(list):
        temp.append(x[0])
    return [(tp, tp) for tp in temp]

class CreateFlightForm(FlaskForm):

    db = DestinationsDatabase()
    db.destinations_db_cursor.execute("SELECT destination FROM destinations")
    dests = db.destinations_db_cursor.fetchall()
    dests = tuple_maker(dests)

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    airc = db2.db_curs.fetchall()
    airc = tuple_maker(airc)

    flight_id = StringField('Flight ID', validators=[DataRequired()])
    aircraft_id = SelectField('Aircraft ID', choices=airc, validators=[DataRequired()])
    destination = SelectField('Destination', choices=dests, validators=[DataRequired()])
    departure_time = StringField('Departure Time', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ModifyFlightForm(FlaskForm):

    db = FlightTrip()
    db.flight_trip_db_cursor.execute("SELECT flight_id FROM flight_trip")
    flig = db.flight_trip_db_cursor.fetchall()
    flig = tuple_maker(flig)

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    airc = db2.db_curs.fetchall()
    airc = tuple_maker(airc)

    flight_id = SelectField('Flight ID', choices=flig, validators=[DataRequired()])
    submit = SubmitField('Load')
    aircraft_id = SelectField('Aircraft ID', choices=airc, validators=[DataRequired()])
    submit2 = SubmitField('Submit')


class BookFlightForm(FlaskForm):

    flight_id = StringField('Enter Flight ID', validators=[DataRequired()])
    passport_id = StringField('Enter passport id', validators=[DataRequired()])
    first_name = StringField('Enter first name', validators=[DataRequired()])
    last_name = StringField('Enter last name', validators=[DataRequired()])
    dob = StringField('Enter Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Submit')