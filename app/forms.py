# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed

class MovieForm(FlaskForm):
    # Title field: A string field with a DataRequired validator
    title = StringField('Movie Title', validators=[
        DataRequired(message="The title is required"),
        Length(max=100, message="The title cannot exceed 100 characters")
    ])
    
    # Description field: A text area field with a DataRequired validator
    description = TextAreaField('Movie Description', validators=[
        DataRequired(message="A brief description is required")
    ])
    
    # Poster field: A file field that only allows image uploads
    poster = FileField('Movie Poster', validators=[
        FileAllowed(['jpg', 'png'], "Only image files (JPG or PNG) are allowed")
    ])
