import re
import datetime
import pytz


# DATESLUG #


def split_dateslug(string):
    try:
        year = string[0:4]
        month = string[4:6]
        day = string[6:]
        return (year, month, day)
    except:
        return ('0', '0', '0')


def validate_dateslug(string):
    rgx = '\d{8}' # later may be more than lenght
    if re.match(rgx, string):
        year, month, day = split_dateslug(string)
        if 2018 < int(year) and 0 < int(month) < 13 and 0 < int(day) < 32:
            return True
    return False


def valid_dateslug(string):
    if validate_dateslug(string):
        return string
    else:
        raise ValueError('{} is not a valid dateslug'.format(string))


# TIMEZONE #


def validate_timezone(string):
    return string in pytz.common_timezones


def valid_timezone(string):
    if validate_timezone(string):
        return string
    else:
        raise ValueError('{} is not a valid timezone'.format(string))


# CURRENT DATE #

def current_date(user):
    tz = pytz.timezone(user.timezone)
    return datetime.datetime.now(tz=tz)
