# player.py in c_black_jack


"""
title: The player class
Author: Austin
date-created: 2023-03-16

"""
import random


class Player:

    def __init__(self, NAME):
        self.__HAND = []
        self.__PAIRED_CARD = []
        self.__NAME = NAME


    # Mutator Methods
    def addCard(self, CARD):
        self.__HAND.append(CARD)
        self.removeStartingPairs()

    def removeStartingPairs(self):
        """
        assumes a sorted hand and removes cards in pairs.

        :return:
        """
        self.__HAND.sort(key = lambda x: x.getValue())
        for i in range(len(self.__HAND) - 1, -1 ,-1):
            if i != len(self.__HAND) - 1:
                if self.__HAND[i].getValue() == self.__HAND[i+1].getValue():
                    self.__PAIRED_CARD.append(self.__HAND.pop(i+1))
                    self.__PAIRED_CARD.append(self.__HAND.pop(i))

    def giveRandomCard(self):
        """
        randomly select a card to leave the player
        :return: Card
        """
        return self.__HAND.pop(random.randrange(len(self.__HAND)))




    # Accessor Methods



    def printHand(self):
        TEXT = ""
        for card in self.__HAND:
            TEXT += card.getCardName()
            TEXT += ", "
        TEXT = TEXT[:-2]
        print(TEXT)

    def getHandSize(self):
        return len(self.__HAND)

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
    PLAYER.addCard(Card(11, 3))
    PLAYER.addCard(Card(5,2))
    PLAYER.addCard(Card(1,2))
    PLAYER.printHand()

    PLAYER.removeStartingPairs()
    PLAYER.printHand()



