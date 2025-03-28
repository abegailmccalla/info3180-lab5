from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
# import flask migrate here
from flask_migrate import Migrate

app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(Config)


db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

# Import models here to ensure they are linked to the app
from app import views
