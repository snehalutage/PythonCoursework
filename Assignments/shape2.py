#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 8                       #
# Due Date       : 04/13/2020              #
############################################

#############################################################################################
# File        : shape2.py                                                                   #
# Usage       : Import the module shape2.py in prog8.py and trigger the python script as    #
#               prog8.py                                                                    #
# Description : This program is to implement 2D Geometric Shape Class having various classes#
#               for 2D shapes and methods to find the area and perimeter of the shapes.     #
# Inputs      : NA                                                                          #
# Module      : Inbuilt - math, for sqrt                                                    #
#               User defined - shape, to inherit the Shape class                            #
#############################################################################################

from shape import Shape
from math import pi,sqrt

############################################################
# Class Name      : Rectangle                              #
# Description     : Inherits the Shape class and implements#
#                   the abtract methods to find area and   #
#                   perimeter of rectangle. Also overloads #
#                   the built in functions                 #
############################################################
class Rectangle(Shape):
    
    #Initialiases the paramters and set the default values for length and width to 0
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width

    #Implementation of abstract method area()
    #Calculates the area of rectangle and returns the area
    def area(self):
        return self.length * self.width

    #Implementation of abstract method perimeter()
    #Calculates the perimeter of rectangle and returns the perimeter
    def perimeter(self):
        return 2*(self.length + self.width)

    #Overloads the inbuilt __str__ function to print the rectangle dimensions in required format
    def __str__(self):
        return 'length = {0:.2f} : width = {1:.2f}'.format(self.length,self.width)

    #Overloads the inbuilt __iadd__ function to add the 2 rectangles dimensions(length and width)
    #It returns the Rectangle class object with the updated dimesions 
    def __iadd__(self,other):
        self.length += other.length
        self.width += other.width
        return Rectangle(self.length,self.width)

############################################################
# Class Name      : Circle                                 #
# Description     : Inherits the Shape class and implements#
#                   the abtract methods to find area and   #
#                   perimeter of circle. Also overloads the#
#                   built in functions                     #
############################################################
class Circle(Shape):
    
    #Initialiases the radius and set the default values for radius to 0
    def __init__(self,radius=0):
        self.radius = radius

    #Implementation of abstract method area()
    #Calculates the area of circle and returns the area
    def area(self):
        return (pi * self.radius ** 2)

    #Implementation of abstract method perimeter()
    #Calculates the perimeter of circle and returns the perimeter
    def perimeter(self):
        return (2 * pi * self.radius)

    #Overloads the inbuilt __str__ function to print the circle dimensions in required format
    def __str__(self):
        return 'radius = {0:.2f}'.format(self.radius)

    #Overloads the inbuilt __iadd__ function to add the 2 circles dimensions(radius)
    #It returns the Circle class object with the updated dimesions
    def __iadd__(self,other):
        self.radius += other.radius
        return Circle(self.radius)

############################################################
# Class Name      : Triangle                               #
# Description     : Inherits the Shape class and implements#
#                   the abtract methods to find area and   #
#                   perimeter of triangle. Also overloads  #
#                   the built in functions                 #
############################################################
class Triangle(Shape):

    #Initialiases the dimensions of triangle and set the default values for sides to 0
    def __init__(self,a=0,b=0,c=0):
        self.a = a
        self.b = b
        self.c = c

    #Implementation of abstract method area()
    #Calculates the area of Triangle and returns the area
    def area(self):
        k=self.perimeter()/2 #calculate the value of k by calling perimeter()
        return (sqrt(k*(k-self.a)*(k-self.b)*(k-self.c)))

    #Implementation of abstract method perimeter()
    #Calculates the perimeter of Triangle and returns the perimeter
    def perimeter(self):
        return (self.a + self.b + self.c)

    #Overloads the inbuilt __str__ function to print the Triangle dimensions in required format
    def __str__(self):
        return 'a = {0:.2f} : b = {1:.2f} : c = {2:.2f}'.format(self.a,self.b,self.c)

    #Overloads the inbuilt __iadd__ function to add the 2 triangles dimensions(sides)
    #It returns the Triangle class object with the updated dimesions
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.b
        self.c += other.c
        return Triangle(self.a,self.b,self.c)

############################################################
# Class Name      : Square                                 #
# Description     : Inherits the Rectangle class and       #
#                   overloads the built in functions       #
############################################################
class Square(Rectangle):

    #Initialiases the dimensions of square and set the default value for side to 0
    #Square is special type of rectangle with length = width
    def __init__(self,length=0):
        self.length=length
        self.width=length

    #Overloads the inbuilt __iadd__ function to add the 2 squares dimensions(sides)
    #It returns the Square class object with the updated dimesions
    def __iadd__(self,other):
        self.length += other.length
        self.width += other.length
        return Square(self.length)

    #Overloads the inbuilt __str__ function to print the Square dimensions in required format
    def __str__(self):
        return 'length = {0:.2f}'.format(self.length)

############################################################
# Class Name      : rightTriangle                          #
# Description     : Inherits the Triangle class and        #
#                   overloads the built in functions       #
############################################################
class rightTriangle(Triangle):

    #Initialiases the dimensions of right triangle and set the default values for sides to 0
    #Right triangles are  special type of Triangles with the hypotenuse c calculated from other
    #two sides a and b
    def __init__(self,a=0,b=0):
        self.a=a
        self.b=b
        self.c=sqrt(self.a**2+self.b**2)

    #Overloads the inbuilt __iadd__ function to add the 2 triangles dimensions(sides)
    #It returns the rightTriangle class object with the updated dimesions
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.b
        self.c += sqrt(self.a**2+self.b**2)
        return rightTriangle(self.a,self.b)

    #Overloads the inbuilt __str__ function to print the Triangle dimensions in required format
    def __str__(self):
        return 'length = {0:.2f} : height = {1:.2f}'.format(self.a,self.b)

############################################################
# Class Name      : rightTriangle                          #
# Description     : Inherits the Triangle class and        #
#                   overloads the built in functions       #
############################################################
class equTriangle(Triangle):

    #Initialiases the dimensions of equilateral triangle and set the default values for sides to 0
    #Equilateral triangles are special type of Triangles with all sides equal
    def __init__(self,a=0):
        self.a = a
        self.b = a
        self.c = a

    #Overloads the inbuilt __iadd__ function to add the 2 triangles dimensions(sides)
    #It returns the equTriangle class object with the updated dimesions
    def __iadd__(self,other):
        self.a += other.a
        self.b += other.a
        self.c += other.a
        return equTriangle(self.a)

    #Overloads the inbuilt __str__ function to print the Triangle dimensions in required format
    def __str__(self):
        return 'length = {0:.2f}'.format(self.a)
