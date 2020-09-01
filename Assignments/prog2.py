#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 2                       #
# Due Date       : 01/29/2020              #
############################################

#############################################################################################
# File        : prog2.py                                                                    #
# Usage       : prog2.py < prog2.d                                                          #
# Description : This program is to implement an interactive calculator for the given        #
#               postfix text expressions from stdin file and display the result             #
# Inputs      : From file prog1.d                                                           #
#               text   - input postfix expression read from prog2.d                         #
# Module      : stack.py, has the stack functions                                           #
#               Inbuilt - sys, for the stderr                                               #
#############################################################################################

from sys import *
from stack import *

############################################################
# Function Name   : proc_input                             #
# Description     : Process the input postfix expression   #
# Input           : text - List having the input read from #
#                          file  prog2.d                   #
#                   stack - List to push the input tokens &#
#                           result of operations           #
############################################################

def proc_input(text,stack):
    token=[]
    #Get the individual tokens from the readline output and add them to token[] list
    for i in range(len(text)):
        token += text[i].rstrip('\n').split(' ')

    #Iterate through the token[] list and perform the respective operation
    #If token is assignment "=" -> Print the Top element in stack
    #If token is operator -> perform operator operations on the stack elements(pop) and push the result to stack
    #If the token is unknow operator -> Throw error
    #If token is unary operation -> Perform the operator on the pop element
    #If token is character "c" -> Empty the stack
    #If token is number push -> convert to float and push to stack
    for t in range(len(token)):       
        if token[t] == "=":
           top_elt=Top(stack)
           if top_elt!=None:
               print("{:>8.3f}".format(float(top_elt)))      
        elif token[t] in "+,-,*,/":
            op1=Pop(stack)
            op2=Pop(stack)
            if op1!=None and op2 !=None:
                result=bin_op(str(op1),str(op2),token[t])
                if result!=None:
                    Push(result,stack)   
        elif token[t] in "$,!,@,#,^,&,(,),%)":
            stderr.write("Invalid operator : %s\n" % (token[t]))
        elif token[t] == "~":
            num=Pop(stack)
            if num!=None:
                #Push(format(float(~(((float(num))))),'.3f'),stack)
                Push(format((-float(num)),'.3f'),stack)
        elif token[t] == "c" :
            clear(stack)
        elif isinstance(eval(token[t]),float) or isinstance(eval(token[t]),int):
            Push(format(float(token[t]),'.3f'),stack)


############################################################
# Function Name   : bin_op                                 #
# Description     : Perform the specific binary operation  #  
#                   on the operands passed                 #
# Input           : op1 - First Operand                    #
#                   op2 - Second Operand                   #
#                   operator - Operation to be perfromed on#
#                              op1 and op2                 #
############################################################
def bin_op(op1,op2,operator):
    if (operator == "/" and op1 == "0.000"):
        stderr.write("Division by 0 : %s/%s\n" %(op2,op1))
        return None
    else:
        res=eval(op2+operator+op1)
        return format(res,'.3f')

#Main function definition
#Initialize stack and call the process input function proc_input()
def main():
    stack=[]
    text=stdin.readlines()
    proc_input(text,stack)

#Call to main function
main()

