from urllib import error,request

try:
    request.urlopen('http://localhost:9087')
except error.URLError as E:
    print(E)
    print(E.reason)

try:
    request.urlopen('http://localhost:9087')
except error.HTTPError as E:
    print(E)
    print(E.code)
    print(E.reason)
    print(E.headers)