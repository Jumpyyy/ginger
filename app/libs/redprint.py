"""
    Created by ldd on 2023/3/29 19:32
"""

class Redprint:
    def __init__(self, name):
        self.name = name
        self.mound = []


    def route(self, rule, **options):
        def decorator(f):
            # endpoint = options.pop("endpoint", f.__name__)
            # self.add_url_rule(rule, endpoint, f, **options)
            self.mound.append((f, rule, options))
            return f
        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = "/" + self.name
        for f, rule, options in self.mound:
            endpoint = options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
            



