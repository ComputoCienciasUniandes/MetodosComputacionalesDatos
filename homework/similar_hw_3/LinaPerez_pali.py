# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import sys
import codecs
from string import lower

#verificar que le archivo este bien
if len(sys.argv)<2:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)


#abrir el archivo y leerlo
filein = codecs.open(sys.argv[1], "r", "utf8")
text = filein.readlines()


#separar el texto por lineas

lines = []

for i in text :
        lower = str(i).lower()
        lines.append(lower.decode("utf-8"))

   #eliminar todo lo que no son letras     
borrar = [' ','.', ',','"','[',']', '\n','\r', ';', ':', '/', '?', '',  '¡','+', '.' , ';' , ':' , ')' , '(' , '*' , '&' , '^' , '%' , '$' , '#' , '@' , '!', '-' , '_' , '+' , '=' ,'|' , '?' , "'" , '{' , '}' , '<' , '>' , '~', '\t', '1','2','3','4','5','6','7','8','9','0', '»'.decode( 'utf-8' ) ,  '«'.decode( 'utf-8' ) , '·'.decode( 'utf-8' ) , '”'.decode( 'utf-8' ) , '“'.decode( 'utf-8' ) , '—'.decode( 'utf-8' ) , '’'.decode( 'utf-8' ) , '‘'.decode( 'utf-8' ),'\ufeff'.decode( 'utf-8 ') , '̄'.decode( 'utf-8' ), '\xef\xbb\xbf'.decode( 'utf-8' ), u'\u0027', u'\xc2', u'\xbf']
 
#remove de las lineas lo que se debe borrar
while '\n' in lines:
    lineas.remove('\n')
        
for i in range(0, len(lines)):
    for j in lines[i]:
        for nom in borrar:
            if j==nom:
                lines[i]=lines[i].replace(j,'')
                break

#ayudaaaaaaaaaaaaaaaaaa
while '' in lines:
    lines.remove('')
 
#igualando vocales
for i in range(0, len(lines)): 
    for voc in lines[i]:

        if voc == u'\xe1' or voc == u'\xc1':
            lines[i]=lines[i].replace(voc,'a') 

        elif voc == u'\xe9' or voc == u'\xc9':
            lines[i]=lines[i].replace(voc,'e') 

        elif voc == u'\xed' or voc == u'\xcd':
            lines[i]=lines[i].replace(voc,'i') 

        elif voc == u'\xf3' or voc == u'\xd3':
            lines[i]=lines[i].replace(voc,'o')     

        elif voc == u'\xfa' or voc == u'\xda':
            lines[i]=lines[i].replace(voc,'u') 

 #mirar si si es palindromo o no cada linea y imprimir true o false           
for let in lines: 
    if let == let[::-1]: 
        print 'TRUE'
    else:
        print 'FALSE'



