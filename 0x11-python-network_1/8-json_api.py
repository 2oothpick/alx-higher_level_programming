#!/usr/bin/python3
"""Script fetches https://alx-intranet.hbtn.io/status
using requests
"""

if __name__ == '__main__':
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    try:
        response_dict = response.json()
        if response_dict == {}:
            print("No result")
        else:
            print(f"[{response_dict.get('id')}] {response_dict.get('name')}")
    except ValueError:
        print("Not a valid JSON")
