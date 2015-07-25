
import sys
import codecs
import math

fileName = sys.argv[1]
inputFile = codecs.open(fileName, encoding='utf-8', mode='r')
outputFile = codecs.open(fileName + '.lz77', encoding='utf-8', mode='w')

def elegantPair(x, y):
	if (x>=y):
		return x*x + x + y
	else:
		return y*y + x

def cantorPair(x, y):
	return (x*x+3*x+2*x*y+y+y*y)/2

def writeFile(index, size, letter):

	#print elegantPair(size,index)
	if size > 1:
		outputFile.write(unichr(index*2+1))

		outputFile.write(unichr(size))
	else:
		outputFile.write(unichr(index*2+0))

	# outputFile.write(unichr(cantorPair(size,index)))

	outputFile.write(letter)  


data = "".join(inputFile.readlines())
prev = ""


def findIndex(prev, data):
	for index in range(0, len(prev)):
		maxsize = min(len(prev)-index, 256)
		for size in range(maxsize, 0, -1):
			if prev[index: index+size] == data[0: size]:
				return (index, size) 
	return (0, 0)


step = 0
print data
while len(data) > 0:
	print 'step =', step 
	(index, size) = findIndex(prev, data)

	#handle special case end of stream	
	if size >= len(data):
		letter = '\x00'
	else:
		letter = data[size]
	
	print (index, size)
	writeFile(index, size, letter)
	

	prev += prev[index:index+size] + letter
	#prev = prev[-1028:]
	data = data[size+1:]

	#print prev+'|'+data
	step += 1