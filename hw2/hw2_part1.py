# File: hw2_part1.py
# Author: Caroline Vantiem
# Date: 9/18/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user how many days they had left on 
#              their design and project. Outputs a designated 
#              answer depending on the input.

def main():
    
    print("Project 1 has just come out, and you have 6 days to complete the design and 13 days to complete the project")
    
    startDesign = int(input("Days left when you start the design: "))
    startProject = int(input("Days let when you start the project: "))

    if startDesign == 0 or startProject == 0:
        print("Why would you wait so long?! :( ")
    elif startDesign >= 6 and startProject >= 10:
        print("Wow, you started really early! Great job! :)")
    else:
        print("Good luck on the project! You can do it!")

    
main()

