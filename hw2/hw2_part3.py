# File: hw3_part3.py
# Author: Caroline Vantiem
# Date: 9/18/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks what the user ordered, and outputs if there
#              was an invalid response.

def main():
    print("Welcome to the CMSC 201 deli ")
    
    print("Choose 'ham', 'cheese', or 'veggie', for your sandwhich")
    sandwhichOrder = str(input("Please choose a sandwhich: "))
    
    print("Choose 'cookies', 'chips', or 'pickle', for your side")
    sideOrder = str(input("Please choose a side: "))

    print("Choose 'water', 'lemonade', or 'soda', for your drink")
    drinkOrder = str(input("Please choose a drink: "))

    if sandwhichOrder == "ham":
        print("You chose a ham sandwhich")
    elif sandwhichOrder == "cheese":
        print("You chose a cheese sandwhich")
    elif sandwhichOrder == "veggie":
        print("You chose a veggie sandwhich")
    elif sandwhichOrder != "cheese" or sandwhichOrder != "ham" or sandhwhichOrder != "veggie":
        print(sandwhichOrder, "is not a proper meal choice")


    if sideOrder == "cookies":
        print("You chose cookies for your side")
    elif sideOrder == "chips":
        print("You chose chips as your side")
    elif sideOrder == "pickle":
        print("You chose pickle for your side")
    elif sideOrder != "cookies" or sideOrder != "chips" or sideOrder != "pickle":
        print(sideOrder, "is not a proper meal choice")
    

    if drinkOrder == "water":
        print("You chose water as your drink")
    elif drinkOrder == "lemonade":
        print("You chose lemonade as your drink")
    elif drinkOrder == "soda":
        print("You chose soda as your drink")
    elif drinkOrder != "water" or drinkOrder != "lemonade" or drinkOrder != "soda":
        print(drinkOrder, "is not a proper meal choice")

main()
