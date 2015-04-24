#!/usr/bin/env python
# -*- coding: utf-8 -*- 


import sys,math


if len(sys.argv)<2:
    print('\nNo hay suficiente información\n'.format(sys.argv[0]))
    sys.exit(0)
    
Maximo=1000000
n=int(sys.argv[1])

if n<0:
	print('\nEl número ingresado es negativo\n'.format(Maximo))
    
if n == 0:
    print ('\n{} no es un número valido para ejecutar este programa\n'.format(0))
    sys.exit(0)

if n>Maximo:
    print('\nEl número es mayor que un millón\n'.format(Maximo))
    sys.exit(0)


arrayprimos = []    
factores = set()
for i in range(2, Maximo+1):
    if i not in factores:
        arrayprimos.append(i)
        factores.update(range(i*i, Maximo+1, i))
        
def es_primo(n):
        if n in arrayprimos:
            return True
        
if es_primo(n):
	    	print('\nEl número ingresado es primo\n'.format(n))
	    	sys.exit(0)
    

k=int(math.sqrt(n)+1)
for i in range (0,k):
    aux=float(n)/arrayprimos[i]
    if aux%1==0 and es_primo(aux):
        if aux!=arrayprimos[i]:
            print('\n{} y {}'.format(arrayprimos[i], int(aux))) 
            sys.exit(0)
            break
        else:
            print('\nexception'.format(arrayprimos[i], int(aux)))
            sys.exit(0)
            break

print('\nEl número en su descomposición tiene más de dos factores primos')
                


    


            

 
 
         
         
