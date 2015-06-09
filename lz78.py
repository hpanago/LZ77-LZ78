file_input = raw_input();
dictionary = {};
position = 1;
buf = "";
file_input += "\EOF";
for c in file_input:
    buf += c;
    if buf not in dictionary:
        dictionary[buf] = position;
        position += 1;
        if len(buf) == 1:
            tupl = (0,buf);
        else:
            char = buf[:-1];
            pos = dictionary[char];
            tupl = (pos, buf[-1]);
        buf = "";
        print tupl;
print dictionary;
