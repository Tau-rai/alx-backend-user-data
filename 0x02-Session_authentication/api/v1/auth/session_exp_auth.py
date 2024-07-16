#!/usr/bin/env python3
"""
Session expiration authentication module
"""
import os
from datetime import datetime, timedelta
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    def __init__(self):
        """Initialize the session expiration authentication"""
        session_duration = os.getenv('SESSION_DURATION')
        try:
            self.session_duration = int(session_duration)
        except (TypeError, ValueError):
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a session ID and store session data with expiration"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        
        session_data = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_data
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve the user ID associated with the session ID, considering expiration"""
        if session_id is None:
            return None

        session_data = self.user_id_by_session_id.get(session_id)
        if not session_data:
            return None

        if self.session_duration <= 0:
            return session_data.get("user_id")

        created_at = session_data.get("created_at")
        if created_at is None:
            return None

        if datetime.now() > created_at + timedelta(seconds=self.session_duration):
            return None

        return session_data.get("user_id")
