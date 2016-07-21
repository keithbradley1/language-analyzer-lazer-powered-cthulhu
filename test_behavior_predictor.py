import unittest
from behavior_predictor import *
#################### behavior predictor tests ####################

class TestBehavior(unittest.TestCase):
  ''' Tests that behavior predictor receives a message to be evaluated'''

  @classmethod
  def setUpClass(self):
    self.behavior = Behavior_Predictor()


#################### dictator tests ####################

  def test_message_has_match_in_dictator(self):
    message = ['commander', 'authoritarian']
    self.assertEqual(self.behavior.check_dictator(message), .16 ) # value grabber

  def test_message_has_no_match_in_dictator(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_dictator(message), 0 ) # value grabber

  #################### hippie tests ####################

  def test_message_has_match_in_hippie(self):
    message = ['freethinker', 'bohemian']
    self.assertEqual(self.behavior.check_hippie(message), .16 ) # value grabber

  def test_message_has_no_match_in_hippie(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_hippie(message), 0 ) # value grabber

  #################### blame tests ####################

  def test_message_has_match_in_blame(self):
    message = ['charge', 'censure']
    self.assertEqual(self.behavior.check_blame(message), .16 ) # value grabber

  def test_message_has_no_match_in_blame(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_blame(message), 0 ) # value grabber

  #################### inspiring tests ####################

  def test_message_has_match_in_inspiring(self):
    message = ['invigorate', 'produce']
    self.assertEqual(self.behavior.check_inspiring(message), .16 ) # value grabber

  def test_message_has_no_match_in_inspiring(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_inspiring(message), 0 ) # value grabber

  #################### hate tests ####################

  def test_message_has_match_in_hate(self):
    message = ['antagonism', 'grievance']
    self.assertEqual(self.behavior.check_hate(message), .16 ) # value grabber

  def test_message_has_no_match_in_hate(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_hate(message), 0 ) # value grabber

  #################### childish tests ####################

  def test_message_has_match_in_childish(self):
    message = ['foolish', 'naive']
    self.assertEqual(self.behavior.check_childish(message), .16 ) # value grabber

  def test_message_has_no_match_in_childish(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_childish(message), 0 ) # value grabber

  #################### mockery tests ####################

  def test_message_has_match_in_mockery(self):
    message = ['farse', 'sham']
    self.assertEqual(self.behavior.check_mockery(message), .16 ) # value grabber

  def test_message_has_no_match_in_mockery(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_mockery(message), 0 ) # value grabber

  #################### pandering tests ####################

  def test_message_has_match_in_pandering(self):
    message = ['please', 'satisfy']
    self.assertEqual(self.behavior.check_pandering(message), .16 ) # value grabber

  def test_message_has_no_match_in_pandering(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_pandering(message), 0 ) # value grabber

  #################### supportive tests ####################

  def test_message_has_match_in_supportive(self):
    message = ['backing', 'footing']
    self.assertEqual(self.behavior.check_supportive(message), .16 ) # value grabber

  def test_message_has_no_match_in_supportive(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_supportive(message), 0 ) # value grabber

  #################### promises tests ####################

  def test_message_has_match_in_promises(self):
    message = ['commitment', 'obligation']
    self.assertEqual(self.behavior.check_promises(message), .16 ) # value grabber

  def test_message_has_no_match_in_promises(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_promises(message), 0 ) # value grabber

  #################### patriotic tests ####################

  def test_message_has_match_in_patriotic(self):
    message = ['country', 'national']
    self.assertEqual(self.behavior.check_patriotic(message), .16 ) # value grabber

  def test_message_has_no_match_in_patriotic(self):
    message = ['trees', 'computer']
    self.assertEqual(self.behavior.check_patriotic(message), 0 ) # value grabber

if __name__ == '__main__':
  unittest.main()
