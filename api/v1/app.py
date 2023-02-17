#!/usr/bin/python3
import os
from flask import Flask
from models import storage
from api.v1.views import api_views

app = Flask(__name_)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """teardown: after each request, this method calls .close()
    (i.e. .remove()) on the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
