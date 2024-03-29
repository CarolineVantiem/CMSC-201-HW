# File: hw4_part6.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Outputs the time and task the user inputs.

#MUST USE LISTS

END = "END"

def main():

    taskName = input("Please enter a task, or 'END' to stop: ")

    taskList = []
    hoursList = []
    while taskName != END:
        taskList.append(taskName)
        taskHours = input("Please enter the hour(s) needed to complete it: ")
        hoursList.append(taskHours)
        taskName = input("Please enter a task, or 'END' to stop: ")
    if taskName == END:
        counter = 0
        print("\n")
        print("Here is your task list:")
        while counter < len(taskList):
            counterOne = 0
            print(hoursList[0 + counter], "", end="")
            print("hours to complete: ", "", end="")
            print(taskList[0 + counter])
            counter += 1
            counterOne += 1

main()
