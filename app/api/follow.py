#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: follow.py 
@time: 2019/11/09 
"""
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app import db
from app.api import api
from app.models.user import User, Follow


@api.resource('/follow')
class FollowVeiw(Resource):
    parser = RequestParser()
    parser.add_argument("follower_id", type=int, location='json', required=True)
    parser.add_argument("followed_id", type=int, location='json', required=True)

    def post(self):
        data = self.parser.parse_args(strict=True)
        follower = User.query.get(data['follower_id'])
        followed = User.query.get(data['followed_id'])
        f = Follow(follower=follower, followed=followed)
        db.session.add(f)
        db.session.commit()
        # db.session.close()
        # TODO response fix
        return {}


@api.resource('/unfollow')
class UnFollowVeiw(Resource):
    parser = RequestParser()
    parser.add_argument("follower_id", type=int, location='json', required=True)
    parser.add_argument("followed_id", type=int, location='json', required=True)

    def put(self):
        data = self.parser.parse_args(strict=True)
        follower = User.query.get(data['follower_id'])
        f = follower.followed.filter_by(followed_id=data['followed_id']).first()
        if f:
            db.session.delete(f)
            db.session.commit()
        # TODO response fix
        return {}

