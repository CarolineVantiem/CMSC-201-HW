# File: hw2_part5.py
# Author: Caroline Vantiem
# Date: 9/19/2017
# Section: 3
# E-mail: Cvantie1@umbc.edu
# Description: Asks the user various questions about dogs
#              and tries to guess the breed depending on the 
#              answers

def main():

    print("Please enter 'yes' or 'no' to these questions")
    
    curlyTail = str(input("Does your dog have a curly tail? "))
    
    if curlyTail == "yes":
        dogBark = str(input("Can your dog bark? "))
        if dogBark == "yes":
           print("Your dog is a Eurasier!")
        elif dogBark == "no":
            print("Your dog is a Basenji!")
    elif curlyTail == "no":
         earsUp = str(input("Do your dogs ear stick up? "))
         if earsUp == "yes":
             print("Your dog is a Pharaoh Hound!")
         elif earsUp == "no":
             multipleColors = str(input("Does your dog come in multiple colors? "))
             if multipleColors == "yes":
                 print("Your dog is a Chesapeake Bay Retriever!")
             elif multipleColors == "no":
                 print("Your dog is a Maremma Sheepdog!")
main()
             
