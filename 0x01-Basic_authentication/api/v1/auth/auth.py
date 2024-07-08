#!/usr/bin/env python3
"""Module holds the basic authentication logic"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class for handling the basic authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns False - path and excluded_paths will not be used
        """
        if path is None or excluded_paths is None:
            return True

        # normalise the path by removing trailing slashes
        normalized_path = path.rstrip('/')

        # normalise the excluded paths
        norm_excluded_paths = [path.rstrip('/') for path in excluded_paths]

        if normalized_path in norm_excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method that returns None - request will not be used
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method that returns None - request will not be used
        """
        return None
