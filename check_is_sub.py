import os
import re
import glob

path = os.getcwd() 

#for file in glob.glob("*.txt"):
#    print(file)

files = os.listdir(path)
#print files
for filename in files:
	r = re.compile('.*\.mp3')
	if r.match(filename):
		match = re.search('(.*)\.mp3', filename)
		#print filename
		#print match.group(1)
		chkfilename = match.group(1)+'.en.srt'
		if os.path.exists(chkfilename) is not True:
			print match.group(1)+'.mp3'
			os.remove(match.group(1)+'.mp3')
