# -*- coding: utf-8 -*-

import sys


def main():
    drzave_mesta = {"Slovenija" : "Ljubljana", "Hrvaška" : "Zagreb" , "Madžarska" : "Budimpešta", "Italija": "Rim"}
    stevec = 0
    for drzava, mesto in drzave_mesta.iteritems():
        if ( (str(raw_input("Glavno mesto " + drzava + " je : "))).lower()  == mesto.lower() ):
            stevec += 1
            print("Pravilno! Imas " + str(stevec) + " tock!")
        else:
            print("NI pravilno! Imas " + str(stevec) + " tock!")

if __name__ == "__main__":
    main()