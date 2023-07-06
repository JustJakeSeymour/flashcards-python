from turn import Turn

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []

    def current_card(self):
        if self.deck:
            return self.deck.cards.pop(0)
        else:
            return None
        
    def take_turn(self, guess):
        current_turn = Turn(self.current_card(), guess)
        self.turns.append(current_turn)
        return current_turn
