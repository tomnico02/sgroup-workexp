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
    
    "January":1,
    "February":2,
    "March":3,
    "April":4,
    "May":5,
    "June":6,
    "July":7,
    "August":8,
    "September":9,
    "October":10,
    "November":11,
    "December":12
}


temp = (monthsOfYear[bookingMonth])
bookingMonth = temp

#Retrieve current date and time
    

today = date.today()

presentTime = strftime("%H%M", gmtime())
presentDay = float(today.strftime('%d'))
presentMonth = float(today.strftime('%m'))
presentYear = float(today.strftime('%Y'))

if (bookingDay < presentDay):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingMonth < presentMonth):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingYear < presentYear):
    ("The date you have inputted has already occured, please try again.")


print("Now you will enter the booking time, please use the following format\nExample: 00:00 (Using 12 hour clock) ")


userStartTime = input("Please enter the time the meeting will start: ")
userEndTime = input("Please enter the time the meeting will end: ")

clock1 = int(userStartTime[0:1])
clock2 = int(userEndTime[0:1])

if clock1 > 12:
    (clock1)-12

elif clock2 > 12:
    (clock2)-12

else:
    None

minutes1 = int(userStartTime[-1:-2])
minutes2 = int(userEndTime[-1:-2])

startTime = (clock1 + minutes1)
endTime = (clock2 + minutes2)

if endTime < startTime:
    print("You have incorrectly inputted your booking times, ensure that the start date is before the end date.")
else:
    None



#Check to ensure that the booking date is not in the past

if (bookingDay < presentDay):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingMonth < presentMonth):
    ("The date you have inputted has already occured, please try again.")
    
elif (bookingYear < presentYear):
    ("The date you have inputted has already occured, please try again.")
    
elif (startTime < presentTime):
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












