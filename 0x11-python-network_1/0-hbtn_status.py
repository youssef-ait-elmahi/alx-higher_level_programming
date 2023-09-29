#!/usr/bin/python3
""" Python script that fetches a URL """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()  # this will be the HTML content of the page
    print("- type: {}".format(type(data)))
    print("- content: {}".format(data))
    print("- utf8 content: {}".format(data.decode('utf-8')))
