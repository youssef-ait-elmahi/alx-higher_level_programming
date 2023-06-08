#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    sum = 0
    for i in range(arguments):
        sum += int(argv[i + 1])
    print(sum)
