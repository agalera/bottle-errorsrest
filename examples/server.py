from bottle import get, install, run, HTTPError
from bottle_errorsrest import ErrorsRestPlugin


@get("/")
def example():
    # {'message': 'oh no!'}
    raise HTTPError(500, "oh no!")


@get("/2")
def example2():
    # {'other_Example': 'oh no!'}
    raise HTTPError(500, {'other_Example': 'oh no!'})


install(ErrorsRestPlugin())

run(host="0.0.0.0", port="9988")
