# -*- coding: utf-8 -*- 
import sys, string, os, codecs

archivo = codecs.open(str(sys.argv[1]), encoding='utf-8')
conteo = [0,0,0,0,0]

while 1:
	char = archivo.read(1)          
	if not char: break

	if char == 'a' or char == 'A' or char == u'á' or char == u'Á':
		conteo[0] += 1
	elif char == 'e' or char == 'E' or char == u'é' or char == u'É':
		conteo[1] += 1
	elif char == 'i' or char == 'I' or char == u'í' or char == u'Í':
		conteo[2] += 1
	elif char == 'o' or char == 'O' or char == u'ó' or char == u'Ó':
		conteo[3] += 1
	elif char == 'u' or char == 'U' or char == u'ú' or char == u'Ú':
		conteo[4] += 1

print 'a', conteo[0]
print 'e', conteo[1]
print 'i', conteo[2]
print 'o', conteo[3]
print 'u', conteo[4]

archivo.close()
