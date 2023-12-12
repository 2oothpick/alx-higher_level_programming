#!/usr/bin/python3
""" 
Script displays the X-Request-Id 
variable found in argv[1] header 
"""

if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
    for i in html:
        if i == "X-Request-Id":
            print(html.get('X-Request-Id'))
