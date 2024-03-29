# File: hw6_part3.py
# Author: Caroline Vantiem
# Date: 11/15/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: counts the number of ears and horns 
#              in a line of horses and unicorns.

##################################################
# count() takes in an integer and counts the     #
#         total number of ears and horns         #
# Input:  numLine; length of the line of equines #
# Output: none                                   #
##################################################
def count(numLine):
    # BASE CASES #
    if numLine == 0:
        return 0 # return total amount when numLine reaches 0
    # RECURSIVE CASES #
    elif numLine % 2 == 0: # if numLine is even #
        return count(numLine - 1) + 2 
    elif numLine % 2 == 1: # if numLine is odd #
        return count(numLine - 1) + 3
               
###################
def main():

    numLine = int(input("How long is the line of equines? ")) # user input #
    
    # print final message #
    print("In a line of", numLine, "equines, there are", count(numLine), "ears and horns.")

main()
