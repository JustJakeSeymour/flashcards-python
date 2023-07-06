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
    
    def category_turns(self, category):
        category_turns = []
        for turn in self.turns:
            if turn.card.category == category:
                category_turns.append(turn)
            else:
                pass
        return category_turns    

    def correct_turns(self):
        correct = []
        for turn in self.turns:
            if turn.is_correct():
                correct.append(turn)
            else:
                pass
        return correct
            
    def number_correct(self):
        return len(self.correct_turns())
    
    def number_correct_by_category(self, category):
        category_correct = []
        for turn in self.category_turns(category):
            if turn.is_correct():
                category_correct.append(turn)
            else:
                pass
        return len(category_correct)
    
    def percent_correct(self):
        percent = self.number_correct() / len(self.turns)*100
        return round(percent, 1)

    def percent_correct_by_category(self, category):
        percent = self.number_correct_by_category(category) / len(self.category_turns(category))*100
        return round(percent, 1)
