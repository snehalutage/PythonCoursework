#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 5                       #
# Due Date       : 02/27/2020              #
############################################

#############################################################################################
# File        : prog5.py                                                                    #
# Usage       : prog5.py inputFile outputFile                                               #
# Description : This program is to implement Word Scanner for the text present in the       #
#               input file. It opens the files passed as argument and prints error if unable#
#               to open the files. Words scanned will have only alphabets and non-alphabets #
#               would be removed. It prints the scanned words along with theie frequency    #
# Inputs      : Files prog5.d1,prog5.d2 and prog5.d3                                        #
#               prog5.d1 - to check condition if file does not exists                       #
#               prog5.d2 - to check if file is empty                                        #
#               prog5.d3 - has the data that needs to be scanned                            #
# Module      : Inbuilt - sys,os,re , for the stderr,to get the absolute path for file,regex#
#############################################################################################
from os import path
from re import match, split, sub
from sys import argv, exit, stderr

############################################################
# Function Name   : checkArgs                              #
# Description     : To check the number of arguments passed#
#                   to the main script and print the usage #
#                   if incorrect arguments passed. Returns #
#                   the arguments passed to script         #
# Input           : NA                                     #
############################################################
def checkArgs():
    if len(argv) == 3 :
        return (argv[1],argv[2])
    else:
        stderr.write("Usage: ./prog5.py inFile outFile\n")
        exit()

############################################################
# Function Name   : openFiles                              #
# Description     : To open the input and output files     #
#                   passed as function arguments. Returns  #
#                   the respective file object             #
# Input           : files - tuple of the parameters passed #
#                           to main script                 #
############################################################
def openFiles(files):
    #Extract the input file and output file from the "files" tuple passed 
    inputfile=files[0]
    outputfile=files[1]
    #Open input file
    try:
        instream=open(inputfile,'r')
    except:
        stderr.write("\nCan't Open File: "+inputfile+"\n")
        exit()

    #Open output file    
    try:
        outstream=open(outputfile,'w')
    except:
        stderr.write("\nCan't Open File: "+outputfile+"\n")
        exit()
    return (instream,outstream)

############################################################
# Function Name   : closeFiles                             #
# Description     : To close the input and output files    #
#                   passed as function arguments.          #
# Input           : fobjects - tuple of the file objects to#
#                              be closed                   #
############################################################
def closeFiles(fobjects):
    for f in fobjects:
        try:
            f.close()
        except:
            stderr.write("\nUnable to close the file "+f+".\n")
            exit()

############################################################
# Function Name   : createList                             #
# Description     : To create & return the list of words   #
#                   from the input file passed by splitting#
#                   text based on whitespace and dash using#
#                   regex and convert text to lower case   #
# Input           : inFileObj - input file stream object   #
############################################################
def createList(inFileObj):
    wordList=[]
    #for each line in file use split function to split the words
    for lines in inFileObj:
        wordList += split(r'\s|-',lines.lower())
    return wordList

############################################################
# Function Name   : createDictionary                       #
# Description     : To create & return the dictionary of   #
#                   scanned words and its frequency in file#
# Input           : words - list of words                  #
############################################################
def createDictionary(words):
    D={}
    words_updated=[]
    for w in words:
        #w=w.lower()
        #Logic to remove the non-alphabetic characters from the words
        if bool(match('^[a-z";].*[a-z.?,]*$',w)) and w!=" " and not bool(match('^[0-9?,]*$',w)):
            if bool(match('^[a-z]*$',w)):
                w=w
            elif bool(match('^[a-z"]*[.,";]$',w)):
                w=sub('[.,";]$','',w)
                if bool(match('^["].*["]$',w)):
                    w=split('"',w)[1]
            elif bool(match('^[".,;][a-z]*$',w)):
                w=sub('^[".,;]','',w)
            elif bool(match('^["][a-z].*["]$',w)):
                w=sub('^[".,;]','',w)
                w=sub('[".,;]$','',w)
            elif bool(match('^.*[\'$,.;?].*$',w)):
                w=sub('[\'$,.;?].*$','',w)
            words_updated.append(w)
    #create the dictionary for the alphabetic words and there frequency in file
    for word in words_updated:
        D.update({word:words_updated.count(word)})
    return D

#main() function definition
def main():
    #Call to openFiles() functions that get the arguments from the checkArgs() function
    #checkArgs() gets the input and output file passed as argument to script while triggering the script
    fobjects=openFiles(checkArgs())

    #Extract the input file and output file object
    inFileObj=fobjects[0]
    outFileObj=fobjects[1]

    #Call to createList() to create list of the words in the input file passed
    words=createList(inFileObj)

    #Print the data file path for which the words are scanned
    outFileObj.write("\nOutput Values for Data: {0}".format(path.abspath(inFileObj.name)))
    outFileObj.write("\n"+"-"*57)

    #Call to createDictionary() to create dictionary with the words and there frequencies in input file
    Dict=createDictionary(words)

    #Print number of words
    outFileObj.write("\nsize = "+str(len(Dict))+"\n")

    #Write the scanned words into output file (only 3 words in a line)
    sorted_list=sorted(Dict.items())
    j=2
    outFileObj.write("\n")
    for i in range(len(sorted_list)):
        if i%3 != j:
            outFileObj.write("{0:<16}:{1:>3}\t".format(sorted_list[i][0],sorted_list[i][1]))
        else:
            outFileObj.write("{0:<16}:{1:>3}\t".format(sorted_list[i][0],sorted_list[i][1])+"\n")
    outFileObj.write("\n")

    #Close the input and output opened files
    closeFiles(fobjects)

#Call to main() function
main()
