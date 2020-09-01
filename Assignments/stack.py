############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 2                       #
# Due Date       : 01/29/2020              #
############################################

#############################################################################################
# File        : stack.py                                                                    #
# Usage       : import the module in the source python code                                 #
# Description : This program is to implement the various stack functions like push,pop,top  #
#               empty stack                                                                 #
# Inputs      : Respective functions have stack[] list and the element to be pushed as the  #
#               input                                                                       #
#############################################################################################

from sys import stderr

#To push the element onto stack
def Push(x,stack):
    stack.append(x)

#To pop the elements from stack if stack is not empty
#If stack empty throw error
def Pop(stack):
    if len(stack)==0:
        stderr.write("Stack is empty!\n")
        return None
    else:
        return stack.pop()

#Retrun the top element in stack if stack not empty
#Throw error when stack empty
def Top(stack):
    if len(stack)==0:
        stderr.write("Top: Stack is empty!\n")
        return None
    else:
        return stack[-1]

#Empty the stack
def clear(stack):
    stack.clear()
