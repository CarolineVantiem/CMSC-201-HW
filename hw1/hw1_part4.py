# File: hw1_part4.py
# Author: Caroline Vantiem
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user a number of questions 
# about a new car and calcualtes the price of it.


def main():
    
    carCost = float(input("How much does the car cost? "))

    warrantyCost = float(input("How much does the warranty cost? "))

    fees = float(input("How much do fees cost? "))

    taxes = float(input("How much do taxes cost? "))

    totalCarCost = (carCost + warrantyCost + fees + taxes)

    print("The total cost of the car will be", totalCarCost)

main()
