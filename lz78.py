import pickle

file_input = raw_input();
dictionary = {};
dictionary2 = {};
position = 1;
buf = "";
tupl = [];
lista = [];
#now the EOF happens when we meet a new paragraph
for c in file_input:
    if c is None:  
        break;
    buf += c;
    if buf not in dictionary:
        dictionary[buf] = position;
        position += 1;
        if len(buf) == 1:
            tupl += (0,buf);
        else:
            char = buf[:-1];
            pos = dictionary[char];
            tupl += (pos, buf[-1]);
        buf = "";
outputFile = open('out.txt','wr')
for item in tupl:
  outputFile.write("%s\n" % item)

for i in  range(0,len(tupl),2):  
    if tupl[i] == 0:
        lista.append(tupl[i+1])
    else:
        prefix = lista[tupl[i]-1]
        lista.append(prefix + tupl[i+1])
string = ""
for i in lista:
    string += i;
print string

