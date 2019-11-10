#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: blog.py 
@time: 2019/11/09 
"""
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from app.api import api
from app.models.blog import Blog


@api.resource('/blog')
class BlogView(Resource):
    parser = RequestParser()
    parser.add_argument("title", type=str, location='json', required=True)
    parser.add_argument("text", type=str, location='json', required=True)
    parser.add_argument("user_id", type=int, location='json', required=True)

    def get(self):
        return [b.to_dict() for b in Blog.query.all()]

    def post(self):
        blog_info = self.parser.parse_args(strict=True)
        b = Blog(
            title=blog_info['title'],
            text=blog_info['text'],
            user_id=blog_info['user_id'],
        )
        id = b.create()
        if id:
            return {'id': id}
        else:
            raise Exception("create blog failed!")
