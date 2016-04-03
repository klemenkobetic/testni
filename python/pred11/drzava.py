# -*- coding: utf-8 -*-
from functions import glavno_mesto
from functions import preveri_glavno_mesto
import sys

def main():
#    Naredi funkcijo, ki bo kot input vzela ime države ter vrnila njeno glavno mesto.
    glavno_mesto("Italija");
# Naredi še eno funkcijo, ki bo kot input vzela glavno mesto ter državo, ter nato
# preverila, ali je podano mesto res glavno mesto te podane države. To je funkcija,
#  ki preveri, ali je uporabnikov odgovor v kvizu Ugani glavno mesto države, res pravilen.
# Ta funkcija naj za pomoč kliče prvo funkcijo.

    print preveri_glavno_mesto(raw_input("Vnesi drzavo : "), raw_input("Vnesi mesto : "));
if __name__ == "__main__":
    main()