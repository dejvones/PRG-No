#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:15:41 2017

@author: vla35123
"""

heslo = input("Zadej své heslo: ") 

MALA = "qwertzuiopasdfghjklyxcvbnm"
VELKA = MALA.upper()
SPEC = '!@#$%^&*(){}[]\|+-"\'~'
CISLA = "0123456789"

if len(heslo) < 8:
    print("Heslo je příliš krátké.")
    exit(1)

jeMALA = False
jeVELKA = False
jeSPEC = False
jeCISLA = False
for znak in heslo:
    if znak in MALA:
        jeMALA = True
    if znak in VELKA:
        jeVELKA = True
    if znak in SPEC:
        jeSPEC = True
    if znak in CISLA:
        jeCISLA = True

print(jeMALA, jeVELKA, jeSPEC, jeCISLA)
if jeMALA + jeVELKA + jeSPEC + jeCISLA >= 3:
    print("Heslo je v pořádku.")
    exit(0)
else:
    print("Heslo je příliš jednoduché.")
    exit(3)