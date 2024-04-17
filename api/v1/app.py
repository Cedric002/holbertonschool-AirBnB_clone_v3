#!/usr/bin/python3


"""
Flask Application
"""


from models import storage
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """
    Close Storage
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    """
    Run Flask server
    """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
