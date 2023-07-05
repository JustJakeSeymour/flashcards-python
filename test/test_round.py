import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')

from round import Round
from turn import Turn
from deck import Deck
from card import Card

class TestRound(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_round_is_round(self):
        pass
    
    def test_round_has_turns(self):
        pass
    
    def test_round_current_card_method(self):
        pass
    
    def test_round_take_turn_method(self):
        # take turn method requires 'guess'
        pass
    
    def test_round_number_correct_method(self):
        pass
    
    def test_round_number_correct_by_category_method(self):
        pass
    
    def test_round_percent_correct_method(self):
        pass
    
    def test_round_percent_correct_by_category_method(self):
        pass
    
if __name__ == '__main__':
        unittest.main()