import datetime
from datetime import date
import csv

# NEW PROGRAM
# NEW PROGRAM
# NEW PROGRAM

# ----------------------------------------------------------------------------------------------------------------------

global strDay
global userMonth
global strYear
global time1
global time2
global roomBooked
bookingData = list

# ----------------------------------------------------------------------------------------------------------------------
def MainMenu():
    print("-------{Meeting Booking System}-------")
    print("1. Create New Booking")
    print("2. View My Bookings")
    print("3. Delete Previous Bookings")
    print("4. Exit Program")
    print("--------------------------------------")
    option = input("Please choose an option: ")
    if option == "1":
        global name
        name = input("Please type your name: ")
        CreateBooking()
    elif option == "2":
        name = input("Please type your name: ")
        ViewBooking()
    elif option == "3":
        DeleteBooking()
    elif option == "4":
        exit()
    else:
        MainMenu()

# ----------------------------------------------------------------------------------------------------------------------
def CreateBooking():
    global bookingDay
    global bookingMonth
    global bookingYear
    global bookingDate
    global presentDate
    global bookedDay
    global monthsOfYear
    # Retrieve current date and time
    today = date.today()
    dT = datetime.datetime.now()
    presentTime = int(dT.strftime("%H%M"))
    presentDay = float(today.strftime('%d'))
    presentMonth = float(today.strftime('%m'))
    presentYear = float(today.strftime('%Y'))
    presentDate = ('presentDay' + 'presentMonth' + 'presentYear')

    # Makes sure days are limited 31
    bookingDay = int(input("Enter the day you are booking: "))
    while bookingDay >= 32:
        print("Make sure the day is in range 1-31 and is not in the past.")
        bookingDay = int(input("Enter the day you are booking: "))

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

    # Allows user input month
    userMonth = input("Enter the month you are booking (as a string): ")
    temp = (monthsOfYear[userMonth])
    bookingMonth = temp

    # Makes sure month is limited to 12 months
    while bookingMonth > 12:
        print("Make sure you inputted the date correctly.")
        bookingMonth = int(input("Enter the month you are booking (as a string): "))

    # Makes sure the year is limited to 2030
    bookingYear = int(input("Enter the year you are booking: "))
    while bookingYear > 2030:
        print("Make sure the year you inputted is not after 2030 and is not in the past.")
        bookingYear = int(input("Enter the year you are booking: "))

    bookingDate = ('bookingDay' + 'bookingMonth' + 'bookingYear')

    while (bookingDay < presentDay) and (bookingMonth < presentMonth) and (bookingYear < presentYear) or (bookingYear < presentYear):
        print("Error. The date you have inputted is in the past.")
        bookingDay = int(input("Enter the day you are booking: "))
        bookingMonth = int(input("Enter the month you are booking: "))
        bookingYear = int(input("Enter the year you are booking: "))

    print("Now you will enter the booking time. \nYou can use both 12 or 24 hour but use '0930' format.")
    startTime = int(input("Please enter the time the meeting will start: "))
    endTime = int(input("Please enter the time the meeting will end: "))
    userRoom = input("Please choose a meeting room by typing 1-4: ")

    if endTime < startTime:
        print("You have incorrectly inputted your booking, make sure that the start date is before the end date.")
    roomBooked = False

    csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
    for roomBooked in csv_file:
        bookedDay = roomBooked[1]
        bookedMonth = (monthsOfYear[roomBooked[2].strip()])
        bookedYear = roomBooked[3]
        bookedStartTime = int(roomBooked[4].strip().replace(':', ''))
        bookedEndTime = int(roomBooked[5].strip().replace(':', ''))
        roomBookedName = roomBooked[6]
        if roomBookedName.strip() == userRoom.strip():
            if int(bookedDay) != int(bookingDay):
                continue
            if int(bookedMonth) != int(bookingMonth):
                continue
            if int(bookedYear) != int(bookingYear):
                continue
            if (bookedStartTime >= startTime <= bookedEndTime) or (bookedStartTime <= startTime >= bookedEndTime) or (
                    bookedStartTime >= endTime <= bookedEndTime) or (bookedStartTime <= endTime >= bookedEndTime):
                roomBooked = True
                break
    if roomBooked:
        print("That room is booked out at that time, please choose another room.")
    print("Your meeting has successfully been booked.")

# ----------------------------------------------------------------------------------------------------------------------
def ViewBooking():
    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if name in row:
                print("--------------------------------------")
                print(
                    "Date booked: " + row[1] + " " + row[2] + " " + row[3] + "\nMeeting Time: " + row[4] + "-" + row[5] +"\nRoom Booked: " +row[6])
                print("--------------------------------------")
                print("")
    MainMenu()

# ----------------------------------------------------------------------------------------------------------------------
def DeleteBooking():
    global whichBookingName
    global whichBookingDate
    global whichBookingTime
    global whichBookingRoom
    whichBookingName = input("Please enter the name of the booking you want to delete: ")
    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if whichBookingName in row:
                print("--------------------------------------")
                print(
                    "Date booked: " + row[1] + " " + row[2] + " " + row[3] + "\nMeeting Time: " + row[4] + "-" + row[5] +"\nRoom Booked: " +row[6])
                print("--------------------------------------")
    whichBookingDate = input("Please enter the date of the booking you want to delete: ")
    whichBookingTime = input("Please enter the start time of the booking you want to delete: ")
    whichBookingRoom = input("Please enter the room of the booking you want to delete: ")
    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if whichBookingDate and whichBookingTime and whichBookingRoom in row:
                print("--------------------------------------")
                print(
                    "Date booked: " + row[1] + " " + row[2] + " " + row[3] + "\nMeeting Time: " + row[4] + "-" + row[5] +"\nRoom Booked: " +row[6])
                print("--------------------------------------")
    MainMenu()

# ----------------------------------------------------------------------------------------------------------------------
def StringTime():
    global time1
    global time2
    strDay = str(bookingDay)
    strYear = str(bookingYear)

    time1 = str(bookingData[0])
    time2 = str(bookingData[1])

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

# ----------------------------------------------------------------------------------------------------------------------
def Booking():
    booking = [name, strDay, userMonth, strYear, time1, time2, bookingData[2]]
    with open('bookingLog.csv', mode='a') as csv_file:
        fieldnames = ['Name', 'Day', 'Month', 'Year', 'Meeting Starts', 'Meeting Ends', 'Chosen Room']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    with open("bookingLog.csv", "a") as f:
        for item in booking:
            f.write("%s," % item)
        f.write("\n")

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    MainMenu()
    CreateBooking()
    ViewBooking()
    DeleteBooking()
    StringTime()
    Booking()
