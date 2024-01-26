#!/usr/bin/python3
"""Takes GitHub credentials and uses
the GitHub API to display the user id"""
from requests import get, auth
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    user = argv[1]
    password = argv[2]
    response = get(url, auth=auth.HTTPBasicAuth(user, password))
    print(response.json().get('id'))
