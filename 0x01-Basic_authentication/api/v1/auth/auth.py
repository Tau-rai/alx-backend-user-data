#!/usr/bin/env python3
"""Module holds the basic authentication logic"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class for handling the basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns False - path and excluded_paths will not be used
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Method that returns None - request will not be used
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns None - request will not be used
        """
        return None
