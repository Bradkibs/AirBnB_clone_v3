#!/usr/bin/python3
""" returns a json response of the status"""


from api.v1.views import app_views
from flask import jsonify
from flasgger import swag_from



@app_views.route('/status')
@swag_from('swagger_spec/status.yml')
def status():
    """that returns a JSON: "status": 'OK'"""
    return jsonify({'status': 'OK'})
