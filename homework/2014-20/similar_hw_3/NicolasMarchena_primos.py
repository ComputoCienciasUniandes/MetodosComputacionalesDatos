import sys, string, os
import math

entrada = int(sys.argv[1])
numero = 0
primo = 0

if(entrada < 0 ):
    print("El numero es negativo, ingrese un entero positivo")
    exit(1)
 
if(entrada > 1000000):
   print("El numero es demasiado grande ")
   exit(1)


def factorizar(num):
    #almacenamos los resultados
    #de la factorizacion en una lista
    primos  = [ ]
    num1 = num

    while num1 % 2 == 0:
        primos.append(2)
        num1 /= 2

    cuenta = 3
    raiz = int(math.sqrt(num1))
    while cuenta <= raiz and num1 > 1:
        if num1 % cuenta == 0:
            primos.append(cuenta)
            num1 /= cuenta
        else:
            cuenta += 2
    if num1 > 1:
        primos.append(num1)
    return primos

factores = factorizar(entrada)

if(len(factores)==1):
  print "el numero ya es un primo"
  exit(1)
if ( len(factores) != 2):
   print "el numero no se puede descomponer en dos factores primos"
   exit(1)

else:
   print factores[0] ,factores[1]






           

      



     


