def main():
    print("Pleas eenter 'y' for yes and 'n' for no")
    firstSwitch = str(input("Is the first switch on? (y/n) "))
    secondSwitch = str(input("Is the second switch on? (y/n) "))
    if firstSwitch == 'y' and secondSwitch == 'n' or firstSwitch == 'n' and secondSwitch == 'y':
        print("The generator is on")
    elif firstSwitch == 'y' and secondSwitch == 'y' or firstSwitch == 'n' and secondSwitch == 'n':
        print("The generator is off")
main()

