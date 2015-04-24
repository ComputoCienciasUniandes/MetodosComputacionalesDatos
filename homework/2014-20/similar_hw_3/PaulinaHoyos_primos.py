import sys

#function that calculates all prime divisors of a number
def factor(n, d = 2):
    if (n%d == 0):
        return [d]+factor(n/d,d)
    if (d*d > n):
        if (n != 1):
            return [n]
        return []
    return factor(n,d+1)


num = int(sys.argv[1])

if(num<0):
    print "El numero es negativo"
elif(num>1000000):
    print "El numero es mayor que 1e6"
else:
    p = factor(num)
    if (len(p) == 2):
        print p[0],p[1]
    else:
        print "El numero no se puede factorizar por 2 primos"
