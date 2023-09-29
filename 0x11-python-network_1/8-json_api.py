#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to"""
import sys
import requests


if __name__ == "__main__":
    query = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": query}

    rqst = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = rqst.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
