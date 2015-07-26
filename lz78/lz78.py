#import pickle
import codecs
import sys

dictionary = {};
dictionary2 = {};
position = 1;
buf = "";
tupl = [];

fileName = sys.argv[1]
inputFile = codecs.open(fileName, encoding='utf-8', mode='r')
outputFile = codecs.open(fileName + '.lz78', encoding='utf-8', mode='w')
def writeFile(index, letter):
	outputFile.write(unichr(index))
	outputFile.write(letter)  

#now the EOF happens when we meet a new paragraph
while True:
	c = inputFile.read(1)
	#print c,
	buf += c;

	if buf not in dictionary:
		dictionary[buf] = position;
		position += 1;
		if len(buf) == 1:
			writeFile(0, buf);
		elif len(buf) == 0:
			writeFile(0, '');
		else:
			char = buf[:-1];
			pos = dictionary[char];
			writeFile(pos, buf[-1]);
		buf = "";

	if c is None or len(c) == 0:
		break;

# for i in range(0,len(tupl),2):
#     if i == int:
#         tupl[i] = alphabet[item]
#print tupl
