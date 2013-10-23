# Number of articles to get 
num_articles = 5000

# Uncomment the getList method you want to use
#import getArticlesList as getList
import getList as getList
#import ueg1990_getListOfArticles as getList

# Import the getPage method
import getPage as getPage

# Import the cleanBody method
import cleanBody as cleanBody

articles = getList.getList(num_articles)

data = []
count = [0] * 5 # create list of 5 zeros 
# tennis (0)
# soccer (1)
# football (2)
# basketball (3)
# nil (4)

max_per_category = 100
c = 0

print "Size of articles:", len(articles)

# for each article in articles
for arturl in articles:
    # if all categories have more than max_per_category then
    # quit looping. nil category excluded
    print count[2:4]
    if min(count[2:4]) < max_per_category:
        c += 1
        print c, "..", arturl
        category,content = getPage.getPage(arturl)
        if category == False and content == False:  # no content on this page? add it to the nil category
            count[4] += 1
        else:
            if count[category - 1] < max_per_category:
                count[category - 1] += 1
                data.append( "%d %s" % (category,cleanBody.cleanBody(content)) )
    else:
        break

print data        
print count

file = open("data.txt", "w")
file.write("\n".join(data).encode('utf-8'))