from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
import cleanBody as cleanBody

''' 

	HackNight AI : Week 4
	
	We modified main.py from week 2 to use the scraper we built last
	week in order to classify articles as football or basketball.
	
	To test classification, put (one) testing article into test.txt, it'll
	print out the category for classification.


'''

# Document data stored in documents, labels (category) is stored in 
# labels list
documents = [] # list that contains a vector of words in / not in the documents
dictionary = {} # contains a list of all words. index of word = position in vector
labels = [] # holds labels for data (categories to classif
di = 0 # stores dictionary index value

count2 = {'1': 0, '2' : 0, '3' : 0, '4' : 0}
categories = ['0', 'tennis', 'soccer', 'football', 'basketball']

# Read in data from file data.txt
for line in open('data.txt', 'r'):
	# cur stores the current document (line) from the dataset
	# split up into a list based on spaces. index 0 will always
	# contain the label (category), the rest is the document
	cur = line.strip().split(' ')
	
	# add category label for this document to the list
	labels.append(int(cur[0]))

	count2["%d" % int(cur[0])] += 1

	# add the entire document to the documents list 
	documents.append(" ".join(cur[1:]))
		
	# for every word in this document, check if it's been added to our dictionary yet
	for word in cur[1:]:
		# if the word isn't already in our dictionary and it's actually a word
		# (i.e. not mistakenly a null character), add it
		if word not in dictionary and len(word) > 0:
			dictionary[word] = di # add the word to the dictionary and 
								  # set its value to the index in the bag of
								  # words vector
			di += 1 # increment dictionary index value for the next word 
					# we add

# Bag of words model, create a vector of words for every document in the documents
# list using the dictionary we created in the loop above
for i in range(0, len(documents)):
	vector = [0] * len(dictionary)

	# iterate through all words in this document split by space and create the vector of words
	for word in documents[i].strip().split(' '): 
		if len(word) > 0:	# if this is a word (i.e. not a null character), we add it to the vector
			vector[ dictionary[word] ] = 1	# the word is in this document, so we set it to 1. For the
											# index, we pull it from the word dictionary we created above
	
	# update the current document we're processing with the new vector of words contained in that document
	documents[i] = vector

# Create Gaussian NB classifier and fit it to the data
gnb = GaussianNB()	# create the classifier object
gnbfit = gnb.fit(documents, labels)	# fit (/train) the classifier to the data

pred = gnbfit.predict(documents) # classify the documents again using the classifier to test
								 # for accuracy

print len(dictionary),"words in the word dictionary"
print len(documents),"data points in the training set"
print "f1-score (weighted) of classifier on training set is:", f1_score(labels, pred, average='weighted')

f = open('test.txt', 'r')
test = cleanBody.cleanBody(f.readline())

vector = [0] * len(dictionary)
for word in test.strip().split(' '):
	if len(word) > 0 and word in dictionary:
		vector[ dictionary[word] ] = 1

prediction = gnbfit.predict(vector)
print "Predicted as category: %s (id:%d)" % (categories[prediction], prediction)
