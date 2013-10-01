import os

direct=os.getcwd()
n=0

lines= os.listdir(direct)

for nombre in lines:
	if os.path.isdir(nombre)==0:
		n=len(open(nombre,'r').readlines())
		print nombre, n
