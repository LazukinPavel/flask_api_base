import json

from .models import User
from playhouse.shortcuts import model_to_dict, dict_to_model


class Controller:
    def create_user(self, user_data):
        user, created = User.get_or_create(
            username=user_data['username'],
            defaults=dict(
                email=user_data['email']
            )
        )
        if created:
            return json.dumps(model_to_dict(user))
        return f'User with name {user_data["username"]} already exists'

    def get_users(self):
        users_qs = User.select(User.username, User.email).dicts()
        if users_qs:
            return json.dumps(list(users_qs))
        return 'No users in DB'

    def get_users_by_id(self, user_id):
        user = User.get_or_none(User.id == user_id)
        if user:
            return json.dumps(model_to_dict(user))
        return 'User not found'     # TODO implement 404


