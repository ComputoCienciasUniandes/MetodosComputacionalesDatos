#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys , string, os,codecs

infile = codecs.open(sys.argv[1] , 'r', "utf-8")
lines = infile.readlines()

infile.close()

numeroA = 0
numeroE = 0
numeroI = 0
numeroO =0
numeroU =0

for lin in lines:
   for letra in lin:
      if letra== 'a' or letra == 'A' or letra == u'á' or letra ==u'Á':
        numeroA = numeroA +1

for lin in lines:
   for letra in lin:
      if letra== 'e' or letra == 'E' or letra == u'é' or letra == u'É':
        numeroE = numeroE +1

for lin in lines:
   for letra in lin:
      if letra== 'i' or letra == 'I' or letra == u'í' or letra == u'Í':
        numeroI = numeroI +1

for lin in lines:
   for letra in lin:
      if letra== "o" or letra == "O" or letra == u'ó' or letra == u'Ó':
        numeroO = numeroO +1

for lin in lines:
   for letra in lin:
      if letra== "U" or letra=="u" or letra == u'ú' or letra == u'Ú':
        numeroU = numeroU +1

print "a",numeroA
print "e",numeroE
print "i",numeroI
print "o",numeroO
print "u",numeroU
