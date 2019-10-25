# File: hw1_part5.py
# Author: Caroline Vantiem
# Date: 9/10/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user for a description of
# a restaurant and prints it out.
def main():

    restaurantName = str(input("What is the restaurant's name? "))

    restaurantFood = str(input("What food does the restaurant serve? "))

    restaurantRating = int(input("What is the restaurant's star rating? "))

    print(restaurantName, "is a", restaurantRating, "star restaurant", "serving", restaurantFood)

main()
