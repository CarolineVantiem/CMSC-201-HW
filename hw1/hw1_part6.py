# File: hw1_part6.py
# Author: Caroline Vantiem
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user about a meal and prints
# out the total cost of it.

def main():
    bill = float(input("How much was the bill? "))

    tax = float(input("How much is tax in your area? "))

    tipPercent = float(input("What percent do you want to tip? "))

    tipP = ((tipPercent / 100)*bill)

    tip = (bill*(tax)/100)

    totalCost = (tip + tipP + bill)

    print("The total cost of the meal will be", totalCost,)

main()

