# Add any model classes for Flask-SQLAlchemy here

from . import db
from werkzeug.security import generate_password_hash, check_password_hash


from app import db
from datetime import datetime

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    #created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, id, title, description, poster, created_at):
        self.id = id
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)