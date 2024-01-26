import random


class Card:
    def __init__(self, nipe, valor):
        self.nipe = nipe
        self.valor = valor

    def __str__(self):
        return f"{self.valor} de {self.nipe}"


class Deck:
    def __init__(self):
        nipes = ["Espadas", "Ouros", "Copas", "Paus"]
        valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(nipe, valor) for nipe in nipes for valor in valores]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

