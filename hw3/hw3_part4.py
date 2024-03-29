# File: hw3_part4.py
# Author: Caroline Vantiem 
# Date: 9/27/2017 
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Calculates how much money will be raised for 
#              charity depending on the users input




def main():
    
    pledgeOne = float(input("How many pledges did you secure? "))
    
    while pledgeOne <= 0:
        if pledgeOne <= 0:
            print("Enter a number greater than zero")
            pledgeOne = float(input("How many pledges did you secure? "))
    
    counter = 1
    
    newCounter = 1

    print("For pledge #1")
    pledgeInput = float(input("How much money was pledged? "))
    
    while counter != pledgeOne:
        print("For pledge #", newCounter + 1)
        pledgeOther = float(input("How much money was pledged? "))
        addedValue = pledgeOther
        newCounter = newCounter + 1
        counter = counter + 1
        pledgeInput = pledgeInput + addedValue
       
    runMoney = float(input("How many miles did you run for charity? " ))
    moneyEarned = runMoney * pledgeInput
    runMoney = int(runMoney)

    print("Based on your", runMoney, "miles, you earned $", moneyEarned, " for the charity")


main()    
