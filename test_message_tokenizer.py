import unittest
from message_tokenizer import *


class TestMessageTokenizer(unittest.TestCase):
  ''' Receives a twitter message as a string to be tokenized below '''

  @classmethod
  def setUpClass(self):
    ''' Sets up an instance of message() '''
    self.tokenizer = Tokenizer()

  def test_(self):
    ''' Our doc string '''
    pass

  def test_that_message_passed_in_is_a_string(self):
    self.assertEqual(str('This is my message!'), tokenizer.message())

  def test_message_is_lowercase(self):
    self.assertEqual(tokenizer.lowercase(), "this is my message!")

# -----------------Alphanumeric Character Set Functions----------------------
  def test_that_message_passed_in_is_a_string(self):
    self.assertTrue(tokenizer.message(), str)

  def test_all_characters_are_alphanumeric(self):
    self.assertEqual({"t", "h", "i", "s", "m", "y", "e", "a", "g"}, tokenizer.alphanumeric())

  def test_alphanumeric_characters_are_a_set(self):
    self.assertTrue(tokenizer.alphanumeric(), set)

# -----------------Word Count----------------------
  def test_split_message_is_a_list_of_words(self):
    self.assertTrue(tokenizer.message_word_list(), list)

  def test_punctuation_is_removed(self):
    self.assertEqual('This is my message', tokenizer.no_punctuation())

  def test_that_word_count_returns_integer(self):
    self.assertEqual(4, tokenzier.word_count())

# -----------------Word Position----------------------
  def test_split_message_is_a_list_of_words(self):
    self.assertTrue(tokenizer.split_message(), list)

  def test_message_order_is_unchanged(self):
    self.assertTrue(['This', 'is', 'my', 'message'], tokenizer.word_position())

  def test_message_list_length_is_integer(self):
    self.assertTrue(int, tokenizer.message_length())

# -----------------Sentence Count----------------------

  def test_message_contains_punctuation(self):
    self.assertTrue("!", tokenizer.punctuation)

  def test_sentence_count_is_an_integer(self):
    self.assertTrue(1, tokenizer.sentence_count)

  # def test_message_list_contains_only_strings(self):
  #   ''' Tests that nothing besides a string is in the list'''
  #   self.assertTrue(['This', 'is', 'my', 'message'], )

  # def test_each_message_string_contains_punctuation(self):
  #   ''' Checks to see if there is a punctuation at the end of each sentence '''
  #

# -----------------Punctuation----------------------
  def test_message_contains_punctuation(self):
    assertEqual("!", tokenizer.punctuation())
    pass

  # def test_punctuation_list_is_a_list(self):
  #   pass

  # def test_punctuation_list_contains_punctuation(self):
  #   pass

  # def test_no_punctuation_list_contains_no_punctuation(self):
  #   pass

if __name__ == '__main__':
    unittest.main()

# Alphanumeric Characters
# Word count
# Word position
# Sentence count
# Punctuation
