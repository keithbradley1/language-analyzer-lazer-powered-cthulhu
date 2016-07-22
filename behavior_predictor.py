from behavior_predictor_lexicon import *

class Behavior_Predictor:
  ''' Runs methods for the list of words recieved from the tokenizer '''
  def __init__(self, message):
    self.message = message

  def check_dictator(self, message):
    ''' Check to see if any words in the list of words matches
        the dictator section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples.

        get the number of matches
        average the matches and the values'''

    dictator_counter = 0
    # matches = 2 (number of values >0)
    for x in self.message:
      for y in behavior_predictor_lexicon["dictator"]:
        if x == y[0]:
          dictator_counter += y[1]

          # dictator_counter = (dictator_counter) / (matches)

    return dictator_counter

  def check_hippie(self, message):
    ''' Check to see if any words in the list of words matches
        the hippie section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    hippie_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["hippie"]:
        if x == y[0]:
          hippie_counter += y[1]
    return hippie_counter


  def check_blame(self, message):
    ''' Check to see if any words in the list of words matches
        the blame section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    blame_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["blame"]:
        if x == y[0]:
          blame_counter += y[1]
    return blame_counter


  def check_inspiring(self, message):
    ''' Check to see if any words in the list of words matches
        the inspiring section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    inspiring_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["inspiring"]:
        if x == y[0]:
          inspiring_counter += y[1]
    return inspiring_counter



  def check_hate(self, message):
    ''' Check to see if any words in the list of words matches
        the hate section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    hate_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["hate"]:
        if x == y[0]:
          hate_counter += y[1]
    return hate_counter



  def check_childish(self, message):
    ''' Check to see if any words in the list of words matches
        the childish section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    childish_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["childish"]:
        if x == y[0]:
          childish_counter += y[1]
    return childish_counter


  def check_mockery(self, message):
    ''' Check to see if any words in the list of words matches
        the mockery section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    mockery_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["mockery"]:
        if x == y[0]:
          mockery_counter += y[1]
    return mockery_counter



  def check_pandering(self, message):
    ''' Check to see if any words in the list of words matches
        the pandering section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    pandering_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["pandering"]:
        if x == y[0]:
          pandering_counter += y[1]
    return pandering_counter



  def check_supportive(self, message):
    ''' Check to see if any words in the list of words matches
        the supportive section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    supportive_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["supportive"]:
        if x == y[0]:
          supportive_counter += y[1]
    return supportive_counter



  def check_promises(self, message):
    ''' Check to see if any words in the list of words matches
        the promises section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    promises_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["promises"]:
        if x == y[0]:
          promises_counter += y[1]
    return promises_counter



  def check_patriotic(self, message):
    ''' Check to see if any words in the list of words matches
        the patriotic section of the behavior predictor lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    patriotic_counter = 0
    for x in self.message:
      for y in behavior_predictor_lexicon["patriotic"]:
        if x == y[0]:
          patriotic_counter += y[1]
    return patriotic_counter


