#!/usr/bin/python3
"""POST Key Value pair data"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
