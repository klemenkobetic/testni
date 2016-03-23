# -*- coding: utf-8 -*-

import sys
from __builtin__ import str

def main():
    result=""
    for x in range(1, 100):
        result=""
        if(x % 3 == 0):
            result="fizz"
        if(x % 5 == 0):
            result+="buzz"
        if (result == ""):
            print "This is x: " + str(x)
        else:
            print result

if __name__ == "__main__":
    main()