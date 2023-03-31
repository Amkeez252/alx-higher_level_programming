#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 01 Apr 12:10 2023
 by Auwal Abdulmalik
 """
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
