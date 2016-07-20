import unittest
from domain_identifier import *

class TestDomainIdentifier(unittest.TestCase):
  ''' Receives strings to be searched in the dictionary '''

  @classmethod
  def setUpClass(self):
    self.domain = Domain_Identifier()
    pass



  # ------------------------- HEALTHCARE ----------------------------------------

  def test_message_has_match_in_healthcare(self):
    message = ['obamacare', 'hospital', 'insurance', 'healthcare']
    self.assertEqual(self.domain.check_healthcare(message), .32 )

  def test_message_has_no_match_in_healthcare(self):
    message = ['trees', 'computer']
    self.assertEqual(self.domain.check_healthcare(message), 0 ) # value grabber




  # ----------------------------- WAR -------------------------------------------

  def test_message_has_match_in_war(self):
    message = ['enemies', 'war']
    self.assertEqual(self.domain.check_war(message), .16 ) # value grabber

  def test_message_has_no_match_in_war(self):
    message = ['trees', 'computer']
    self.assertEqual(self.domain.check_war(message), 0 ) # value grabber




  # ------------------------ CLIMATE CHANGE -------------------------------------

  def test_message_has_match_in_climate_change(self):
    message = ['climate', 'greenhouse', 'aerosols', 'deforestation', 'atmosphere']
    self.assertEqual(self.domain.check_climate_change(message), .4)

  def test_message_has_no_match_in_climate_change(self):
    message = ['food', 'computer']
    self.assertEqual(self.domain.check_climate_change(message), 0 ) # value grabber




if __name__ == '__main__':
    unittest.main()
