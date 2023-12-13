#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status
using requests
"""

if __name__ == '__main__':
    import requests
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
