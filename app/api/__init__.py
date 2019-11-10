#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: __init__.py.py 
@time: 2019/11/09 
"""

from flask import Blueprint
from flask_restful import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')
api = Api(api_bp)

from . import blog, user, follow