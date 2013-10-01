#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys , string, os,codecs

infile = codecs.open(sys.argv[1] , 'r', "utf-8")
lines = infile.readlines()

infile.close()

#contadores para la respuesta
numA = 0
numE = 0
numI = 0
numO =0
numU =0

    
#contar 

for lin in lines:
   for letra in lin:
      if letra== 'a' or letra == 'A' or letra == u'á' or letra ==u'Á':
        numA = numA +1

for lin in lines:
   for letra in lin:
      if letra== 'e' or letra == 'E' or letra == u'é' or letra == u'É':
        numE = numE +1

for lin in lines:
   for letra in lin:
      if letra== 'i' or letra == 'I' or letra == u'í' or letra == u'Í':
        numI = numI +1

for lin in lines:
   for letra in lin:
      if letra== "o" or letra == "O" or letra == u'ó' or letra == u'Ó':
        numO = numO +1

for lin in lines:
   for letra in lin:
      if letra== "U" or letra=="u" or letra == u'ú' or letra == u'Ú':
        numU = numU +1

#respuesta

print "a",numA
print "e",numE
print "i",numI
print "o",numO
print "u",numU
