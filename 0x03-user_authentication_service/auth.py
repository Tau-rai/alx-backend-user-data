#!/usr/bin/env python3
"""Encryption module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
