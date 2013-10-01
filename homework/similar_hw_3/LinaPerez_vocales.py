# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import sys
import codecs

#verificar el sys

if len(sys.argv)<2:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programaa\n'.format(sys.argv[0]))
    sys.exit(0)

# abrir los archivos y que los lea


filein = codecs.open(sys.argv[1], "r", "utf8")
carp = filein.read()
text = carp.lower() 
#make everything lower case
filein.close()

#crear los contadores de las variables

numa = 0
nume = 0 
numi = 0
numo = 0
numu = 0

#contar las vocales en todo el texto y almacenarlas en los contadores

for letter in text:
    if letter in 'a' or letter in u'\u00E1':
        numa+=1
    elif letter in 'e' or letter in u'\u00E9':
        nume+=1
    elif letter in 'i' or letter in u'\u00ED':
        numi+=1
    elif letter in 'o' or letter in u'\u00F3':
        numo+=1
    elif letter in 'u' or letter in u'\u00FA':
        numu+=1

#imprimir el numero de vocales
print('\na : {}'.format(numa))
print('\ne : {}'.format(nume))
print('\ni : {}'.format(numi))
print('\no : {}'.format(numo))
print('\nu : {}'.format(numu))
