import unittest
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')

from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
         self.my_card = Card('Question', 'Answer', 'Category')

    def test_card_is_card(self):
        # Card is of Card class
        self.assertIsInstance(self.my_card, Card)

    def test_card_questions(self):
        # Card has a Quesiton
        self.assertEqual(self.my_card.question, 'Question')

    def test_card_answers(self):
        # Card has an Answer
        self.assertEqual(self.my_card.answer, 'Answer')

    def test_card_categories(self):
        # Card has a Category
        self.assertEqual(self.my_card.category, 'Category')

if __name__ == '__main__':
        unittest.main()