# File: hw3_part6.py
# Author: Caroline Vantiem
# Date: 9/27/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Creates a box based on the users input of width
#              and height.

def main():

    #Ask the user for the inputs
    widthBox = int(input("Please enter a width: "))
    heightBox = int(input("Please enter a height: "))

    #While loop for the width/ height
    counterValue = 0
    num = 1
    while counterValue < heightBox:
        counterValue += 1
        # PRINTS WIDTH OF BOX
    
        #Loop for height of box
        newCounter = 0
        while newCounter < widthBox:
            print(num, "", end="")
            num += 1
            newCounter += 1
        print("\n")
main()
