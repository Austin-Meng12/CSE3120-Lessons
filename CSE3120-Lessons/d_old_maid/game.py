# game.py in c_black_jack

'''

Title: The Old Maid game
author: Austin Meng
date-created: 2023-03-21

'''


from player import  Player
from deck import Deck
class Game:

    def __init__(self):
        """
        setup for the game
        """
        self.__displayTitle()
        self.__PLAYERS = []
        self.__DECK = Deck() # DECK object
        self.__DECK.shuffle()
        self.__createPlayers()
        self.__dealCard()
        for player in self.__PLAYERS:
            player.removeStartingPairs()
    def run(self):
        """
        The main program code loop
        :return:
        """
        while self.__PLAYERS[0].getHandSize() != 0 and self.__PLAYERS[1].getHandSize() != 0:
            self.__PLAYERS[0].addCard(self.__PLAYERS[1].giveRandomCard())
            if self.__PLAYERS[0].getHandSize() > 0:
                self.__PLAYERS[1].addCard(self.__PLAYERS[0].giveRandomCard())
            for player in self.__PLAYERS:
                player.printHand()
        # output
        if self.__PLAYERS[0].getHandSize() == 0:
            print(f"{self.__PLAYERS[0]} Wins")
        else:
            print(f"{self.__PLAYERS[1]} Wins")
        for player in self.__PLAYERS:
            player.printHand()


    ## input methods
    def __createPlayers(self):
        NAME1 = input("Player 1 name: ")
        NAME2 = input("Player 2 name: ")
        self.__PLAYERS.append(Player(NAME1))
        self.__PLAYERS.append(Player(NAME2))



    ## processing methods

    def __dealCard(self):
        for i in range(26):
            for player in self.__PLAYERS:
                if self.__DECK.getDeckSize() > 0:
                    CARD = self.__DECK.drawTopCard()
                    if CARD.getValue() == 12 and CARD.getSuit() == 0:
                        CARD = self.__DECK.drawTopCard()
                    player.addCard(CARD)


    ## output methods
    def __displayTitle(self):
        print("Welcome to old Maid")


if __name__ == "__main__":
    GAME = Game()
    GAME.run()
    print("Hello World")

