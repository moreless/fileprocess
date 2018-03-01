import os
import re
import glob

path = os.getcwd() 
#print path
#for file in glob.glob("*.txt"):
#    print(file)

files = os.listdir(path)
#print files
for filename in files:
	r = re.compile('.*\.txt')
	if r.match(filename):
		match = re.search('(.*)\.txt', filename)
		with open(filename, "rt") as fin:
			with open('modify/'+match.group(1)+'.mod', "wt") as fout:
				for line in fin:
					fout.write(line.replace('&gt;', '>'))

path = path+'/modify/'
#print path
for fileName in os.listdir("./modify/"):
	print path+fileName
	os.rename(path+fileName, (path+fileName).replace(".mod", ".txt"))
