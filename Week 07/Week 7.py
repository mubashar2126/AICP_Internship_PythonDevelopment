NUM_CHARITIES = 3
charity_names = []
# Task 1Setting up the donation system
def setup_donation_system():
    global charity_names
    print("Welcome to the Charity Donation System!")


    for i in range(NUM_CHARITIES):
        charity_name = input(f"Enter the name of Charity {i+1}: ")
        charity_names.append(charity_name)


    for i, name in enumerate(charity_names, start=1):
        print(f"{i}. {name}")


    charity_totals = [0] * NUM_CHARITIES

    return charity_totals

# Task 2Recording total each donation
def record_and_total_donation(charity_totals):
    while True:

        charity_choice = int(input("Enter the number of the chosen charity (1, 2, or 3), or -1 to show totals: "))

    #
        if charity_choice == -1:
            show_totals(charity_totals)
            continue


        if 1 <= charity_choice <= NUM_CHARITIES:

            shopping_bill = float(input("Enter the value of the customer's shopping bill: "))


            donation = shopping_bill * 0.01


            charity_totals[charity_choice - 1] += donation


            print(f"Donation of ${donation:.2f} recorded for {charity_names[charity_choice - 1]}.")

        else:
            print("Invalid charity choice. Please enter 1, 2, 3, or -1.")

# Task 3Showing  the totals so far
def show_totals(charity_totals):
    print("\nCharity Totals:")
    sorted_charities = sorted(range(NUM_CHARITIES), key=lambda i: charity_totals[i], reverse=True)

    for i in sorted_charities:
        print(f"{charity_names[i]}: ${charity_totals[i]:.2f}")

    grand_total = sum(charity_totals)
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")


charity_totals = setup_donation_system()
record_and_total_donation(charity_totals)
