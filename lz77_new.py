def lz77step(prev, data):
	for index in range(0, len(prev)):
		for size in range(len(prev)-index, 0, -1):
			if prev[index: index+size] == data[0: size]:
				if size == len(data):
					return (index, size, 'EOF') 
	
				return (index, size, data[size])

print lz77step("hello", "hello world")