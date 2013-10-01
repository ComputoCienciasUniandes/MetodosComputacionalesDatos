import os
filenames = os.listdir(os.getcwd())

for filename in filenames:
    if (os.path.isfile(filename)):   
        file = open(filename, 'r')
        file_lines = file.readlines()
        print filename, len(file_lines)
    file.close()
