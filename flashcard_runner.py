# load necessities
import sys
sys.path.append('/Users/jseymour22/_projects/flashcards-python/lib/')

from round import Round
from turn import Turn
from deck import Deck
from card import Card

card1 = Card('Do you know Python?', 'I do now!', 'meta')
card2 = Card('How are you?', 'Okay', 'meta')
card3 = Card('What is the name of your cat?', 'Conrad', 'names')
card4 = Card('What is your name?', 'Jake', 'names')
cards = [card1, card2, card3, card4]
cards2 = [card1, card2, card3, card4]
deck = Deck(cards)
round = Round(deck)

def player_turn():
    turn = round.take_turn('')
    print('This is card number %s of %s' %(len(round.turns), len(cards2)))
    print('Question: %s' %(turn.card.question))
    guess = input()
    turn.guess = guess
    print(turn.feedback())
    
def intro():
    print("Welcome! You're playing with %s cards." %(len(cards2)))
    print('-------------------------------------')

def game():
    for card in cards2:
        player_turn()

def end_game():
    print('****** Game over! ******')
    print('You had %s correct guesses out of %s for a total score of %s' %(round.number_correct(), len(cards2), round.percent_correct()))
    category_scores()

def category_scores():
    categories = []
    for card in cards2:
        if card.category not in categories:
            categories.append(card.category)
    for category in categories:
        print('%s - %s'%(category.capitalize(), round.percent_correct_by_category(category)))
    

intro()
game()
end_game()
