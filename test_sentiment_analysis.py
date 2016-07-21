import unittest

from sentiment_identifier import *

class TestSentimentIdentifier(unittest.TestCase):
  ''' Receives strings to be searched in the dictionary '''

  @classmethod
  def setUpClass(self):
    self.sentiment = Sentiment_Identifier()



  # ------------------------- Positive ----------------------------------------

  def test_message_has_match_in_positive(self):
    message = ['totally', 'good', 'smart']
    self.assertEqual(self.sentiment.check_positive(message), 1.5 )

  def test_message_has_no_match_in_positive(self):
    message = ['trees', 'computer']
    self.assertEqual(self.sentiment.check_positive(message), 0 ) # value grabber



  # ------------------------ Negative -------------------------------------

  def test_message_has_match_in_negative(self):
    message = ['divided', 'not', 'tough']
    self.assertEqual(self.sentiment.check_negative(message), 1.5 )

  def test_message_has_no_match_in_negative(self):
    message = ['food', 'computer']
    self.assertEqual(self.sentiment.check_negative(message), 0 ) # value grabber



  # ----------------------------- Neutral -------------------------------------------

  def test_message_has_match_in_neutral(self):
    message = ['country', 'watching', 'looking']
    self.assertEqual(self.sentiment.check_neutral(message), 1.5 ) # value grabber

  def test_message_has_no_match_in_neutral(self):
    message = ['trees', 'computer']
    self.assertEqual(self.sentiment.check_neutral(message), 0 ) # value grabber



if __name__ == '__main__':
    unittest.main()
