#Task2 Purchase Tickets
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
# Function to purchase tickets
def purchase_tickets(journey_type, journey_num, num_passengers):
    if available_tickets[journey_type][journey_num] >= num_passengers:
        # Sufficient tickets available
        cost = num_passengers * (UP_COST if journey_type == 'up' else DOWN_COST)

        # Group discount calculation
        free_tickets = num_passengers // 10
        cost -= free_tickets * (UP_COST if journey_type == 'up' else DOWN_COST)

        available_tickets[journey_type][journey_num] -= num_passengers
        money_collected[journey_type][journey_num] += cost

        print(f"Tickets purchased for {num_passengers} passengers for {journey_type} journey {journey_num + 1}.")
        print(f"Total cost: ${cost}")
        print(
            f"Remaining tickets for {journey_type} journey {journey_num + 1}: {available_tickets[journey_type][journey_num]}")
    else:
        print(f"Insufficient tickets available for {journey_type} journey {journey_num + 1}.")


# Testing ticket purchase
purchase_tickets('up', 0, 15)  # Attempting to purchase 15 tickets for the first up journey
