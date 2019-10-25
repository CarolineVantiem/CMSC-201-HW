# File: hw2_part4.py
# Author: Caroline Vantiem
# Date: 9/18/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user what math operation they want to
#              use and outputs the answer.

def main():
    print("You can do many operations with this program: add, subtract, multiply, divide, int divide, mod, and exponents.")
    mathOp = str(input("Which operation do you want to perform? "))
    numOne = float(input("Enter the first number of the operation: "))
    numTwo = float(input("Enter the second number of the operation: "))
    if mathOp == "add":
       print(numOne, "+", numTwo, "=", numOne + numTwo)
    elif mathOp == "subtract":
        print(numOne, "-", numTwo, "=", numOne - numTwo)
    elif mathOp == "multiply":
        print(numOne, "*", numTwo, "=", numOne * numTwo)
    elif mathOp == "divide":
        print(numOne, "/", numTwo, "=", numOne / numTwo)
    elif mathOp == "int divide":
        print(numOne, "//", numTwo, "=", numOne // numTwo)
    elif mathOp == "mod":
        print(numOne, "%", numTwo, "=", numOne % numTwo)
    elif mathOp == "exponents":
        print(numOne, "**", numTwo, "=", numOne ** numTwo)
    else: 
        print("Invalid operation")
main()
