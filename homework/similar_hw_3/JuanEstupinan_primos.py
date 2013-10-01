import sys
def esPrimo (num):
    for divisor in range(2,num):
        if (num%divisor == 0):
            return False
    return True


n_argv = len(sys.argv)
if n_argv != 2:
    print "el Programa debe inicializarse con un entero"
    sys.exit(1)

#hacer lista de primos
for i in range(n_argv):
    print sys.argv[i]

listaprimos = [2]
n = int(sys.argv[1])
if n>1000000 or n<0:
    print "el numero debe ser menor a millon o positivo"
nd = float(sys.argv[1])
i=3
for i in range(3,n+1):
    if (esPrimo(i)):
        listaprimos.append(i)

for item in listaprimos:
    div = nd/item
    for num in listaprimos:
        if div == num:
            print item, num
            sys.exit(0)

print "el numero no puede espresarse como producto de primos"
