#!/usr/bin/env python3
"""Basic Authentication module"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Authentication class"""
    pass

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the base64 part of Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[len('Basic '):]
