import os
import random
from random import choice
from math import inf as infinity
os.system("cls")

#Am creat o tabla pe care se va desfasura jocul 
class Board():
    #Am creat o lista de elemente 
    def __init__(self):
        self.cells=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    #Am afisat tabla (initial aceasta va fi goala)   
    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("__________")
        print("          ")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("__________")
        print("          ")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
    #inserare mutare in celula corespunzatoare
    def update_cell(self,state,cell_no,player):
        if self.cells[cell_no]==" ":
            self.cells[cell_no]=player
    #verificare castigator
    def is_winner(self,player):
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]:
            result= True
            for cell_no in combo:
                if self.cells[cell_no]!=player:
                    result=False
            if result==True:
                return True        
        return False
    #reset board
    def reset(self):
        self.cells=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]    
    #verificare egalitate
    def is_draw(self):
        used_cells=0
        for cell in self.cells:
            if cell !=" ":
                used_cells+=1
        if used_cells==9:
            return True
        else:
            return False
    #DUMB COMPUTER
    def computer_move_easy(self, player):     
        while True:
            move=random.randint(1,9)
            if self.cells[move]==" ":
                self.update_cell(move,player)
                break

   
    def copy_game_state(self,state):
        new_state=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        for i in range(10):
            new_state[i]=state[i]
        return new_state
    def refresh_screen(self):
        os.system("cls")
        self.display()
    def computerAI(self,state,player):        
        moves=[]
        empty_cells=[]
        for i in range(10):
            if self.cells[i]==" ":
                empty_cells.append(i)
        for empty_cell in empty_cells:
            move={}
            move['index']=empty_cell
            new_state=self.copy_game_state(state)
            self.update_cell(new_state,empty_cell,player)
            if player=='0':
                result=self.computerAI(new_state,'X')
                move['score']=result
            else:
                result=self.computerAI(new_state,'0')
                move['score']=result
            moves.append(move)
        best_move=0
        if player=='0':
            best=-infinity
            for move in moves:
                if move['score']>best:
                    best=move['score']
                    best_move=move['index']
        else:
            best=infinity
            for move in moves:
                if move['score']<best:
                    best=move['score']
                    best_move=move['index']
        return best_move
    def computer_move_hard(self,player):
        if self.cells[5]==" ":
            return 5
        for i in [1,3,7,9]:
            if self.cells[i]==" ":
                return i
        for i in [2,4,6,8]:
            if self.cells[i]==" ":
                return i
        for i in range(10):
            if self.cells[i]==" ":
                self.update_cell(i,player)
                if self.is_winner(player):
                    return i
        return random.randint(1,9)
board=Board()
#Am creat o functie de refresh, astfel incat la fiecare mutare sa se afiseze tabla actualizata


while True:
    board.refresh_screen()

    x_player=int(input("\n Player x) Alege mutarea 1 -> 9. >>>"))
    board.update_cell(board.cells,x_player,"X")
#    board.refresh_screen()
    #o_player=int(input("\n Player 0) Alege mutarea 1 -> 9. >>>"))
    #board.update_cell(o_player,"0")
    
    board.refresh_screen()

    #board.computer_move_easy("0")
    
    move=board.computerAI(board.cells,"0")
    board.update_cell(board.cells,move,"0")
    board.refresh_screen()
    


    #move=board.computer_move_hard("0")
    #board.update_cell(move,"0")
#    board.computer_move_hard("0")  
    
    if board.is_winner("X"):
        print("\n Player X wins")
        play_again=input("New game? (Y/N) ")
        if play_again=="Y" or "y":
            board.reset()
            continue
        else:
            break
    if board.is_draw():
        print("\n DRAW!! ")
        play_again=input("New game? (Y/N) ")
        if play_again=="Y" or "y":
            board.reset()
            continue
        else:
            break
    if board.is_winner("0"):
        print("\n Player 0 wins")
        play_again=input("New game? (Y/N)")
        if play_again=="N":
            board.reset()
            continue
        else:
            break