import datetime
from datetime import date
import csv

# All of the users input (name, booking date and times)
name = input("Please enter your name: ")

found = False

f = open('bookingLog.csv', 'r')
for line in f:
    if name in line:
        found = True
        bookingYN = input("You already have previous bookings, would you to view them? ")
        if bookingYN == "Yes":
            with open('bookingLog.csv', 'rt') as f:
                reader = csv.reader(f, delimiter=',')
                for row in reader:
                    if name == row[0]:
                        print(
                            "Date booked: " + row[1] + " " + row[2] + " " + row[3] + " Meeting Time: " + row[4] + "-" +
                            row[5])
        else:
            None

print("You will now need to enter the date you are booking the meeting room for.")

# Retrieve current date and time
today = date.today()
dT = datetime.datetime.now()
presentTime = int(dT.strftime("%H%M"))

presentDay = float(today.strftime('%d'))
presentMonth = float(today.strftime('%m'))
presentYear = float(today.strftime('%Y'))

# Makes sure days of month are capped at 31
bookingDay = int(input("Enter the day you are booking: "))
while bookingDay >= 32:
    print("Make sure the day is in range 1-31 and is not in the past.")
    bookingDay = int(input("Enter the day you are booking: "))

# Input booking month
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

# Makes sure the year booked is capped at 2100
bookingYear = int(input("Enter the year you are booking: "))
while bookingYear > 2030:
    print("Make sure the year you inputted is not after 2030 and is not in the past.")
    bookingYear = int(input("Enter the year you are booking: "))


bookingDate = (bookingDay + bookingMonth + bookingYear)

print("Now you will enter the booking time. \nYou can use both 12 or 24 hour times but use '0930' format.")
startTime = int(input("Please enter the time the meeting will start: "))
endTime = int(input("Please enter the time the meeting will end: "))

if endTime < startTime:
    print("You have incorrectly inputted your booking times, ensure that the start date is before the end date.")
else:
    None

meetingRoom = ['room1', 'room2', 'room3', 'room4']
emptyRoom = False
chosenRoom = None
userRoom = input("Please choose a meeting room by typing 1-4: ")

# Makes sure that the users chosen room is not booked already
while not emptyRoom:
    if userRoom == "1":
        csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
        if "room1" in csv_file:
            print("That meeting room is booked, please choose another.")
            empty = False

        else:
            empty = True
            chosenRoom = meetingRoom[0]
            break

    elif userRoom == "2":
        csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
        if "room2" in csv_file:
            print("That meeting room is booked, please choose another.")
            empty = False

        else:
            empty = True
            chosenRoom = meetingRoom[1]
            break

    elif userRoom == "3":
        csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
        if "room3" in csv_file:
            print("That meeting room is booked, please choose another.")
            empty = False

        else:
            empty = True
            chosenRoom = meetingRoom[2]
            break

    elif userRoom == "4":
        csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
        if "room4" in csv_file:
            print("That meeting room is booked, please choose another.")
            empty = False

        else:
            empty = True
            chosenRoom = meetingRoom[3]
            break

else:
    print("All of the rooms are booked out at that time, please choose another time.")
    print("You can use both 12 or 24 hour times but use '0930' format.")
    startTime = int(input("Please enter the time the meeting will start: "))
    endTime = int(input("Please enter the time the meeting will end: "))
    chosenRoom = None
    emptyRoom = False

# Check to ensure that the booking date is not in the past
# Reading and writing to the text file
strDay = str(bookingDay)
strYear = str(bookingYear)

time1 = str(startTime)
time2 = str(endTime)

if len(time1) == 3:
    temp1 = '0' + time1
    temp2 = temp1[:2] + ':' + temp1[2:]
    time1 = temp2
else:
    temp = time1[:2] + ':' + time1[2:]
    time1 = temp

if len(time2) == 3:
    temp1 = '0' + time2
    temp2 = temp1[:2] + ':' + temp1[2:]
    time2 = temp2
else:
    temp = time2[:2] + ':' + time2[2:]
    time2 = temp

booking = [name, strDay, userMonth, strYear, time1, time2, chosenRoom]

with open('bookingLog.csv', mode='a') as csv_file:
    fieldnames = ['Name', 'Day', 'Month', 'Year', 'Meeting Starts', 'Meeting Ends', 'Chosen Room']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
with open("bookingLog.csv", "a") as f:
    for item in booking:
        f.write("%s, " % item)
    f.write("\n")

print("Your meeting has successfully been booked.")
