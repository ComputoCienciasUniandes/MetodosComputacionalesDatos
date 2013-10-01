import sys, string, os
import math

numeroEntrada = int(sys.argv[1])
numero = 0
primo = 0

if(numeroEntrada < 0 ):
    print("El numero es negativo")
    exit(1)
 
if(numeroEntrada > 1000000):
   print("El numero es mayor a 1000000")
   exit(1)


def factorizar(num):
    primos  = [ ]
    primerNumero = num

    while primerNumero % 2 == 0:
        primos.append(2)
        primerNumero /= 2

    cuenta = 3
    raiz = int(math.sqrt(primerNumero))
    while cuenta <= raiz and primerNumero > 1:
        if primerNumero % cuenta == 0:
            primos.append(cuenta)
            primerNumero /= cuenta
        else:
            cuenta += 2
    if primerNumero > 1:
        primos.append(primerNumero)
    return primos

numeroFactores = factorizar(numeroEntrada)

if(len(numeroFactores)==1):
  print "El numero es primo"
  exit(1)
if ( len(numeroFactores) != 2):
   print "El numero no se descompone en dos factores primos"
   exit(1)

else:
   print numeroFactores[0] ,numeroFactores[1]






           

      



     


