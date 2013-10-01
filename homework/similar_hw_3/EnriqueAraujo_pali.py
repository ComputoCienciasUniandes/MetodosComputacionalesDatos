import sys

archivo = open(str(sys.argv[1]), 'r')

lineas = archivo.readlines()

for linea in lineas:
	
	letras = [c for c in linea.lower() if c.isalpha()]
	print (letras == letras[::-1])


