from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class GuessForm(FlaskForm):
    guess_number = IntegerField('Guess Number:', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')
