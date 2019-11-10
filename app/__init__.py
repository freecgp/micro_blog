#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: __init__.py.py 
@time: 2019/11/09 
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from jinja2.utils import import_string

from app.error import api_abort, ReturnCode
from config import config


blueprint = 'app.api:api_bp'

db = SQLAlchemy()


def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return api_abort(ReturnCode.BadRequest)

    @app.errorhandler(500)
    def internal_server_error(e):
        return api_abort(ReturnCode.InterError, message='An internal server error occurred.')

    @app.errorhandler
    def default_error_handler(e):
        message = 'An unhandled exception occurred. -> {}'.format(str(e))
        # if not settings.FLASK_DEBUG:
        return api_abort(ReturnCode.InterError, message=message)


def create_app(mode):
    app = Flask(__name__)

    bp = import_string(blueprint)
    app.register_blueprint(bp)

    register_errors(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = config[mode].SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config[mode].SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = config[mode].SQLALCHEMY_COMMIT_ON_TEARDOWN
    db.init_app(app=app)

    return app

