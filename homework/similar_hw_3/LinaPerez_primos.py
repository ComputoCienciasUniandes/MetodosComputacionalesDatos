# -*- coding: UTF-8 -*-
#!/usr/bin/env python

import sys
import math

#verificar el archivo

if len(sys.argv)<2:
    print('\n Se necesita otro parametro ademas de {} para ejecutar este programa\n'.format(sys.argv[0]))
    sys.exit(0)

#definir las variables
NumMayor = 1000000
Primos = 78498
num=int(sys.argv[1])

#error1: si el numero ingresado es cero
if num == 0:
    print ('\n{} no es un número valido\n'.format(0))
    sys.exit(0)

#error2: si el numero es menor que cero y menor mayor al numero mayor posible
if num<0 or num>NumMayor:
    print('\nEl número es negativo o mayor que {}\n'.format(NunMayor))
    sys.exit(0)

#arreglos
array_primos = []    
multiplos = set()
for i in range(2, NumMayor+1):
    if i not in multiplos:
        array_primos.append(i)
        multiplos.update(range(i*i, NumMayor+1, i))

#si el numero si es primo      
def siesprimo(n):
        if n in array_primos:
            return True
        
        #cuando el numero primo no se puede descomponer por la multiplicacion esa
if siesprimo(num):
    print('\nEl número {} es primo, pero no se puede descomponer\n'.format(num))
    sys.exit(0)
    
#encontrar en cuales numeros se puede descomponer 
raiz = int(math.sqrt(num)+1)
for i in range (0,raiz):
    auxiliar = float(num)/array_primos[i]
    if auxiliar%1==0 and siesprimo(auxiliar):
        if auxiliar!=array_primos[i]:
            print('\n{}  {}'.format(array_primos[i], int(auxiliar))) 
            sys.exit(0)
            break
        else:
            print('\nexception'.format(array_primos[i], int(auxiliar)))
            sys.exit(0)
            break

print('\nNo se puede descomponer')
