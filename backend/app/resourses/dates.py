from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo
from app import jwt
from app import api
from app.models.user import User
from app.models.text import Text
from app.utils.date import current_date
from dateutil import rrule
import datetime
import pytz



class DatesApi(Resource):
    @jwt_required
    def get(self):
        current_user = User.get_by_identity(get_jwt_identity())
        query = ({'user': current_user.uid}, {'date': 1, '_id': 0})
        dates_with_text = [t['date'] for t in mongo.db.texts.find(*query)]
        ct = current_date(current_user)
        st = ct - datetime.timedelta(days = 30)
        dates = [d.strftime('%Y%m%d') for d in rrule.rrule(rrule.DAILY, dtstart=st, until=ct)]
        response = [{'date': d, 'textPresent': d in dates_with_text} for d in dates]
        return response, 200



class DateApi(Resource):
    @jwt_required
    def get(self):
        current_user = User.get_by_identity(get_jwt_identity())
        ct = current_date(current_user)
        response = {
            'timezone': current_user.timezone,
            'datetime': ct.isoformat(),
            'dateslug': ct.strftime("%Y%m%d"),
            'utc': datetime.datetime.utcnow().isoformat()
        }
        return response, 200
