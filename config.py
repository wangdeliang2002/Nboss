# -*- coding=utf-8 -*-
import os
class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        '''初始化配置文件'''
        pass

# the config for development
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@135.251.163.198:3306/nboss'
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.3.58:3306/nboss'
    SQLALCHEMY_TRACK_MODIFICATIONS = 'False'
    DEBUG = False

# define the config
config = {
    'default': DevelopmentConfig
}
