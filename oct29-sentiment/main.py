from sklearn.naive_bayes import GaussianNB

# Contains "positive" words
positive = [(line.strip(), 1) for line in open('positive_words.txt', 'r')]

# Contains "negative" words
negative = [(line.strip(), -1) for line in open('negative_words.txt', 'r')]

# Create the dictionary of positive and negative words
dictionary = positive + negative

# more soon..
