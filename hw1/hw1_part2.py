# File: hw1_part1.py
# Author: Caroline Vantiem
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user how much the bill was
# and how many people there were, and calculates how
# much each person needs to pay.

def main():

    totalBill = float(input("How much was your total bill? "))

    totalPeople = int(input("How many people are in your party? "))

    print("Each person in your party needs to pay $", totalBill/totalPeople,)

main()

