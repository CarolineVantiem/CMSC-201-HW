# File: hw6_part2.py
# Author: Caroline Vantiem
# Date: 11/15/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: generates a triangle based 
#              on the users input

####################################################
# recurTri() takes in the height and char and      #
#            returns the right triangle            #
# Input:     height; height of the triangle        #
#            char; the user inputs symbol          #
# Output:    None (the function keeps printing out #
#                  lines of the triangle)          #
####################################################
def recurTri(char, height):
    # BASE CASES #
    if height == 0: 
        print() 
    elif height == 1: # when the height is maxed / 1 #
        print(char * height)
    # RECURSIVE CALL #
    elif height > 1: 
        recurTri(char, height - 1) # recursive call #
        print(char * height) # print triangle #
    
#######################
def main():

    # user input #
    height = int(input("Please enter the height of the triangle: "))
    char = str(input("Please enter the symbol to use: "))
    
    recurTri(char, height) # run recursive function #

main()
