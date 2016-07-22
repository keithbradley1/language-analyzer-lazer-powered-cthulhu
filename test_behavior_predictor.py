import unittest
from behavior_predictor import *
#################### behavior predictor tests ####################

class TestBehavior(unittest.TestCase):
  ''' Tests that behavior predictor receives a message to be evaluated'''

  # @classmethod
  # def setUpClass(self):
  #   self.behavior = Behavior_Predictor()


#################### dictator tests ####################

  def test_message_has_match_in_dictator(self):
    message = ['commander', 'authoritarian']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_dictator(), .16 ) # value grabber

  def test_message_has_no_match_in_dictator(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_dictator(), 0 ) # value grabber

  def test_number_of_matches_in_dictator(self):
    number_of_matches = 2
    message = ['commander', 'authoritarian']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_dictator(), .16)

  def test_average_of_match_values_in_dictator(self):
    average_of_match_values = .16
    message = ['commander', 'authoritarian']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_dictator(), .16)

  #################### hippie tests ####################

  def test_message_has_match_in_hippie(self):
    message = ['freethinker', 'bohemian']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_hippie(), .16 ) # value grabber

  def test_message_has_no_match_in_hippie(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_hippie(), 0 ) # value grabber

  #################### blame tests ####################

  def test_message_has_match_in_blame(self):
    message = ['charge', 'censure']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_blame(), .16 ) # value grabber

  def test_message_has_no_match_in_blame(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_blame(), 0 ) # value grabber

  #################### inspiring tests ####################

  def test_message_has_match_in_inspiring(self):
    message = ['invigorate', 'produce']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_inspiring(), .16 ) # value grabber

  def test_message_has_no_match_in_inspiring(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_inspiring(), 0 ) # value grabber

  #################### hate tests ####################

  def test_message_has_match_in_hate(self):
    message = ['antagonism', 'grievance']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_hate(), .16 ) # value grabber

  def test_message_has_no_match_in_hate(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_hate(), 0 ) # value grabber

  #################### childish tests ####################

  def test_message_has_match_in_childish(self):
    message = ['foolish', 'naive']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_childish(), .16 ) # value grabber

  def test_message_has_no_match_in_childish(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_childish(), 0 ) # value grabber

  #################### mockery tests ####################

  def test_message_has_match_in_mockery(self):
    message = ['farse', 'sham']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_mockery(), .16 ) # value grabber

  def test_message_has_no_match_in_mockery(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_mockery(), 0 ) # value grabber

  #################### pandering tests ####################

  def test_message_has_match_in_pandering(self):
    message = ['please', 'satisfy']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_pandering(), .16 ) # value grabber

  def test_message_has_no_match_in_pandering(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_pandering(), 0 ) # value grabber

  #################### supportive tests ####################

  def test_message_has_match_in_supportive(self):
    message = ['backing', 'footing']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_supportive(), .16 ) # value grabber

  def test_message_has_no_match_in_supportive(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_supportive(), 0 ) # value grabber

  #################### promises tests ####################

  def test_message_has_match_in_promises(self):
    message = ['commitment', 'obligation']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_promises(), .16 ) # value grabber

  def test_message_has_no_match_in_promises(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_promises(), 0 ) # value grabber

  #################### patriotic tests ####################

  def test_message_has_match_in_patriotic(self):
    message = ['country', 'national']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_patriotic(), .16 ) # value grabber

  def test_message_has_no_match_in_patriotic(self):
    message = ['trees', 'computer']
    behavior = Behavior_Predictor(message)
    self.assertEqual(behavior.check_patriotic(), 0 ) # value grabber

if __name__ == '__main__':
  unittest.main()
