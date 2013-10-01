#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys, codecs
from string import lower

if len(sys.argv)<2:
    print('\nNo hay suficiente información\n'.format(sys.argv[0]))
    sys.exit(0)


filein = codecs.open(sys.argv[1], "r", "utf8")
documento = filein.read()
archivo = documento.lower() 
filein.close()


lista_a=0
lista_e=0
lista_i=0
lista_o=0
lista_u=0

for vocal in archivo:
    if vocal in 'a' or vocal in u'\u00E1':
        lista_a +=1
    elif vocal in 'e' or vocal in u'\u00E9':
        lista_e +=1
    elif vocal in 'i'or vocal in u'\u00ED':
        lista_i +=1
    elif vocal in 'o'or vocal in u'\u00F3':
        lista_o +=1
    elif vocal in 'u'or vocal in u'\u00FA':
        lista_u +=1

print('\n a:'.format(lista_a))
print('\n e:'.format(lista_e))
print('\n i:'.format(lista_i))
print('\n o:'.format(lista_o))
print('\n u:'.format(lista_u))
    
        

