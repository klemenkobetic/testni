# -*- coding: utf-8 -*-
from functions import cenik
import sys

def main():
    assert cenik("kruh" == 50), "Kruh ni 50?!";
    assert cenik("pivo" == 12), "Pivo ni 12?!";
    assert cenik("racunalnik" == 200), "Racunalnik ni 200?!";
    assert cenik("NIC" == "nimamo_cene"), "Kaj si vrnil, ce niammo cene?!";
    print cenik("kruh");
    print cenik("pivo");
    print cenik("racunalnik");
    print cenik("NIC");
if __name__ == "__main__":
    main()