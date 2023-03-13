from flask import Flask, url_for
from .config import Config
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


migrate = Migrate(app, db)

app.config.from_object(Config)
from app import views