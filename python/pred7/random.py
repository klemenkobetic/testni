# -*- coding: utf-8 -*-

import sys

def main():
    random = 15
    # SyntaxError: Non-ASCII character '\xc4' in file random.py on line 5,
    # but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
    print("Just testing foreign signs : čšćđž")
    tekst = "Please enter number : "

    n = raw_input(tekst)

    while( n.isdigit() != True ):
        n = raw_input(tekst)

    while int(n.strip()) != random:
        n = raw_input(tekst)
        while( n.isdigit() != True ):
            n = raw_input(tekst)

    print("You are a genious. Buy yourself a beer!")

if __name__ == "__main__":
    main()