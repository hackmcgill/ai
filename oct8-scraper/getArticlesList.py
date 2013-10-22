# By Gueorgui Savadjiev
from HTMLParser import HTMLParser
import requests
import itertools

# mp: wrapper method
def getList(numArticles):
    return getArticlesList(numArticles)
    
def getArticlesList(numArticles):

        #create a subclass and override the handler methods
        class MyHTMLParser(HTMLParser):
                isInOl = False
                htmlList = []

                def handle_starttag(self, tag, attrs):
                        if tag == "ol":
                                attrs = list(itertools.chain(*attrs))
                                if "articles-list" in attrs:
                                        self.isInOl = True

                        if self.isInOl == True:
                                attrs = list(itertools.chain(*attrs))
                                if "href" in attrs:
                                        self.htmlList.append("http://bleacherreport.com" + attrs[1])


                def handle_endtag(self, tag):
                        if tag == "ol":
                                self.isInOl = False

        #instantiate the parser and feed it some HTML
        parser = MyHTMLParser()
        numPages = 1 + int(numArticles / 30)

        for i in range(numPages):
                parser.feed(requests.get("http://bleacherreport.com/articles?page=%d" % i).text)
        
        return parser.htmlList
