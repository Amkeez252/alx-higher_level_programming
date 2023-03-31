#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 01 of Apr 12:25 2023
by Auwal Abdulmalik
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    response = get(url)
    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
