#!/usr/bin/python3
""" Python script that takes in a URL and an email,
sends a POST request to the"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    rqst = requests.post(url, data=value)
    print(rqst.text)
