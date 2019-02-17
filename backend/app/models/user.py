from passlib.apps import custom_app_context as pwd_context
from bson.objectid import ObjectId
from datetime import datetime
from app import mongo
from app import bcrypt
import time
import uuid


class User:
    def __init__(self, uid=None, name=None, email=None, password_hash=None,
        timezone='America/New_York',
        created=None, _id=None
    ):
        self.uid = uid or uuid.uuid4().hex
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
            uid=self.uid,
            name=self.name,
            email=self.email,
            passwordHash = self.password_hash,
            timezone = self.timezone,
            created = self.created
        )
        if with_id:
            dic['_id'] = ObjectId(self._id)
        return dic


    def update_from_dict(self, dic, update_password=False):
        for k, v in dic.items():
            if v:
                setattr(self, k, v)

        if update_password and dic['password']:
            self.hash_password(dic['password'])


    @classmethod
    def from_dict(cls, dic):
        if dic:
            return cls(
                uid=dic.get('uid', None),
                name=dic.get('name', None),
                email=dic.get('email', None),
                password_hash=dic.get('passwordHash', None),
                timezone=dic.get('timezone', None),
                created=dic.get('created', None),
                _id=dic.get('_id', None)
            )


    @classmethod
    def get_by_email(cls, email):
        user = mongo.db.users.find_one({'email': email})
        return cls.from_dict(user)


    @classmethod
    def get_by_identity(cls, identity):
        return cls.get_by_email(identity['email'])
