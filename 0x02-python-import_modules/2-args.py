#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argvLen = len(sys.argv) - 1
    if argvLen == 0:
        print("{} arguments.".format(argvLen))
    elif argvLen == 1:
        print("{} argument:".format(argvLen))
    else:
        print("{} arguments:".format(argvLen))
    if argvLen > 0:
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
