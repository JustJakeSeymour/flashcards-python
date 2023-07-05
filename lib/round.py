class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []

    def current_card():
        if self.deck:
            return self.deck[0]
        else:
            return None
        
    def take_turn(self, guess):
        current_turn = Turn(self.current_card(), guess)
        