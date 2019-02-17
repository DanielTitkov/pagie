from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import mongo
from app import jwt
from app import api
from app.models.user import User
from app.models.text import Text
from app.utils.date import valid_dateslug, split_dateslug
import uuid
import time


parser = reqparse.RequestParser()
parser.add_argument('text', required=True)
parser.add_argument('dateslug', type=valid_dateslug, required=True)


class TextsApi(Resource):
    @jwt_required
    def get(self):
        '''All texts by user'''
        current_user = User.get_by_identity(get_jwt_identity())
        texts = [Text.from_dict(t).to_dict() for t in mongo.db.texts.find({'user': current_user.uid})]
        return texts, 200


    @jwt_required
    def post(self):
        '''Add text for current day or update if already exists'''
        args = parser.parse_args()
        current_user = User.get_by_identity(get_jwt_identity())

        existing_text = mongo.db.texts.find_one({'user': current_user.uid, 'date': args.dateslug})
        if existing_text:
            text = Text.from_dict(existing_text)
            text.updated = time.time()
            text.text = args.text
            mongo.db.texts.save(text.to_dict(with_id=True))
            code = 200
        else:
            text = Text(user=current_user.uid, text=args.text, date=args.dateslug)
            mongo.db.texts.insert(text.to_dict())
            code = 201

        return text.to_dict(), code



class TextApi(Resource):
    @jwt_required
    def get(self):
        pass


    @jwt_required
    def post(self):
        pass
