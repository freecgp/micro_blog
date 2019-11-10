#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: blog.py
@time: 2019/11/09 
"""
import datetime
import time

from app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    text = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'user_id': self.user_id,
            'create_time': self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            'update_time': self.update_time.strftime("%Y-%m-%d %H:%M:%S")
        }

    def create(self):
        try:
            self.create_time = datetime.datetime.utcnow()
            self.update_time = datetime.datetime.utcnow()
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            print("{} blog add: {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"), self.name))
            db.session.rollback()
            return None
        finally:
            db.session.close()
