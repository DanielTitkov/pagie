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



class TextsApi(Resource):
    def __init__(self):
        # get_parser
        self.get_parser = reqparse.RequestParser()
        self.get_parser.add_argument('dateslug', type=valid_dateslug, location=['args'])
        # post_parser
        self.post_parser = reqparse.RequestParser()
        self.post_parser.add_argument('text', required=True)
        self.post_parser.add_argument('dateslug', type=valid_dateslug, required=True)
        self.post_parser.add_argument('words', type=int, required=False) # maybe better to count on frontend
        super(TextsApi, self).__init__()


    @jwt_required
    def get(self):
        '''All texts by user'''
        args = self.get_parser.parse_args()
        user = User.get_by_identity(get_jwt_identity())
        query = {'user': user.uid, 'date': args.dateslug} if args.dateslug else {'user': user.uid}
        texts = [Text.from_dict(t).to_dict() for t in mongo.db.texts.find(query)]
        return texts, 200


    @jwt_required
    def post(self):
        '''Add text for current day or update if already exists'''
        args = self.post_parser.parse_args()
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
