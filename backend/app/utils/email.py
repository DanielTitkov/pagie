import re


def validate_email(string):
    rgx = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
    valid = re.match(rgx, string)
    return True if valid else False


def valid_email(string):
    if validate_email(string):
        return string
    else:
        raise ValueError('{} is not a valid email'.format(string))
