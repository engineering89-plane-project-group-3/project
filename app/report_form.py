from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    flight_id = StringField(validators=[DataRequired()])
    submit = SubmitField()
