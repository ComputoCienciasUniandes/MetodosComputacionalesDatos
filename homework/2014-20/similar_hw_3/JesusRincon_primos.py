import sys, string, os
import math 
numero= int(sys.argv[1])
primos=[]
i=3
if numero<1 or numero>1000000:
	print "El numero no esta en el rango"
	exit (1) 

while numero%2==0:
	primos.append(2)
	numero=numero/2
for i in range(3,int(math.sqrt(numero)),2):
	while numero%i==0:
		primos.append(i)
		numero=numero/i
if numero>2:
	primos.append(numero)
l = len(primos)
if l>2:
	print "El numero no es divisible en dos numeros primos"
if l==1:
	print "El numero es primo"
if l==2:
	print primos


