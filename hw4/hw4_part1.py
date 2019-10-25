# File: hw4_part1.py
# Author: Caroline Vantiem
# Date: 10/1/2017 
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user for two integers and creates a modtable.

def main():
    
    #Asks the user for the input
    numOne = int(input("Please enter the number to mod by: "))
    numTwo = int(input("Please enter how high you'd like to go: "))

    #Start while loop 
    counter = -1
    counterOther = 0
    while counter < numTwo:
            modAns = (counterOther % numOne)
            print(counter + 1, "%", numOne, "=", modAns)
            counter += 1
            counterOther += 1
main()
