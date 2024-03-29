# File: hw5_part1.py
# Author: Caroline Vantiem
# Date: 10/8/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user for a string and a letter 
# and ouputs how many there are of the specified letter.

############################################################
# numLetter() counts the instances of a letter in a string #
# Input:      aString; a string of the phrase to search in #
#             letter; a single character to search for     #
# Output:     None                                         #
############################################################
def numLetter(aString, letter):
    #Case insensitive
    if letter == letter.lower():
        aString = aString.lower()
    elif letter == letter.upper():
        aString = aString.upper()
    #Checks if the letter is in the word
    counter = 0
    newList = []
    counterOne = 0
    while counter < len(aString):
        if letter == aString[counter:counter + len(letter)]:
            newList.append(counterOne)
            counterOne += 1
        counter += 1
    print("There are", len(newList), "instances of", letter, "in the string")

def main():
    #Asks the user for the strings
    aString = input("Enter a string: ")
    letter = input("Enter a letter to search for: ")
    numLetter(aString, letter)
main()






