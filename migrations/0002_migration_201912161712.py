# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    username = CharField(max_length=255)
    email = CharField(max_length=255)
    class Meta:
        table_name = "user"


def forward(old_orm, new_orm):
    user = new_orm['user']
    return [
        # Apply default value '' to the field user.email
        user.update({user.email: ''}).where(user.email.is_null(True)),
    ]
