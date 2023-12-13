#!/usr/bin/python3
"""
Sends a POST request to a url with an
email as parameter
"""

if __name__ == '__main__':
    from urllib import request, parse
    import sys
    url = sys.argv[1]
    value = sys.argv[2]
    data = (parse.urlencode(value).encode('ascii'))
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print((response.read()).decode('utf-8'))
