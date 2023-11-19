#21-cp-26 Ibrahim
# Source data (matrix)
units_matrix = [
    [55, 65, 75],
    [1120, 150, 230],
    [1, 170, 210, 240]
]

# Student ID
student_id = "XY12345678"

# Function to calculate and display cost for slab 1
def costSlab1():
    print("Bill for Slab 1 is")
    for units in units_matrix[0]:
        cost = units * 10  # Each unit costs Rs.10 in slab 1
        print(cost, end=" ")
    print()

# Function to calculate and display cost for slab 2
def costSlab2():
    print("Bill for Slab 2 is")
    for units in units_matrix[1]:
        cost = units * 15  # Each unit costs Rs.15 in slab 2
        print(cost, end=" ")
    print()

# Function to calculate and display cost for slab 3
def costSlab3():
    print("Bill for Slab 3 is")
    for units in units_matrix[2]:
        cost = units * 20  # Each unit costs Rs.20 in slab 3
        print(cost, end=" ")
    print()

# Main menu loop
while True:
    print(f"My Student ID is {student_id}\n")
    print("Enter your choice:")
    print("Press 1 to display the bill of slab 1 and slab 2.")
    print("Press 2 to display the bill of slab 3.")
    print("Press any other key to exit.")

    choice = input()

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        print("Program terminated.")
        break