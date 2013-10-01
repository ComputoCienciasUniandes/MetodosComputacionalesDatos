# -*- coding: utf-8

import sys, string, os, codecs 

infile=codecs.open(str(sys.argv[1]), encoding='utf-8')

vocales=[0,0,0,0,0]

while 1:
	char=infile.read(1)
	if not char: break
	if char=='a'or char=='A' or char==u'á':
		vocales[0]+=1
	elif char=='e'or char=='E' or char==u'é':
		vocales[1]+=1
	elif char=='i'or char=='I' or char==u'í':
		vocales[2]+=1	
	elif char =='o'or char=='O' or char==u'ó':
		vocales[3]+=1
	elif char =='u'or char=='U' or char==u'ú':
		vocales[4]+=1
print 'a', vocales[0]
print 'e', vocales[1]
print 'i', vocales[2]
print 'o', vocales[3]
print 'u', vocales[4]	

infile.close()


