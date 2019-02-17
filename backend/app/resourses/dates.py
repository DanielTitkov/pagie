from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import jwt
from app import api
from app.models.user import User
import datetime
import pytz


class DateApi(Resource):
    @jwt_required
    def get(self):
        current_user = User.get_by_identity(get_jwt_identity())
        tz = pytz.timezone(current_user.timezone)
        ct = datetime.datetime.now(tz=tz)
        response = {
            'timezone': current_user.timezone,
            'datetime': ct.isoformat(),
            'dateslug': ct.strftime("%Y%m%d"),
            'utc': datetime.datetime.utcnow().isoformat()
        }
        return response, 200
