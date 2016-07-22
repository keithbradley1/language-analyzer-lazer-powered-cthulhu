import unittest

from domain_identifier import *


class TestDomainIdentifier(unittest.TestCase):
  ''' Receives strings to be searched in the dictionary '''

  # @classmethod
  # def setUpClass(self):
  # self.domain = Domain_Identifier()




  # ------------------------- HEALTHCARE ----------------------------------------

  def test_message_has_match_in_healthcare(self):
    message = ['obamacare', 'hospital', 'insurance', 'healthcare']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_healthcare(), .32 )

  def test_message_has_no_match_in_healthcare(self):
    message = ['trees', 'computer']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_healthcare(), 0 ) # value grabber




  # ----------------------------- WAR -------------------------------------------

  def test_message_has_match_in_war(self):
    message = ['enemies', 'war']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_war(), .16 ) # value grabber

  def test_message_has_no_match_in_war(self):
    message = ['trees', 'computer']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_war(), 0 ) # value grabber




  # ------------------------ CLIMATE CHANGE -------------------------------------

  def test_message_has_match_in_climate_change(self):
    message = ['climate', 'greenhouse', 'aerosols', 'deforestation', 'atmosphere']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_climate_change(), .4)

  def test_message_has_no_match_in_climate_change(self):
    message = ['food', 'computer']
    domain = Domain_Identifier(message)
    self.assertEqual(domain.check_climate_change(), 0 ) # value grabber




if __name__ == '__main__':
    unittest.main()
