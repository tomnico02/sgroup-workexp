import datetime
import time
from datetime import date
from datetime import time
from time import gmtime, strftime


#All of the users input (name, booking date and times)

name = input("Please enter your name: ")
print("You will now need to enter the date you are booking the meeting room for.")

bookingDay = int(input("Enter the day you are booking: "))
bookingMonth = input("Enter the month you are booking: ")
bookingYear = int(input("Enter the year you are booking: "))


      
monthsOfYear = {
    
    'January':01,
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
    
if bookingMonth in monthsOfYear.values():
    bookingMonth=value
else:
    print("You have incorrectly entered the month you are booking.")

print(bookingMonth)


print("Now you will enter the booking time, please use the following format - 12:30 with 24 hour clock")
startTime = input("Please enter the time the meeting will start: ")
endTime = input("Please enter the time the meeting will end: ")


if endTime < startTime:
    print("You have incorrectly inputted your booking times, ensure that the start date is before the end date.")
else:
    None


#Retrieve current date and time
    
bookingDate = (bookingDay + bookingMonth + bookingYear)
today = date.today()

presentTime = strftime("%H%M", gmtime())
presentDay = float(today.strftime('%d'))
presentMonth = float(today.strftime('%m'))
presentYear = float(today.strftime('%Y'))

startTime2 = startTime.replace(':', '')
endTime2 = endTime.replace(':', '')


#Check to ensure that the booking date is not in the past

if (bookingDay < presentDay):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingMonth < presentMonth):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingYear < presentYear):
    ("The date you have inputted has already occured, please try again.")
    
elif (startTime2 < presentTime):
    ("This time slot has already passed.")
    
else:
    print("The date and time you have selected is available, the meeting room has been booked for you")


#Reading and writing to the text file

f= open("bookings.txt","w+")

f.write(name)
f.write(bookingDate)
f.write(startTime)
f.write(endTime)
f.close()












