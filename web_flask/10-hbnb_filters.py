#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:15:54 2023

@author: @author: Nancy Idiong, Niyi Abidogun

"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """use storage for fetching data from the storage engine
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def state_id():
    """Display a HTML page inside the tag BODY"""
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State),
                           amenities=storage.all(Amenity))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
