filename = 'empty.txt'
myFile = open(filename, "w")

myFile.write('Hello Python!\n')
myFile.write('Save me Jeebus!!\n')
myFile.seek(0)

for line in open(filename):
    print (line)

myFile.close()
