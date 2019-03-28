from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

from app.resourses.dates import DateApi, DatesApi
from app.resourses.tokens import TokenApi
from app.resourses.users import UsersApi, UserApi
from app.resourses.texts import TextsApi

api.add_resource(UsersApi, '/v1/users', endpoint='users')
api.add_resource(UserApi, '/v1/users/<uid>', endpoint='user')
api.add_resource(TokenApi, '/v1/token', endpoint='token')
api.add_resource(DatesApi, '/v1/dates', endpoint='dates')
api.add_resource(DateApi, '/v1/date', endpoint='date')
api.add_resource(TextsApi, '/v1/texts', endpoint='texts')
