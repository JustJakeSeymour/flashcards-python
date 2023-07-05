import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib')

from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def test_deck_is_deck(self):
        # Deck is of Deck class
        pass
    
    def test_deck_contains_cards(self):
        # Deck contains cards
        pass
    
    def test_deck_cards_are_cards(self):
        # Deck's cards are card class
        pass
    
    def test_deck_count_method(self):
        # Deck has .count method
        pass
    
    def test_deck_cards_in_category_method(self):
        # Deck has .cards_in_category method
        pass
    
if __name__ == '__main__':
    unittest.main()