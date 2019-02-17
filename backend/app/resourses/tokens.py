from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import mongo
from app import jwt
from app import api
from app.models.user import User
from app.utils.email import valid_email



class TokenApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=valid_email, required=True)
        self.parser.add_argument('password', required=True)
        super(TextsApi, self).__init__()


    def get(self):
        args = self.parser.parse_args()
        user = User.from_dict(mongo.db.users.find_one({'email': args.email}))
        if user and user.verify_password(args.password):
            token = create_access_token(identity={'email': user.email})
            return {'token': token}, 200
        return {'message': 'invalid email or password'}, 401
