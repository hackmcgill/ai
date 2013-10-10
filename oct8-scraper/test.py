from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
import requests

soup = BeautifulSoup(requests.get("http://bleacherreport.com/articles/1805479-ufc-fight-night-29-what-we-learned-from-joey-beltran-vs-fabio-maldonado").text)

dat = ""
for item in (soup.find('div', {'class' : 'article-body'}).contents):
    dat = "%s%s" % (dat, item)
print dat

#class Parser(HTMLParser):