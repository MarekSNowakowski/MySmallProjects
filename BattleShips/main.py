import time
from os import system
from random import randint
from terminaltables import SingleTable
import tkinter.font

'''
BattleShips v.1.0 by Marek Nowakowski
20.10.2019
'''

class Board:
    
    def __init__( self, name ):
        self.name = name
        self.board = {}

    def drawboard(self):
        for column in range(10):
            for row in range(10):
                self.board[column,row] = ' '

    def printboard(self):
        table_instance = SingleTable([
        [self.name,'A', 'B','C','D','E','F','G','H','I','J'],
        ['1',self.board[0,0],self.board[0,1],self.board[0,2],self.board[0,3],self.board[0,4],self.board[0,5],self.board[0,6],self.board[0,7],self.board[0,8],self.board[0,9]],
        ['2',self.board[1,0],self.board[1,1],self.board[1,2],self.board[1,3],self.board[1,4],self.board[1,5],self.board[1,6],self.board[1,7],self.board[1,8],self.board[1,9]],
        ['3',self.board[2,0],self.board[2,1],self.board[2,2],self.board[2,3],self.board[2,4],self.board[2,5],self.board[2,6],self.board[2,7],self.board[2,8],self.board[2,9]],
        ['4',self.board[3,0],self.board[3,1],self.board[3,2],self.board[3,3],self.board[3,4],self.board[3,5],self.board[3,6],self.board[3,7],self.board[3,8],self.board[3,9]],
        ['5',self.board[4,0],self.board[4,1],self.board[4,2],self.board[4,3],self.board[4,4],self.board[4,5],self.board[4,6],self.board[4,7],self.board[4,8],self.board[4,9]],
        ['6',self.board[5,0],self.board[5,1],self.board[5,2],self.board[5,3],self.board[5,4],self.board[5,5],self.board[5,6],self.board[5,7],self.board[5,8],self.board[5,9]],
        ['7',self.board[6,0],self.board[6,1],self.board[6,2],self.board[6,3],self.board[6,4],self.board[6,5],self.board[6,6],self.board[6,7],self.board[6,8],self.board[6,9]],
        ['8',self.board[7,0],self.board[7,1],self.board[7,2],self.board[7,3],self.board[7,4],self.board[7,5],self.board[7,6],self.board[7,7],self.board[7,8],self.board[7,9]],
        ['9',self.board[8,0],self.board[8,1],self.board[8,2],self.board[8,3],self.board[8,4],self.board[8,5],self.board[8,6],self.board[8,7],self.board[8,8],self.board[8,9]],
        ['10',self.board[9,0],self.board[9,1],self.board[9,2],self.board[9,3],self.board[9,4],self.board[9,5],self.board[9,6],self.board[9,7],self.board[9,8],self.board[9,9]]
        ])                    

        # Get second table lines.
        table_instance.outer_border = True
        table_instance.inner_column_border = True
        table_instance.inner_row_border = True
        table = table_instance.table.splitlines()

        return table

def operateboard(board1, board2):
    board1.drawboard()
    board2.drawboard()
    smallest, largest = sorted([board1.printboard(), board2.printboard() ], key=len)
    largest += [''] * (len(smallest) - len(largest))  # Make both same size.
    combined = list()
    for i, row in enumerate(smallest):
        if (i == 2):
            combined.append(row.ljust(10) + '       BATTLESHIPS!       ' + largest[i])
        elif (i == 3):
            combined.append(row.ljust(10) + '   by Marek Nowakowski    ' + largest[i])
        elif (i == 7):
            combined.append(row.ljust(10) + "     Ennemy's ships:      " + largest[i])
        elif (i == 10):
            combined.append(row.ljust(10) + '       Carrier (5)        ' + largest[i])
        elif (i == 12):
            combined.append(row.ljust(10) + '      BattleShip  (4)     ' + largest[i])
        elif (i == 14):
            combined.append(row.ljust(10) + '       Cruiser  (3)       ' + largest[i])
        elif (i == 16):
            combined.append(row.ljust(10) + '      Submarine  (3)      ' + largest[i])
        elif (i == 18):
            combined.append(row.ljust(10) + '      Destroyer  (2)      ' + largest[i])
        else:
            combined.append(row.ljust(10) + '                          ' + largest[i])
    print( '\n'.join(combined) )


if __name__ == '__main__':
    board1 = Board("ME")
    board2 = Board("BOT")
    operateboard(board1, board2)