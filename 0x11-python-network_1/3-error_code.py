#!/usr/bin/python3
"""Script fetches url using urllib
dixplays an error code status code
if there is an issue
"""

if __name__ == '__main__':
    from urllib import request, error
    import sys
    url = sys.argv[1]  # 'http://example.com'
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
