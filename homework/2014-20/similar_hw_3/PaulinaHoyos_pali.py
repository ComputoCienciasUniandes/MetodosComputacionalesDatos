#!/usr/bin/python
# -*- coding: utf-8 -*- 

import string
import sys
from unidecode import  unidecode

def remove_not_letters(line):
    return ''.join([unidecode(a) for a in line if a.isalpha()])

#open and read the file
file = open(sys.argv[1],'r')
text = file.readlines()
file.close()

for line in text:
   nl = remove_not_letters(line.decode('utf-8'))
   phrase = nl.upper()
   if(phrase[::-1]==phrase):
        print "true"
   else:
        print "false"
