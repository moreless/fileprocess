import os
import re
import glob

path = os.getcwd() 

#for file in glob.glob("*.txt"):
#    print(file)

files = os.listdir(path)
#print files
for filename in files:
	r = re.compile('.*\.txt')
	if r.match(filename):
		match = re.search('(.*)\.txt', filename)
		#print filename
		#print match.group(1)
                size = os.path.getsize(filename)
		if size <100:
			print 'small txt file, removing... 'filename, size
                	os.remove(filename)
			os.remove(match.group(1)+'.mp3')
