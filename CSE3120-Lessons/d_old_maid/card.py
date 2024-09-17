# card.py in c_black_jack

"""
title: Card class with protection
author: Austin Meng
date-created: 2023 - 03 -15


"""

class Card:

    FACES = {
        1:"ACE",
        11:"Jack",
        12:"Queen",
        13:"King"
    }
    SUITS = {
        0:"Diamonds",
        1:"Clubs",
        2:"Hearts",
        3:"Spades",
    }
    def __init__(self, VALUE, SUIT):
        self.__VALUE = VALUE
        self.__SUIT = SUIT

    def getValue(self):
        return self.__VALUE

    def getSuit(self):
        return self.__SUIT


    def getCardName(self):
        if self.__VALUE in Card.FACES:
            return f"{Card.FACES[self.__VALUE]} of {Card.SUITS[self.__SUIT]}"
        else:
            return f"{self.__VALUE} of {Card.SUITS[self.__SUIT]}"
    def __str__(self):

        """

        modifying the string value of the object
        :return: str
        """
        return self.getCardName()
    def __repr__(self):
        return self.getCardName()


if __name__ == "__main__":
    CARD = Card(11,0)
    print(CARD.getCardName())
    print(CARD.getValue())
