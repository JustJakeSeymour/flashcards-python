import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib')

from deck import Deck
from card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.card1 = Card('question1', 'answer1', 'category1')
        self.card2 = Card('question2', 'answer2', 'category1')
        card3 = Card('question3', 'answer3', 'category2')
        self.cards = [self.card1, self.card2, card3]
        self.deck = Deck(self.cards)

    def test_deck_is_deck(self):
        # Deck is of Deck class
        self.assertIsInstance(self.deck, Deck)
    
    def test_deck_contains_cards(self):
        # Deck contains cards
        self.assertEqual(self.deck.cards, self.cards)
    
    def test_deck_cards_are_cards(self):
        # Deck's cards are card class
        self.assertIsInstance(self.deck.cards[0], Card)
    
    def test_deck_count_method(self):
        # Deck has .count method
        self.assertEqual(self.deck.count(), 3)
    
    def test_deck_cards_in_category_method(self):
        # Deck has .cards_in_category method
        selected = self.deck.cards_in_category('category1')
        self.assertEqual(selected, [self.card1, self.card2])
        self.assertEqual(len(selected), 2)
    
if __name__ == '__main__':
    unittest.main()