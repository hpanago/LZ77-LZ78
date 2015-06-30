tupl = [];
lista = [];
alphabet = "ABCDEFGHIJKLMNOPQRSTWXYZabcdefgh"

outputFile = open('out.txt','rb')
for item in outputFile:
 	tupl.append(item.rstrip('\n'))
for i in  range(0,len(tupl),2):  
    if tupl[i] == '0':
        lista.append(tupl[i+1])
    else:
        prefix = lista[int(tupl[i])-1]
        lista.append(prefix + tupl[i+1])
string = ""
for i in lista:
    string += i;
print string