#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    tally = 0
    if len(sys.argv) > 1:
        for count in range(1, len(sys.argv)):
            tally += int(sys.argv[count])
    print("{:d}".format(tally))
