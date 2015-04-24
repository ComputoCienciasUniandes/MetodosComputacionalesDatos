# -*- coding: UTF-8 -*-
#!/usr/bin/env python

## Author: Mateo Restrepo

import os

#Crea un arreglo con los archivos y directorios en el directorio de ejecución del programa.
archivos = os.listdir(os.getcwd())

#Recorre buscando archivos y contando su número de líneas. Imprime el archivo y cuantas líneas tiene.
for nombre_archivo in archivos:
    if os.path.isdir(nombre_archivo) != True:#Revisa la dirección no sea de un directorio.
        archivo = open(nombre_archivo, 'r')
        file_lines = archivo.readlines()
        print 'El archivo:', nombre_archivo,'tiene',  len(file_lines), 'lineas\n' 
        archivo.close()
