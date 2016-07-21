
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
    lowercase_character_list = list(self.message)
    for toke in lowercase_character_list:
      if toke.isalnum():
        alphanumeric_set.add(toke)

    return alphanumeric_set

  def split_message(self):
    # message_without_spaces = list()
    split_message = self.message.split(" ")
    # for word in split_message:
    #   message_without_spaces.extend(word)

    return split_message



  # def no_punctuation(self):
  #   ''' Takes the message as a string and returns the stringed messaged
  #   without punctuation '''

  def stripped_message(self):
    split_sentence = self.split_message()
    plain_message_list = list()

    for word in split_sentence:
      plain_message_list.append(word.rstrip(string.punctuation))

    return plain_message_list


# fish = Tokenizer("This is my message!")
# gum = fish.stripped_message()
#
# print(gum)
#   '''splits on spaces'''
#
#   word_position():
#   message_length()
#   sentence_count
#     split sentence on punctuation
#   punctuation
#
#   lowercase

# "This is my message!"
