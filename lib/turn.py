class Turn:
    def __init__(self, card, guess):
        self.card = card
        self.guess = guess

    def is_correct(self):
        return self.card.answer == self.guess
    
    def feedback(self):
        if self.is_correct():
            return 'Correct.'
        else:
            return 'Incorrect.'