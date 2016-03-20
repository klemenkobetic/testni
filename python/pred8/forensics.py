# -*- coding: utf-8 -*-

import sys
from __builtin__ import str


def main():
    random = 15
    # SyntaxError: Non-ASCII character '\xc4' in file random.py on line 5,
    # but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
    print("Just testing foreign signs : čšćđž")
    tekst = "Please enter number : "

    f = open("dna.txt")
    data = f.readlines()
    f.close()
    #print(data)
    ziga=0
    matej=0
    miha=0

    lasje_crna = "CCAGCAATCGC"
    lasje_rjava =  "GCCAGTGCCG"
    lasje_korencek = "TTAGCTATCGC"

    obraz_kvadraten = "GCCACGG"
    obraz_okrogel = "ACCACAA"
    obraz_ovalen = "AGGCCTCA"

    oci_modra = "TTGTGGTGGC"
    oci_zelena = "GGGAGGTGGC"
    oci_rjava = "AAGTAGTGAC"

    spol_moski = "TGCAGGAACTTC"
    spol_zenska = "TGAAGGACCTTC"

    rasa_Belec = "AAAACCTCA"
    rasa_crnec = "CGACTACAG"
    rasa_azijec = "CGCGGGCCG"

    if(lasje_crna in str(data)):
        print("Lasje so crni")
        matej=matej+1
    if(lasje_korencek in str(data)):
        print("Lasje so korencek")
        ziga=ziga+1
    if(lasje_rjava in str(data)):
        print("Lasje so rjava")
        miha=miha+1

    if(obraz_kvadraten in str(data)):
        print("Obraz je kvadraten")
        miha = miha + 1
    if(obraz_okrogel in str(data)):
        print("Obraz je okrogel")
        ziga = ziga + 1
    if(obraz_ovalen in str(data)):
        print("Obraz je ovalen")
        matej = matej + 1

    if(oci_modra in str(data)):
        print("Oči so modre")
        matej = matej + 1
    if(oci_rjava in str(data)):
        print("Oči so rjave")
        ziga = ziga + 1
    if(oci_zelena in str(data)):
        print("Oči so zelene")
        miha = miha + 1

    if(spol_moski in str(data)):
        print("Moški je")
        miha = miha + 1
        ziga = ziga + 1
        matej = matej + 1
    if(spol_zenska in str(data)):
        print("Ženska je")

    if(rasa_azijec in str(data)):
        print("Azijec je")
    if(rasa_Belec in str(data)):
        print("Belec je")
        miha = miha + 1
        ziga = ziga + 1
        matej = matej + 1
    if(rasa_crnec in str(data)):
        print("Crnec je")

    # Žiga:
    # Spol: Moški
    # Rasa: Belec
    # Barva las: Oranžna
    # Barva oči: Rjava
    # Oblika obraza: Okrogla
    #
    # Matej:
    # Spol: Moški
    # Rasa: Belec
    # Barva las: Črna
    # Barva oči: Modra
    # Oblika obraza: Ovalna
    #
    # Miha:
    # Spol: Moški
    # Rasa: Belec
    # Barva las: Rjava
    # Barva oči: Zelena (kot Esmeralda, ki je bila njegova mladostna vzornica)
    # Oblika obraza: Kvadratna

    winner = "Matej"
    if (miha > matej):
        winner = "Miha"
    if (ziga > matej & ziga > miha):
        winner = "Miha"
    #print(miha,matej,ziga)
    print("Najbolj ustreza : " + winner)
    print("You are a genious. Buy yourself a beer!")

if __name__ == "__main__":
    main()