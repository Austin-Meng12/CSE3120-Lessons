# game.py in c_black_jack

'''

Title: The black jack game engine
author: Austin Meng
date-created: 2023-03-17

'''

from player import  Player
from deck import Deck
class Game:

    def __init__(self):
        """
        setup for the game
        """
        self.__displayTitle()
        self.__PLAYER1 = Player  # player classes as a stand in for the object
        self.__PLAYER2 = Player
        self.__DECK = Deck() # DECK object
        self.__DECK.shuffle()
        self.__createPlayers()
        self.__TURN = 1

    def run(self):
        """
        The main program code loop
        :return:
        """

        self.__playerTurn(self.__PLAYER1)

        self.__playerTurn(self.__PLAYER2)


    ## input methods
    def __createPlayers(self):
        NAME1 = input("Player 1 name: ")
        NAME2 = input("Player 2 name: ")
        self.__PLAYER1 = Player(NAME1)
        self.__PLAYER2 = Player(NAME2)



    ## processing methods
    def __playerTurn(self, PLAYER1):
        for i in range(2):
            PLAYER1.addCard(self.__DECK.drawTopCard())

            if PLAYER1.setStay() == True:
                PLAYER1.setStay()
                PLAYER1.addCard(self.__DECK.drawTopCard())
                OUTPUT = input("Want to stay: (y/n)")

                PLAYER1.printHand()
                print(PLAYER1.getHandScore())

















    ## output methods
    def __displayTitle(self):
        print("Welcome to Black Jack")



if __name__ == "__main__":
    GAME = Game()
    GAME.run()
