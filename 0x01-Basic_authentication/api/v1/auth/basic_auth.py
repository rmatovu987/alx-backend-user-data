#!/usr/bin/env python3
"""
Basic Auth
"""
from .auth import Auth


class BasicAuth(Auth):
    """
    Basic Auth Class
    """

    def extract_base64_authorization_header\
                    (self, authorization_header: str) -> str:
        """

        :param authorization_header:
        :return:
        """
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif not authorization_header.startswith('Basic '):
            return None
        else:
            return authorization_header.split(' ')[-1]
