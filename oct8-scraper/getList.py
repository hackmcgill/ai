# ANASS AL-WOHOUSH

from HTMLParser import HTMLParser
import requests
import itertools

def getList(num):
	htmlList = []
	# create a subclass and override the handler methods
	class MyHTMLParser(HTMLParser):
		isInOl = False
		def handle_starttag(self, tag, attrs):
			if tag == "ol":
				attrs = list(itertools.chain(*attrs))
				if "articles-list" in attrs:
					self.isInOl = True
			if self.isInOl:
				if tag == "a":
					htmlList.append("http://bleacherreport.com/articles" + attrs[0][1])
		def handle_endtag(self, tag):
			if tag == "ol":
				self.isInOl = False
	parser = MyHTMLParser()
	num /= 30
	num += 1
	for i in range(num):
		parser.feed(requests.get("http://bleacherreport.com/articles?page=%d" %i).text)
	return htmlList
