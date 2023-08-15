#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv[1:]

    if argc == 0:
        print(") arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i, arg in enumerate(argv):
        print(f"{i + 1}: {arg}")
