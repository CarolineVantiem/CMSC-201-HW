# File: hw3_part2.py
# Author: Caroline Vantiem
# Date: 9/25/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Calculate an answer to an exponentiation problem
#              without using exponentiation.

def main():
   
    #Ask the user for the input of the first base
    numOne = int(input("Please enter the first number: "))
    #Second number- power of
    numTwo = int(input("Please enter the second number: "))

    
    #Raising anything to the 0 power = 1    
    if numTwo == 0:
        print(numOne, "**", numTwo, "=", "1")
    
    #Start the while loop, counter for multiplying first number by itself
    counter = 0
    while counter != numTwo:
        newValue = numOne * numOne
        counter += 2
        #Multiply through if counter still doesnt equal second num
        while counter != numTwo:
            newValue *= numOne
            counter += 1
        print(numOne, "**", numTwo, "=", newValue)

main()


        
        
