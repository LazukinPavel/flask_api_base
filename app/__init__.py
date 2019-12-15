from flask import Flask
from config import Config

import peewee


app = Flask(__name__)
app.config.from_object(Config)

from app import views

# TODO find a better way to pass config
with app.app_context():
    from app import models

models.initialize()
# print(app.config)
