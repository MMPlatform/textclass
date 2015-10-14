# -*- coding: utf-8 -*-
#!/usr/bin/env python

import web
from bs4 import BeautifulSoup
import urllib2
from tgrocery import Grocery


urls = (
	'/(.*)', 'index'
)

class index:
	def GET(self,name):
		#i = web.input(name=None)	
		#url = "http://"+name
		#html = urllib2.urlopen(url).read()
		#soup = BeautifulSoup(html)
		#title =  soup.html.head.title.contents.pop().encode('utf-8')
		title = name.encode('utf-8')
		new_grocery = Grocery('sample')
		new_grocery.load()
		return new_grocery.predict(title)
	

if __name__ == "__main__":
	#grocery.train('train.txt')
	grocery = Grocery('sample')
	train_src = [('education', '名师指导托福语法技巧：名词的复数形式'),('education', '中国高考成绩海外认可 是“狼来了”吗？'),('sports', '图文：法网孟菲尔斯苦战进16强 孟菲尔斯怒吼'),('sports', '四川丹棱举行全国长距登山挑战赛 近万人参与')]
	grocery.train('train.txt')
	#grocery.train(train_src)	
	grocery.save()
	app = web.application(urls, locals())
	app.run()

