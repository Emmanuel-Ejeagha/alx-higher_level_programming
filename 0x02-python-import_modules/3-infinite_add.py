#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0

    if (len(sys.argv) == 1):
        print("{:d}".format(0))
    else:
        for x in range(1, len(sys.argv)):
            add += int(sys.argv[x])
        print(add)
