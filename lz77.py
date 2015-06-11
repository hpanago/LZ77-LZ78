#lz77, authors: potsas, hpanago
#pickles kai tuples pantou <:
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
	print counter
	for char in string2:
		print string1
		print string2
		toCheck += char
		if string1.find(toCheck) == -1:
			print "inside if == -1"
			if len(toCheck) == 1:
				length = 0
				pos = length+1
				cut = char
				print pos,length,cut
			else:
				print "i am inside else for legth>1 to check"
				pos = posBefore
				length = len(toCheck)-1
				cut = char
				print pos,length,cut
				print "STRIIIIINGS"
			text = text[length:]
			string1 = text[pos-1:pos+7]
			string2 = text[pos+7:pos+15]
			print "nNEW ONES????"
			
			break 
		else:
			print "inside big else where we find stuff"
			pos = string1.find(toCheck)
			length = len(toCheck)-1
			cut = char
			print pos,length,cut
		posBefore = string1.find(toCheck)
	counter += pos
	
		
	
