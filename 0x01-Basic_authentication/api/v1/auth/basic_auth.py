#!/usr/bin/env python3
"""Basic Authentication module"""


from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Decodes the value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf_8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None