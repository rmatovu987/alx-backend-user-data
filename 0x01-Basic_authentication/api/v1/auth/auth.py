#!/usr/bin/env python3
"""
Class to manager authentication
"""
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
        return False

    def authorization_header(self, request=None) -> str:
        """

        :param request:
        :return:
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None
