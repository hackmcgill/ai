from HTMLParser import HTMLParser
import requests
import itertools
 
 # Function will return articles from given number of pages
 # number - Number of pages to extract articles from
def getListOfArticles(number):

	listOfArticles = []
	# To keep track of the number of pages
	i = 1
	class Parser(HTMLParser):
	    
	    isInOl = False
	    
	    # Look for <ol> start tag and look for attribute "article=list" and save all the 
	    # articles	    
	    def handle_starttag(self, tag, attrs):
	    	links = []
	        if tag == "ol":
	        	# Flattens all the tuples in the list in one whole list
	            attrs = list(itertools.chain(*attrs))
	            if "articles-list" in attrs:
	                self.isInOl = True
	        
	        if self.isInOl == True :
	        	for index in range(len(attrs)):
	        		if attrs[index][0] == "href":
	        			listOfArticles.append("http://bleacherreport.com" + attrs[index][1])
	    
	    def handle_endtag(self, tag):
	        if tag == "ol":
	            self.isInOl = False
	    def handle_data(self, data):
	        if self.isInOl == True:
	            #print data
	            pass
	
	p = Parser()
	while (i != number+1):
		
		p.feed(requests.get("http://bleacherreport.com/articles?page=%d" %i).text)
		#articles.append(p.listOfArticles)
		i = i + 1
return listOfArticles
