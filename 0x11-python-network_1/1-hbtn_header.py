#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on fri 31 mar 11:55 2023
by Auwwl Abdulmallik
"""
from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        info = response.info()
        print(info['X-Request-Id'])
