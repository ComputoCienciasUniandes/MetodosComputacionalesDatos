import sys , string, os
import os.path

dirname = os.getcwd()
listado = os.listdir(dirname)

def countLines(arch):
  contador= 0
  b=""
  a= open(arch,"r")
  for line in a:
     b=b+line
     contador=b.count("\n")
  print arch ,contador

for arch in listado:
  if(os.path.isfile(arch)==1):
   countLines(arch)
      

    


 

    

