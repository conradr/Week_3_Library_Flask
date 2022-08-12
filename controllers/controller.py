from flask import Flask
from app import app
from models.book import *
from models.books import *


@app.route('/')
def home():
    return '<p>Home</p>'
