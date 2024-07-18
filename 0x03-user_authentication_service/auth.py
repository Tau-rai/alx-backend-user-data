#!/usr/bin/env python3
"""Encryption module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import NoResultFound
import uuid


def _generate_uuid() -> str:
    """Generates a UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Returns a hashed password"""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """Registers a user"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(
                email, hashed_password.decode('utf-8'))
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validates a user's login information"""
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                    password.encode('utf-8'),
                    user.hashed_password.encode('utf-8')):
                return True
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session ID"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> str:
        """Gets a user from a session ID"""
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            if user:
                return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session"""
        self._db.update_user(user_id, session_id=None)
        return None
