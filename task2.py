# ----------- TASK 2 -----------
NumOfPassengers = UpTrip = DownTrip = FreeTickets = 0  # INTEGER
OneWayTicket = 25.0  # CONSTANT
OneWayCost = 0.0  # REAL
# DECLARE num : INTEGER //for FOR loops


choice = input("Do you want to buy ticket(s)? Enter True or False: ")
while choice != "True" and choice != "False":
    choice = input("Invalid Input! Enter True or False: ")

while choice != "False":
    print("\n-----------------------\n")
    #
    UpTrip = int(input("Enter Journey number for your chosen departure hour: ")) - 1
    while UpTrip not in range(0, 4):
        UpTrip = int(input("Error! Enter Journey number from (1, 2, 3, 4): ")) - 1
    #
    print("\n----- Return Hours Available -----\n")
    for num in range(UpTrip, 4):
        print(
            "Journey No:",
            num + 1,
            " | Return Hour:",
            DownTime[num],
            " | Remaining Tickets:",
            DownSeats[num],
        )
    print()
    DownTrip = int(input("Enter Journey number for your chosen Return hour: ")) - 1
    while DownTrip < UpTrip or DownTrip > 3:
        DownTrip = (
            int(input("Error! Enter Journey number from the given list above: ")) - 1
        )
    #
    print()
    NumOfPassengers = int(input("Enter number of passengers for trip: "))
    while NumOfPassengers <= 0:
        NumOfPassengers = int(input("Error! Enter number greater than 0: "))

    if NumOfPassengers > UpSeats[UpTrip] or NumOfPassengers > DownSeats[DownTrip]:
        print("\n####################\n")
        print("Seats not available for chosen hours")
        print("Please check the display below for available Seats =>")

    else:
        print("\n//// Seats Booked ////")
        if NumOfPassengers >= 10 and NumOfPassengers <= 80:
            FreeTickets = NumOfPassengers // 10
        else:
            FreeTickets = 0
        OneWayCost = (NumOfPassengers - FreeTickets) * OneWayTicket
        print("Total price for two-way journey: $", OneWayCost * 2, sep="")
        #
        UpPassengers[UpTrip] = UpPassengers[UpTrip] + NumOfPassengers
        UpSeats[UpTrip] = UpSeats[UpTrip] - NumOfPassengers
        UpMoneyTotal[UpTrip] = UpMoneyTotal[UpTrip] + OneWayCost
        #
        DownPassengers[DownTrip] = DownPassengers[DownTrip] + NumOfPassengers
        DownSeats[DownTrip] = DownSeats[DownTrip] - NumOfPassengers
        DownMoneyTotal[DownTrip] = DownMoneyTotal[DownTrip] + OneWayCost

    ScreenDisplay()  # CALL PROCEDURE
    print("Do you want to buy ticket(s)? Enter True or False")
    choice = input()
    while choice != "True" and choice != "False":
        choice = input("Invalid Input! Enter True or False: ")