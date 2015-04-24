import os
import sys

infile = open(sys.argv[1],'r')
text = infile.readlines( )

for linea in text:
    caracteres = [c for c in linea.lower() if c.isalpha()]
    
    if(caracteres == caracteres[::-1]):
      print True 
    else:
      print False


