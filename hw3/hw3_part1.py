# File: hw3_part1.py
# Author: Caroline Vantiem
# Date: 9/24/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user to input the starting input for
#              hail and outputs the up and down movement of the
#              storm.

def main():
    #Ask the user for the starting height
    startHeight = int(input("Please enter the starting height of the hailst\
one: "))
    #If the height is 0 or 1 it stops
    if startHeight == 0 or startHeight == 1:
        print("Hail stopped at height: ", startHeight,)
    else:
        print("Hail is currently at height: ",startHeight,)
    #Print the starting height
     
    
    #All heights are current height
    currentHeight = startHeight
    
    #While the current height is not 0 or 1
    while currentHeight != 0 and currentHeight != 1:
        #Check if the curren height is even or odd. Even(0) Odd(1)
        checkHeight = currentHeight % 2
        #Print the starting height
        #While the current height is even
        if checkHeight == 0:
            currentHeight = currentHeight / 2
            if currentHeight == 0 or currentHeight == 1:
                print("Hail has stopped at height: ", currentHeight,)
            else:    
                print("Hail is currently at height: ",currentHeight,)
        #If current height is odd
        elif checkHeight == 1:
            currentHeight = ((currentHeight * 3) + 1)
            if currentHeight == 0 or currentHeight == 1:
                print("Hail has stopped at height: ", currentHeight,)
            else:    
                print("Hail is currently at height: ", currentHeight,)
main()
