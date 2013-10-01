# -*- coding: UTF-8 -*-
#!/usr/bin/env python

## Author: Mateo Restrepo

import sys, codecs
from string import lower

#Si el programa recibe menos de dos argumentos por consola no se ejecuta.
if len(sys.argv)<2:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)


#Abre el archivo con el encoding correcto, lee todo y guarda cada línea en una lista.
filein = codecs.open(sys.argv[1], "r", encoding='utf8')
texto = filein.readlines()
lineas = []

#Pasa todo el texto minusculas.	
for c in texto:
	lineas.append(c.lower())

#Arreglo de caracteres para eliminar de cualquier string en el texto.        
eliminar = [u'0',u'1',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u' ', u',', u'_', u'-', u'*', u'+', u'.', u',', u'(', u')', u'#', u'"', u'[', u']', u'\n', u'\r', u';', u':', u'!', u'"', u'#', u'$', u'%', u'&', u'/', u'?', u'',  u'¡', u' ' , u'\n' , u'\r' , u',' , u'.' , u';' , u':' , u'!' , u'@' , u'#' , u'$' , u'%' , u'^' , u'*' , u'(' , u')' , u'-' , u'_' , u'+' , u'=' , u'/' , u'|' , u'?' , u"'" , u'[' , u']' , u'{' , u'}' , u'<' , u'>' , u'~' , u'"' , u'\t', u'&','»'.decode( 'utf-8' ) ,  '«'.decode( 'utf-8' ) , '·'.decode( 'utf-8' ) , '”'.decode( 'utf-8' ) , '“'.decode( 'utf-8' ) , '—'.decode( 'utf-8' ) , '’'.decode( 'utf-8' ) , '‘'.decode( 'utf-8' ),'\ufeff'.decode( 'utf-8 ') , '̄'.decode( 'utf-8' ), '\xef\xbb\xbf'.decode( 'utf-8' ) ]
 
#Elimina líneas vacias en el archivo.
while '\n' in lineas:
    lineas.remove('\n')

#Elimina cualquier caracter en la lista de caracteres a eliminar de las líneas guardadas en la lista.        
for i in range(0, len(lineas)):
    for j in lineas[i]:
        for m in eliminar:
            if j==m:
                lineas[i]=lineas[i].replace(j,'')
                break

#Elimina cualquier string vacio que haya quedado luego de la eliminación de caracteres indeseados
while '' in lineas:
    lineas.remove('')


 
#Revisa las lineas y si exiten vocales con acento las cambia a vocales sin acento.
for i in range(0, len(lineas)): 
    for c in lineas[i]:
        if c == u'\xe1' or c == u'\xc1':
            lineas[i]=lineas[i].replace(c,'a') 
        elif c == u'\xe9' or c == u'\xc9':
            lineas[i]=lineas[i].replace(c,'e') 
        elif c == u'\xed' or c == u'\xcd':
            lineas[i]=lineas[i].replace(c,'i') 
        elif c == u'\xf3' or c == u'\xd3':
            lineas[i]=lineas[i].replace(c,'o')     
        elif c == u'\xfa' or c == u'\xda':
            lineas[i]=lineas[i].replace(c,'u') 
 
#Imprime un mensaje indicando que líneas del texto son palindromos.            
for s in lineas: 
    if s == s[::-1]: 
        print '\n', s, 'TRUE! Es un palindromo'
    else:
        print '\n', s, 'FALSE! No es un palindromo'
print '\n'
