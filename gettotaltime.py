import os
import mutagen
from mutagen.mp3 import MP3


path = os.getcwd() 
total_time = 0
files = os.listdir(path)
#print files
for filename in files:
    if filename.endswith('.mp3'):
        #print path+filename
        audio = MP3(path+'/'+filename)
        total_time += audio.info.length/3600
        print audio.info.length/3600
print 'Total time is %0.2f' % total_time, 'hours'
