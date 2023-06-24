#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    argvLen = len(sys.argv)
    for i in range(1, argvLen):
        count = count + int(sys.argv[i])
    print(count)
 



