# File: hw5_part5.py
# Author: Caroline Vantiem 
# Date: 10/10/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Prints out a list of words in reverse order and backwards
# depending on what words the user inputs into the list.

#######################################################
# backwards() reverses a string and prints the result #
# Input:      forString, a string to reverse          #
# Output:     None                                    #
#######################################################
def backwards(forString):
    #Each single word  gets printed backwards
    counter = 0
    newIndex = len(forString) - 1
    newString = ""
    while counter < len(forString):
        newString = newString + forString[newIndex]
        newIndex = newIndex - 1
        counter += 1
    print("The string", "'", forString , "'", "reversed is", "'", newString, "'")

        
def main():
    wordsIn = int(input("How many words would you like to turn backwards: "))
    counter = 0
    cOne = 1
    newList = [] 
    while counter < wordsIn:
        forString = input("Please enter string #" + str(cOne) + ": ") 
        cOne += 1
        newList.append(forString)
        counter += 1
    #Sends each word into the function starting from the end of the list.
    cTwo = 0
    cThree = 0
    while cTwo < len(newList):
        backwards(newList[cThree - 1])
        cThree -= 1
        cTwo += 1

main()
