# File: hw5_part2.py
# Author: Caroline Vantiem
# Date: 10/8/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Search for a word in a phrase the user wants to
# find.

############################################################
# inPhrase()  Counts the instances of a word in a string   #
# Input:      aPhrase; a string of the phrase to search in #
#             aWord; a word to search for                  #
# Output:     None                                         #  
############################################################
def inPhrase(aPhrase, aWord):
    #To make the program case insensitive
    if aWord.upper() == aWord:
        aPhrase = aPhrase.upper()
    elif aWord.lower() == aWord:
        aPhrase = aPhrase.lower()
    #Search for the word in the phrase
    counter = 0
    newList = []
    counterOne = 0
    while counter < len(aPhrase):
        if aWord == aPhrase[counter:counter + len(aWord)]:
            newList.append(counterOne)
            counterOne += 1
            #PRINT where the word is at the INDEX
            print("Found", aWord, "at index", counter)
        counter += 1
    print("Found", aWord, "a total of", len(newList), "times")

def main():
    aPhrase = input("Please enter a phrase: ")
    aWord = input("Please enter a word: ")
    while len(aWord) > len(aPhrase):
        print("The word cannot be longer than the phrase")
        aWord = input("Please enter a shorter word to search for: ")
        
    inPhrase(aPhrase, aWord)
main()
