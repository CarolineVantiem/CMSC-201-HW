# File: hw1_part8.py
# Author: Caroline Vantiem 
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie@umbc.edu
# Description: Asks the user how many items of food 
# they want to buy at a fixed price and prints the total
# cost of the meal.

print("Appetizers cost 100")
appCost = int(input("How many appetizers would you like to buy? "))
totalAppCost = (appCost * 100)

print("Main dishes cost 200")
mainCost = int(input("How many main dishes would you like to buy? "))
totalMainCost = (mainCost * 200)

print("Desserts cost 300")
dessertCost = int(input("How many desserts would you like to buy? "))
totalDessCost = (dessertCost * 300)

totalCost = (totalAppCost + totalMainCost + totalDessCost)

print("Your total bill for the meal is", totalCost,)
 
