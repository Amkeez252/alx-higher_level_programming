#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 01 of Apr 12:35 2023
by Auwal Abdulmalik
"""
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, password))
    try:
        obj = response.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
