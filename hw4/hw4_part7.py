# File: hw4_part7.py
# Author: Caroline Vantiem
# Date: 10/1/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description:
#

END = "STOP"
#If its true add it, if its false dont add it
def main():
    #Boolean Flag
    #Evaluate to True, as long as the item isn't in the list
    grocItem = str(input("Please enter a grocery item ('STOP' to exit): "))
    groceryItem = True
    grocList = []
    while grocItem != END:
        groceryItem = True
        counterThree = 0
        while counterThree < len(grocList):
            if grocList[counterThree] == grocItem:
                groceryItem = False
                print("Error: The item", grocItem, "is already in the list")
            counterThree += 1
        if groceryItem == True:
            grocList.append(grocItem)
        grocItem = str(input("Please enter a grocery item ('STOP' to exit): "))
    

    if grocItem == END:
        counter = 0
        print("")
        print("There are", len(grocList), "groceries in your list: ")            
        while counter < len(grocList):
            counterOne = 0

            print(grocList[0 + counter])
            counterOne += 1
            counter += 1

main()



            

        
