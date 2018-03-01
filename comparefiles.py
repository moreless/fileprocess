file2 = open('list2.txt', 'r')


with open('list11.txt') as file1:
    lines1 = file1.read().splitlines() 
output_file = open('outputlist.txt', 'w')
print lines1
lines2 = file2.readlines()

for line in lines2:
	#print line
	if line.strip() not in lines1:
		print line.strip()
		output_file.write(line)

file1.close()
file2.close()
output_file.close()