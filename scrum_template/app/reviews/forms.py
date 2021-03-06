from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TimeField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange

class ReviewForm(FlaskForm):
    rating = DecimalField(default=0.0, validators=[NumberRange(min=0, max=5)])
    text = TextAreaField('Write a review!')
    submit = SubmitField('Submit')