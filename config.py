#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@author:cgp 
@file: config.py 
@time: 2019/11/09 
"""


class Config:
    SECRET_KEY = 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class MySQLConfig:
    MYSQL_USERNAME = 'cgp'
    MYSQL_PASSWORD = 'cgp'
    MYSQL_HOST = '192.168.27.4'


# class SqliteConfig:
#     SQLALCHEMY_DATABASE_URI =  'sqlite:///D:\\workspace\\python\\micro_blog\\micro-blog.db'


class DevelopmentConfig(Config):
    DEBUG = True
    database = 'micro_blog_dev'
    # SQLALCHEMY_DATABASE_URI = SqliteConfig.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(MySQLConfig.MYSQL_USERNAME,
                                                                   MySQLConfig.MYSQL_PASSWORD,
                                                                   MySQLConfig.MYSQL_HOST, database)


config = {
    'development': DevelopmentConfig
}
