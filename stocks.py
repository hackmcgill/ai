#!/usr/bin/python

from twitter import *

import urllib
import csv
from string import punctuation




#def twitterSetup():
	
def twitterSearch(symbolName):
	t = Twitter(auth=OAuth('put in your twitter info here babe'))
	#hashedSymbolName = "$" + symbolName
	
	symbolQuery = t.search.tweets(q=symbolName,result_type='recent', count=100)
	#hashedSymbolQuery = t.search.tweets(q=symbolName,result_type='recent', count=100)

	with open("results.txt", "w") as symbolNameFile:

		for b in symbolQuery['statuses']:
			for c in b['entities']['urls']:
				x = b['text']
				y = x.encode('ascii', 'ignore')
				symbolNameFile.write(y)
				symbolNameFile.write('\n')
		symbolNameFile.close()
				

	#print hashedSymbolQuery
	# loop through each of returned tweets, and print its content
	#	for b in hashedSymbolQuery['statuses']:
	#		for c in b['entities']['urls']:
	#			x = b['text']
	#			y = x.encode('ascii', 'ignore')
	#s			symbolNameFile.write(y)
	#			symbolNameFile.write('\n')
	#	symbolNameFile.close()

def resultParser():
	files=['negative.txt','positive.txt','results.txt']

	tweets = open("results.txt").read()
	tweets_list = tweets.split('\n')

	pos_sent = open("positive.txt").read()
	positive_words=pos_sent.split('\n')
	positive_counts=[]

	neg_sent = open('negative.txt').read()
	negative_words=neg_sent.split('\n')
	negative_counts=[]


	for tweet in tweets_list:
	    positive_counter=0
	    negative_counter=0
	    
	    tweet_processed=tweet.lower()
	    
	    
	    for p in list(punctuation):
	        tweet_processed=tweet_processed.replace(p,'')

	    words=tweet_processed.split(' ')
	    word_count=len(words)
	    for word in words:
	        if word in positive_words:
	            positive_counter=positive_counter+1
	        elif word in negative_words:
	            negative_counter=negative_counter+1
	        
	    positive_counts.append(positive_counter/word_count)
	    negative_counts.append(negative_counter/word_count)

	print len(positive_counts)

	output=zip(tweets_list,positive_counts,negative_counts)

	writer = csv.writer(open('tweet_sentiment.csv', 'wb'))
	writer.writerows(output)





if __name__ == '__main__':
	symbol = raw_input('Enter company symbol: ')
	twitterSearch(symbol)
	resultParser()