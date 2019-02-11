from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from datetime import datetime
from config import Config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token

from app.models import User

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

CORS(app)

from app.resourses import UsersApi
api.add_resource(UsersApi, '/v1/users', endpoint='users')
