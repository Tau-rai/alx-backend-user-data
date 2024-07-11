#!/usr/bin/env python3
"""Module for session authentication"""

from flask import Blueprint, request, jsonify, make_response
from models.user import User
from api.v1.app import auth
import os

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


@app_views.route(
        '/auth_session/login/', methods=['POST'], strict_slashes=False)
@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Handles the login for session authentication"""
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(user.id)
    response = jsonify(user.to_json())
    session_name = os.getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response


@app_views.route(
        '/auth_session/logout/', methods=['DELETE'], strict_slashes=False)
@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logs out the user"""
    if auth.destroy_session(request):
        return jsonify({}), 200
    return jsonify({}), 404
