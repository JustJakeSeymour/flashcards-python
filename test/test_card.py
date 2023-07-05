import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')
from card import Card

class TestCard(unittest.TestCase):
    def test_card_properties(self):
        # Card has an Answer
        my_card = Card("Question", "Answer", "Category")
        my_card.answer = "Answer"
        self.assertEqual(my_card.answer, "Answer")

if __name__ == '__main__':
        unittest.main()