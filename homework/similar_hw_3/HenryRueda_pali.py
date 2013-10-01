# -*- coding: UTF-8 -*-
#!/usr/bin/env python


import sys, codecs
from string import lower


if len(sys.argv)<2:
    print('\nNo hay suficiente información\n'.format(sys.argv[0]))
    sys.exit(0)


filein = codecs.open(sys.argv[1], "r", "utf8")
archivo = filein.readlines()




lineas = []

for n in archivo :
        menor = str(n).lower()
        lineas.append(menor.decode("utf-8"))
#Datos obtenidos del github de Jaime Forero
        
remove = ['0','1','2','3','4','5','6','7','8','9',' ', ',', '_', '-', '*','+','.', ',','(', ')', '#','"','[',']', '\n','\r', ';', ':', '!', '"', '#', '$', '%', '&', '/', '?', u'\u0027', u'\xc2', u'\xbf', '',  '¡', ' ' , '\n' , '\r' , ',' , '.' , ';' , ':' , '!' , '@' , '#' , '$' , '%' , '^' , '*' , '(' , ')' , '-' , '_' , '+' , '=' , '/' , '|' , '?' , "'" , '[' , ']' , '{' , '}' , '<' , '>' , '~' , '"' , '\t', '&', '»'.decode( 'utf-8' ) ,  '«'.decode( 'utf-8' ) , '·'.decode( 'utf-8' ) , '”'.decode( 'utf-8' ) , '“'.decode( 'utf-8' ) , '—'.decode( 'utf-8' ) , '’'.decode( 'utf-8' ) , '‘'.decode( 'utf-8' ),'\ufeff'.decode( 'utf-8 ') , '̄'.decode( 'utf-8' ), '\xef\xbb\xbf'.decode( 'utf-8' )]
 
while '\n' in lineas:
    lineas.remove('\n')
        
for n in range(0, len(lineas)):
    for l in lineas[n]:
        for m in remove:
            if m==l:
                	lineas[n]=lineas[n].replace(l,'')
	break

while '' in lineas:
    lineas.remove('')
 
for n in range(0, len(lineas)): 
    for i in lineas[n]:
        	if i == u'\xe1': 
            		lineas[n]=lineas[n].replace(i,'a')
		elif i == u'\xc1': 
			lineas[n]=lineas[n].replace(i,'a')
        	elif i == u'\xe9':
            		lineas[n]=lineas[n].replace(i,'e') 
		elif i == u'\xc9':
            		lineas[n]=lineas[n].replace(i,'e') 
       		elif i == u'\xed':
        		lineas[n]=lineas[n].replace(i,'i') 
		elif i == u'\xcd':
        		lineas[n]=lineas[n].replace(i,'i') 
        	elif i == u'\xf3':
            		lineas[n]=lineas[n].replace(i,'o')
		elif i == u'\xd3':
            		lineas[n]=lineas[n].replace(i,'o')     
        	elif i == u'\xfa':
            		lineas[n]=lineas[n].replace(i,'u') 
		elif i == u'\xda':
            		lineas[n]=lineas[n].replace(i,'u') 
            
for j in lineas: 
    if j==j[::-1]: 
        print j, 'True'
    else:
        print j, 'False'



