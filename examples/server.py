from bottle import get, install, run, HTTPError
from bottle_errorsrest import ErrorsRestPlugin


@get("/")
def example():
    # {'message': 'oh no!'}
    raise HTTPError(500, {'prueba': "oh no!"})


install(ErrorsRestPlugin())

run(host="0.0.0.0", port="9988")
