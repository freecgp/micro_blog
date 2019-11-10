#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: user.py 
@time: 2019/11/09 
"""
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from sqlalchemy import desc

from app.api import api
from app.models.blog import Blog
from app.models.user import User, db


@api.resource('/users/<string:user_id>')
class UserView(Resource):
    def get(self, user_id):
        return [u.to_dict() for u in User.query.all()]

    def put(self, user_id):
        return {}


@api.resource('/user')
class UserCreateView(Resource):
    def post(self):
        parser = RequestParser()
        parser.add_argument("name", type=str, location='json', required=True)
        parser.add_argument("password", type=str, location='json', required=True)

        user_info = parser.parse_args(strict=True)
        u = User(name=user_info['name'])
        u.password = user_info['password']
        id = u.create()
        if id:
            return {'id': id}
        else:
            raise Exception("create user failed!")


@api.resource('/users/<string:user_id>/blogs/<string:blog_id>')
class UserBlogDelete(Resource):
    def delete(self, user_id, blog_id):
        print("delete user %s blog %s" % (user_id, blog_id))
        b = Blog.query.filter_by(user_id=user_id, id=blog_id).first()
        db.session.delete(b)
        db.session.commit()
        db.session.close()
        return {"status": 0}


@api.resource('/users/<string:user_id>/news_feed')
class GetNewsFeed(Resource):
    def get(self, user_id):
        u = User.query.get(user_id)
        id_list = [u.followed_id for u in u.followed.all()]
        id_list.append(u.id)
        return [b.to_dict() for b in Blog.query.filter(Blog.user_id.in_(id_list)).
            order_by(desc(Blog.create_time)).limit(3).all()]

