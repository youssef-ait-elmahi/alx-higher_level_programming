#!/usr/bin/python3
for comb in range(80):
    if ((comb / 10) < (comb % 10)):
        print("{:02}".format(int(comb)), end=", ")
print(89)
