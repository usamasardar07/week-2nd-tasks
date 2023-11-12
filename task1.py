# ------ TASK 1 ------

# DECLARE index : INTEGER //for FOR loop
UpTime = ["09:00", "11:00", "13:00", "15:00"]  # ARRAY STRING
UpSeats = [480, 480, 480, 480]  # ARRAY INTEGER
UpPassengers = [0, 0, 0, 0]  # ARRAY INTEGER
UpMoneyTotal = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL

DownTime = ["10:00", "12:00", "14:00", "16:00"]  # ARRAY STRING
DownSeats = [480, 480, 480, 640]  # ARRAY INTEGER
DownPassengers = [0, 0, 0, 0]  # ARRAY INTEGER
DownMoneyTotal = [0.0, 0.0, 0.0, 0.0]  # ARRAY REAL


def ScreenDisplay():  # DECLARING PROCEDURE
    print("\n\t>>>>>>>     TRAIN JOURNEY DISPLAY     <<<<<<<\n")
    for index in range(0, 4):
        if UpSeats[index] != 0:
            print(
                "Journey No:",
                index + 1,
                "| Departure Hour:",
                UpTime[index],
                "\t| Tickets available:",
                UpSeats[index],
            )
        else:
            print(
                "Journey No:",
                index + 1,
                "| Departure Hour:",
                UpTime[index],
                "\t| Closed!",
            )

        if DownSeats[index] != 0:
            print(
                "Journey No:",
                index + 1,
                "| Return Hour:",
                DownTime[index],
                "\t| Tickets available:",
                DownSeats[index],
            )
        else:
            print(
                "Journey No:",
                index + 1,
                "| Return Hour:",
                DownTime[index],
                "\t| Closed!",
            )
        print()
        print("-----------------------\n")


# ENDPROCEDURE

ScreenDisplay()  # CALL PROCEDURE
