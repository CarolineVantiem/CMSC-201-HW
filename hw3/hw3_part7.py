#File: hw3_part7.py
#Author: Caroline Vantiem
#Date: 9/29/2017
#Section: 3
#E-mail: cvantie1@umbc.edu
#Description: Asks the user to give the height of a triangle and a character, 
#             and the program prints out a right triangle of the character. 



def main():

    heightNum = int(input("Please enter the height of the trian\
gle: "))
    symbolNum = str(input("Please enter a single character for \
the triangle: "))

    if heightNum == 0:
        print("")

    
    counterNew = 0
    addSymbol = ("")
    addSymbol = addSymbol
    while counterNew != heightNum:
        counterNew += 1
        addSymbol += symbolNum
        print(addSymbol)
main()

