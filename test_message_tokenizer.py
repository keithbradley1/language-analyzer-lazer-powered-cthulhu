import unittest
from message_tokenizer import *


class TestMessageTokenizer(unittest.TestCase):
  ''' Receives a twitter message as a string to be tokenized below '''

  @classmethod
  def setUpClass(self):
    ''' Sets up an instance of message() '''
    self.tokenizer = Tokenizer('This is my message!')

  def test_(self):
    ''' Our doc string '''
    pass

  def test_that_message_passed_in_is_a_string(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertEqual(str('This is my message!'), tokenizer.message)

  def test_message_is_lowercase(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertEqual(tokenizer.lowercase(), "this is my message!")

# -----------------Alphanumeric Character Set Functions----------------------

  def test_all_characters_are_alphanumeric(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertEqual({'y', 'T', 's', 'm', 'i', 'h', 'e', 'g', 'a'}, tokenizer.alphanumeric())

  def test_alphanumeric_characters_are_a_set(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertTrue(tokenizer.alphanumeric(), set)

# -----------------Word Count----------------------
  def test_split_message_is_a_list_of_words_with_spaces_removed(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertTrue(tokenizer.split_message(), ['This', 'is', 'my', 'message', '!'])

  def test_that_word_count_returns_integer(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertEqual(4, tokenizer.word_count())

# -----------------Word Position----------------------

  def test_message_is_list_of_tuples_with_index_and_the_word(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertTrue([(0, 'this'), (1, 'is'), (2, 'my'), (3, 'message')], tokenizer.word_position())

# -----------------Sentence Count----------------------

  def test_message_contains_punctuation(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertTrue("!", tokenizer.punctuation())

  def test_sentence_count_is_an_integer(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertTrue(1, tokenizer.sentence_count())

# -----------------Punctuation----------------------

  def test_stripped_message_is_list_of_strings_with_no_punctuation(self):
    tokenizer = Tokenizer('This is my message!')
    self.assertEqual(['This', 'is', 'my', 'message'], tokenizer.stripped_message())

if __name__ == '__main__':
    unittest.main()
