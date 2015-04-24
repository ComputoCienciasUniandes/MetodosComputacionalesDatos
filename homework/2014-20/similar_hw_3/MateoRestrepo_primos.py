# -*- coding: UTF-8 -*-
#!/usr/bin/env python

## Author: Mateo Restrepo


import sys,math

#Si el programa recibe menos de dos argumentos por consola no se ejecuta.
if len(sys.argv)<2:
    print('\nSe necesita otro parametro ademas de {} para ejecturar este programa\n'.format(sys.argv[0]))
    sys.exit(0)
    
#Define las constantes que usará el programa y crea una variable para el parámetro que ingresa por consola.
LIMITE=1000000
PRIMOS=78498
numero=int(sys.argv[1])


#Si el número es 0 no se puede efectuar división en factores primos.   
if numero == 0:
    print ('\n{} no es un número valido para ejecutar este programa\n'.format(0))
    sys.exit(0)

#Si el número es nagativo o mayor a 1000000 no se ejecuta el programa.
if numero<0 or numero>LIMITE:
    print('\nEl número Ingresado es negativo o mayor que {}\n'.format(LIMITE))
    sys.exit(0)

#Se genera un array de primos que contenga todos los primos menores que 1000000
arrayprimos = []    
multiples = set()
for i in range(2, LIMITE+1):
    if i not in multiples:
        arrayprimos.append(i)
        multiples.update(range(i*i, LIMITE+1, i))

#función que revisa si un número es primo.        
def es_primo(n):
        if n in arrayprimos:
            return True

#Si el número que entra por consola es primo no se puede descomponer.        
if es_primo(numero):
    print('\nEl número {} es primo! NO se puede descomponer como la multiplicación de dos factores primos\n'.format(numero))
    sys.exit(0)
    
#Recorre el arreglo de primos buscando dos factores primos del número ingresado.
s=int(math.sqrt(numero)+1)
for i in range (0,s):
    aux=float(numero)/arrayprimos[i]
    if aux%1==0 and es_primo(aux):
        if aux!=arrayprimos[i]:#Si los factores del número son dos primos diferentes imprime los factores.
            print('\nEl número {} se puede representar como la multiplicacón de: {} y {}\n'.format(numero, arrayprimos[i], int(aux))) 
            sys.exit(0)
            break
        else:#Si el número es el cuadrado de un número primo le indica al usuario y le devuelve dicho primo.
            print('\nHa escogido uno de los 168 números entre 1 y 1000000 que su raíz es un numero primo. Dicha raíz es: {}\n'.format(arrayprimos[i], ))
            sys.exit(0)
            break
#Si el número no se puede descomponer imprime un mensaje en consola.
print('\nEl número {} NO se puede representar como la multiplicacón de dos factores primos\n'.format(numero))
         




    

    


    
        
    
    
    
        


    


            

 
 
         
         
