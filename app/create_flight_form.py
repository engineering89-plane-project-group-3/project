from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired
from destinations import DestinationsDatabase
from aircraft import AircraftDatabase
from flight_trip import FlightTrip

class CreateFlightForm(FlaskForm):

    db = DestinationsDatabase()
    db.destinations_db_cursor.execute("SELECT destination FROM destinations")
    dests = db.destinations_db_cursor.fetchall()

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    airc = db2.db_curs.fetchall()

    aircraft_id = SelectField('Aircraft ID', choices=airc, validators=[DataRequired()])
    destination = SelectField('Destination', choices=dests, validators=[DataRequired()])
    departure_time = StringField('Departure Time', validators=[DataRequired()])
    #arrival_time = StringField('Arrival Time', validators=[DataRequired()])
    #terminal_id =
    price = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ModifyFlightForm(FlaskForm):

    db = FlightTrip()
    db.flight_trip_db_cursor.execute("SELECT flight_id FROM flight_trip")
    flig = db.flight_trip_db_cursor.fetchall()

    db2 = AircraftDatabase()
    db2.db_curs.execute("SELECT aircraft_id FROM aircraft")
    airc = db2.db_curs.fetchall()

    flight_id = SelectField('Flight ID', choices=flig, validators=[DataRequired()])
    submit = SubmitField('Load')
    aircraft_id = SelectField('Aircraft ID', choices=airc, validators=[DataRequired()])
    submit2 = SubmitField('Submit')