#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    lst = dir(hidden_4)
    for i in range(0, len(lst)):
        if lst[i][0] != '_' and lst[i][1] != '_':
            print("{:s}".format(lst[i]))
