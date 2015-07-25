import codecs
import math
import sys

tupl = [];
lista = [];

fileName = sys.argv[1]

outputFile = codecs.open(fileName, encoding='utf-8', mode='r')

def cantorPair(x, y):
	return 1/2*(x+y)*(x+y+1)*y;

def reverseCantor(z):

	print z

	i = (-1 + math.sqrt(1+8*z))/2
	i = math.floor(i)

	x = z - (i + i*i)/2

	y = (i * ( 3 + i ))/2 -z

	return (x,y)

def writeFile(index, size, letter):
	outputFile.write(unichr(cantorPair(size,index)))
	outputFile.write(letter)  

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

print data

# 	if index == 0:
# 		lista.append(letter)
# 	else:
# 		prefix = lista[index-1]
# 		lista.append(prefix+letter)

# string = ""
# for i in lista:
#     string += i;
# print string