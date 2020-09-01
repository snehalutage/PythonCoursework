#!/usr/bin/python3

############################################
# Name & ZID     : Snehal Utage, Z1888637  #
# Assignment No. : 8                       #
# Due Date       : 04/13/2020              #
############################################

#############################################################################################
# File        : shape3.py                                                                   #
# Usage       : Import the module shape3.py in prog8.py and trigger the python script as    #
#               prog8.py                                                                    #
# Description : This program is to implement 3D Geometric Shape Class having various classes#
#               for 3D shapes and methods to find the area and volume of the shapes         #
# Inputs      : NA                                                                          #
# Module      : Inbuilt - math, for sqrt                                                    #
#               User defined - shape2, to inherit the 2D Shapes Super classes               #
#############################################################################################
from shape2 import *
from math import sqrt

############################################################
# Class Name      : Cube                                   #
# Description     : Class to find area and volume of Cube  #
#                   Inherits the Square class. Implements  #
#                   the abtract methods to find area and   #
#                   volume of cube. Also overloads the     #
#                   built in functions                     #
############################################################
class Cube(Square):

    #Implementation of abstract method area()
    #Calculates the area of Cube and returns the area
    def area(self):
        return 6 * Square.area(self) # 6 * Area of square forming one side of cube

    #Implementation of abstract method volume()
    #Calculates the volume of Cube and returns the volume
    def volume(self):
        return self.length * Square.area(self) #side * Area of square forming side of cube

    #Overloads the inbuilt __iadd__ function to add the 2 cube dimensions(length)
    #It returns the Cube class object with the updated dimesions 
    def __iadd__(self,other):
        self.length += other.length
        self.width += other.length
        return Cube(self.length)

    #Overloads the inbuilt __str__ function to print the Cube dimensions in required format
    def __str__(self):
        return 'length = {0:.2f}'.format(self.length)

############################################################
# Class Name      : Box                                    #
# Description     : Class to find area and volume of Box   #
#                   Inherits the Rectangle class.Implements#
#                   the abtract methods to find area and   #
#                   volume of Box. Also overloads the      #
#                   built in functions                     #
############################################################
class Box(Rectangle):

    #Initialiases the paramters and the default values for length ,width and height to 0
    #Calls Rectangle's __init__ to initialise length and width
    #Adds height attribute
    def __init__(self,length=0,width=0,height=0):
        Rectangle.__init__(self,length,width)
        self.height = height

    #Implementation of abstract method area()
    #Calculates the area of Box and returns the area
    def area(self):
        return 2*Rectangle.area(self) + self.height * Rectangle.perimeter(self) #2*area of rectangle + height of box * perimeter of rectangle

    #Implementation of abstract method volume()
    #Calculates the volume of Box and returns the volume
    def volume(self):
        return self.height * Rectangle.area(self) #height * area of rectangle

    #Overloads the inbuilt __iadd__ function to add the 2 box dimensions(length,width,height)
    #It returns the Box class object with the updated dimesions 
    def __iadd__(self,other):
        self.length += other.length
        self.width += other.width
        self.height += other.height
        return Box(self.length,self.width,self.height)

    #Overloads the inbuilt __str__ function to print the Box dimensions in required format
    def __str__(self):
        return 'length = {0:.2f} : width = {1:.2f} : height = {2:.2f}'.format(self.length,self.width,self.height)

############################################################
# Class Name      : Cylinder                               #
# Description     : Class to find area & volume of Cylinder#
#                   Inherits the Circle class. Implements  #
#                   the abtract methods to find area and   #
#                   volume of Cylinder. Also overloads the #
#                   built in functions                     #
############################################################
class Cylinder(Circle):
    
    #Initialiases the paramters and the default values for radius and height to 0
    #Calls Circle's __init__ to initialise radius
    #Adds height attribute
    def __init__(self,radius=0,height=0):
        Circle.__init__(self,radius)
        self.height = height

    #Implementation of abstract method area()
    #Calculates the area of Cylinder and returns the area
    def area(self):
        return 2*Circle.area(self) + Circle.perimeter(self)*self.height 

    #Implementation of abstract method volume()
    #Calculates the volume of Cylinder and returns the volume
    def volume(self):
        return self.height * Circle.area(self)

    #Overloads the inbuilt __iadd__ function to add the 2 cylinder dimensions(radius and height)
    #It returns the Cylinder class object with the updated dimesions 
    def __iadd__(self,other):
        self.radius += other.radius
        self.height += other.height
        return Cylinder(self.radius,self.height)

    #Overloads the inbuilt __str__ function to print the Cylinder dimensions in required format
    def __str__(self):
        return 'radius = {0:.2f} : height = {1:.2f}'.format(self.radius,self.height)

############################################################
# Class Name      : Cone                                   #
# Description     : Class to find area and volume of Cone  #
#                   Inherits the Circle class. Implements  #
#                   the abtract methods to find area and   #
#                   volume of Cone. Also overloads the     #
#                   built in functions                     #
############################################################
class Cone(Circle):

    #Initialiases the paramters and the default values for radius and height to 0
    #Calls Circle's __init__ to initialise radius
    #Adds height attribute
    def __init__(self,radius=0,height=0):
        Circle.__init__(self,radius)
        self.height = height

    #Implementation of abstract method area()
    #Calculates the area of Cone and returns the area
    def area(self):
        return Circle.area(self) + (1/2 * sqrt(self.radius ** 2 + self.height **2)) * Circle.perimeter(self)

    #Implementation of abstract method volume()
    #Calculates the volume of Cone and returns the volume
    def volume(self):
        return 1/3 * self.height * Circle.area(self)

    #Overloads the inbuilt __iadd__ function to add the 2 cone dimensions(length)
    #It returns the Cone class object with the updated dimesions 
    def __iadd__(self,other):
        self.radius += other.radius
        self.height += other.height
        return Cone(self.radius,self.height)

    #Overloads the inbuilt __str__ function to print the Cone dimensions in required format
    def __str__(self):
        return 'radius = {0:.2f} : height = {1:.2f}'.format(self.radius,self.height)

############################################################
# Class Name      : Sphere                                 #
# Description     : Class to find area and volume of Box   #
#                   Inherits the Circle class. Implements  #
#                   the abtract methods to find area and   #
#                   volume of Circle. Also overloads the   #
#                   built in functions                     #
############################################################
class Sphere(Circle):

    #Implementation of abstract method area()
    #Calculates the area of Sphere and returns the area
    def area(self):
        return 4*Circle.area(self)

    #Implementation of abstract method volume()
    #Calculates the volume of Sphere and returns the volume
    def volume(self):
        return 4/3 * self.radius * Circle.area(self)

    #Overloads the inbuilt __iadd__ function to add the 2 sphere dimensions(radius)
    #It returns the Cube class object with the updated dimesions 
    def __iadd__(self,other):
        self.radius += other.radius
        return Sphere(self.radius)

    #Overloads the inbuilt __str__ function to print the Sphere dimensions in required format
    def __str__(self):
        return 'radius = {0:.2f}'.format(self.radius)

############################################################
# Class Name      : Tetrahedron                            #
# Description     : Class to find area & volume of         #
#                   Tetrahedron. Inherits the equTriangle  #
#                   class. Implements the abtract methods  #
#                   to find area and volume of Box. Also   #
#                   overloads the built in functions       #
############################################################
class Tetrahedron(equTriangle):

    #Implementation of abstract method area()
    #Calculates the area of Tetrahedron and returns the area
    def area(self):
        return 4*equTriangle.area(self)

    #Implementation of abstract method volume()
    #Calculates the volume of Tetrahedron and returns the volume
    def volume(self):
        self.height = sqrt(2/3)*self.a
        return 1/3 * self.height * equTriangle.area(self)

    #Overloads the inbuilt __iadd__ function to add the 2 Tetrahedron dimensions(sides)
    #It returns the Tetrahedron class object with the updated dimesions 
    def __iadd__(self,other):
        self.a += other.a
        return Tetrahedron(self.a)

    #Overloads the inbuilt __str__ function to print the Tetrahedron dimensions in required format
    def __str__(self):
        return 'length = {0:.2f}'.format(self.a)
