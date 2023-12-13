#!/usr/bin/python3
"""
Script displays the X-Request-Id
variable found in argv[1] header
"""

if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print((r.headers).get('X-Request-Id'))
