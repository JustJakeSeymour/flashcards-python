class Turn:
    def __init__(self, card, guess):
        self.card = card
        self.guess = guess

    def is_correct(self):
        return self.card.answer == self.guess