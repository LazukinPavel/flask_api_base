import json

from .models import User
from playhouse.shortcuts import model_to_dict, dict_to_model


class Controller:
    def get_users(self):
        users_qs = User.select().dicts()
        if users_qs:
            return json.dumps(list(users_qs))
        return 'No users in DB'
