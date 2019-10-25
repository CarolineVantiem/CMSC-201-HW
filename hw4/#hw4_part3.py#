# File: hw4_part3.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Prints out if the list is enrolled perfectly based on how many people
# the user inputs in the class.

#MUST USE LISTS

END = "QUIT"

def main():
    
    studentName = str(input("Please enter a student name ('QUIT' to stop): "))
    
    newList = []
    perfectClass = 8
    counter = 0 
    while studentName != END:
        studentName = str(input("Please enter a student name ('QUIT' to stop): "))
        newList.append(studentName)        
    if len(newList) < perfectClass:
        print("There are", len(newList), "students in the course")
        print("The course is under enrolled!")
    elif len(newList) == perfectClass:
        print("There are", len(newList), "students in the course")
        print("The course is perfectly enrolled!")
    elif len(newList) > perfectClass:
        print("There are", len(newList), "students in the course")
        print("The course is over enrolled!")
        

main()    
    
