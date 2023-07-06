import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')

from turn import Turn
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('Do you know Python?', 'I do now!', 'meta')
        self.guess1 = 'Not yet.'
        self.turn1 = Turn(self.card1, self.guess1)
        guess2 = 'I do now!'
        self.turn2 = Turn(self.card1, guess2)
    
    def test_turn_is_turn(self):
        # Test is of Test Class
        self.assertIsInstance(self.turn1, Turn)

    def test_turn_has_card(self):
        # Test has a card with attributes
        self.assertEqual(self.turn1.card, self.card1)
    
    def test_turn_has_guess(self):
        # Test has a guess
        self.assertEqual(self.turn1.guess, 'Not yet.')
    
    def test_turn_is_correct_method(self):
        # Test has correct method
        self.assertFalse(self.turn1.is_correct())
        self.assertTrue(self.turn2.is_correct())

    def test_turn_feedback_method(self):
         # test1.feedback returns "Incorrect."
         self.assertEqual(self.turn1.feedback(), "Incorrect.")
         self.assertEqual(self.turn2.feedback(), "Correct.")
         
if __name__ == '__main__':
        unittest.main()