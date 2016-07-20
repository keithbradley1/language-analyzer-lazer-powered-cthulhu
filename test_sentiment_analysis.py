import unittest
from language_analyzer import *

########################## Sentiment Analysis Test ################################

class sentiment_analysis(unittest.TestCase):
	'''get key value pairs from the lexicon
	each value should have True or False
	giving it a value'''

######################## Test for Positive #######################################


class TestPositive():

	def test_for_matches(self):
		'''Test that keywords match'''

	def test_that_it_stores_matches_in_dict(self):
		'''Tests that matches are stored in a dict'''

######################## Test for Negative #######################################


class TestNegative():

	def test_for_matches(self):
		'''Test that keywords match'''

	def test_that_it_stores_matches_in_dict(self):
		'''Tests that matches are stored in a dict'''

######################## Test for Neutral #######################################

class TestNeutral():

	def test_for_matches(self):
	'''Test that keywords match'''

	def test_that_it_stores_matches_in_dict(self):
	'''Tests that matches are stored in a dict'''




############ ignore this test thingie just for showing the group ##################

#my idea for getting values for things. using the lexicon1

sampleSentenceSplitUpIntoIndividualKeys = {'I', 'enjoy', 'and', 'love', 'waffles'}
sentimentLexiconThingie = {'love': .05, 'joy': .05, 'enjoy': .05, 'smile': .05, }

for key in sentimentLexiconThingie():
	if key in sampleSentenceSplitUpIntoIndividualKeys():
		print(sentimentLexiconThingie[key])

#this could also potentially be stated as this below

for key in sentimentLexiconThingie:
	if key in sampleSentenceSplitUpIntoIndividualKeys:
		print(sentimentLexiconThingie[key])

'''prints: or gives us. we can also instead of printing the values
we could just store it into a new list
[.05, .05]
We then add those values
that gives us the sentiment value total. which here would be .1

then definitely print the total sentiment value
'''