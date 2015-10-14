#!/usr/bin/env python
#encoding=utf-8



from glob import glob
import re
from lxml import etree 
import os, sys
import io


def cur_file_dir():
        path = sys.path[0]
        if os.path.isdir(path):
                return path
        elif os.path.isfile(path):
                return os.path.dirname(path)



trainfile= cur_file_dir()  + os.sep + 'train.txt' 
tfile = io.open(trainfile,'w', encoding='utf8')


try:
	file_names = glob('news.sohunews.*.txt.utf8.new')
	for file_name in file_names:
		tree = etree.parse(file_name)  
		root = tree.getroot() 
		for article in root:
			for field in article:
				if field.tag=="contenttitle": 
					if field.text:
						fieldtext = field.text.strip().replace('"',"").replace("'","").replace("\n","").replace("\r","").replace(" ","").replace("\t","")
				if field.tag=="url":
					if field.text: 
						titleurl = field.text
						m = re.match(r'http://(\w+)\.(.+)',titleurl)
						title = m.group(1).replace("try","woman")
			tfile.write(title+'\t'+fieldtext+'\n')

finally:   
	tfile.close()
