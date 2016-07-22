import unittest

from sentiment_identifier import *

class TestSentimentIdentifier(unittest.TestCase):
  ''' Receives strings to be searched in the dictionary '''

  # @classmethod
  # def setUpClass(self):
  #   self.sentiment = Sentiment_Identifier()



  # ------------------------- Positive ----------------------------------------

  def test_message_has_match_in_positive(self):
    message = ['totally', 'good', 'smart']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_positive(), 1.5 )

  def test_message_has_no_match_in_positive(self):
    message = ['trees', 'computer']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_positive(), 0 ) # value grabber



  # ------------------------ Negative -------------------------------------

  def test_message_has_match_in_negative(self):
    message = ['divided', 'not', 'tough']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_negative(), 1.5 )

  def test_message_has_no_match_in_negative(self):
    message = ['food', 'computer']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_negative(), 0 ) # value grabber



  # ----------------------------- Neutral -------------------------------------------

  def test_message_has_match_in_neutral(self):
    message = ['country', 'watching', 'looking']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_neutral(), 1.5 ) # value grabber

  def test_message_has_no_match_in_neutral(self):
    message = ['trees', 'computer']
    sentiment = Sentiment_Identifier(message)
    self.assertEqual(sentiment.check_neutral(), 0 ) # value grabber



if __name__ == '__main__':
    unittest.main()
