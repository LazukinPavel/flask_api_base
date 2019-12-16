
from app import app, db
from flask import render_template, redirect, request


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
