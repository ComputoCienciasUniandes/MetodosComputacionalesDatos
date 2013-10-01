#!/usr/bin/ python
#encoding: UTF-8

import sys, codecs
import os 

directorio = os.listdir('./')

for file in directorio:
    infile = open(file,'r')
    numline = infile.readlines()
    ubicacion = len(numline)
    print file, ubicacion



