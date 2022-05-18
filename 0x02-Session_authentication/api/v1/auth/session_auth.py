#!/usr/bin/env python3
"""
Session Auth Class
"""
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Auth class
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session"""
        if user_id is None:
            return None
        elif not isinstance(user_id, str):
            return None
        else:
            idd = uuid4()
            self.user_id_by_session_id[str(idd)] = user_id
            return str(idd)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """

        :param session_id:
        :return:
        """
        if session_id is None:
            return None
        elif not isinstance(session_id, str):
            return None
        else:
            return self.user_id_by_session_id.get(session_id)
