# File: hw6_part6.py
# Author: Caroline Vantiem
# Date: 11/19/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Generates levels of Pascal's triangle

# CONSTANTS #
MIN_LEVEL = 0 # min level to generate #

#################################################################
# pascal() uses recursion to create each level of Pascal's      #
#          triangle, reaching the requested height              #
# Input:   currLevel; an int, the current level being created   #
#          levelsToMake; an int, the number of levels requested #
#          levelList; a 2D list of ints, containing the levels  #
#          as they are created                                  #
# Output:  None (levelList is changed in place, and the updated #
#          levelList will be the same in main() )               #
#################################################################
def pascal(currLevel, levelsToMake, levelList):
    # BASE CASES #
    if currLevel == levelsToMake:
        return levelList # return list  when done recursion #

    # RECURSIVE CASES #
    if currLevel == 0:
        levelList.append([1]) # append starter 1 #
        return pascal(currLevel + 1, levelsToMake, levelList)
    elif currLevel == 1:
        startList = [ 1 , 1 ]
        levelList.append(startList) # append next row #
        return pascal(currLevel + 1, levelsToMake, levelList)

    startList = [1] # starting level 1 #
    for x in range(len(levelList[currLevel - 1]) - 1):
        # add neighboring two nums #
        startList.append(levelList[currLevel - 1][x] + levelList[currLevel - 1][x + 1])

    startList.append(1) # append 1 at the end of the row #
    levelList.append(startList) # make 2D list #

    return pascal(currLevel + 1, levelsToMake, levelList)

##################
def main():

    print("Welcome to the Pascal's triangle generator.")

    # user input / validation #
    prompt = int(input("Please enter the number of levels to generate: "))
    while prompt <= MIN_LEVEL:
        print("Your number must be positive (greater than zero.)")
        prompt = int(input("Please enter the number of levels to generate: "))

    # pascal function #
    currLevel = 0
    levelsToMake = prompt
    levelList = []

    # + 1 to print out xtra level #
    pascalTriangle = pascal(currLevel, levelsToMake + 1, levelList)

    # print levels of 2D list without brackets #
    for x in range(len(levelList)):
        for y in range(len(levelList[x])):
            print(levelList[x][y], end= " ")
        print("\n")

main()





















