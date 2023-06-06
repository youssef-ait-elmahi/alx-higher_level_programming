#!/usr/bin/python3
def uppercase(str):
    for char in (str):
        if 122 >= ord(char) >= 97:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
