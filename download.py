#!/usr/local/bin/python
# coding: utf-8

import os
import sys, time

sys.path.append('/usr/bin/')
#print sys.path

filename ='youtubelist2.txt'
str= (time.strftime('%m_%d_%Y-%H:%M:%S'))
out_filename = 'output-'+str+'.log'


file = open(filename, 'r')
for line in file:
	#line = line.rstrip('\n')
	str= (time.strftime('%H:%M:%S %m/%d/%Y'))
	output = str + " Get: " + line
	print output
	outfile = open(out_filename, 'a')
	outfile.write(output)
        outfile.close()
	#url = 'https://www.youtube.com/watch?v=sSy56Q7lcVo'
	#os.system("/usr/local/bin/youtube-dl -x --audio-format 'mp3' -f 'bestaudio[ext!=webm]/best[ext!=webm]' --write-sub --convert-subs 'srt' --verbose "+line)
	os.system("youtube-dl -x --audio-format 'mp3' -f 'bestaudio[ext!=webm]/best[ext!=webm]'  --write-auto-sub --write-sub --convert-subs 'srt' "+line)

file.close()
