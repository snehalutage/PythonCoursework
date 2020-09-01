#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 7                       #
# Due Date       : 04/02/2020              #
############################################

#############################################################################################
# File        : rational.py                                                                 #
# Usage       : Import the module rational.py in prog7.py and trigger the python script as  #
#               prog7.py < prog7.d                                                          #
# Description : This program is to implement Rational Numbers Class having various methods  #
#               overloaded to perform operations on rational numbers. It reads the input    #
#               from prog7.d and throws error for incorrect rational number                 #
# Inputs      : From file prog7.d                                                           #
# Module      : Inbuilt - sys, for the stderr                                               #
#############################################################################################
from sys import *


class Rational:
    """ Define the Rational class """
    
    def __init__(self,num=0,den=1):
        """__init__() method - Initialise the numerator and denominator of Rational number"""
        if den == 0:
            stderr.write("Error: invalid rational number: 5/0\n")
        self.num=num
        self.den=den
        if num != 0 and den !=0:
            #Take gcd to reduce the rational number to lowest terms
            res=self.gcd(num,den)
            self.num//=res
            self.den//=res

    def gcd(self,num,den):
        """gcd() method - Returns the gcd of the numbers passed"""
        while (den) :
            num,den=den,num%den
        return num

    def __str__(self):
        """__str__() method - Overloads the __str__ method to print the Rational number in format num / den """
        if self.den == 1 or self.num == 0:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
        
    def __float__(self):
        """__float__() method - Overloads the __float__ method to print float value of Rational number"""
        if self.den == 1 or self.num == 0:
            return float(self.num)
        else:
            return self.num/self.den

    def __add__(self,other):
        """__add__ method - Overloads the operator '+' to add two Rational numbers"""
        num = self.num * other.den + self.den * other.num
        den = self.den * other.den
        return Rational(num,den)

    def __sub__(self,other):
        """__sub__ method - Overloads the operator '-' to subtract two Rational numbers"""
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return Rational(num,den)

    def __mul__(self,other):
        """__mul__ method - Overloads the operator '*' to multiply two Rational numbers"""
        num=self.num * other.num
        den=self.den * other.den
        return Rational(num,den)

    def __truediv__(self,other):
        """__truediv__ method - Overloads the operator '/' to divide two Rational numbers"""
        num=self.num * other.den
        den=self.den * other.num
        return Rational(num,den)

    def __eq__(self,other):
        """__eq__ method - Overloads the relational operator '==' to compare two Rational numbers"""
        if self.num == other.num and self.den == other.den :
            return True
        else:
            return False

    def __ne__(self,other):
        """__ne__ method - Overloads the relational operator '!=' to compare two Rational numbers"""
        if self.num == other.num and self.den == other.den :
            return False
        else:
            return True

    def __lt__(self,other):
        """__lt__ method - Overloads the relational operator '<' to compare two Rational numbers"""
        num1=self.num * other.den
        den1=self.den * other.den
        num2=other.num * self.den
        den2=other.den * self.den
        if num1 < num2 :
            return True
        else:
            return False
        
    def __le__(self,other):
        """__le__ method - Overloads the relational operator '<=' to compare two Rational numbers"""
        num1=self.num * other.den
        den1=self.den * other.den
        num2=other.num * self.den
        den2=other.den * self.den
        if num1 < num2 or num1 == num2:
            return True
        else:
            return False

    def __gt__(self,other):
        """__gt__ method - Overloads the relational operator '>' to compare two Rational numbers"""
        num1=self.num * other.den
        den1=self.den * other.den
        num2=other.num * self.den
        den2=other.den * self.den
        if num1 > num2 :
            return True
        else:
            return False

    def __ge__(self,other):
        """__ge__ method - Overloads the relational operator '>=' to compare two Rational numbers"""
        num1=self.num * other.den
        den1=self.den * other.den
        num2=other.num * self.den
        den2=other.den * self.den
        if num1 > num2 or num1 == num2:
            return True
        else:
            return False

    def __neg__(self):
        """__neg__ method - Overloads the negation operator '-' to negate the value  of Rational number"""
        if self.den < 0:
            num=-self.num
            den=-self.den
        num=-self.num
        den=self.den
        return Rational(num,den)

    def read():
        """read() method - Used the readline() to read the Rational numbers from stdin and print error if invalid Rational number"""
        line=stdin.readline()
        while line:
            l=line.strip().split("/")
            if len(l) == 2:
                for i in l:
                    if i.isnumeric():
                        stderr.write("Error: invalid rational number: "+line.strip()+"\n")
                        return " "
                return Rational(int(l[0].strip()),int(l[1].strip()))
            elif len(l) == 1:
                if l[0].isnumeric():
                    return Rational(int(l[0].strip()))
                else:
                    stderr.write("Error: invalid rational number: "+line.strip()+"\n")
                    return " "
            line=stdin.readline()
