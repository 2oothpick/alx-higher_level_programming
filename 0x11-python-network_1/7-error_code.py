#!/usr/bin/python3
"""
Prints out the error code if status code
is greater than or equal to 400
"""

if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code < 400:
        print(r.text)
    else:
        print(f"Error code: {r.status_code}")
