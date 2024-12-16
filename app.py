"""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from flask import Flask
from apis import api

import werkzeug.exceptions as wz

import data.people as ppl


app = Flask(__name__)
api.init_app(app)
