# Bottle Errors Rest
bottle_errorsrest plugin for bottle

All errors are now returned bottle json format.

If HTTPError receives a string becomes {'message': string}

## installation

Via pip:
```pip install bottle_errorsrest```

Or clone:
```git clone https://github.com/agalera/bottle_errorsrest.git```


## example server:
```python
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

```

## Test:
```bash
curl http://localhost:9988/ --head; curl http://localhost:9988/
HTTP/1.0 500 Internal Server Error
Date: Tue, 27 Sep 2016 11:16:41 GMT
Server: WSGIServer/0.2 CPython/3.4.3
Content-Type: application/json
Content-Length: 20

{"message": "oh no!"}

curl http://localhost:9988/2 --head; curl http://localhost:9988/2
HTTP/1.0 500 Internal Server Error
Date: Tue, 27 Sep 2016 11:16:41 GMT
Server: WSGIServer/0.2 CPython/3.4.3
Content-Type: application/json
Content-Length: 20

{"other_Example": "oh no!"}

curl http://localhost:9988/not_found --head; curl http://localhost:9988/not_found
HTTP/1.0 404 Not Found
Date: Tue, 27 Sep 2016 11:11:39 GMT
Server: WSGIServer/0.2 CPython/3.4.3
Content-Length: 38
Content-Type: application/json

{"message": "Not found: '/not_found'"}
```
