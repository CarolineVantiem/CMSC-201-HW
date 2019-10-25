# File: hw4_part5.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Checks a pin number from a user and if the pin is correct, then
# outputs the pin

def main():

    pinNum = input("Please enter a PIN: ") #Ask the user for the PIN number
    accType = input("Please enter the account type (c, d, or s): ") #Ask the user for the account type

    pinValid = False
    while not pinValid:
        
        #Checks if the account type is Checking account
        if accType == "c":
            #If the PIN is 4 numbers long AND is valid
            if len(pinNum) == 4:
                if pinNum[0] != "0":
                    if pinNum[-1] != "0":
                        print("Thank you for entering the PIN", pinNum, "for your account")
                        pinValid = True
            #If the PIN is less than 4 numbers. / or
            if len(pinNum) < 4:
                print("The PIN", pinNum, "is too short for a checking account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum , "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum , "cannot end with a zero")
            #If the PIN is greater than 4 numbers. / or
            elif len(pinNum) > 4:
                print("The PIN", pinNum, "is too long for a checking account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum , "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum , "cannot end with a zero")
            #If the PIN length is 4 BUT starts/ends with a 0
            elif len(pinNum) == 4:
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum, "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum, "cannot end with a zero")
            #When PIN is not correct, prompt user to input data AGAIN
            if pinValid == False: 
                pinNum = input("Please enter a PIN: ")
                accType = input("Please enter the account type (c, d, or s): ")
        
        #Checks if the account type is Debit account
        if accType == "d":
            #If the PIN is 4 numbers long AND is valid
            if len(pinNum) == 4:
                if pinNum[0] != "0":
                    if pinNum[-1] != "0":
                        print("Thank you for entering the PIN", pinNum, "for your account")
                        pinValid = True
            #If the PIN is less than 4 numbers
            if len(pinNum) < 4:
                print("The PIN", pinNum, "is too short for a debit account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum , "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum, "cannot end with a zero")
            #If the PIN is greater than 4 numbers
            elif len(pinNum) > 4:
                print("The PIN", pinNum, "is too long for a debit account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum , "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum, "cannot end with a zero")
            #If the PIN is 4 numbers long BUT is not valid
            elif len(pinNum) == 4:
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum, "cannot start with a zero")
                #If the PIN ends with a 0
                if pinNum[-1] == "0":
                    print("Error, the PIN", pinNum, "cannot end with a zero")
            #When the PIN is not correct, prompt user to input AGAIN
            if not pinValid: 
                pinNum = input("Please enter a PIN: ")
                accType = input("Please enter the account type (c, d, or s): ")

        #Checks if the account is Savings account
        if accType == "s":
            #If the PIN is 3 numbers AND is valid
            if len(pinNum) == 3:
                if pinNum[0:1] != pinNum[1:2] and pinNum[2:3] != pinNum[3:4]:
                    if pinNum[0] != "0":
                            print("Thank you for picking", pinNum, "for your account")
                            pinValid = True
            #If the PIN is less than 3 characters
            if len(pinNum) < 3:
                print("The PIN", pinNum, "is too short for a savings account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum, "cannot start with a zero")
            #If the PIN is greater than 3 numbers
            elif len(pinNum) > 3:
                print("The PIN", pinNum, "is too long for a savings account")
                #If the PIN starts with a 0
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum, "cannot start with a zero")
            #If the PIN is 3 numbers long BUT repeats or starts with a 0
            elif len(pinNum) == 3:
                if pinNum[0] == "0":
                    print("Error, the PIN", pinNum, "cannot start with a zero")
                if pinNum[0:1] == pinNum[1:2] and pinNum[1:2] == pinNum[2:3]:
                    print("The PIN", pinNum, "is", len(pinNum), "numbers repeated")
            #When the PIN is not correct, prompt user to input AGAIN
            if not pinValid:
                pinNum = input("Please enter a PIN: ")
                accType = input("Please enter the account type (c, d, or s): ")

main()








