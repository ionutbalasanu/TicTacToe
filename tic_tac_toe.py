# -*- coding: utf-8 -*-
"""
@author: Ionut
"""

import os
os.system("cls")

# In[1]:
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
        
    def update_cell(self,cell_no,player):
        if self.cells[cell_no]==" ":
            self.cells[cell_no]=player
    def is_winner(self,player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True
        if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            return True
        if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            return True
        if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            return True
        
        return False
    def reset(self):
        self.cells=[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    
    def is_draw(self):
        used_cells=0
        for cell in self.cells:
            if cell !=" ":
                used_cells+=1
        if used_cells==9:
            return True
        else:
            return False
    def computer_move_easy(self, player):
        for i in range(1,10):
            if self.cells[i]==" ":
                self.update_cell(i,player)
                break
board=Board()
#Am creat o functie de refresh, astfel incat la fiecare mutare sa se afiseze tabla actualizata
def refresh_screen():
    os.system("cls")
    board.display()

while True:
    refresh_screen()
    
    x_player=int(input("\n Player x) Alege mutarea 1 -> 9. >>>"))
    board.update_cell(x_player,"X")
    refresh_screen()
    
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
        
    
    #o_player=int(input("\n Player 0) Alege mutarea 1 -> 9. >>>"))
    board.computer_move_easy("0")
    #board.update_cell(o_player,"0")

    if board.is_winner("0"):
        print("\n Player 0 wins")
        play_again=input("New game? (Y/N)")
        if play_again=="N":
            board.reset()
            continue
        else:
            break