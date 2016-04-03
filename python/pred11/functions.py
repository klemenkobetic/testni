# -*- coding: utf-8 -*-

import sys

seznam_izdelkov = {
    "kruh":50,
    "pivo":12,
    "racunalnik":200,
    "NIC":"nimamo_cene"
}

seznam_drzav = {
    "Slovenija" : "Ljubljana",
    "Hrvaška" : "Zagreb" ,
    "Madžarska" : "Budimpešta",
    "Italija": "Rim"
}

def cenik(izdelek):
    if (izdelek=="kruh"):
        return seznam_izdelkov["kruh"];
    if (izdelek=="pivo"):
        return seznam_izdelkov["pivo"];
    if (izdelek == "racunalnik"):
        return seznam_izdelkov["racunalnik"];
    return seznam_izdelkov["NIC"];

def glavno_mesto(drzava):
    return seznam_drzav[drzava]
    #return seznam_izdelkov["NIC"];

def preveri_glavno_mesto(drzava, mesto):
    return (glavno_mesto(drzava) == mesto);

def main():
    exit();

if __name__ == "__main__":
    main()