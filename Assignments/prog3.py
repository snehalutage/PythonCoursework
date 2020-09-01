#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 3                       #
# Due Date       : 02/06/2020              #
############################################

#############################################################################################
# File        : prog3.py                                                                    #
# Usage       : prog3.py < prog3.d1                                                         #
# Description : This program is to implement Caesars Ciphers for the text present in the    #
#               input file prog3.d2, using the shift and key input from prog3.d1            #
# Inputs      : From file prog3.d1 and prog3.d2                                             #
#               text   - input postfix expression read from prog2.d                         #
# Module      : Inbuilt - sys and os , for the stderr and get the filename from path        #
#############################################################################################

from sys import *
from os import path

############################################################
# Function Name   : open_infile                            #
# Description     : Open the text input file and return    #
#                   inputstream if unable to open file     #
#                   error thrown and exit                  #
# Input           : NA                                     #
############################################################
def open_infile():
    try:
        #Get the filename from th full path 
        inputFilename="/home/cs503/progs/20s/p3/prog3.d2"
        ins=open(inputFilename,"r")
        return ins
    except:
        stderr.write("Unable to open file - "+path.basename(inputFilename)+"\n")
        exit(1)

############################################################
# Function Name   : new_position                           #
# Description     : Calculate the encoded value for input  #
#                   character using the shift and key and  #
#                   return the encoded value               #
# Input           : c - character for which encoded value  #
#                       to be found                        #
#                   shift,key - shift for calculating the  #
#                               ciphers                    #
############################################################
def new_position(c,shift,key):
    #Get the standard alphabets to get the location of alphabets while calculating the second cipher values
    std="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #Convert the passed shift value from string to int
    shift=int(shift)

    #Check if passed character is alphabet or not, if not use the character as it is in cipher
    #Check if alphabet is upper case, find the cipher using first the shift value passed and then use key
    #Check if alphabet is lower case, convert the lower case to upper case to find the cipher
    #For the key, check if key length is <26, >26,=26 and find the cipher
    if not c.isalpha():
        replacechar=c
    elif c.isupper():
        #calculate the encoded value for first shift
        encvalueshift1=chr((ord(c) + shift - 65) % 26 + 65)
        #find the replace char using the second shift i.e key
        if len(key) < 26 :
            shift2=std.find(encvalueshift1)%len(key)
            #maintain the character case
            if key[shift2].islower():
                replacechar=key[shift2].upper()
            else:
                replacechar=key[shift2]
        elif len(key) > 26 :
            newkey=key[:26]
            shift2=std.find(encvalueshift1)
            if newkey[shift2].islower():
                replacechar=newkey[shift2].upper()
            else:
                replacechar=newkey[shift2]
        elif len(key) == 26 :
            shift2=std.find(encvalueshift1)
            if key[shift2].islower():
                replacechar=key[shift2].upper()
            else:
                replacechar=key[shift2]
    elif c.islower():
        encvalueshift1=chr((ord(c.upper()) + shift - 65) % 26 + 65)
        if len(key) < 26 :
            shift2=std.find(encvalueshift1)%len(key)
            replacechar=key[shift2].lower()
        elif len(key) > 26 :
            newkey=key[:26]
            shift2=std.find(encvalueshift1)
            replacechar=newkey[shift2].lower()
        elif len(key) == 26 :
            shift2=std.find(encvalueshift1)
            replacechar=key[shift2].lower()
    return replacechar

############################################################
# Function Name   : encodeCaesarCipher                     #
# Description     : For each line returns new string formed#
#                   by calculating ciphers using shift and #
#                   key                                    #
# Input           : line - text line from input file for   #
#                   which cipher to be found               #
#                   shift,key - shift for calculating the  #
#                               ciphers                    #
############################################################
def encodeCaesarCipher(line,shift,key):
    encoded=""
    for c in line:
       #Call to new_position() to get the replace character(encoded value)
       encvalue=new_position(c,shift,key)
       encoded = encoded + encvalue
    return encoded

############################################################
# Function Name   : process_infile                         #
# Description     : Open the input text file and prints the#
#                   encrypted value for the text file for  #
#                   different shift and key values         #
# Input           : shift,key - shift for calculating the  #
#                               ciphers                    #
############################################################
def process_infile(shift,key):
    #Call to open_infileI() to get the input stream form the input file prog3.d2
    inputstream=open_infile()
    final=""
    print("key, shift =",key+",",shift)
    print("----------------------------------------------------------------")
    for line in inputstream:
        #Call the encodeCaesarCipher() to get the Ciphers for the input text lines
        output=encodeCaesarCipher(line,shift,key)
        final = final + output
    print(final)
    #Close the file
    inputstream.close()

#Main function definition
#Initialize stack and call the process input function proc_input()
def main():
    #Read the input shift and key values
    text=stdin.read()
    for i in text.rstrip("\n").split('\n'):
        key,shift=i.split()
        #For each pair of shift and key value call the process_infile to find the Caesar Cipher
        process_infile(shift,key)

#Call to main function
main()
