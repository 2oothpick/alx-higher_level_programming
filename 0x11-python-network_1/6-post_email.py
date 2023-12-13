#!/usr/bin/python3
"""
Sends a POST request to a url with an
email as parameter
"""

if __name__ == '__main__':
    import requests
    import sys
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    r = requests.post(url, data=email)
    print(r.text)
