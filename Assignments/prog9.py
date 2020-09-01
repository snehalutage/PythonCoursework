#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 9                       #
# Due Date       : 04/21/2020              #
############################################

#############################################################################################
# File        : prog9.py                                                                    #
# Usage       : prog9.py                                                                    #
# Description : This program is to implement N Queens Puzzle. A recursive Python program    #
#               that solves the problem of whether it is possible to place N queens for     #
#               N = 1 to 8 on N * N chessboard                                              #
# Inputs      : NA                                                                          #
# Module      : Inbuilt - random , for the random number generation                         #
#               time - for random starting point                                            #
#############################################################################################

from time import time
from random import seed, randint

############################################################
# Function Name   : driver                                 #
# Description     : Driver program to start the program    #
# Input           : NA                                     #
############################################################
def driver():
    #Loop for 1-8
    for N in range(1,9):
        #Call to solveNQueens() for each value of N
        solveNQueens(N)

############################################################
# Function Name   : initBoard                              #
# Description     : Initialize the board and returns the   #
#                   N*N board with default values          #
# Input           : N - Size of board/no. of queens        #
############################################################
def initBoard(N):
    SEED=time()
    #seed(SEED)
    seed(SEED)
    #Initialize the board of size N*N with default value as False
    board=[[False for i in range(N)] for j in range(N)]
    return board

############################################################
# Function Name   : solveNQueens                           #
# Description     : Place the N Queens on board , if it is #
#                   able to place Queen then it prints the #
#                   board else prints message              #
# Input           : N - Size of board/no. of queens        #
############################################################
def solveNQueens(N):
    #Initialise the board
    board=initBoard(N)
    print("\nBoard size : {0}".format(N))
    
    #Call solveNQueenUtil() for placing the Queens using backtracking
    result=solveNQueensUtil(board,0)
    if result == True:
        printBoard(board)
    else:
        print("Solution does not exists.")

############################################################
# Function Name   : solveNQueensUtil                       #
# Description     : Recursive function to place the N queen#
#                   using Backtracking                     #
# Input           : board - 2D list & row = 0              #
############################################################
def solveNQueensUtil(board,row):
    #Base case , if row is the last row and all queens are placed
    if row >= len(board):
        return True

    #Backtracking and recursive call and place the Queen if possible
    for i in range(len(board)):
        #Generate random number for column
        col=randint(0,len(board)-1)

        #Call to isSafe() to check if it is safe to place the Queen on the
        #given position(row,col)
        res=isSafe(board,row,col)
        if res == True:
            #If return True then place the Queen
            board[row][col]="Q"

            #Recursive call for next row
            if solveNQueensUtil(board,row+1) == True:
                return True
            
            #If the solution is not able to place the Queen in any row
            #backtrack to previous row to change the values of Queens
            #previously placed
            board[row][col]=False
    return False

############################################################
# Function Name   : isSafe                                 #
# Description     : Check if Queen can be placed at row,col#
#                   if possible return True else False     #
# Input           : board - 2D list, row,col               #
############################################################
def isSafe(board,row,col):
    pos_Queen=[]
    #Get the positions where the Queens are already present on board
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "Q":
                pos_Queen.append([i,j])
                
    #If there is no Queen already present, return True
    if len(pos_Queen) == 0:
        return True

    #Check the row,column with the dimensions of already present Queens
    #If any row,col or diagonal matches it returns False
    for x in pos_Queen:
            #If row is same as row of the already present Queen
            if row == x[0]:
                return False
            #If column is same as column of already present Queen
            elif col == x[1]:
                return False
            #If the queen to place is having position diagonal to already existing queen
            elif abs(row-x[0]) == abs(col-x[1]):
                return False
    return True

############################################################
# Function Name   : printBoard                             #
# Description     : Prints the board wiht the N Queens with#
#                   the rectangular table format           #
# Input           : board                                  #
############################################################
def printBoard(board):
    print("","-"*(len(board)*5 + len(board)-1),"")
    for i in range(len(board)):
        print(("|"+" "*5)*(len(board)+1))
        for j in range(len(board)):
            if board[i][j] == False:
                board[i][j] = " "
            if j != len(board)-1:
                    print("|"+" "*2+board[i][j]+" "*2,end="")
            else:
                print("|"+" "*2+board[i][j]+" "*2+"|")
        print(("|"+" "*5)*(len(board)+1))
        print("","-"*(len(board)*5 +len(board)-1),"")

#Call the driver function
driver()

