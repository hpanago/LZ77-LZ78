#lz77, authors: botsas, hpanago
import sys

file = sys.argv[1]
f = open(file, 'r')
text = f.read()
toCheck = ""
string1 = text[:8]

string2 = text[8:16]

counter = 1
posBefore = 0

while counter <= 14:
	for char in string2:
		toCheck += char
		if string1.find(toCheck) == -1:
			if len(toCheck) == 1:
				length = 0
				pos = length+1
				cut = char
			else:
				pos = posBefore
				length = len(toCheck)-1
				cut = char
			text = text[length:]
			string1 = text[pos-1:pos+7]
			string2 = text[pos+7:pos+15]
			
			break 
		else:
			pos = string1.find(toCheck)
			length = len(toCheck)-1
			cut = char
		posBefore = string1.find(toCheck)
	counter += pos
	
		
	
