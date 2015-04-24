#!/usr/bin/ python
#encoding: UTF-8
import sys, codecs

filein = codecs.open(sys.argv[1], "r", "utf8") 
fullin = filein.read()
fulltext = fullin.lower() 
filein.close()

lista = list(set(fulltext))

a=0
e=0
i=0
o=0
u=0

for letra in lista:
	if(letra== 'a' or letra== u'á'):
		a = a+1
	elif(letra== 'e' or letra== u'é'):
		e = e+1
	elif(letra== 'i' or letra== u'í'):
		i = i+1
	elif(letra== 'o' or letra== u'ó'):
		o = o+1
	elif(letra== 'u' or letra== u'ú'):
		u = u+1
		

print 'a=', a
print 'e=', e
print 'i=', i
print 'o=', o
print 'u=', u