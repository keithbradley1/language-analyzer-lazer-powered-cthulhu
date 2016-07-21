from domain_lexicon import *


class Domain_Identifier:
  ''' Runs methods for the list of words recieved from the tokenizer '''

  def check_healthcare(self, message):
    ''' Check to see if any words in the list of words matches
        the healthcare section of the domain lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    health_counter = 0
    for x in message:
      for y in domain_lexicon["healthcare"]:
        if x == y[0]:
          health_counter += y[1]
    return health_counter



  def check_war(self, message):
    ''' Check to see if any words in the list of words matches
        the war section of the domain lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    war_counter = 0
    for x in message:
      for y in domain_lexicon["war"]:
        if x == y[0]:
          war_counter += y[1]
    return war_counter



  def check_climate_change(self, message):
    ''' Check to see if any words in the list of words matches
        the climate change section of the domain lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''

    climate_change_counter = 0
    for x in message:
      for y in domain_lexicon["climate change"]:
        if x == y[0]:
          climate_change_counter += y[1]
    return climate_change_counter
