# player.py in c_black_jack


"""
title: The player class
Author: Austin
date-created: 2023-03-16

"""

class Player:

    def __init__(self, NAME):
        self.__HAND = []
        self.__NAME = NAME
        self.__STAY = False
        self.__SCORE = 0

    # Mutator Methods
    def addCard(self, CARD):
        self.__HAND.append(CARD)
    def __calcHandscore(self):
        ACES = 0
        self.__SCORE = 0
        for card in self.__HAND:

            if card.getValue() == 1 and ACES == 0:
                  ACES += 1
                  self.__SCORE += 11  # assume first ace is worth 11
            elif card.getValue() > 10:
                self.__SCORE += 10
            else:
                self.__SCORE += card.getValue()
            # Check if the first Ace should be valued at 11.
        if ACES > 0 and self.__SCORE > 21:
            self.__SCORE -= 10

    def setStay(self):
        self.__STAY = True

    def getStay(self):
        return self.__STAY



    def resetPlayer(self):
        self.__HAND = []
        self.__STAY = False
        self.__SCORE = 0

    # Accessor Methods

    def getHandScore(self):
        self.__calcHandscore()
        return self.__SCORE



    def printHand(self):
        TEXT = ""
        for card in self.__HAND:
            TEXT += card.getCardName()
            TEXT += ", "
        TEXT = TEXT[:-2]
        print(TEXT)


    def __str__(self):
        return self.__NAME




if __name__ == "__main__":
    from deck import Deck
    from card import Card
    PLAYER = Player("Austin")
    DECK = Deck()
    DECK.shuffle()
    PLAYER.addCard(Card(1,0))
    PLAYER.addCard(Card(11, 1))
    PLAYER.addCard(Card(1,2))
    print(PLAYER)
    PLAYER.printHand()
    print(PLAYER.getHandScore())


