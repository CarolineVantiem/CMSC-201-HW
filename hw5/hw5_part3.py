# File: hw5_part3.py
# Author: Caroline Vantiem
# Date: 10/10/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Checks the punctuation and capitilization of a sentence.

#############################################################################
# checkCapital() Checks to see if the sentence starts with a capital letter #
# Input:         aSent; the sentence the user enter                         #
# Output:        Whether or not the sentence begins with a capital letter   #
#############################################################################
def checkCapital(aSent):
    #Checks the first INDEX of the word
    firstSent = aSent[0:1]
    if firstSent != firstSent.upper():
        print("WRONG - Sentences start with a capital letter.")
    elif firstSent == firstSent.upper():
        print("Correct capitalization!")

####################################################################
# checkPunctuation() Checks to see if the sentence has punctuation #
# Input:             aSent; to checkfor punctuation                #
# Output:            Whether or not the sentence has punctuation   #
####################################################################
def checkPunctuation(aSent):
    #Checks the last INDEX of the word
    lastSent = aSent[len(aSent) - 1]
    if lastSent != "." and lastSent != "!" and lastSent != "?":
        print("WRONG - Sentences use punctuation.")    
    elif lastSent == "." or lastSent == "!" or lastSent == "?":
        print("Correct punctuation!")

END = ""
def main():
    aSent = input("Enter a sentence (Enter nothing to quit): ")
    #Prompts the user to keep entering until nothing is entered 
    while aSent != END:
        checkCapital(aSent)
        checkPunctuation(aSent)
        aSent = input("Enter a sentence (Enter nothing to quit): ")
main()

