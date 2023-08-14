#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print(argc, "arguments. ")
    elif (argc == 1):
        print(argc, "argument:".format(aya.argv[0]))
        print("1:", sys.argv[1])
    else:
        print(argc, "argument:")
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[I]))
