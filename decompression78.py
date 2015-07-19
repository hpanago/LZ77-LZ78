import codecs

tupl = [];
lista = [];
alphabet = "ABCDEFGHIJKLMNOPQRSTWXYZabcdefgh"

outputFile = codecs.open('testText.lz78', encoding='utf-8', mode='r')

while True:
	c = outputFile.read(1)
	if c is None or len(c) == 0:
		break;

	index = ord(c)
	letter = outputFile.read(1)

	print index, letter

	if index == 0:
		lista.append(letter)
	else:
		prefix = lista[index-1]
		lista.append(prefix+letter)

string = ""
for i in lista:
    string += i;
print string