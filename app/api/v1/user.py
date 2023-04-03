"""
    Created by ldd on 2023/3/29 19:23
"""
from flask import Blueprint

from app.libs.redprint import Redprint

"""
之前是blueprint--view funcs。现在是redprint--view funcs
"""
# user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('/create')
def create_user():
    return 'create user'


@api.route('/get')
def get_user():
    return 'get user'