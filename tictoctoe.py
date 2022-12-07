import pyfiglet
import random
import time
start = time.time()
sum = 0
for n in range(1,500):
    sum += n
print(sum)
from colorama import Fore
title=pyfiglet.figlet_format("Tic_Toc_Toe" , font="slant")
print(title)


print("Run Time: " + str( time.time() - start ))

def show():
 for row in game_board:
    for cell in row:
      if cell=="X":
        print(Fore.BLUE,cell ,Fore.RESET, end=" ")
      elif cell=="O":
        print(Fore.RED,cell ,Fore.RESET, end=" ")
      else:
        print(cell, end=" ")
    print()

game_board=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

def check_game():
  if game_board[0][0]==game_board[0][1]==game_board[0][2]=="X" or game_board[1][0]==game_board[1][1]==game_board[1][2]=="X" or game_board[2][0]==game_board[2][1]==game_board[2][2]=="X" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="X" or game_board[2][0]==game_board[1][1]==game_board[0][2]=="X" or game_board[0][0]==game_board[1][0]==game_board[2][0]=="X" or game_board[0][1]==game_board[1][1]==game_board[2][1]=="X" or game_board[0][2]==game_board[1][2]==game_board[2][2]=="X":
    print("YOU WIN")
     
  elif game_board[0][0]==game_board[0][1]==game_board[0][2]=="O" or game_board[1][0]==game_board[1][1]==game_board[1][2]=="O" or game_board[2][0]==game_board[2][1]==game_board[2][2]=="O" or game_board[0][0]==game_board[1][1]==game_board[2][2]=="O" or game_board[2][0]==game_board[1][1]==game_board[0][2]=="O" or game_board[0][0]==game_board[1][0]==game_board[2][0]=="O" or game_board[0][1]==game_board[1][1]==game_board[2][1]=="O" or game_board[0][2]==game_board[1][2]==game_board[2][2]=="O":
    print("YOU WIN")
    
  else:
    print("there is no winner")


print("WELLCOME TO MY TIC TOC TOE GAME") 
print("please choose from menu")
user_choice=int(input("Pree 1 if you wanna play with a player else Pree 2 if you wanna play with computer: "))


if user_choice==1:
 while 1==1:
    print("player1")
    while 1==1:
        row=input("Enter row: ")
        col=input("Enter col: ")
        if 0<=row<=2 and  0<=col<=2:
         if game_board[row][col]=="-":
            game_board[row][col]="X"
            break
         else:
            print("select another row and col")
        else:
            print("try again")
    show()
    check_game()

    print("player2")
    while 1==1:
        row=int(input("Enter row: "))
        col=int(input("Enter col: "))
        if 0<=row<=2 and  0<=col<=2:
          if game_board[row][col]=="-":
            game_board[row][col]="O"
            break
          else:
            print("select another row and col")
        else:
            print("try again")
    show()
    check_game()
elif user_choice==2:
  while 1==1:
    print("YOU")
    
    while 1==1:
        row=int(input("Enter row: "))
        col=int(input("Enter col: "))
        if 0<=row<=2 and  0<=col<=2:
         if game_board[row][col]=="-":
            game_board[row][col]="X"
            break
         else:
            print("select another row and col")
        else:
            print("try again")
    show()
    check_game()

    print("computer")
    while 1==1:
        row=random.randint(0,2)
        col=random.randint(0,2)
        if game_board[row][col]=="-":
           game_board[row][col]="O"
           break
        else:
            print("select another row and col")
    show()
    check_game()

print("Run Time: " + str( time.time() - start ))