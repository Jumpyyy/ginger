"""
    Created by ldd on 2023/3/29 19:23
"""
from flask import Blueprint

from app.libs.redprint import Redprint

# book = Blueprint('book', __name__)
# test = Blueprint('book', __name__)

api = Redprint('book')
@api.route('/get')
def get_book():
    return 'get book'

# @test.route('test')
# def test():
#     return 'test'