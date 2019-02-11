from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import create_access_token
from app import mongo
from app import jwt
from app import api
from app.models import User



class UsersApi(Resource):
    def get(self):
        users =  [User.from_dict(u).to_dict() for u in mongo.db.users.find({})]
        return users


    def post(self):
        user = User(
            name = request.get_json()['name'],
            email = request.get_json()['email'],
        )
        user.hash_password(request.get_json()['password'])

        _id = mongo.db.users.insert(user.to_dict())

        return user.to_dict(), 201, {'Location': api.url_for(UsersApi, id = user._id, _external = True)}



class UserApi(Resource):
    def get(self, id):
        pass


    def post(self, id):
        pass



class TokenApi(Resource):
    def get(self):
        if not request.is_json:
            return {"error": "Missing JSON in request"}, 400

        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if email and password:
            user = User.from_dict(mongo.db.users.find_one({'email': email}))
            if user:
                if user.verify_password(password):
                    access_token = create_access_token(identity={
                        'name': user.name,
                        'email': user.email
                    })
                    return {'token': access_token}, 200
                else:
                    return {'error': 'invalid email or password'}, 401
            else:
                return {'error': 'no such user'}, 404
        else:
            return {'error': 'not enough data'}, 400



class DaysApi(Resource):
    def get(self):
        pass



class DayApi(Resource):
    def get(self):
        pass


    def post(self):
        pass
