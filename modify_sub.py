import os
import re, shutil

path = os.getcwd() 
print  os.path.exists(path + '/output') 

if os.path.exists(path + '/output') :
	shutil.rmtree('output')
        print 'output deleted'

os.system('mkdir -p output/modify')
files = os.listdir(path)
#print files
for filename in files:
	r = re.compile('.*\.en\.srt')
	if r.match(filename):
		match = re.search('(.*)\.en\.srt', filename)
		output_filename = match.group(1)+'.txt'
		#print output_filename
		#print filename

		file = open(filename.rstrip(), "r")
		lines = file.readlines()

		if len(lines) <10:
			print 'Caption file is too small, deleting', filename
			os.remove(filename)
			os.remove(match.group(1)+'.mp3')
			continue
		output_file = open ('output/'+output_filename, 'w')


		i =0
		first = 0
		second = 0
		type_1 = False
		type_2 = False
		type_3 = False


		while i<10:
			r = re.compile('.*:.*:.*,')
			if r.match(lines[i]) :
				if first == 0:
					first = i
					#print first
				else:
					second  = i
					#print second
					break
			i+=1

		if second - first <=4:
			type_1 = True
			#print 'type_1' #type_1 is one line subtitle
		else :
			if lines[first+2].strip() == lines[second+1].strip():
				type_2 = True
				#print 'type_2' #type_2 is more than 1 line, up scrolling subtitle

			if lines[first+2].strip() != lines[second+1].strip():
				type_3 = True
				#print 'type_3' #type_3 is more than 1 line, totally updated subtitle
		
		for i in range(5,len(lines)):
			r = re.compile('.*:.*:.*,')
			if r.match(lines[i]):
				#print lines[i]
				if type_3:
					if r.match(lines[i-4]):
						line = lines[i-3]#.rstrip()+' '
					else :
						line = lines[i-4].strip()+' '+lines[i-3]#.rstrip()+''
				else:
					if type_1 or type_2:
						line = lines[i-3]#.rstrip()+' '
				#print line
				output_file.write(line)
		#print lines[len(lines)-2].rstrip('\n')
		output_file.write(lines[len(lines)-2].rstrip('\n'))

		file.close()
		output_file.close()
