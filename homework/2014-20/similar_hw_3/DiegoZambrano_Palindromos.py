import os
import sys

infile = open(sys.argv[1],'r')
text = infile.readlines( )

for lines in text:
    letras = [c for c in lines.lower() if c.isalpha()]
    
    if(letras == letras[::-1]):
      print True 
    else:
      print False


