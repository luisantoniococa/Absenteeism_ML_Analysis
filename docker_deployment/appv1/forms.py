from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField

class PredictForm(FlaskForm):
    reason = StringField('reason')
    month = StringField('month')
    transportation = StringField('transportation')
    age = StringField('age')
    body = StringField('body')
    education = SelectField(label='education', choices=['GED', 'Undergrad', 'Graduate', 'PhD'])
    children = StringField('children')
    pets = StringField('pets')    
    submit = SubmitField('Make Prediction')