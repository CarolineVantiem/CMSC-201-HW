# File: hw3_part5.py
# Author: Caroline Vantiem
# Date: 9/27/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Outputs a response based on if the number is 
#              divisible by 4 or 5, or both.
def main():
    
    num = 1
    
    while num <= 77:
        if num % 4 == 0 and num % 5 == 0:
            print("The year 2020 is coming soon!")
        elif num % 5 == 0:
            print("Where do you see yourself in five years?")
        elif num % 4 == 0:
            print("Four leaf clovers are lucky!")
        else:
            print(num)
        num += 1
main()














