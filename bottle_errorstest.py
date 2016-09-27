from bottle import HTTPError
from functools import wraps


class ErrorsRestPlugin(object):
    name = 'ErrorsRestPlugin'
    api = 2

    def setup(self, app):
        def default_error_handler(res):
            return res.body
        app.default_error_handler = default_error_handler

    def apply(self, callback, route):
        @wraps(route.callback)
        def wrapper(*args, **kwargs):

            try:
                result = route.callback(*args, **kwargs)
            except HTTPError as resp:
                result = resp
            if (isinstance(result, HTTPError) and
                    not isinstance(result.body, dict)):
                result.body = {'message': str(result.body)}
            return result
        return wrapper
