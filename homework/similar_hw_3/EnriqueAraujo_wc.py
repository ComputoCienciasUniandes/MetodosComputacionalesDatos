import os

path = os.getcwd()
n = 0;

dirList=os.listdir(path)

for fname in dirList:
	if os.path.isdir(fname) == 0:
		n = len(open(fname,'r').readlines())
		print fname, n
