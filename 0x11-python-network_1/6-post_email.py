#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat 01 of Apr 12:20 2023
by Auwal Aabdulmalik
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
    print(response.text)
