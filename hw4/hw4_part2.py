# File: hw4_part2.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Draw a box depending on the users inputs.
 
def main():
    
    #Asks for the users inputs
    widthBox = int(input("Please enter the width of the box: "))
    heightBox = int(input("Please enter the height of the box: "))
    symbolOut = str(input("Please enter a symbol for the box outline: "))
    symbolIn = str(input("Please enter a symbol for the box fill: "))
    
    #If the width or height is 1
    if widthBox == 1 and heightBox == 1:
        print(symbolOut)
    elif widthBox != 1 and heightBox == 1:
        counterTen = 0
        while counterTen < widthBox:
            counterEleven = 0
            while counterEleven < widthBox:
                print(symbolOut, "", end="")
                counterEleven += 1
                counterTen += 1
            print("")
    elif heightBox != 1 and widthBox == 1:
        counterTwelve = 0
        while counterTwelve < heightBox:
            counterThirteen = 0
            while counterThirteen < heightBox:
                print(symbolOut, "")
                counterThirteen += 1
                counterTwelve += 1
            print("")

    #Code for making the box        
    elif widthBox != 1 and heightBox != 1:    
        counterOne = 0
        while counterOne < widthBox:
            counterTwo = 0
            while counterTwo < widthBox:
                print(symbolOut, "", end="")
                counterTwo += 1
                counterOne += 1
        print("")       
        counterTwo = 0
        newHeight = heightBox - 2
    
        while counterTwo < newHeight:
            counterThree = 0
            print(symbolOut, "", end="")
            newWidth = widthBox - 2
            while counterThree < newWidth:
                print(symbolIn, "", end="")
                counterThree += 1
            print(symbolOut, "", end="")
            print("")
            counterTwo += 1
    
        counterFour = 0
        while counterFour < widthBox:
            counterFive = 0
            while counterFive < widthBox:
                print(symbolOut, "", end="")
                counterFive += 1
                counterFour += 1
        print("")       
        print("\n")        

main()
