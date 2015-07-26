
import sys
import codecs
import math
import string

fileName = sys.argv[1]
inputFile = codecs.open(fileName, encoding='utf-8', mode='r')
outputFile = codecs.open(fileName + '.lz77', encoding='utf-8', mode='w')

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
	maxsize = min(len(prev), 512, len(data))
	for size in range(maxsize, 0, -1):
		index = string.find(prev, data[:size])
		if index > -1:
			return (index, size) 
	return (0, 0)


step = 0
#print data
while len(data) > 0:
	#print 'step =', step 
	(index, size) = findIndex(prev, data)

	#handle special case end of stream	
	if size >= len(data):
		letter = ''
	else:
		letter = data[size]
	
	#print (index, size)
	writeFile(index, size, letter)
	

	prev += prev[index:index+size] + letter
	#prev = prev[-1028:]
	data = data[size+1:]

	#print prev+'|'+data
	step += 1