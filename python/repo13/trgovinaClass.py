# -*- coding: utf-8 -*-

import sys
# class notebook(contact):
class Contact:
    def __init__(self):
        ime = ""
        primek = ""
        naslov = ""
        telefonskaStevilka = ""
        email = ""
    def __init__(self, arg_ime, arg_priimek, arg_naslov, arg_telefonskaStevilka, arg_email):
        self.ime = arg_ime
        self.priimek = arg_priimek
        self.naslov = arg_naslov
        self.telefonskaStevilka = arg_telefonskaStevilka
        self.email = arg_email
    def __str__(self):
        return self.ime + " " + self.priimek

class ContactExt(Contact):
    def __init__(self, arg_ime, arg_priimek, arg_naslov, arg_telefonskaStevilka, arg_email, arg_spol):
        Contact.__init__(self, arg_ime, arg_priimek, arg_naslov, arg_telefonskaStevilka, arg_email)
        self.spol = arg_spol
    def __str__(self):
        return self.ime + " " + self.priimek + " Spol : " + self.spol

class Ljubica(Contact):
    def __init__(self, arg_contact, arg_ljubica,):
        Contact.__init__(self, arg_contact.ime, arg_contact.priimek, arg_contact.naslov, arg_contact.telefonskaStevilka, arg_contact.email)
        self.ljubica = arg_ljubica
    def __str__(self):
        return self.ime + " " + self.priimek + " Ljubica : " + self.ljubica

def main():
    # notebook = []
    # while (raw_input("Do you want to add a new contact ? ").lower() in ["d", "da", "y", "yes"]):
    #     ime = raw_input("Please enter ime : ")
    #     priimek = raw_input("Please enter priimek : ")
    #     naslov = raw_input("Please enter naslov : ")
    #     telefonskaStevilka = raw_input("Please enter telefonska stevilka : ")
    #     contact1 = Contact(ime,priimek,naslov,telefonskaStevilka,raw_input("Please enter email : "))
    #     notebook.append(contact1)
    #
    # for contact in notebook:
    #     print contact

    # notebook = []
    # while (raw_input("Do you want to add a new contact ? ").lower() in ["d", "da", "y", "yes"]):
    #     ime = raw_input("Please enter ime")
    #     priimek = raw_input("Please enter priimek")
    #     naslov = raw_input("Please enter naslov")
    #     telefonskaStevilka = raw_input("Please enter telefonska stevilka")
    #     email = raw_input("Please enter email")
    #     contact1 = ContactExt(ime,priimek,naslov,telefonskaStevilka,email, raw_input("Please enter gender details : "))
    #     notebook.append(contact1)
    #
    # for contact in notebook:
    #     print contact

    notebook = []
    while (raw_input("Do you want to add a new contact ? ").lower() in ["d", "da", "y", "yes"]):
        ime = raw_input("Please enter ime")
        priimek = raw_input("Please enter priimek")
        naslov = raw_input("Please enter naslov")
        telefonskaStevilka = raw_input("Please enter telefonska stevilka")
        email = raw_input("Please enter email")
        contact1 = Contact(ime,priimek,naslov,telefonskaStevilka,email)
        contact2 = Ljubica(contact1, raw_input("Ali je to tvoja ljubica ? "))
        notebook.append(contact2)

    for contact in notebook:
        print contact

if __name__ == "__main__":
    main()

# Naredi program, v katerega bo uporabnik lahko shranjeval svoje kontakte.
#
# Program ga bo najprej vprašal, če želi uporabnik dodati nov kontakt.
# V kolikor bo odgovor da, mu bo program rekel, naj doda: ime kontakta, priimek kontakta, naslov kontakta,
# tel.št. kontakta in email kontakta.
# Program naj teče v zanki, torej naj vsakič znova vpraša, ali želi uporabnik dodati nov kontakt.
# Če uporabnik ne bo več želel dodati novega kontakta, bo program izpisal seznam vnešenih kontaktov ter se zaključil.
# Hint: Kako narediti model za kontakt (Kontakt):
#
# ime modela/classa je Kontakt().
# spremenljivke so:
# first_name
# last_name
# email
# phone
# address
# Naredi funkcijo __init__, s katero boš ustvarjal/a objekte.
# V modelu tudi ustvari funkcijo, ki bo izpisala polno ime uporabnika (torej skupaj first_name in last_name).
# Ko bo uporabnik dodajal nove kontakte, naredi za vsakega svoj objekt in objekte shranjuj v seznam (list).
# Na koncu uporabniku izpišeš vse objekte v tem seznamu.