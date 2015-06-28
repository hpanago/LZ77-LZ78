import pickle

file_input = raw_input();
dictionary = {};
dictionary2 = {};
position = 1;
buf = "";
tupl = [];
#file_input += "\EOF";
for c in file_input:
    if c is None:  
        break;
    buf += c;
    if buf not in dictionary:
        dictionary[buf] = position;
        position += 1;
        #print buf
        if len(buf) == 1:
            tupl += (0,buf);
        else:
            char = buf[:-1];
            pos = dictionary[char];
            dictionary2[pos] = char;
            tupl += (pos, buf[-1]);
        buf = "";
        
# print dictionary
# print dictionary2       
with open('out.txt', 'wb') as handle1:
    pickle.dump(tupl, handle1)

with open('out.txt', 'rb') as handle1:
    b1 = pickle.loads(handle1.read())

with open('out1.txt', 'wb') as handle:
  pickle.dump(dictionary2, handle)

with open('out1.txt', 'rb') as handle:
  b = pickle.loads(handle.read())
#print "NOW THE OUTPUT", b


#print "NOW THE TUPLE", b1
#print b1
counter = 0;
string = ""
strin1g = ""
#print b, b1
#print len(b1)/2
for i in range(0,len(b1)/2):
    if tupl[counter] == 0:
        #print "COUNTERRR TUPE:E ", tupl[counter] 
        string += tupl[counter +1]
        counter += 2;
    else:
        #print tupl[counter]
        #if i == int():
        string += b[tupl[counter]] + tupl[counter+1]
        counter +=2;
print string


for i in range(0,len(b1)/2):
    if tupl[i] == 0:
        #print "COUNTERRR TUPE:E ", tupl[counter] 
        strin1g += tupl[i+1]
        
#print strin1g

test= ""
for i in dictionary2:
    test += dictionary2[i];
    # if tupl[counter] == 0:
    #     test += tupl[counter+1]
    #     counter += 2; 
#print test