October 8th Web Scraper
==

On October 8th @ HackNight we built a web scraper for bleacherreport.com that pulls in 100 articles about tennis, soccer, football and basketball, cleans up the article content and then puts it into a data.txt using the same format as last week.

Next week we will link the data.txt together and use it to generate a classifier which can tell you which sport (tennis, soccer, football or basketball) an article is about.

Some possible issues to be addressed before that:
- Besides football, it seems that the other 3 sports are not that popular on bleacherreport. We may want to change the sports next week.

Setup of this dir:
- main.py is the file that brings the web scraper together and creates the data.txt.
- getArticlesList.py provides a method to download a list of articles from bleacherreport.
- getList.py provides a method to download a list of articles from bleacherreport
- ueg1990_getListOfArticles.py provides a method to download a list of articles from bleacherreport
- getPage.py provides a method to download a page and pull out the keywords (category) and content
- cleanBody.py provides a method to clean up a downloaded article (remove punc, remove whitespace, clean up the characters and html, etc)
