# Author: Mike Noseworthy
# Given a string containing the body of an article, clean body will
# return a string in all lowercase with all the html tags and punctuation
# removed.

from HTMLParser import HTMLParser
import string

htmlBodyTest = "Witten was targeted 23 times last year in Dallas' two contests with the Redskins, and should remain a high-volume target against Washington this time around as well.  Witten has been targeted 10 times apiece in each of the last two games for the Cowboys this season as well.<br>The Redskins will pay loads of attention to Dez Bryant on the outside, which should once again leave Witten as Tony Romo's safety valve in the middle of the field.  Witten broke the 100-yard receiving mark for the first time in 2013 last week, while also scoring a touchdown.  He remains one of the better fantasy options at tight end."

class MyHTMLParser(HTMLParser):
	paragraphs = ""
	def handle_data(self, data):
		self.paragraphs = self.paragraphs + data
	def getParagraphs(self):
		return self.paragraphs

# Main function called with the body of the article.
def cleanBody(body):
	text = removeTags(body)
	text = removePunctuation(text)
	text = removeNumbers(text)
	text = text.replace("  ", " ")
	return text.lower()	

# Given a string, return the string without any numbers
def removeNumbers(text):
	words = text.split(" ")
	for i in range(0, len(words)):
		if words[i].isdigit():
			words[i] = ""
	return string.join(words)
# Given a string, returns the string without any html tags.
def removeTags(text):
	parser = MyHTMLParser()
	parser.feed(text)
	return parser.getParagraphs()

# Given a string, returns the string without any punctuation.
def removePunctuation(text):
	words = text.split(" ")
	for i in range(0,len(words)):
		for punc in string.punctuation:
			if punc == "'":
				words[i] = words[i].replace(punc, "").strip()
			else:
				words[i] = words[i].replace(punc, " ").strip()
	return string.join(words)
