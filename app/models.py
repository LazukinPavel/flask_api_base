from peewee import *

from flask import current_app


db = PostgresqlDatabase(
    'flask_api_db',
    user='master',
    password=current_app.config['DB_PASS'],
    # password='MW6XEu',
    host='localhost'
)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField()


def initialize():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()
