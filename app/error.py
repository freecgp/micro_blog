#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: error.py 
@time: 2019/11/09 
"""

from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


class ReturnCode:
    Unauthorized = 403
    BadRequest = 400
    InterError = 500
    Forbidden = 401


def api_abort(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(message=message, **kwargs)
    return response, code


def token_expired():
    response, code = api_abort(ReturnCode.Forbidden, message='token expired')
    return response, code

