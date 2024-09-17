# deck.py in c_black_jack

"""
title: deck of cards
author: Austin Meng
date-created: 2023-03-15


"""
from card import Card
from random import shuffle

class Deck:

    def __init__(self):

        self.__DECK = []
        self.__createDeck() # protected method
    # mutator Methods
    def __createDeck(self):
        # protected method
        for i in range(4):
            for j in range(1,14):
                self.__DECK.append(Card(j, i))

    def shuffle(self):
        # unprotected method
        shuffle(self.__DECK)

    def drawTopCard(self):
        return self.__DECK.pop(0)



if __name__ == "__main__":
    DECK = Deck()
    HAND = []
    DECK.shuffle()
    HAND.append(DECK.drawTopCard())
    HAND.append(DECK.drawTopCard())
    print(HAND[0])
    print(HAND)








