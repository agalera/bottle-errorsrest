from bottle import json_dumps, JSONPlugin


class ErrorsRestPlugin(object):
    name = 'ErrorsRestPlugin'
    api = 2

    def __init__(self, dumps=None):
        self.json_dumps = dumps

    def setup(self, app):
        for plugin in app.plugins:
            if isinstance(plugin, JSONPlugin):
                self.json_dumps = plugin.json_dumps
                break

        if not self.json_dumps:
            self.json_dumps = json_dumps

        def default_error_handler(res):
            if res.content_type == "application/json":
                return res.body
            res.content_type = "application/json"
            return self.json_dumps({'message': str(res.body)})

        app.default_error_handler = default_error_handler

    def apply(self, callback, route):
        return callback
