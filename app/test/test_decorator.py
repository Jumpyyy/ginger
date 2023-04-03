"""
    Created by ldd on 2023/3/29 20:23
"""
from flask.scaffold import setupmethod, T_route


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

"""把@log放到now()的定义处，相当于执行了now=log(now)"""
@log
def now():
    print('2023.3.29')

def log2(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


# @api.route('/create')
# def create_user():
#     return 'create user'




def route0(self, rule: str, **options):
    def decorator(f: T_route) -> T_route:
        endpoint = options.pop("endpoint", None)
        self.add_url_rule(rule, endpoint, f, **options)
        return f

    return decorator


def add_url_rule(self, rule, endpoint=None, view_func=None):
    if endpoint:
        assert '.' not in endpoint, "Redprint endpoints wrong"
    pass


def endpoint(self, endpoint: str):
    def decorator(f) :
        self.view_functions[endpoint] = f
        return f
    return decorator