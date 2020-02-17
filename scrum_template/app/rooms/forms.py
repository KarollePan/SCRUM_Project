
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange

class AddRoomForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(min=4, max=30)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=50, max=5000)])
    image = FileField('Add image', validators=[FileAllowed(['jpg', 'png'])])
    price = DecimalField('Price', validators=[DataRequired()])
    submit = SubmitField('Add room')

class EditRoomForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),Length(min=4, max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=50, max=5000)])
    image = FileField(
        'Update room image - <span style="color:red;">only replace if old or incorrect</span>', 
        validators=[
            FileAllowed(['jpg', 'png'], 'Images only with extension .jpg or .png')
        ]
    )
    price = DecimalField('Price', validators=[DataRequired()])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')