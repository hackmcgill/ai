from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score

''' 

	HackNight AI Group Session 2: SKLearn, Document Classification
	October 1st, 2013. HackMcGill. 

	In this HackNight we're going over the basics of document classification and 
	the python library for machine learning / learning algorithms called sklearn.

	data.txt contains around 5000 documents seperated by new lines. In every line, 
	the first value is always an integer that corresponds to the category that this
	document is for. There are 8 categories. After the integer (space delimited), the document
	begins and every word is seperated by spaces.

	The sample implementation below uses a gaussian naive bayes classifier with a bag of words
	model. No steps toward optimization have been taken, this is the task of the hacknight (make
	it better, use a better classifier, model for representing documents, etc).

	The sample implementation below works in the following way:

	1. Read in data from data.txt line by line. Clean it up and split it up by spaces
	   into a list. Populate labels (categories) list, document list and the dictionary
	   which contains all words across all documents.

	2. After the dictionary of words is created, go through the documents one by one, split them up
	   into a list of words and then generate a "vector of words" for that document using the 
	   word dictionary. Save it back into that specific document in the document list.

	3. Create the gaussian NB classifier using sklearn, fit it to the data and classify all of the
	   documents using the classifier we have. Compare it against the correct labels on the training
	   data to gauge how accurate the classifier is (using the f1-score).

	This sample implementation works off a similar concept as very (very, very) basic spam
	filters for emails. 

	For more background on the concepts used in this sample implementation, read over
	the following wikipedia pages:
	- Naive Bayes Classifier
	- Bag of Words Model
	- Bayesian Spam Filter

	Note: in this code I refer to "vectors of words" / "vectors". These
	are not actual vector objects but rather lists which "reference" words
	by index.

	For example, if we have a dictionary of:
		{"hello" : 0, "world" : 1, "hackmcgill" : 1}
	and a string:
		"hello world"
	then a vector of that string is:
		[1, 1, 0]
	because hello and world are both words in the string
	but hackmcgill is not (hence why the hackmcgill index in the
	vector is zero).

	TASK: Download the code, learn it, rip it apart and make a better classifier either sticking
	with GaussNB and improving the bag of words model (or implementing something better like looking at 
	frequencies of words or occurences of words together) or using another type of classifier 
	(like a SVM or k-nearest-neighbor) or a mix of both. Whatever goes. When you're done, check out 
	hackerrank.com (this dataset is pulled from the document classification challenge 
	(https://www.hackerrank.com/challenges/document-classification). Modify your code to work with 
	stdin and stuff, and upload it. See how you rank!


'''

# Document data stored in documents, labels (category) is stored in 
# labels list
documents = [] # list that contains a vector of words in / not in the documents
dictionary = {} # contains a list of all words. index of word = position in vector
labels = [] # holds labels for data (categories to classify)

di = 0 # stores dictionary index value

# Read in data from file data.txt
for line in open('data.txt', 'r'):
	# cur stores the current document (line) from the dataset
	# split up into a list based on spaces. index 0 will always
	# contain the label (category), the rest is the document
	cur = line.strip().split(' ')
	
	# add category label for this document to the list
	labels.append(int(cur[0]))

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
