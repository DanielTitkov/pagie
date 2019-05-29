from flask import Flask, request, jsonify, current_app
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo
from app import jwt
from app import api
from app.models.user import User
import datetime
import time
from app.utils.email import valid_email
from app.utils.password import valid_password
from app.utils.date import valid_timezone
from app import app



class UsersApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', required=True)
        self.parser.add_argument('email', type=valid_email, required=True)
        self.parser.add_argument('password', type=valid_password, required=True)
        self.parser.add_argument('userKey', required=True)
        self.parser.add_argument('inviteCode')
        super(UsersApi, self).__init__()


    @jwt_required
    def get(self):
        '''Return the user'''
        current_user = User.get_by_identity(get_jwt_identity())
        return current_user.to_dict()


    def post(self):
        '''Create new user'''
        args = self.parser.parse_args()

        if mongo.db.users.find_one({'email': args.email}):
            return {'message': 'email already in use'}, 422

        if app.config['REQUIRE_INVITE']:
            invite = mongo.db.invites.find_one({'inviteCode': args.inviteCode})
            if not invite:
                return {'message': 'invalid invite code'}, 422
            if invite['used']:
                return {'message': 'invite code is already used'}, 422
            invite['used'] = True
            invite['user'] = {'email': args.email, 'registered': time.time()}
            mongo.db.invites.save(invite)

        user = User(name=args.name, email=args.email, user_key=args.userKey)
        user.hash_password(args.password)
        mongo.db.users.insert(user.to_dict())

        return user.to_dict(with_password=False), 201, {'Location': api.url_for(UserApi, uid = user.uid, _external = True)}



class UserApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name')
        self.parser.add_argument('email', type=valid_email)
        self.parser.add_argument('password', type=valid_password)
        self.parser.add_argument('timezone', type=valid_timezone)
        super(UserApi, self).__init__()


    @jwt_required
    def get(self, uid):
        user = User.from_dict(mongo.db.users.find_one({'uid': uid}))
        if not user:
            return {'message': "user with id '{}' not found".format(uid)}, 404
        return user.to_dict()


    @jwt_required
    def post(self, uid):
        '''update user'''
        user = User.from_dict(mongo.db.users.find_one({'uid': uid}))
        if not user:
            return {'message': "user with id '{}' not found".format(uid)}, 404

        args = self.parser.parse_args()
        user.update_from_dict(args, update_password=True)
        mongo.db.users.save(user.to_dict(with_id=True))

        return user.to_dict(with_password=False), 200


    @jwt_required
    def delete(self, uid):
        user = User.from_dict(mongo.db.users.find_one({'uid': uid}))
        if not user:
            return {'message': "user with id '{}' not found".format(uid)}, 404
