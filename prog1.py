#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 1                       #
# Due Date       : 01/21/2020              #
############################################

#############################################################################################
# File        : prog1.py                                                                    #
# Usage       : prog1.py < prog1.d                                                          #
# Description : This program is to illustrate the chaotic function for the given initial    #
#               floating-point input from stdin file and display it in tabular form         #
# Inputs      : From file prog1.d                                                           #
#               x   - First floating-point number for which chaos function needs to be run  #
#               y   - Second floating-point number for which chaos function needs to be run #
#               num - Integer, number of iterations                                         #
#############################################################################################

#main() function definition
def main():
    print("This progragm illustrates a chaotic function.")

    #Accept the input from stdin input file prog1.d
    print("\nInput ===>")
    x=eval(input())
    y=eval(input())
    num=eval(input())
    print("Enter a number between 0 and 1 :",x)
    print("Enter another number between 0 and 1 :",y)
    print("How many numbers to print?",num)

    #Execute the chaotic function on user input for the given number of iterations
    print("\nChaotic Function Output ===>")
    print("Input{:^11}{:^15}".format(x,y))
    print("-"*27)
    #Loop for the number of iterations
    for i in range(num):
        #Execute the expression for chaotic function - 3.9*input*(1-input)
        x=3.9*x*(1-x)
        y=3.9*y*(1-y)
        print("{:14.6f}{:13.6f}".format(x,y))

#main() function call
main()
