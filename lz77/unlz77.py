import codecs
import math
import sys

tupl = [];
lista = [];

fileName = sys.argv[1]

outputFile = codecs.open(fileName, encoding='utf-8', mode='r')

data = ""

while True:
	c = outputFile.read(1)
	if c is None or len(c) == 0:
		break;

	index = ord(c)

	if index == 0:
		index = 0
		size = 0
	elif index % 2 == 1:
		index = index/2
		size = ord(outputFile.read(1))
	else:
		index = index/2
		size = 1


	letter = outputFile.read(1)

	data += data[index:index+size] + letter

outputFile = codecs.open(fileName.strip('.lz77') + ".decompressed77", encoding='utf-8', mode='w')
outputFile.write(data)



#print data

# 	if index == 0:
# 		lista.append(letter)
# 	else:
# 		prefix = lista[index-1]
# 		lista.append(prefix+letter)

# string = ""
# for i in lista:
#     string += i;
# print string