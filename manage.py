#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: manage.py 
@time: 2019/11/09 
"""
from flask_script import Server, Manager, Shell
from flask_migrate import MigrateCommand

from app import create_app, db
from app.models.user import User, Follow
from app.models.blog import Blog

app = create_app('development')
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, User=User, Blog=Blog, Follow=Follow)


manager.add_command('runserver', Server(host='127.0.0.1', port=5000, use_debugger=True, use_reloader=True))
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run(default_command='runserver')
