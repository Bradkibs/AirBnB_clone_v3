#!/usr/bin/python3

from flask import Blueprint
"""create a Blueprint instance for the api/v1/views package """
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

"""Import all of the views from the index module"""
from api.v1.views.index import *
