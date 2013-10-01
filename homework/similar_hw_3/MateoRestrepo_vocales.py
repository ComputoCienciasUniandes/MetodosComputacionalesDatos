# -*- coding: UTF-8 -*-
#!/usr/bin/env python

## Author: Mateo Restrepo

import sys, codecs

#Si el programa recibe menos de dos argumentos por consola no se ejecuta.
if len(sys.argv)<2:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)


#abre el archivo con el enconding correcto y lee todo el texto.
filein = codecs.open(sys.argv[1], "r", "utf8")
archivo = filein.read()
#Pasa todo el texto a minusculas
texto = archivo.lower() 
filein.close()

#inicia los contadores de las vocales
cuenta_a=0
cuenta_e=0
cuenta_i=0
cuenta_o=0
cuenta_u=0

#Recorre el texto buscando el número de incidencia de cada vocal
for letter in texto:
    if letter in 'a' or letter in u'\u00E1':
        cuenta_a +=1
    elif letter in 'e' or letter in u'\u00E9':
        cuenta_e +=1
    elif letter in 'i'or letter in u'\u00ED':
        cuenta_i +=1
    elif letter in 'o'or letter in u'\u00F3':
        cuenta_o +=1
    elif letter in 'u'or letter in u'\u00FA':
        cuenta_u +=1

#Imprime en consola el número de vocales en el archivo.
print('\nNúmero de a en el archivo: {}\n'.format(cuenta_a))
print('\nNúmero de e en el archivo: {}\n'.format(cuenta_e))
print('\nNúmero de i en el archivo: {}\n'.format(cuenta_i))
print('\nNúmero de o en el archivo: {}\n'.format(cuenta_o))
print('\nNúmero de u en el archivo: {}\n'.format(cuenta_u))
    
        

