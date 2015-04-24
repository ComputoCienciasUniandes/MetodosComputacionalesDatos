# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import sys
import codecs
from string import lower

if len(sys.argv)<2:
    print('\nSe necesita otro parametro aparte de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)

filein = codecs.open(sys.argv[1], "r", "utf8")
txt = filein.readlines()

lineas = []
for i in txt :
        lower = str(i).lower()
        lineas.append(lower.decode("utf-8"))

remov = [' ','.', ',','"','[',']', '\n','\r', ';', ':', '/', '?', '',  '¡','+', '.' , ';' , ':' , ')' , '(' , '*' , '&' , '^' , '%' , '$' , '#' , '@' , '!', '-' , '_' , '+' , '=' ,'|' , '?' , "'" , '{' , '}' , '<' , '>' , '~', '\t', '1','2','3','4','5','6','7','8','9','0', '»'.decode( 'utf-8' ) ,  '«'.decode( 'utf-8' ) , '·'.decode( 'utf-8' ) , '”'.decode( 'utf-8' ) , '“'.decode( 'utf-8' ) , '—'.decode( 'utf-8' ) , '’'.decode( 'utf-8' ) , '‘'.decode( 'utf-8' ),'\ufeff'.decode( 'utf-8 ') , '̄'.decode( 'utf-8' ), '\xef\xbb\xbf'.decode( 'utf-8' ), u'\u0027', u'\xc2', u'\xbf']
 
while '\n' in lineas:
    lineas.remove('\n')
        
for i in range(0, len(lineas)):
    for j in lineas[i]:
        for let in remov:
            if j==let:
                lineas[i]=lineas[i].replace(j,'')
                break

while '' in lineas:
    lineas.remove('')
 
for i in range(0, len(lineas)): 
    for vocales in lineas[i]:

        if vocales == u'\xe1' or vocales == u'\xc1':
            lineas[i]=lineas[i].replace(vocales,'a') 
        elif vocales == u'\xe9' or vocales == u'\xc9':
            lineas[i]=lineas[i].replace(vocales,'e') 
        elif vocales == u'\xed' or vocales == u'\xcd':
            lineas[i]=lineas[i].replace(vocales,'i') 
        elif vocales == u'\xf3' or vocales == u'\xd3':
            lineas[i]=lineas[i].replace(vocales,'o')     
        elif vocales == u'\xfa' or vocales == u'\xda':
            lineas[i]=lineas[i].replace(vocales,'u') 

for pali in lineas: 
    if pali == pali[::-1]: 
        print 'TRUE'
    else:
        print 'FALSE'



