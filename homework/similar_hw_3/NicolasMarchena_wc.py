import sys , string, os
import os.path

dirname = os.getcwd()
lista = os.listdir(dirname)

def countLines(arch):
  contar= 0
  b=""
  a= open(arch,"r")
  for line in a:
     b=b+line
     contar=b.count("\n")
  print arch ,contar

for arch in lista:
  if(os.path.isfile(arch)==1):
   countLines(arch)
      

    


 

    

