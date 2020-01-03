#importing Form
from flask_wtf import FlaskForm

#Importing form elements; textfield, passwordfield
from wtforms import StringField, RadioField, PasswordField, SubmitField, TextField, DateTimeField

#Importing validators to validate Form
from wtforms.validators import DataRequired, Email

class Register_Coach(FlaskForm):
    reg_number = StringField("Coach Number", validators=[DataRequired()])
    origin = StringField("Place of Depature", validators=[DataRequired()])
    destination = StringField("Final Destination", validators=[DataRequired()])
    departure_time = DateTimeField('Depature Time(GMT)',validators=[DataRequired()],format = "%d/%m/%Y %H:%M")
    submit = SubmitField("Add Bus")

class Add_Driver(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
