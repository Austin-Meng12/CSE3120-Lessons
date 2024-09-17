'''
title: War Card Game
Author: Austin Meng
date-created: 2023 - 03 -10

'''
import random

from random import randint
class Card:
    """
    Create die objects to roll for random numbers

    """

    def __init__(self):
        """
        1 in suits represent Diamonds
        2 in suits represent Hearts
        3 in suits represent spades
        4 in Suits represent clubs

        """

        self.SUIT = ["1", "2", "3", "4"]
        self.NUMBER = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.DECK = []



# "Merges the deck and Suit together into a single deck"
    def createCards(self):
      CARD = []

      for i in range(len(self.SUIT)):
            for j in range(len(self.NUMBER)):

                CARD.append(self.SUIT[i])
                CARD.append(self.NUMBER[j])
                self.DECK.append(CARD)
                CARD = []

      return self.DECK

    def deckSplit(self):
        half = len(self.DECK)//2
        return self.DECK[:half], self.DECK[half:]


    def shuffleDeck(self):
        random.shuffle(self.DECK)
        return self.DECK








if __name__ == "__main__":
    FINAL_DECK = Card()
    FULL_DECK = FINAL_DECK.createCards()

    SHUFFLE_DECK = FINAL_DECK.shuffleDeck()
    print(SHUFFLE_DECK)

    PLAYER_1_DECK,PLAYER_2_DECK = FINAL_DECK.deckSplit()

    print(PLAYER_1_DECK)
    print(PLAYER_2_DECK)
























