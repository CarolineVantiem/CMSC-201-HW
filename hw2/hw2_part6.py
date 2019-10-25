# File: hw2_part6.py
# Author: Caroline Vantiem
# Date: 9/19/2017
# Section: 3
# E-mail: cvantie1@umbc.edu
# Description: Asks the user to enter the day of the month, and
#              outputs the correct day of the week.

def main():
   dateNum = str(input("Please enter the day of the month: "))
   if dateNum == "3" or dateNum == "10" or dateNum == "17" or dateNum == "24":
      print("Today is a Sunday!")
   elif dateNum == "4" or dateNum == "11" or dateNum == "18" or dateNum == "25":
      print("Today is a Monday!")
   elif dateNum == "5" or dateNum == "12" or dateNum == "19" or dateNum == "26":
      print("Today is a Tuesday!")
   elif dateNum == "6" or dateNum == "13" or dateNum == "20" or dateNum == "27":
      print("Today is a Wednesday!")
   elif dateNum == "7" or dateNum == "21" or dateNum == "21" or dateNum == "28":
      print("Today is a Thursday!")
   elif dateNum == "1" or dateNum == "8" or dateNum == "15" or dateNum == "22" or dateNum == "29":
      print("Today is a Friday!")
   elif dateNum == "2" or dateNum == "9" or dateNum == "16" or dateNum == "23" or dateNum == "30":
      print("Today is a Saturday!")
   else:
      print("The date", dateNum, "is an invalid date")

main()


