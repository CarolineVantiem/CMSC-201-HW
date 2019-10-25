# File: hw3_part3.py
# Author: Caroline Vantiem
# Date: 9/26/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user to input the time, and displays the time
#              if the time is not right, asks the user to input a valid time.
def main():
    print("Please enter the time: hours, then minutes, then AM/PM")
    
    hourTime = int(input("Please enter the hour: "))
    while hourTime < 1 or hourTime > 12: 
        if hourTime > 12:
            print("The hours value is too high")
        elif hourTime < 1:
            print("The hours value is too low")
        hourTime = int(input("Please enter the hour: "))
        
    minuteTime = int(input("Please enter the minutes: "))
    while minuteTime < 1 or minuteTime > 59:
        if minuteTime > 59:
            print("The minute value is too high")
        elif minuteTime < 1:
            print("The minute value is too low")
        minuteTime = int(input("Please enter the minute: "))

    timePeriod = str(input("Please enter the time period: "))
    while timePeriod != "AM" and timePeriod != "PM":
        if timePeriod != "AM":
            print("The time period must be 'AM' or 'PM'")
            timePeriod = str(input("Please enter the time period: "))
        elif timePeriod != "PM":
            print("The time period must be 'AM' or 'PM'")
            timePeriod = str(input("Please enter the time period: "))

    print("The time is", hourTime,":",minuteTime, "", timePeriod)  


main()
