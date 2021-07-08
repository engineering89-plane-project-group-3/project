from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    flight_id = StringField('Enter Flight ID', validators=[DataRequired()])
    submit = SubmitField('Submit')
