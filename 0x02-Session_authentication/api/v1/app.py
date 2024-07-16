#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")
if AUTH_TYPE == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
if AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
if AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
if AUTH_TYPE == "session_exp_auth":
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request():
    """Before request handler.

    This function is executed before each request to the API. It performs authentication checks
    to ensure that the request is authorized.

    Returns:
        None: If the authentication is successful.
        Tuple: If the authentication fails, it returns a tuple containing None and an HTTP 401 error response.

    Raises:
        HTTPException: If the authentication fails, it raises an HTTP 401 or 403 error response.
    """
    if auth is None:
        return
    paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        '/api/v1/auth_session/login/',
    ]
    if auth.require_auth(request.path, paths):
        if not auth.authorization_header(request):
            return None, abort(401)
        if not auth.session_cookie(request):
            return None, abort(401)
        request.current_user = auth.current_user(request)
        if request.current_user is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
