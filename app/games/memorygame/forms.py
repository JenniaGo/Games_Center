from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired

class MemoryForm(FlaskForm):
    selected_cards = IntegerField('Selected Cards:', validators=[InputRequired(), NumberRange(min=1, max=8)])
    submit = SubmitField('Submit')
