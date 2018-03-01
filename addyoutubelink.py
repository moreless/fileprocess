file = open('list1.txt', 'r')
output = open('list11.txt', 'w')
for line in file:
	#line=line.rstrip('\n')
	line = 'https://www.youtube.com/watch?v='+line
	print line
	output.write(line)

file.close()
output.close()
