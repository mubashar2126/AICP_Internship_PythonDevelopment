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

