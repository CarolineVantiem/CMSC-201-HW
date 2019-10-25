# File: hw2_part7.py
# Author: Caroline Vantiem
# Date: 9/19/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user about the state of two switches
#              and outputs if the generator is on or off.


def main():
    print("Pleas eenter 'y' for yes and 'n' for no")
    firstSwitch = str(input("Is the first switch on? (y/n): "))
    secondSwitch = str(input("Is the second switch on? (y/n): "))
    if firstSwitch == 'y' and secondSwitch == 'n' or firstSwitch == 'n' and secondSwitch == 'y':
        print("The generator is on")
    elif firstSwitch == 'y' and secondSwitch == 'y' or firstSwitch == 'n' and secondSwitch == 'n':
        print("The generator is off")
main()


