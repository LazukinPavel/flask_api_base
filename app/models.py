from peewee import *

from app import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField()
    email = CharField(default=None)




