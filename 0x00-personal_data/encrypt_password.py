#!/usr/bin/env python3
""" Encrypt module """
import bcrypt


def hash_password(password: str) -> bytes:
    """ Password encrypter function """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ method to verify the given password """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
