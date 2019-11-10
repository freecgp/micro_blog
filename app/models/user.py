#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: user.py 
@time: 2019/11/09 
"""
import time

from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Follow(db.Model):
    __tablename__ = 'follow'
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    blogs = db.relationship('Blog', backref='user', lazy="subquery")
    followers = db.relationship(
        'Follow',
        foreign_keys=[Follow.followed_id],
        backref=db.backref('followed', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )
    followed = db.relationship(
        'Follow',
        foreign_keys=[Follow.follower_id],
        backref=db.backref('follower', lazy='joined'),
        lazy='dynamic',
        cascade='all, delete-orphan'
    )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'followers': [u.follower_id for u in self.followers.all()],
            'followed': [u.followed_id for u in self.followed.all()],
        }

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except Exception as e:
            print("{} user add: {} failure...".format(time.strftime("%Y-%m-%d %H:%M:%S"), self.name))
            db.session.rollback()
            return None
        finally:
            db.session.close()
