from flask import Flask
from peewee import *

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = PostgresqlDatabase(
    'flask_api_db',
    user='master',
    password=app.config['DB_PASSWORD'],
    host='localhost'
)

from .models import User
from app import views

db.create_tables([User])
