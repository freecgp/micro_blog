#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: init_db.py 
@time: 2019/11/09 
"""

from app import create_app


def init_db(mysql_db='development'):
    from app.models.user import User, Follow
    from app.models.blog import Blog
    from app import db
    app = create_app(mysql_db)
    app.app_context().push()
    db.drop_all()
    db.create_all()
    db.session.commit()


init_db()
