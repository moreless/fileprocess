import os
import re
import glob

path = os.getcwd()

#for file in glob.glob("*.txt"):
#    print(file)
output = open('filelist.txt', 'w')
files = os.listdir(path)
#print files
for filename in files:
	r = re.compile('.*\.mp3')
	if r.match(filename):
		match = re.search('(.*)\.mp3', filename)
		video_url = 'https://www.youtube.com/watch?v='+ match.group(1)[-11:]+'\n'
		print match.group(1)[-11:]
		output.write(video_url)
		#chkfilename = match.group(1)+'.mp3'
output.close()
