import sys, math

if len(sys.argv) != 2:
	print "Este programa necesita un (1) argumento para funcionar"
	sys.exit()

n = int(sys.argv[1])
i = 3
factores = []

if n <= 1:
	print "El numero no puede ser negativo o igual a 1"
	sys.exit()
if n > 1000000:
	print "El numero no puede ser superior a 1.000.000"
	sys.exit()

while n%2 == 0:
	factores.append(2)
	n = n/2

for i in range(3, int(math.sqrt(n)),2):
	while n%i == 0:
		factores.append(i)
		n = n/i

if n>2:
	factores.append(n)

if len(factores) == 1:
	print "El numero que digito es primo"
elif len(factores) == 2:
	print factores[0], factores[1]
else:
	print "El numero que digito no puede ser descompuento en solo 2 factores primos"
