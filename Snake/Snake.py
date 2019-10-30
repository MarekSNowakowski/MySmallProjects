'''
Marek Nowakowski
08-10.09.2019
'''

import keyboard
import time
from os import system
from random import randint

firsttime = True
Playing = False
minute = 0

class Board:
    
    def __init__(self,width,height):
        self.height = height
        self.width = width
        self.board = {}

    def drawboard(self):
        for column in range(self.height):
            for row in range(self.width):
                self.board[column,row] = ' '
                
    def drawbaundries(self):
        for column in range(self.height):
            self.board[column,0] = '|'
        for column in range(self.height):
            self.board[column,self.width - 1] = '|'
        for row in range(self.width):
            self.board[0,row] = '-'
        for row in range(self.width):
            self.board[self.height - 1, row] = '-'        
                
    def printboard(self):
        for column in range(self.height):
            for row in range(self.width):
                print (self.board[column,row],end='')
            print("")

class Player:
    def __init__(self,x,y,length):
        self.x = []
        self.y = []
        self.x.append(x)
        self.y.append(y)
        self.length = length
        self.direction = 'd'
        self.savedx = []
        self.savedy = []
        self.savedx.append(self.x)
        self.savedy.append(self.y)

    def __str__(self):
            return f"({self.x[0]}:{self.y[0]})"
            
    def show(self):
        for i in range(self.length):
            print(f"Position{i}: ({self.x[i]}:{self.y[i]})")
        
    def move(self):
        '''save every position'''
        for i in range(self.length+1):
            try:
                self.savedx[i] = self.x[i]
                self.savedy[i] = self.y[i]
            except IndexError:
                pass
        '''move head'''    
        if self.direction == 'w':
            self.x[0] = self.x[0] - 1
        if self.direction == 'a':
            self.y[0] = self.y[0] - 1
        if self.direction == 's':
            self.x[0] = self.x[0] + 1
        if self.direction == 'd':
            self.y[0] = self.y[0] + 1
        '''move other positions'''    
        if self.length > 1:
            for i in range(self.length-1):
                self.x[i+1] = self.savedx[i]
                self.y[i+1] = self.savedy[i]
    
    def addlength(self):
        self.length = self.length + 1
        self.x.append(self.savedx[-1])
        self.y.append(self.savedy[-1])
        self.savedx.append(0)
        self.savedy.append(0)

    def moving(self):
        if (keyboard.is_pressed('w') and self.direction!='s'):
            self.direction = 'w'
        if (keyboard.is_pressed('a') and self.direction!='d'):
            self.direction = 'a'
        if (keyboard.is_pressed('s') and self.direction!='w'):
            self.direction = 's'
        if (keyboard.is_pressed('d') and self.direction!='a'):
            self.direction = 'd'

    def printlen(self):
    	print(f"Length: {self.length}")

class Apple:
    
    def __init__(self,board,player):
        self.board = board
        self.player = player
        
        self.generateapple()
        
    def generateapple(self):
        self.applex = randint(1, self.board.height - 2)
        self.appley = randint(1, self.board.width - 2)
        if (self.applex == self.player.x[0] and self.appley == self.player.y[0]):
            while (self.applex == self.player.x[0] and self.appley == self.player.y[0]):
                self.applex = randint(1, self.board.height - 1)
                self.appley = randint(1, self.board.width - 1)               
                
    def drawapple(self):
        self.board.board[self.applex,self.appley] = "O"
        
    def eat(self):
        if (self.applex == self.player.x[0] and self.appley == self.player.y[0]):
            self.player.addlength()
            self.generateapple()
            self.drawapple()

def timer():
	global firsttime
	timer = int(time.clock())
	return timer

def drawplayer(board,player):
    global firsttime

    if (firsttime == False):
        board.board[player.savedx[-1],player.savedy[-1]] = " "
    firsttime = False
    for i in range(player.length):
    	board.board[player.x[i],player.y[i]] = "X"

def colision(board, player):
	global Playing
	if(player.x[0] == 0 or player.x[0] == board.height-1):
		Playing = False
	if(player.y[0] == 0 or player.y[0] == board.width-1):
		Playing = False
	for i in range(player.length-1):
		if(player.x[0]==player.x[i+1] and player.y[0]==player.y[i+1]):
			Playing = False

def gameover(player):
	system("cls")
	print("\n\n")
	print("		    _______  _______  __   __  _______    _______  __   __  _______  ______   ")
	print("		   |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |  ")
	print("		   |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||  ")
	print("		   |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_ ")
	print("		   |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |")
	print("		   |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |")
	print("		   |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|")
	print("\n\n")
	print(f"						    Score: {player.length}")
	print(f"						    Time: {timer()}")
	print("\n\n\n\n\n")
	print("Marek Nowakowski 10.09.2019")
	system("pause")

if __name__ == '__main__':

	board1 = Board(120,25)
	player1 = Player(5,20,1)
	apple1 = Apple(board1,player1)

	board1.drawboard()
	board1.drawbaundries()
	apple1.drawapple()

	Playing = True
	while Playing:
		apple1.eat()
		colision(board1,player1)
		player1.moving()
		if keyboard.is_pressed('x'):
			break
		drawplayer(board1,player1)
		board1.printboard()
		player1.printlen()
		print(f"Time: {timer()}")
		player1.move()
		target_time = time.clock() + 0.05
		while time.clock() < target_time:
			player1.moving()
			if keyboard.is_pressed('x'):
				break
		system('cls')
	gameover(player1)