# _*_ Coding:utf-8 _*_

from flask import Blueprint
#定义蓝图
admin = Blueprint("admin",__name__)

import app.admin.views
