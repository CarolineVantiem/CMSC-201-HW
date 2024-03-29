# File: hw6_part1.py
# Author: Caroline Vantiem
# Date: 11/14/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Calculates the summation of a number
#              stopping at a second number. 

######################################################
# summation() calculates the summation of the number #
# Input:      numOne; number to sum from             #
#             numTwo; number to sum to               #
# Output:     None (numbers are summed)              #
######################################################
def summation(numOne, numTwo):
    # BASE CASES # 
    if numOne == numTwo - 1: 
        return 0 # return final value #
    # RECURSIVE CALL #
    else:
        return numOne + summation(numOne - 1, numTwo) # summation of numbers #

########################
def main():

    # user input #
    numOne = int(input("Please input the number you want to sum from: "))
    numTwo = int(input("Please input the number you want to sum down to: "))        
    
    # print summation #
    print("The summation from", numOne, "to", numTwo, "is", summation(numOne, numTwo))

main()
