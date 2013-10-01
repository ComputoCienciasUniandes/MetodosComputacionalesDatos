# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import sys
import math

mayor = 1000000
nprimos = 78498
numero=int(sys.argv[1])

if len(sys.argv)<2:
    print('\n Se necesita otro parametro aparte de {} para ejecutar este programa\n'.format(sys.argv[0]))
    sys.exit(0)

if numero == 0:
    print ('\n{} no es un valido\n'.format(0))
    sys.exit(0)

if numero<0 or numero>mayor:
    print('\nEl número es negativo o mayor que {}\n'.format(mayor))
    sys.exit(0)

array_prim = []    
multi = set()
for a in range(2, mayor+1):
    if a not in multi:
        array_prim.append(a)
        multi.update(range(a*a, mayor+1, a))

def siprimo(n):
        if n in array_prim:
            return True
        
if siprimo(numero):
    print('\nEl número {} es primo pero no se puede descomponer\n'.format(numero))
    sys.exit(0)
    
raiz = int(math.sqrt(numero)+1)
for a in range (0,raiz):
    aux = float(numero)/array_prim[a]
    if aux%1==0 and siprimo(aux):
        if aux!=array_prim[a]:
            print('\n{}  {}'.format(array_prim[a], int(aux))) 
            sys.exit(0)
            break
        else:
            print('\nexception'.format(array_prim[a], int(aux)))
            sys.exit(0)
            break

print('\nNo se puede descomponer')
