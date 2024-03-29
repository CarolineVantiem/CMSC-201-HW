# File: hw4_part4.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Outputs the users highest exam score based on
# how many exams and the scores of those exams.

ZERO_CONSTANT = 0
MAX_GRADE = 100
MIN_GRADE = 0



def main():
    myList = []
    numTest = int(input("Enter the number of tests taken: "))

    #If tests value is negative
    while numTest <= ZERO_CONSTANT:
        if numTest == ZERO_CONSTANT:
            print("")
        elif numTest < ZERO_CONSTANT:
            print("Number of tests cannot be 0.")
            numTest = int(input("Enter the number of tests taken: "))
    print("")
    #Start code for valid test value
    print("For test #1", "", end="")
    extraCred = str(input("was extra credit allowed? " "\n" "Please enter 'yes' or 'no' : "))
    #If extracredit = YES
    if extraCred == "yes":
        firstGrade = int(input("Please enter your grade for the test: "))

        #If test grade is negative
        while firstGrade < MIN_GRADE:
            print("Test grade cannot be negative.")
            firstGrade = int(input("Please enter your grade for the test: "))
        myList.append(firstGrade)
    #If extracredit = NO
    elif extraCred == "no":
        firstGrade = int(input("Please enter your grade for the test: "))

        #If test grade is below 0 or above 100
        while firstGrade > MAX_GRADE or firstGrade < MIN_GRADE:
            print("Test grade must be between 0 and 100")
            firstGrade = int(input("Please enter your grade for the test: "))
        myList.append(firstGrade)

    print("")
    #Ask again
    counter = 1
    newCounter = 1
    while counter != numTest:
        print("For test #", newCounter + 1, "", end="")
        extraCred = str(input("was extra credit allowed? " "\n""Please enter 'yes' or 'no': "))
        #If extracredit = YES
        if extraCred == "yes":
            secondGrade = int(input("Please enter your grade for the\
 test: "))

            #If test grade is negative
            while secondGrade < MIN_GRADE:
                print("Test grade cannot be negative.")
                secondGrade = int(input("Please enter your grade for\
 the test: "))
            myList.append(secondGrade)
        #If extracredit = NO
        elif extraCred == "no":
            secondGrade = int(input("Please enter your grade for th\
e test: "))

            #If test grade is below 0 or above 100
            while secondGrade > MAX_GRADE or secondGrade < MIN_GRADE:
                print("Test grade must be between 0 and 100.")
                secondGrade = int(input("Please enter your grade fo\
r the test: "))
            myList.append(secondGrade)

        counter += 1
        newCounter += 1
        print("\n")
    print("The highest grade received was: ", (max(myList)))
main()






