"""
    Created by ldd on 2023/3/29 19:12
"""
from flask import Blueprint

from app.api.v1 import book, user

"""在app.api.v1模块下的init文件，完成v1蓝图的初始化，比如创建v1蓝图，注册红图"""

def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    # 将红图注册到蓝图上
    # user.api.register(bp_v1, url_prefix='/user')
    # book.api.register(bp_v1, url_prefix='/book')
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    return bp_v1