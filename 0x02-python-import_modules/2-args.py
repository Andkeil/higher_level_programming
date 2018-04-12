#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 1
    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1), end="\n")
    if len(sys.argv) > 1:
        for arg in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]), end="\n")
            i += 1
