from flask_wtf import FlaskForm
from wtforms import StringField,validators,TextAreaField,SelectField,FileField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from random import choices


class AddPropertyForm(FlaskForm):
    title = StringField('Property Title',validators=[DataRequired()])
    description= TextAreaField('Description',validators=[DataRequired()])
    No_Rooms=StringField('No. of Rooms',validators=[DataRequired()])
    No_bathrooms= StringField('No. of Bathrooms',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    property_type= SelectField('Property Type', choices=[('House'),('Apartment')],validators=[DataRequired()])
    location= StringField('Location',validators=[DataRequired()])
    photo=FileField('Photo', validators=[FileRequired('No photo was submitted.'), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])

