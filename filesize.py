import os
import re
import glob

path = os.getcwd() 

#for file in glob.glob("*.txt"):
#    print(file)

files = os.listdir(path)
#print files
total_size = 0
txt_total_size =0
for filename in files:
	if filename.endswith('mp3'):
		size = os.path.getsize(filename)
		total_size += size
	r = re.compile('.*\.txt')
	if r.match(filename):
		match = re.search('(.*)\.txt', filename)
		#print filename
		#print match.group(1)
		tsize = os.path.getsize(filename)
		txt_total_size +=tsize
print 'total mp3 size is', total_size, 'bits'
print 'total txt size is', txt_total_size, 'bits'

