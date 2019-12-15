
from app import app
from flask import render_template, redirect, request


@app.route('/')
def root():
    return 'This is a Flask-based API'
