class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0

    # Insert card in current hand
    def join_card(self, card):
        self.hand.append(card)
        return self.hand

    def show_hand(self):
        for card in self.hand:
            print(f"|{card}", end="|")
        print()

    def show_hand_dealer(self, gstate):
        if gstate:
            for i in range(len(self.hand) - 1):
                card = self.hand[i]
                print(f"|{card}", end="|")
            print()
        else:
            for card in self.hand:
                print(f"|{card}", end="|")
            print()

    # Clean current hand for a new game
    def clean_hand(self):
        self.hand.clear()

    def hand_value(self):
        self.value = 0
        for card in self.hand:
            if card.valor in ['J', 'Q', 'K']:
                self.value += 10
            elif card.valor == 'A':
                if self.value <= 10:
                    self.value += 11
                else:
                    self.value += 1
            else:
                self.value += int(card.valor)
        return self.value
