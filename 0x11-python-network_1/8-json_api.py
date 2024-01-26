#!/usr/bin/python3
"""JSON formatted and not empty"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'

    q = argv[1] if len(argv) > 1 else ""
    values = {'q': q}

    try:
        req = requests.post(url, data=values)

        data = req.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except (ValueError) as e:
        print("Not a valid JSON")
