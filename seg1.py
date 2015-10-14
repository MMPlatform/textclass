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


file_names = glob('news.sohunews.*')
for file_name in file_names:
	cmd = 'iconv -f gb2312 -t utf8 -c %s > %s.utf8' %(file_name,file_name)  
	os.system(cmd)
	cmd1 = "sed 's/&//g' %s.utf8  >  %s.utf8.new " % (file_name,file_name)
	os.system(cmd1)

