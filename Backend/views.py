""" This code executes:
1) GET:
    a) gets information about all sheets
    b) gets information about any sheet
"""
# Import flask Modules
from flask import jsonify, abort, redirect, url_for, request
# Import project Modules
from application import app
from application import client
# It's used to unit-tests
from settings import ENDPOINT
import tests.run as test_run


@app.route(ENDPOINT, methods=['GET'])
def get_sheets():
    """
    get_sheets does response to a request "get all sheets information"
    :return: response to a request in the format of json
    """
    return 'Hello world, Моя Лиззи!'


@app.route("/", methods=['GET', 'POST'], strict_slashes=False)
def redirect_main():
    """
    Redirect_main redirects user from URL "/" or "" to URL "api/v1/"
    :return: path to URL "api/v1/"
    """
    return redirect(url_for("get_sheets"))


@app.route(ENDPOINT + "/tests", methods=['GET'], strict_slashes=False)
def tests():
    """
    run tests
    """
    return test_run.run_tests()