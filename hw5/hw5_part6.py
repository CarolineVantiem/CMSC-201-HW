# File: hw5_part6.py
# Author: Caroline Vantiem
# Date: 10/10/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Calculate the average value of temperatures 
# inputed by the user

########################################################
# average() calculates and returns the average         #
# Input:    numList; a list of floats                  #
# Output:   avgNum; a float, average of list's numbers #
########################################################
def average(numList):
    #Calculates the sum of the list
    sumOne = 0
    counter = 0
    cOne = 0
    while counter < len(numList):
        sumOne = sumOne + numList[cOne]
        cOne += 1
        counter += 1
    #Calculates avgNum/ returns value
    avgNum = sumOne / len(numList)
    return avgNum

    
END = "STOP"
def main():
    aTemp = input("Enter a temperature, 'STOP' to exit: ")
    numList = []
    while aTemp != END:
        #Turns str into float, if user doesn't enter STOP
        aTemp = float(aTemp)
        numList.append(aTemp)
        average(numList)
        aTemp = input("Enter a temperature, 'STOP' to exit: ")
    average(numList)
    print("The average is", average(numList))    
main()
    
