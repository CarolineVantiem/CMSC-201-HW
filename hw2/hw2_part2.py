# File: hw2_part2.py
# Author: Caroline Vantiem
# Date: 9/18/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user to input a number and rounds up or
#              down depending on the response. 
 
def main():

    numInput = float(input("Input the number you are rounding: "))
    roundNum = str(input("Do you want to round up or down: "))

    if roundNum == "down":
        print("Original value: ", numInput,)
        numInput = int(numInput)
        roundDown = numInput // 1
        print("Rounding down...")
        print("Rounded Value: ", roundDown,)
    
    elif roundNum == "up":
        print("Original Value: ", numInput,)
        roundUp = (numInput * 10) // 9
        print("Rounding up...")
        roundUp = int(roundUp)
        print("Rounded Value: ",roundUp)

    elif roundNum != "up" or roundNum != "down":    
        print("Invalid input")

main()


>= <=
