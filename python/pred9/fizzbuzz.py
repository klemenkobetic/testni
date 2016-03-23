# -*- coding: utf-8 -*-

import sys
from __builtin__ import str

def main():
    st = int(raw_input("Vpisi stevilko med 1 in 100: "))

    result=""
    for x in range(1, st+1):
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