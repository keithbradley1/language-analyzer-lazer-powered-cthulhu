class Tokenizer():
  def __init__(self, message):
    self.message = message
    pass

  def lowercase(self):
    lowercase_message = self.message.lower()
    return lowercase_message

  def alphanumeric(self):
    ''' Takes in the message and turns it to lowercase. Then it splits
    the message into list of characters. Finally it loops through the list
    of strings and adds each alphanumeric character to a set'''
    alphanumeric_set = set()
    lowercase_character_list = list(self.message.lower())
    for toke in lowercase_character_list:
      if toke.isalnum():
        alphanumeric_set.add(toke)

    return alphanumeric_set

  def split_message(self):
    message_without_spaces = list()
    split_message = self.message.split(" ")
    for word in split_message:
      message_without_spaces.extend(word)

    return message_without_spaces

  def no_punctuation(self):
    pass

#   '''splits on spaces'''
#
#   word_count(): #start here
#   word_position():
#   message_length()
#   sentence_count
#     split sentence on punctuation
#   punctuation
#
#   lowercase

# "This is my message!"
