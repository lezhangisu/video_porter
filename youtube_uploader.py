#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from os import listdir
from os.path import isfile, join
import sys
import os
reload(sys)  
sys.setdefaultencoding('utf-8')


mypath = sys.argv[1]

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

cnt=0
for file in onlyfiles:
	filename = mypath+file.encode('utf-8')
	if os.path.getsize(filename) > 50000000:
		print filename+' '+ str(os.path.getsize(filename))
		os.system('youtube-upload --title="'+file.encode('utf-8')+'" --playlist "王者荣耀张大仙是神仙" '+filename.encode('utf-8'))
		cnt+=1
print 'Total files: '+str(cnt)

