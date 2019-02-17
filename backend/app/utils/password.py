import re


def validate_password(string):
    return len(string) >= 3


def valid_password(string):
    if validate_password(string):
        return string
    else:
        raise ValueError('{} is not a valid password'.format(string))
