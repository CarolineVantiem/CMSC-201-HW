# File: hw6_part4.py
# Author: Caroline Vantiem
# Date: 11/15/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: asks the user for a word and checks 
#              to see if that word is a palindrome

#########################################################
# reverseStr() takes in a word and returns it backwards #
# Input:       word; the word the user chooses to check #
# Output:      string in reverse order                  #
######################################################### 
def reverseStr(word):
    # BASE CASE #
    if word == "":
        return word # return word backwards #
    # RECURSIVE CALL #
    else:
        return reverseStr(word[1:]) + word[0] # recursive function / returns backwards

#############################################################
# palindromeness() takes in a word and checks if            #
#                  its a palindrome                         #
# Input:           word; the word the user chooses to check #
# Output:          none                                     #
#############################################################
def palindromeness(word):
    # appends word #
    newList = []
    counter = 0
    counterOne = 0
    while counter < len(word):
        newList.append(word[counterOne])
        counterOne += 1
        counter += 1
    
    # appends word backwards #
    otherList = []
    counter = 0
    counterOne = -1
    while counter < len(word):
        otherList.append(word[counterOne])
        counterOne -= 1
        counter += 1

    # check if the word is a palindrome #
    if newList == otherList:
        palindrome = 0
    else:
        palindrome = 1
    return palindrome 
    
##################### 
def main():

    # user input #
    word = str(input("Please enter a word to check for palindrome-ness: "))

    # check if the word is a palindrome #
    palindromeValid = palindromeness(word)
    
    if palindromeValid == 0: # if word IS a palindrome
        print("The word", word,"IS a palindrome.")
    elif palindromeValid == 1: # if word is NOT a palindrome
        palindromeWord = reverseStr(word) # run recursive function #
        print("Sorry, the word", word, "is NOT a palindrome.")
        print("Backwards, it becomes", palindromeWord + ".") 

main()


