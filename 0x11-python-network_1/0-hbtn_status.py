#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status
using urllib
"""

if __name__ == '__main__':
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type:{type(html)}")
        print(f"\t- content:{(html)}")
        print(f"\t- utf8 content:{(html.decode('utf-8'))}")
