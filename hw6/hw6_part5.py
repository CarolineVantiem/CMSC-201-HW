# File: hw6_part5.py
# Author: Caroline Vantiem
# Date: 11/15/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Generates levels of Pascal's Triangle

# CONSTANTS #
MIN_LEVEL = 0 # min number of levels #

#################################################################
# pascal() creates each level of Pascal's                       #
#          triangle, reaching the requested height              #
# Input:   levelsToMake; an int, the number of levels requested #
# Output:  None (the levels are printed from the function)      #
#################################################################
def pascal(levelsToMake):
    newList = [1] # starting list # 
    print("1", "\n") # first 1 #

    # starting triangle #
    for x in range(levelsToMake):
        otherList = []
        otherList.append(newList[0]) # append 1 #
        
        # numbers for inner triangle #
        for x in range(len(newList) - 1):
            otherList.append(newList[x] + newList[x+1]) # add neighboring two numbers #
        otherList.append(newList[-1]) # append last num in list #
        newList = otherList
        
        # to print triangle without brackets #
        for x in range(len(newList)):
            print(newList[x], end=" ") # prints number in the same sequence on same line # 
        print("\n")

#####################
def main():

    print("Welcome to Pascal's Triangle generator.") # welcome message #

    # user input / validation #
    levelsToMake = int(input("Please enter the number of levels to generate: "))
    while levelsToMake <= MIN_LEVEL:
        print("Your number must be positive (greater than zero).")
        levelsToMake = int(input("Please enter the number of levels to generate: "))

    pascal(levelsToMake) # run pascal triangle #
    
main()
