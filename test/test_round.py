import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')

from round import Round
from turn import Turn
from deck import Deck
from card import Card

class TestRound(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('Do you know Python?', 'I do now!', 'meta')
        self.card2 = Card('How are you?', 'Okay', 'meta')
        self.card3 = Card('What is the name of your cat?', 'Conrad', 'names')
        self.card4 = Card('What is your name?', 'Jake', 'names')
        cards = [self.card1, self.card2, self.card3, self.card4]
        self.deck = Deck(cards)
        self.round = Round(self.deck)
        
    def test_round_is_round(self):
        # Round is of Round class
        self.assertIsInstance(self.round, Round)    
    
    def test_round_has_turns(self):
        # Round.turns is a list
        self.assertEqual(self.round.turns, [])
    
    def test_round_current_card_method(self):
        # Round.current_card is the index 0 of deck
        self.assertEqual(self.round.current_card(), self.card1)

    def test_round_take_turn_method(self):
        # take turn method requires 'guess'
        new_turn = self.round.take_turn('I do now!')
        self.assertIsInstance(new_turn, Turn)
        self.assertTrue(new_turn.is_correct)

    def test_round_holds_past_turn(self):
        # after take_turn method, round.turns has Turn obj
        self.assertEqual(self.round.turns, [])
        the_turn = self.round.take_turn('I do now!')
        self.assertEqual(self.round.turns, [the_turn])

    
    def test_round_number_correct_method(self):
        self.assertEqual(self.round.number_correct(), 0)

        turn1 = self.round.take_turn('I do now!')
        turn2 = self.round.take_turn('Not Okay')
        
        self.assertTrue(turn1.is_correct())
        self.assertFalse(turn2.is_correct())
        self.assertEqual(self.round.number_correct(), 1)
    
    def test_round_number_correct_by_category_method(self):
        self.round.take_turn('I do now!')
        self.round.take_turn('Not Okay')
        self.round.take_turn('Conrad')
        self.round.take_turn('Jake')
        
        self.assertEqual(self.round.number_correct(), 3)
        self.assertEqual(self.round.number_correct_by_category('meta'), 1)
        self.assertEqual(self.round.number_correct_by_category('names'), 2)
    
    def test_round_percent_correct_method(self):
        pass
    
    def test_round_percent_correct_by_category_method(self):
        pass
    
if __name__ == '__main__':
        unittest.main()