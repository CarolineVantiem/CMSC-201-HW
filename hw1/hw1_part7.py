# File: hw1_part7.py
# Author: Caroline Vantiem
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user about their restaurant
# experience and prints out a summary.

rateFood = float(input("How would you rate the food? (1-5) "))

rateService = float(input("How would you rate the service? (1-5) "))

rateAtmosphere = float(input("How would you rate the atmosphere? (1-5) "))

overallRating = ((rateFood + rateService + rateAtmosphere) /3)

print("Your overall experince was", overallRating, "stars")
