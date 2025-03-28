# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import InputRequired, DataRequired, Length
from flask_wtf.file import FileRequired, FileField, FileAllowed


# Add any form classes for Flask-WTF here
class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = TextAreaField('Decription', validators=[InputRequired()])
    poster = FileField('Poster', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'or', 'jpeg', 'images only!'])])
    