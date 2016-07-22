from sentiment_lexicon import *

class Sentiment_Identifier:
  ''' Runs methods for the list of words received from the tokenizer '''
  def __init__(self, message):
    self.message = message

  def check_positive(self):
    ''' Check to see if any words in the list of words matches
        the positive section of the sentiment lexicon.

        If a matched word is found, take it's value and calculate
        the total of all words matched in the list of tuples. '''

    positive_counter = 0
    for x in self.message:
      for y in sentiment_lexicon["positive"]:
        if x == y[0]:
          positive_counter += y[1]
    return positive_counter


  def check_negative(self):
    ''' Check to see if any words in the list of words matches
        the negative change section of the sentiment lexicon.

        If a matched word is found, take it's value and calculate
        the total of all words matched in the list of tuples. '''

    negative_counter = 0
    for x in self.message:
      for y in sentiment_lexicon["negative"]:
        if x == y[0]:
          negative_counter += y[1]
    return negative_counter


  def check_neutral(self):
    ''' Check to see if any words in the list of words matches
        the neutral section of the sentiment lexicon.

        If a matched word is found, take it's value and calculate
        the total of all words matched in the list of tuples. '''

    neutral_counter = 0
    for x in self.message:
      for y in sentiment_lexicon["neutral"]:
        if x == y[0]:
          neutral_counter += y[1]
    return neutral_counter


