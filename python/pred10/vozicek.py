# -*- coding: utf-8 -*-

import sys  


def main():
    nakupovalni_listek = []
    while ( (str(raw_input("Želiš dodati nov izdelek ? ( D/N ) : "))).lower() in ["d", "da", "y", "yes"]):
        nakupovalni_listek.append(str(raw_input("Vnesi ime izdelka : ")))
    for izdelek in nakupovalni_listek:
        print izdelek
if __name__ == "__main__":
    main()