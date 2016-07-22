
import string
import re



class Tokenizer():
  '''  '''
  def __init__(self, message):
    self.message = message

  def lowercase(self):
    ''' Takes a string, makes all characters lowercased, and then returns
    the lowercased string '''
    lowercase_message = self.message.lower()
    return lowercase_message

  def alphanumeric(self):
    ''' Takes in the message and turns it to lowercase. Then it splits
    the message into list of characters. Finally it loops through the list
    of strings and adds each alphanumeric character to a set'''
    alphanumeric_set = set()
    lowercase_character_list = list(self.message)

    for toke in lowercase_character_list:
      if toke.isalnum():
        alphanumeric_set.add(toke)
    return alphanumeric_set

  def split_message(self):
    ''' Splits the sentence up into words on spaces '''
    split_message = self.message.split(" ")
    return split_message

  def stripped_message(self):
    ''' Takes the message, runs the split_message function, and then
    removes all punctuation '''
    split_sentence = self.split_message()
    plain_message_list = list()

    for word in split_sentence:
      plain_message_list.append(word.rstrip(string.punctuation))
    return plain_message_list

  def word_count(self):
    ''' Takes the stripped_message and counts the length of the list '''
    message = self.stripped_message()
    word_count = len(message)
    return word_count

  def word_position(self):
    ''' Returns each word in the message with its index in the message '''
    message = self.stripped_message()
    word_position = list(enumerate(message))
    return word_position

  def sentence_count(self):
    ''' Splits the message on period, exclamation point, and question mark.
    Then gives the sentence count as an integer '''
    split_message = re.split("[.!?]+", self.message)
    return len(split_message)

  def punctuation(self):
    ''' Returns a list of all punctuation contained in the message '''
    punctuation_list = list()

    for character in self.message:
      if character in string.punctuation:
        punctuation_list.append(character)

    return punctuation_list
