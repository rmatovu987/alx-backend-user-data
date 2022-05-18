#!/usr/bin/env python3
"""
Basic Auth
"""
from .auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic Auth Class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """

        :param base64_authorization_header:
        :return:
        """
        if base64_authorization_header is None:
            return None
        elif not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(decoded)
            return decoded.decode('utf-8')
        except Exception:
            return None

        def extract_user_credentials(self,
                                     decoded_base64_authorization_header:
                                     str) -> (str, str):
            """
            Returns user email and password from Base64 decoded value
            """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = decoded_base64_authorization_header.split(":")[0]
        password = decoded_base64_authorization_header[len(email) + 1:]
        return (email, password)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Return a User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for u in users:
                if u.is_valid_password(user_pwd):
                    return u
            return None
        except Exception:
            return None
