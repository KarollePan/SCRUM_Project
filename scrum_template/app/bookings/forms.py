
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TimeField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange

class AddWeddingBookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telno = StringField('Telephone Number',validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    incl_catering = BooleanField('Catering')
    incl_flowers = BooleanField('Flowers')
    incl_carhire = BooleanField('Car Hire')
    incl_visual_and_audio = BooleanField('Visual & Audio System')
    incl_photography = BooleanField('Photography')
    submit = SubmitField('Submit')

class EditWeddingBookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telno = StringField('Telephone Number',validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    incl_catering = BooleanField('Catering')
    incl_flowers = BooleanField('Flowers')
    incl_carhire = BooleanField('Car Hire')
    incl_visual_and_audio = BooleanField('Visual & Audio System')
    incl_photography = BooleanField('Photography')
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')
    delete = SubmitField('Delete')

class AddTourBookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telno = StringField('Telephone Number',validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time_id = SelectField('Time', coerce=int)
    submit = SubmitField('Submit')

class EditTourBookingForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    telno = StringField('Telephone Number',validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    time_id = SelectField('Time', coerce=int)
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')
    delete = SubmitField('Delete')