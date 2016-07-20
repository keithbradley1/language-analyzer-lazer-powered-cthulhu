# for x in message:
#   assertEqual(True, isinstance(x, message))

# def check_healthcare(self):
# find a match
# grab values

import domain_lexicon

class Domain_Identifier:
  ''' Runs methods for the list of words recieved from the tokenizer '''

  def check_healthcare(self, message):
    ''' Check to see if any words in the list of words matches
        the healthcare section of the domain lexicon.

        If a matched word is found, take it's value and calcualte
        the total of all words matched in the list of tuples. '''
    for x in message:

      for y in domain_lexicon.healthcare:

        y[0]

    pass

  def check_war(self, message):
    pass

  def check_climate_change(self, message):
    pass


