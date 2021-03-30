# _*_ coding:utf-8 _*_

from flask import Blueprint
#定义蓝图
home = Blueprint("home",__name__)

import app.home.views   # import /app/home/views.py

