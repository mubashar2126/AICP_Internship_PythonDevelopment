#Task 3
# Constants
NUM_JOURNEYS = 4
SEATS_PER_COACH = 80
COACHES_PER_TRAIN = 6
UP_COST = 25
DOWN_COST = 25

# Data Structures
available_tickets = {
    'up': [SEATS_PER_COACH * COACHES_PER_TRAIN] * NUM_JOURNEYS,
    'down': [SEATS_PER_COACH * COACHES_PER_TRAIN] * NUM_JOURNEYS
}

money_collected = {
    'up': [0] * NUM_JOURNEYS,
    'down': [0] * NUM_JOURNEYS
}
# Function to display end-of-day summary
def end_of_day_summary():
    total_passengers = sum(sum(ticket) for ticket in available_tickets.values())
    total_money = sum(sum(money) for money in money_collected.values())

    print("\nEnd of Day Summary:")
    print("Total Passengers Traveled:")
    for journey_type in available_tickets:
        for i, tickets in enumerate(available_tickets[journey_type]):
            passengers = SEATS_PER_COACH * COACHES_PER_TRAIN - tickets
            print(f"{journey_type.capitalize()} Journey {i + 1}: {passengers} passengers")

    print("\nTotal Money Collected for Each Journey:")
    for journey_type in money_collected:
        for i, money in enumerate(money_collected[journey_type]):
            print(f"{journey_type.capitalize()} Journey {i + 1}: ${money}")

    print("\nTotal Passengers for the Day:", total_passengers)
    print("Total Money Collected for the Day: $", total_money)


# Testing end-of-day summary
end_of_day_summary()
