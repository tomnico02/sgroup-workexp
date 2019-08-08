
import datetime
from datetime import date
import csv

#All of the users input (name, booking date and times)
name = input("Please enter your name: ")

found = False

f= open('bookingLog.csv', 'r')
for line in f:
    if name in line:
        found = True
        bookingYN = input("You already have previous bookings, would you to view them? ")
        if bookingYN == "Yes":
            with open("bookingLog.csv", 'r') as inp:
                row = csv.reader(inp)
        for i in row:
            if name in i[0]:
                print(i[1:5])


print("You will now need to enter the date you are booking the meeting room for.")

#Retrieve current date and time
today = date.today()
dT = datetime.datetime.now()
presentTime = int(dT.strftime("%H%M"))

presentDay = float(today.strftime('%d'))
presentMonth = float(today.strftime('%m'))
presentYear = float(today.strftime('%Y'))


#Makes sure days of month are capped at 31
bookingDay = int(input("Enter the day you are booking: "))
while (bookingDay >= 32 or bookingDay < presentDay):
    print("Make sure the day is in range 1-31 and is not in the past.")
    bookingDay = int(input("Enter the day you are booking: "))

#Input booking month
userMonth = input("Enter the month you are booking (as a string): ")
# Stores months of the year as numbers so they can be converted
monthsOfYear = {

    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

temp = (monthsOfYear[userMonth])
bookingMonth = temp

while (bookingMonth >12 or bookingMonth > presentMonth):
    print("Make sure the month you entered is correct and is not in the past.")
    bookingMonth = int(input("Enter the day month are booking: "))

#Makes sure the year booked is capped at 2100
bookingYear = int(input("Enter the year you are booking: "))
while (bookingYear > 2100 or bookingYear < presentYear):
    print("Make sure the year you inputted is not after 2100 and is not in the past.")
    bookingDay = int(input("Enter the year you are booking: "))


if (bookingDay < presentDay):
    ("The date you have inputted has already occured, please try again.")
elif (bookingMonth < presentMonth):
    ("The date you have inputted has already occured, please try again.")
elif (bookingYear < presentYear):
    ("The date you have inputted has already occured, please try again.")



bookingDate = (bookingDay + bookingMonth + bookingYear)

print("Now you will enter the booking time. \nYou can use both 12 or 24 hour times but use '0930' format.")
startTime = int(input("Please enter the time the meeting will start: "))
endTime = int(input("Please enter the time the meeting will end: "))

if endTime < startTime:
    print("You have incorrectly inputted your booking times, ensure that the start date is before the end date.")
else:
    None


#Check to ensure that the booking date is not in the past
#Reading and writing to the text file
strDay = str(bookingDay)
strYear = str(bookingYear)
strTime1 = str(startTime)
strTime2 = str(endTime)

if (startTime < presentTime):
    ("This time slot has already passed.")

elif (bookingDay < presentDay):
    ("Error. You are trying to book a date in the past.")

elif (userMonth < bookingMonth):
    ("Error. You are trying to book a date in the past.")

elif (bookingYear < presentYear):
    ("Error. You are trying to book a date in the past.")

else:
    booking = [name, strDay, userMonth, strYear, strTime1, strTime2]

    with open('bookingLog.csv', mode='a') as csv_file:
        fieldnames = ['Name', 'Day', 'Month', 'Year', 'Meeting Starts', 'Meeting Ends']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    with open("bookingLog.csv", "a") as f:
        for item in booking:
            f.write("%s," % item)


#while (emptySlot != True):
 #   break
  #  if bookingDate:
   #     emptySlot = True
    #elif startTime:
     #   emptySlot = True
    #elif endTime:
        #emptySlot = True

