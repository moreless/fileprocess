import os
import json
import subprocess


file = open('youtubelist.txt', 'r')
file2 = open('titlelist.txt', 'w')
result = {}
for line in file:
	#result= os.system('/usr/local/bin/you-get --json '+line)
	try:
		proc = subprocess.Popen(["/usr/local/bin/you-get --json "+line], stdout=subprocess.PIPE, shell=True)
		(out, err) = proc.communicate()
	except:
		print line, 'not retrieveable'
		continue
	#file2.write('https://www.youtube.com/watch?v='+line)
	#print out
	info = json.loads(out)
	output = line.strip() +': ' + info['title']
	print output
 	file2.write(output)
file.close()
file2.close()