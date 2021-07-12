from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from app.destinations_database import DestinationsDatabase
from app.aircraft_database import AircraftDatabase
from app.flight_trip import FlightTrip


def tuple_maker(given_list):
    return [('', x[0]) for x in given_list]


class CreateFlightForm(FlaskForm):
    db = DestinationsDatabase()
    db.destinations_db_cursor.execute("SELECT destination FROM destinations")
    destinations = tuple_maker(db.destinations_db_cursor.fetchall())

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    aircraft = tuple_maker(db2.db_curs.fetchall())

    flight_id = StringField(validators=[DataRequired()])
    aircraft_id = SelectField(choices=aircraft, validators=[DataRequired()])
    destination = SelectField(choices=destinations, validators=[DataRequired()])
    departure_time = StringField(validators=[DataRequired()])
    price = StringField(validators=[DataRequired()])
    submit = SubmitField()


class ModifyFlightForm(FlaskForm):
    db = FlightTrip()
    db.flight_trip_db_cursor.execute("SELECT flight_id FROM flight_trip")
    flights = tuple_maker(db.flight_trip_db_cursor.fetchall())

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    aircraft = tuple_maker(db2.db_curs.fetchall())

    flight_id = SelectField(choices=flights, validators=[DataRequired()])
    submit = SubmitField()
    aircraft_id = SelectField(choices=aircraft, validators=[DataRequired()])
    submit2 = SubmitField()


class BookFlightForm(FlaskForm):
    flight_id = StringField(validators=[DataRequired()])
    passport_id = StringField(validators=[DataRequired()])
    first_name = StringField(validators=[DataRequired()])
    last_name = StringField(validators=[DataRequired()])
    dob = StringField(validators=[DataRequired()])
    submit = SubmitField()
