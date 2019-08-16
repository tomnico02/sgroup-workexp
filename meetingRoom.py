import datetime
from datetime import date
import random
import csv

# NEW PROGRAM
# NEW PROGRAM
# NEW PROGRAM

# ----------------------------------------------------------------------------------------------------------------------

global userMonth
global strYear
global time1
global time2
global roomBooked


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
    global fullRoom
    global bookingRef
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

    while (bookingYear < presentYear) or (bookingYear < presentYear) and (bookingMonth < presentMonth) or (bookingYear <= presentYear) and (bookingMonth <= presentMonth) and (bookingDay < presentDay):
        print("Error. The date you have inputted is in the past.")
        bookingDay = int(input("Enter the day you are booking: "))
        userMonth = input("Enter the month you are booking (as a string): ")
        temp = (monthsOfYear[userMonth])
        bookingMonth = temp
        bookingYear = int(input("Enter the year you are booking: "))

    # -------------

    print("Now you will enter the booking time. \nPlease use 24 hour times with [HHMM] or [HMM] format.")
    startTime = int(input("Please enter the time the meeting will start: "))
    endTime = int(input("Please enter the time the meeting will end: "))

    while endTime < startTime:
        print("Now you will enter the booking time. \nPlease use 24 hour times with [HHMM] or [HMM] format.")
        startTime = int(input("Please enter the time the meeting will start: "))
        endTime = int(input("Please enter the time the meeting will end: "))

    while startTime < presentTime and (bookingYear == presentYear) and (bookingMonth == presentMonth) and (bookingDay == presentDay):
        print("--------------------------------------")
        print("Time inputted in the past, you will now start the booking process again.")
        print("--------------------------------------")
        CreateBooking()

    global time1
    global time2

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

    # --------------

    global roomBooked
    hour1 = startTime // 100
    hour2 = endTime // 100
    minutes1 = startTime % 100
    minutes2 = endTime % 100

    while (hour1 >= 24) or (minutes1 > 60) or (hour2 >= 24) or (minutes2 > 60) or (endTime < startTime):
        print("Error. Please input the time again.")
        startTime = int(input("Please enter the time the meeting will start: "))
        endTime = int(input("Please enter the time the meeting will end: "))
        hour1 = startTime // 100
        hour2 = endTime // 100
        minutes1 = startTime % 100
        minutes2 = endTime % 100

    userRoom = int(input("Please choose a meeting room by typing 1-4: "))
    while 1 > userRoom or userRoom > 4:
        userRoom = int(input("Please choose a meeting room by typing 1-4: "))


    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            while bookingDay and userMonth and bookingYear and time1 and time2 and userRoom in row:
                print("That room is already booked for that time, please choose another room.")
                userRoom = int(input("Please choose a meeting room by typing 1-4: "))
    # ----------------

    csv_file = csv.reader(open('bookingLog.csv', "r"), delimiter=",")
    fullRoom = False
    for roomBooked in csv_file:
        bookedDay = roomBooked[1]
        bookedMonth = (monthsOfYear[roomBooked[2].strip()])
        bookedYear = roomBooked[3]
        bookedStartTime = int(roomBooked[4].strip().replace(':', ''))
        bookedEndTime = int(roomBooked[5].strip().replace(':', ''))
        roomBookedName = roomBooked[6]
        if roomBookedName.strip() == userRoom:
            if int(bookedDay) != int(bookingDay):
                continue
            if int(bookedMonth) != int(bookingMonth):
                continue
            if int(bookedYear) != int(bookingYear):
                continue
            if (bookedStartTime >= startTime <= bookedEndTime) or (bookedStartTime <= startTime >= bookedEndTime) or (
                    bookedStartTime >= endTime <= bookedEndTime) or (bookedStartTime <= endTime >= bookedEndTime):
                fullRoom = True
                break
    if fullRoom:
        print("That room is booked out at that time, please choose another room.")

    bookingRef = (random.randint(0, 10000))

    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            while bookingRef in row:
                bookingRef = (random.randint(0, 10000))
                return bookingRef

    booking = [name, bookingDay, userMonth, bookingYear, time1, time2, userRoom, bookingRef]
    with open("bookingLog.csv", "a") as f:
        for item in booking:
            f.write("%s," % item)
        f.write("\n")
    print("--------------------------------------")
    print("Your meeting has successfully been booked.")
    MainMenu()

# ----------------------------------------------------------------------------------------------------------------------
def ViewBooking():
    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if name in row:
                print("--------------------------------------")
                print(
                    "Date booked: " + row[1] + " " + row[2] + " " + row[3] + "\nMeeting Time: " + row[4] + "-" + row[
                        5] + "\nRoom Booked: " + row[6] + "\nBooking Ref Number: " + row[7])
                print("--------------------------------------")
    MainMenu()


# ----------------------------------------------------------------------------------------------------------------------
def DeleteBooking():
    global whichBookingName, input
    global whichBookingDate
    global whichBookingTime
    global whichBookingRoom
    global delRef
    delName = input("Please enter the name of the booking you want to delete: ")
    with open('bookingLog.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if delName in row:
                print("--------------------------------------")
                print(
                    "Date booked: " + row[1] + " " + row[2] + " " + row[3] + "\nMeeting Time: " + row[4] + "-" + row[
                        5] + "\nRoom Booked: " + row[6] + "\nBooking Ref Number: " + row[7])
                print("--------------------------------------")
    delRef = input("Please enter the reference number of the booking you want to delete: ")
    with open("bookingLog.csv", "r") as f:
        data = list(csv.reader(f))
    with open("bookingLog.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            if delRef != row[7]:
                writer.writerow(row)
    print("--------------------------------------")
    print("Booking successfully deleted.\n")
    MainMenu()


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    MainMenu()
    CreateBooking()
    ViewBooking()
    DeleteBooking()

