from peewee import *

from app import db


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    email = CharField(default=None)




