# -*- coding: utf-8 -*-
# Código de python que cuenta las vocales (inlcuyendo mayúsculas y tildes) en un archivo
# texto recibido por parámetro.

import sys
import codecs
import string
import os

#Función auxiliar
def esPali(frase):
	fraseInvertida = frase[::-1]
	esPali = False
	if(frase == fraseInvertida):
		esPali = True
	return esPali

# Importar archivo desde terminal    	
filein = codecs.open(sys.argv[1], "r", "utf8")
texto = filein.readlines()
filein.close()

# Operaciones con las líneas
tamano = len(texto)

# Reconocimiento de mayúsculas, tildes y ñ
for i in range (0, tamano):
	texto[i] = texto[i].lower()
	texto[i] = texto[i].replace(u'á','a')
	texto[i] = texto[i].replace(u'é','e')
	texto[i] = texto[i].replace(u'í','i')
	texto[i] = texto[i].replace(u'ó','o')
	texto[i] = texto[i].replace(u'ú','u')

for i in range (0, tamano):
	#Remover otros caracteres
	texto[i] = texto[i].replace(',', '')
	texto[i] = texto[i].replace(';', '')
	texto[i] = texto[i].replace('.', '')
	texto[i] = texto[i].replace(':', '')
	texto[i] = texto[i].replace('-', '')
	texto[i] = texto[i].replace('-', '')
	texto[i] = texto[i].replace(' ', '')
	texto[i] = texto[i].replace('\n', '')
		
# Comparar palíndromos e imprimir resultados
for i in range (0, tamano):
	comprobacion = esPali(texto[i])
	print comprobacion