import getArticlesList as getArticlesList
import getPage as getPage
import cleanBody as cleanBody

articles = getArticlesList.getArticlesList(10)

data = []
string = ""
count = [0] * 5
# tennis
# soccer
# football
# basketball
# nil

max_per_category = 1
c = 0

print "Size of articles:", len(articles)

for arturl in articles:
    if min(count[0:4]) < max_per_category:
        c += 1
        print c, ".."
        category,content = getPage.getPage(arturl)
        if category == False and content == False:
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
file.write("\n".join(data))
