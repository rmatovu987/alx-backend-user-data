#!/usr/bin/env python3
"""
Class to manager authentication
"""
import os
from typing import List, TypeVar

from flask import request


class Auth:
    """
    Auth Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        :param path:
        :param excluded_paths:
        :return:
        """
        if path is None:
            return True
        elif excluded_paths is None or len(excluded_paths) == 0:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """

        :param request:
        :return:
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None

    def session_cookie(self, request=None):
        """

        :param request:
        :return:
        """
        if request is None:
            return None
        session = os.getenv('SESSION_NAME')
        return request.cookies.get(session)
