from board.board import Board
from game import GameException


class UI:
    def __init__(self,board):
        self.__board=board

    def game_on(self):
        try:
            while True:
                    # print("1.Play")
                    # print("2.exit")
                    # opt=input("Enter option:").strip()
                    # if opt=="2":
                    #     print("bye")
                    #     return
                    # elif opt=="1":
                print("Enter the dimensions for the board:")
                x=int(input("Length:"))
                y=int(input("Height:"))
                self.__board = Board(x + 1, y + 1)
                self.pvc()

                    # else:
                    #     raise GameException("wrong option")
        except Exception as e:
            print(e)

    def pvc(self):
        ok=True
        print(self.__board.str())
        while ok:
            try:

                player=input("Your turn.Insert the line and coloumn :").strip()
                self.__board.move(player)
                print(self.__board.str())
                if self.__board.check()==True:
                    print("The player wins")
                    return
                print("Computer turn")
                self.__board.move_computer()
                print(self.__board.str())
                if self.__board.check()==True:
                    print("The computer wins")
                    return



            except Exception as e:
                print(e)




