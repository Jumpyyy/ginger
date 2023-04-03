"""
    Created by ldd on 2023/3/29 19:03
"""
from flask import Flask

"""app.py 在app模块下，类似于app.init，完成app的初始化工作，比如创建app，注册蓝图"""


def register_blueprints(app):
    # from app.api.v1.book import book
    # from app.api.v1.user import user
    # app.register_blueprint(book)
    # app.register_blueprint(user)
    # 之前是将book user这俩蓝图注册到app上，现在book user不再是蓝图，而是红图，v1是蓝图了。

    from app.api.v1 import create_blueprint_v1
    bp_v1 = create_blueprint_v1()
    app.register_blueprint(bp_v1, url_prefix='/v1')
    pass

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprints(app)
    return app