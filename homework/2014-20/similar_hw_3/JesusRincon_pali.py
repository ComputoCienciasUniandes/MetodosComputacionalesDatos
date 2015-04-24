import sys

archivo=open(str(sys.argv[1]),'r')

lineas = archivo.readlines()

for nombre in lineas:
	letra= [c for c in nombre.lower() if c.isalpha()]
	print (letra==letra[::-1])

