# Erle and Charles

from BeautifulSoup import BeautifulSoup
# Beautiful Soup might be called bs4, try that if this doesn't work.
from urllib2 import urlopen

def make_soup(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html)
	return soup
	
def getPage(url):
    soup = make_soup(url)
    content = soup.find('div', {'class' : 'article-body'})
    
    if content == None:
        return False, False
        
    # mp: Part added in to get the html without removed whitespace (was having issues with this before
    # for some reason)
    dat = ""
    for item in content.contents:
        dat = "%s%s" % (dat, item)
    content = dat
    # end addition

    keywords = soup.find('meta', {'name': 'keywords'})['content'].lower()
    if "soccer" in keywords:
		category = 2
    elif ("football" in keywords or "nfl" in keywords) and "tennis" not in keywords and "basketball" not in keywords:
        category = 3
    elif "tennis" in keywords and "football" not in keywords and "basketball" not in keywords:
        category = 1
    elif "basketball" in keywords and "football" not in keywords and "tennis" not in keywords:
        category = 4
    else:
        return False, False
    return category, content