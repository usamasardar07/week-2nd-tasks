# ----------- TASK 3 -----------
TotalAmount = 0.0  # INTEGER (FOR TASK 3)
TotalPassengers = 0  # INTEGER
MaxTrain = ""  # STRING (Empty)
MostPassengers = 0  # INTEGER
# DECLARE count : INTEGER //for FOR loops

print("\n")
print(" ------ END OF THE DAY ------ ")
print("\n")
for counti in range(0, 4):
    print(
        "Journey No:",
        counti + 1,
        "\t| Departure Hour:",
        UpTime[counti],
        "\t| Number of passengers:",
        UpPassengers[counti],
        "\t| Total money: $",
        UpMoneyTotal[counti],
        sep="",
    )
    print(
        "Journey No:",
        counti + 1,
        "\t| Return Hour:",
        DownTime[counti],
        "\t| Number of passengers:",
        DownPassengers[counti],
        "\t| Total money: $",
        DownMoneyTotal[counti],
        sep="",
    )
    print("\n-----------------------\n")

for index in range(0, 4):
    TotalPassengers = TotalPassengers + UpPassengers[index]
    TotalAmount = TotalAmount + (UpMoneyTotal[index] * 2)
for count in range(0, 4):
    if UpPassengers[count] > MostPassengers:
        MostPassengers = UpPassengers[count]
        MaxTrain = UpTime[count]
    if DownPassengers[count] > MostPassengers:
        MostPassengers = DownPassengers[count]
        MaxTrain = DownTime[count]


print("Total money earned today: $", TotalAmount, sep="")
print("Total passengers travelled today:", TotalPassengers)
print("The train journey with the highest number of passengers today:", MaxTrain)
input("Press Enter to Exit!")