# class Board:
#     def __init__(self,lines,coloumns,empty_value=0):
#         self.__lines=lines
#         self.__coloumns=coloumns
#         self.__empty_value=empty_value
#
#         self.__cells=self._create_board()
#
#     def _create_board(self):
#         for i in range(self.__lines):
#             return [self.__empty_value]*self.__coloumns
#
#     def get_lines(self):
#         return self.__lines
#
#     def get_coloumns(self):
#         return self.__coloumns
from texttable import Texttable

from game import GameException


class Board:
    def __init__(self,line=8,coloumn=8):
        self.__data=[]
        self.__line=line
        self.__coloumn=coloumn
        for i in range(self.__coloumn):
            self.__data.append([" "]* (self.__line))
        for i in range(self.__line):
            self.__data[0][i]=i-1
        for j in range(self.__coloumn):
            self.__data[j][0]=j-1
        self.__data[0][0]="/"

    def str(self):
        """
        draws the board
        """
        text=Texttable()
        for i in range (self.__coloumn):
            text.add_row(self.__data[i])
        return text.draw()
    def check(self):
        """
        returns False if there are spaces left on the board
        returns True otherwise
        """
        for i in range(0,self.__coloumn):
            for j in range(0,self.__line):
                if self.__data[i][j]==" ":
                    return False

        return True
    def move(self,move1):
        """
        input:the move of the player, the line and coloumn of the board
        if the square is space it puts the x on the board
        """
        cf1=int(move1[0])+1
        cf2=int(move1[1])+1
        if self.__data[cf1][cf2]=="#" or self.__data[cf1][cf2]=="X" or self.__data[cf1][cf2]=="O":
            raise GameException("do another move")
        self.__data[cf1][cf2]="X"
        self.around(cf1,cf2)


    def around(self,n1,n2):
        """
        it puts the "#" all around the X or O
        """
        if n1==1:
            if n2==1:
                self.__data[n1+1][n2]="#"
                self.__data[n1][n2+1]="#"
                self.__data[n1+1][n2+1]="#"
            elif n2==self.__line-1:
                self.__data[n1][n2-1]="#"
                self.__data[n1+1][n2]="#"
                self.__data[n1+1][n2-1]="#"
            else:
                self.__data[n1][n2-1]="#"
                self.__data[n1+1][n2]="#"
                self.__data[n1+1][n2-1]="#"
                self.__data[n1+1][n2+1]="#"
                self.__data[n1][n2+1]="#"
        elif n1==self.__coloumn-1:
            if n2==1:
                self.__data[n1 - 1][n2] = "#"
                self.__data[n1 - 1][n2 + 1] = "#"
                self.__data[n1][n2 + 1] = "#"
            elif n2==self.__line-1:
                self.__data[n1-1][n2]="#"
                self.__data[n1][n2-1]="#"
                self.__data[n1-1][n2-1]="#"
            else:
                self.__data[n1][n2-1]="#"
                self.__data[n1][n2+1]="#"
                self.__data[n1-1][n2]="#"
                self.__data[n1-1][n2-1]="#"
                self.__data[n1-1][n2+1]="#"
        elif n2==1:
            self.__data[n1-1][n2]="#"
            self.__data[n1-1][n2+1]="#"
            self.__data[n1][n2+1]="#"
            self.__data[n1+1][n2]="#"
            self.__data[n1+1][n2+1]="#"
        elif n2==self.__line-1:
            self.__data[n1-1][n2]="#"
            self.__data[n1+1][n2]="#"
            self.__data[n1-1][n2-1]="#"
            self.__data[n1][n2-1]="#"
            self.__data[n1+1][n2-1]="#"
        else:
            self.__data[n1][n2-1]="#"
            self.__data[n1][n2+1]="#"
            self.__data[n1-1][n2-1]="#"
            self.__data[n1 - 1][n2] = "#"
            self.__data[n1 - 1][n2+1] = "#"
            self.__data[n1+1][n2 - 1] = "#"
            self.__data[n1+1][n2] = "#"
            self.__data[n1+1][n2 +1] = "#"

    def move_computer(self):
        """
        the computer looks where there are more spaces
        around a space and then puts "O"
        """
        max=0
        for n1 in range(self.__coloumn):
            for n2 in range(self.__line):
                k=0
                if self.__data[n1][n2]==" ":
                    if n1 == 1:
                        if n2 == 1:
                            if self.__data[n1 + 1][n2] ==" ":
                                k=k+1
                            if self.__data[n1][n2 + 1] ==" ":
                                k=k+1
                            if self.__data[n1 + 1][n2 + 1] ==" ":
                                k=k+1
                        elif n2 == self.__line - 1:
                            if self.__data[n1][n2 - 1] == " ":
                                k=k+1
                            if self.__data[n1 + 1][n2] == " ":
                                k=k+1
                            if self.__data[n1 + 1][n2 - 1] == " ":
                                k=k+1
                        else:
                            if self.__data[n1][n2 - 1] == " ":
                                k=k+1
                            if self.__data[n1 + 1][n2] ==" ":
                                k=k+1
                            if self.__data[n1 + 1][n2 - 1] == " ":
                                k=k+1
                            if self.__data[n1 + 1][n2 + 1] == " ":
                                k=k+1
                            if self.__data[n1][n2 + 1] == " ":
                                k=k+1
                    elif n1 == self.__coloumn - 1:
                        if n2 == 1:
                            if self.__data[n1 - 1][n2] == " ":
                                k=k+1
                            if self.__data[n1 - 1][n2 + 1] == " ":
                                k=k+1
                            if self.__data[n1][n2 + 1] == " ":
                                k=k+1
                        elif n2 == self.__line - 1:
                            if self.__data[n1 - 1][n2] == " ":
                                k=k+1
                            if self.__data[n1][n2 - 1] == " ":
                                k=k+1
                            if self.__data[n1 - 1][n2 - 1] == " ":
                                k=k+1
                        else:
                            if self.__data[n1][n2 - 1] == " ":
                                k=k+1
                            if self.__data[n1][n2 + 1] == " ":
                                k = k + 1

                            if self.__data[n1 - 1][n2] == " ":
                                k = k + 1
                            if self.__data[n1 - 1][n2 - 1] == " ":
                                k = k + 1
                            if self.__data[n1 - 1][n2 + 1] == " ":
                                k = k + 1
                    elif n2 == 1:
                        if self.__data[n1 - 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 - 1][n2 + 1] == " ":
                            k = k + 1
                        if self.__data[n1][n2 + 1] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2 + 1] == " ":
                            k = k + 1
                    elif n2 == self.__line - 1:
                        if self.__data[n1 - 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 - 1][n2 - 1] == " ":
                            k = k + 1
                        if self.__data[n1][n2 - 1] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2 - 1] == " ":
                            k = k + 1
                    else:
                        if self.__data[n1][n2 - 1] == " ":
                            k = k + 1
                        if self.__data[n1][n2 + 1] == " ":
                            k = k + 1
                        if self.__data[n1 - 1][n2 - 1] == " ":
                            k = k + 1
                        if self.__data[n1 - 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 - 1][n2 + 1] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2 - 1] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2] == " ":
                            k = k + 1
                        if self.__data[n1 + 1][n2 + 1] == " ":
                            k = k + 1
                    if max<=k:
                        max=k
                        a=n1
                        b=n2

        self.__data[a][b]="O"
        self.around(a,b)



















