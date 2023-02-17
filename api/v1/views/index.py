#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_Views


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)
