#!/usr/bin/ python
#encoding: UTF-8
import sys, codecs
import os 

# leer el directorio donde se encuentra
dire = os.listdir('./')

# listar los archivos del directorio
for file in dire:
    # coger cada archivo y leerlo
    infile = open(file, 'r')
    # contar las lineas del archivo
    numline = infile.readlines()
    ubi = len(numline)
#imprimir el nombre del archivo y el numero de lineas
    print file, ubi



