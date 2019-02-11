from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from app import mongo
from app import bcrypt
from app import jwt
from app import api
from app.models import User


class UsersApi(Resource):
    def get(self):
        users = mongo.db.users.find({})
        return 'foofffdsf'


    def post(self):
        password = request.get_json()['password']
        user = User(
            name = request.get_json()['name'],
            email = request.get_json()['email'],
            password_hash = bcrypt.generate_password_hash(password).decode('utf=8')
        )

        _id = mongo.db.users.insert(user.to_dict())

        return user.to_dict(), 201, {'Location': api.url_for(UsersApi, id = user._id, _external = True)}


class UserApi(Resource):
    def get(self, id):
        pass


    def post(self, id):
        pass



class TokenApi(Resource):
    def get(self):
        pass



class DaysApi(Resource):
    def get(self):
        pass



class DayApi(Resource):
    def get(self):
        pass


    def post(self):
        pass
