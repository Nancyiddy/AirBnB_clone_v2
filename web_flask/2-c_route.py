#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:15:54 2023

@author: Nancy Idiong,  Niyi Abidogun
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Adding a specific route /hbnb"""
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def text(text=None):
    """Dynamic inputed text: replace _ for space and show text"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
