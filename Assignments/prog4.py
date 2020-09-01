#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 4                       #
# Due Date       : 02/18/2020              #
############################################

#############################################################################################
# File        : prog4.py                                                                    #
# Usage       : prog4.py                                                                    #
# Description : This program is to implement Tic-Tac-Toe Game for two players X and O.      #
#               Program simulates for 12 consecutive games. User needs to input yes/no to   #
#               continue the game(till 12)                                                  #
# Inputs      : NA                                                                          #
#               Prompts for yes/no to continue the game                                     #
# Module      : Inbuilt - random , for the random number generation                         #
#               graphics - for displaying the Tic-Tac-Toe window                            #
#############################################################################################

from graphics import *
from random import seed, randrange
import time

############################################################
# Function Name   : draw_board                             #
# Description     : Draw the Tic-Tac-Toe board             #
# Input           : win - Graph window object              #
############################################################
def draw_board(win):
    win.setCoords(0,0,3,3)
    Line(Point(0,1),Point(3,1)).draw(win)
    Line(Point(0,2),Point(3,2)).draw(win)
    Line(Point(1,0),Point(1,3)).draw(win)
    Line(Point(2,0),Point(2,3)).draw(win)
    for i in range(3):
        for j in range(3):
            if i == 0:
                Text(Point(j+0.1,i+0.1),j).draw(win)
            elif i == 1:
                Text(Point(j+0.1,i+0.1),j+3).draw(win)
            else:
                Text(Point(j+0.1,i+0.1),j+6).draw(win)

############################################################
# Function Name   : init_play                              #
# Description     : Get the first player                   #
# Input           : NA                                     #
############################################################
def init_play():
    #random.seed(s)
    player_num=randrange(2)
    if player_num == 0 :
        return 0
    else:
        return 1

############################################################
# Function Name   : print_stat                             #
# Description     : Print the game statistics              #
# Input           : no_wins - Wins and draw count          #
#                   no_games - Count of total games        #
############################################################
def print_stat(no_wins,no_games):
    for i in range(2):
        print("No of wins for Player {0}: {1} ({2:.1f} %)".format(i+1,no_wins[i],(no_wins[i]/no_games)*100))
    print("No of draws: {0} ({1:.1f} %)".format(no_wins[2],no_wins[2]/no_games * 100))

############################################################
# Function Name   : check_win                              #
# Description     : Check the cells indexes for winning or #
#                   draw of match                          #
# Input           : f,s,t - 1st,2nd and 3rd selected cells #
#                   index                                  #
############################################################
def check_win(f,s,t):
    if f%3 == s%3 and f%3== t%3:
        return True
    elif f//3 == s//3 and f//3 == t//3:
        return True
    elif abs(f%3 - s%3)  == abs (f//3 - s//3) and abs(s%3 - t%3) == abs(s//3- t//3) and abs(f%3 - t%3) == abs(f//3 - t//3):
        return True
    else :
        return False

############################################################
# Function Name   : after_3_steps                          #
# Description     : Create combinations of cells and check #
#                   winner and if match is draw            #
# Input           : n - number of cells selected           #
#                   cell - index values list for respective#
#                          player                          #
#                   player - player number                 #
############################################################
def after_3_steps(n,cell,player):
    if n == 3:
        #get the first, second and third selected values and call check_win() for checking winner
        f=cell[0]
        s=cell[1]
        t=cell[2]
        is_win=check_win(f,s,t)
        if is_win:
            print("Player",player+1,"wins.")
            return player
        else:
            return None
    elif n == 4:
        #Logic to create combination from the 4 selected indexes and call check_win() to check winner
        comb=[]
        for i in cell[0:2]:
            for j in cell[1:3]:
                if i != j:
                    comb.append((i,j,cell[-1]))
        for t in comb:
            f=t[0]
            s=t[1]
            t=t[2]
            is_win=check_win(f,s,t)
            if is_win:
                print("Player",player+1,"wins.")
                return player
        return None
    #Logic to create combination from the 5 selected indexes and call check_win() to check winner or draw
    elif n == 5:
        comb=[]
        for i in range(3):
            for j in range(1,4):
                if i<j:
                    comb.append((cell[i],cell[j],cell[-1]))
        for t in comb:
            f=t[0]
            s=t[1]
            t=t[2]
            is_win=check_win(f,s,t)
            if is_win:
                print("Player",player+1,"wins.")
                return player
        print("Draw.")
        return None

############################################################
# Function Name   : play                                   #
# Description     : Simulate the Tic-Tac-Toe game          #
# Input           : win - GraphWindow object, player - 1st #
############################################################
def play(win,player):
    #Select the block number from choice by each player X and O
    choice=[0,1,2,3,4,5,6,7,8]
    P0=[]
    P1=[]
    for i in range(len(choice)):
        #X- first player, O - second
        if player == 0:
            flag="X"
        else:
            flag="O"
        #Logic for selecting the index in Tic-Tac-Toe window and printing X or O
        #Maintin the selected index in lists
        select=choice[randrange(len(choice))]
        choice.remove(select)
        x=select%3
        y=select//3
        txt=Text(Point(x+0.5,y+0.5),flag)
        txt.setTextColor("blue")
        txt.setSize(26)
        txt.setStyle("bold")
        txt.draw(win)
        time.sleep(1)
        if player == 0:
            P0.append(select)
        else:
            P1.append(select)

        #Logic to check if we have any winner
        if len(P0) >= 3 or len(P1) >=3 :
            if player==0:
                cell=P0
            else:
                cell=P1
            winner=after_3_steps(len(cell),cell,player)
            if winner == 0 :
                return 0
            elif winner == 1:
                return 1
            else:
                if len(choice)==0:
                    return None

        player=(player+1)%2
        #input("Press enter to continue")

############################################################
# Function Name   : main                                   #
# Description     : Initialize the variables and call the  #
#                   the respective functions to simulate   #
#                   Tic-Tac-Toe game                       #
# Input           : NA                                     #
############################################################
def main():
    #Set seed as 1 to get the same sequence of input to have same output
    seed(1)

    #Set the variables
    win_player1=0
    win_player2=0
    num_draw=0
    no_games=1
    print()

    #Loop for 12 consecutive games
    while no_games != 13:
        #Call draw_board function to display Tic-Tac-toe window
        win=GraphWin("Tic Tac Toe",400,400)
        draw_board(win)

        #Get the random player1
        player=init_play()

        print("Game {0}:".format(no_games),end=" ")

        #Call play() to simulate the game
        #Get the count for the number of wins for player 1 and player 2 and the no. of draw matches
        status=play(win,player)
        if status==0:
            win_player1=win_player1+1
        elif status==1:
            win_player2=win_player2+1
        else:
            num_draw=num_draw+1

        #Ask user if game needs to be continued
        check=input("\nAnother game (yes/no) ? ")

        #To run the code in one go uncomment the below section till else part and comment the above line to take input from user
        #print("\nAnother game (yes/no) ?",end=" ")
        #if no_games != 12:
         #   check="yes"
        #else:
         #   check="no"
        if (check=="yes"):
            win.close()
            if no_games == 12:
                break
            no_games+=1
            continue
        elif check=="no":
            win.close()
            break
        else:
            print("Invalid option given - {0} , Exiting the game!!".format(check))
            exit(0)

    #Put the count of wins and draw in list and call print_stat() to print the game statistics
    no_wins=[win_player1,win_player2,num_draw]
    print_stat(no_wins,no_games)

#Call to main() function
main()
