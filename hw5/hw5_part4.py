# File: hw5_part4.py
# Author: Caroline Vantiem 
# Date: 10/10/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Checks if a number is odd/even, or if its positive 
# and if its divisible by a number the user chooses.


EVEN_NUM = 0
ODD_NUM = 1
EVENODD_NUM = 2
##########################################################
# checkOddOrEven() prints if the given number            #
#                 is odd or even                         #
# Input:          userNum; an integer chosen by the user #
# Output:         None                                   #
##########################################################
def checkOddOrEven(userNum):
    #Num EVEN if % 2 = 0
    if userNum % EVENODD_NUM == EVEN_NUM:
        print(userNum, "is even")
    elif userNum % EVENODD_NUM == ODD_NUM:
        print(userNum, "is odd")


ZERO_NUM = 0
##########################################################
# checkPositive() prints if the given number             #
#                 is positive, negative, or zero         #
# Input:          userNum; an integer chosen by the user #
# Output:         None                                   #
##########################################################
def checkPositive(userNum):
    #If user enters zero, prompts 'zero is zero'
    if userNum == ZERO_NUM:
        print(userNum, "is zero")
    elif userNum > ZERO_NUM:
        print(userNum, "is positive")
    elif userNum < ZERO_NUM:
        print(userNum, "is negative")
DIV_NUM = 0
################################################################
# checkDivisible() prints if the given number                  #
#                  is divisible by the number the user chooses #
# Input:           userNum; an integer chosen by the user      #
#                  divNum; integer chosen by user to divide by # 
# Output:          None                                        #
################################################################
def checkDivisible(userNum, divNum):
    #Divide the num by divNum
    newNum = userNum % divNum
    if newNum != DIV_NUM:
        print(userNum, "is not divisible by", divNum)
    else:
        print(userNum, "is divisible by", divNum)


def main():
    #Ask the user for the inital num
    userNum = int(input("Enter the number you would like to check: "))
    #Call function even-odd/positive
    checkOddOrEven(userNum)
    checkPositive(userNum)
    #Asks the user for num divisible. Send divNum in div FUNCTION
    divNum = int(input("Enter number to divide by: "))
    checkDivisible(userNum, divNum)

main()
