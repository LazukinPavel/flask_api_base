
from app import app, db
from flask import render_template, redirect, request
from .controllers import Controller

controller = Controller()


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/')
def root():
    return 'This is a Flask-based API'


@app.route('/users')
def get_users():
    users = controller.get_users()
    return users


@app.route('/users/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_user(user_id):

    if request.method == 'GET':
        result = controller.get_users_by_id(user_id)

    elif request.method == 'POST':
        print('=== req', request.args)
        user_data = {
            'username': request.args.get('username'),
            'email': request.args.get('email')
        }
        result = controller.update_user(user_id, user_data)
    else:
        result = 'Unknown command, please refer API docs'

    return result


@app.route('/users/create', methods=['POST'])
def create_user():
    result = controller.create_user({
            'username': request.args.get('username'),
            'email': request.args.get('email')
        })

