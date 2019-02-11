from passlib.apps import custom_app_context as pwd_context
from datetime import datetime
import time
from app import mongo
from app import bcrypt


class User:
    def __init__(self, name=None, email=None, password_hash=None, timezone=None,
        created=None, _id=None
    ):
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.timezone = timezone
        self._id = _id
        self.created = created or time.time()


    def hash_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf=8')


    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    def to_dict(self, with_id=False):
        dic = dict(
            name=self.name,
            email=self.email,
            passwordHash = self.password_hash,
            timezone = self.timezone,
            created = self.created
        )
        if with_id:
            dic['_id'] = self._id
        return dic


    @classmethod
    def from_dict(cls, dic):
        return cls(
            name=dic.get('name', None),
            email=dic.get('email', None),
            password_hash=dic.get('passwordHash', None),
            timezone=dic.get('timezone', None),
            created=dic.get('created', None),
            _id=dic.get('_id', None)
        )



class Day:
    def __init__(user=None, text=None, words=None, started=None, updated=None, date=None):
        self.user = user
        self.text = text
        self.words = words
        self.started = started
        self.updated = updated
        self.date = date
