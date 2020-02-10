import numpy as np
from math import inf as infinity
import math
import random
import os
os.system("cls")

class Board():
    boardSize=0
    def __init__(self,boardSize):
        self.boardSize=boardSize
        self.marks = np.empty((boardSize, boardSize),dtype='str')
        self.marks[:,:] = ' '
        self.players=['X','0']

    def printBoard(self): 
        print(' ',end='')
        for j in range(self.boardSize):
            print(" "+str(j+1), end='')
        
        
        print("")
        for i in range(self.boardSize):
            print(" ",end='')
            for j in range(self.boardSize):
                print("--",end='')
            
            print("-")

            print(i+1,end='')
            
            for j in range(self.boardSize):
                print("|"+self.marks[i][j],end='')
            
            print("|")
                
        
        print(" ",end='')
        for j in range(self.boardSize):
            print("--",end='')
        
        print("-")
    def refresh_screen(self):
        os.system("cls")
        self.printBoard()
    def checkWin(self, mark):
        won = False
        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break
        
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won
    def noMoreMoves(self):
        return (self.marks!=' ').all()
    def copy_game_state(self,state):
        new_state=np.empty((self.boardSize, self.boardSize),dtype='S')
        new_state[:,:]=' '
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                new_state[i][j]=state[i][j]
        return new_state


class HumanPlayer(Board):
    def __init__(self,board):
       self.name=" "
       self.playerLetter=' '
       self.boardSize=board.boardSize
       self.marks=board.marks
       
    def getPlayerName():
        name=str(input("Enter your name:"))
        return name
    def getPlayerLetter():
        playerLetter=' '
        while not (playerLetter=='X' or playerLetter=='0'):
            playerLetter=str(input("Choose your symbol(X or 0): ")).upper()
        if playerLetter=='X':
            return ['X','0']
        else:
            return['0','X']
    def makeMove(self, row, col, mark):
        possible = False  
        if row==-1 and col==-1:
            return False
        
        row = row - 1
        col = col - 1
        
        if row<0 or row>=self.boardSize or col<0 or col>=self.boardSize:
            print("Not a valid row or column!")
            return False
        
        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    
        
        if not possible and mark=='X':
            print("\nself position is already taken!")
class ComputerPlayer(Board):
    def computerEasy(self):
        while True:
            col=random.randint(1,3)
            row=random.randint(1,3)
            if self.marks[row-1][col-1]==' ':
                return row,col
            break
    
    def play_comp_move(self,state, player,block_num):
        if state[int((block_num-1)/3)][(block_num-1)%3]==' ':
            state[int((block_num-1)/3)][(block_num-1)%3]==player
    def copy_game_state(self,state):
        new_state=np.empty((self.boardSize, self.boardSize),dtype='S')
        new_state[:,:]=' '
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                new_state[i][j]=state[i][j]
        return new_state
    def getBestMove(self,state, player):        
        moves = []
        empty_cells = []
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if state[i][j] == ' ':
                    empty_cells.append(i*self.boardSize + (j+1))
        
        for empty_cell in empty_cells:
            move = {}
            move['index'] = empty_cell
            new_state = self.copy_game_state(state)
            self.play_comp_move(new_state, player, empty_cell)
            
            if player == 'O':    
                result = self.getBestMove(new_state, 'X')   
                move['score'] = result
            else:
                result = self.getBestMove(new_state, 'O')    
                move['score'] = result
            
            moves.append(move)
    
        # Find best move
        best_move = 0
        if player == 'O':   
            best = -infinity
            for move in moves:
                if move['score'] > best:
                    best = move['score']
                    best_move = move['index']
        else:
            best = infinity
            for move in moves:
                if move['score'] < best:
                    best = move['score']
                    best_move = move['index']
                    
        return best_move
class GamePlay(Board):
    def __init__(self):
        self.boardSize=0
    def Round(self):
        boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        choice=int(input('Enter your choice: 1) Multiplayer  2)Computer easy  3)Computer hard: '))
        board = Board(boardSize)
        board.printBoard()
        player1,player2=HumanPlayer.getPlayerLetter()
        playerName=HumanPlayer.getPlayerName()
        humanPlayer=HumanPlayer(board)

        while True:
            if choice==1:
                row, col = -1, -1
                while not humanPlayer.makeMove(row, col, player1):
                    print(playerName+ "'s Move")
                    row, col = input("Choose your move (row, column): ").split(',')
                    row = int(row)
                    col = int(col)
            
                board.printBoard()
                while not humanPlayer.makeMove(row, col, player2):
                    print("Player 2 Move")
                    row, col = input("Choose your move (row, column): ").split(',')
                    row = int(row)
                    col = int(col)
            
                board.printBoard()
            if choice==2:
                row,col=-1,-1

                while not humanPlayer.makeMove(row, col, player1):
                    print(playerName+" Move")
                    row, col = input("Choose your move (row, column): ").split(',')
                    row = int(row)
                    col = int(col)
                board.printBoard()
                row,col=ComputerPlayer.computerEasy()
                humanPlayer.makeMove(row,col,player2)
                board.printBoard()
            if choice==3:
                game_state=np.empty((boardSize, boardSize),dtype='str')
                game_state[:,:]=' '
                row,col=-1,-1
                while not humanPlayer.makeMove(row, col, player1):
                    print(playerName+ " Move")
                    row, col = input("Choose your move (row, column): ").split(',')
                    row = int(row)
                    col = int(col)
                board.printBoard()
                
                block_choice=ComputerPlayer.getBestMove(board.marks,board.players[1])
                row=math.ceil((block_choice)/board.boardSize)
                print("row ",row)
                col=math.ceil((block_choice)%board.boardSize)
                print("col ",col)
                print("alegere ",block_choice)
                humanPlayer.makeMove(row,col,player2)
                board.printBoard()
                
            if board.checkWin('X'):
                print("PLayer x won!")
                break
            elif board.noMoreMoves():
                print("It's a Draw!")
                break
            if board.checkWin('0'):
                print("player 0 won!")
                break
            elif board.noMoreMoves():
                print("It's a Draw!")
                break
    
                
        
play=GamePlay()
play.Round()
    
    
    
     
    