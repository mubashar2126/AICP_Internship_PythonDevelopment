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

# Display initial train schedule
def display_schedule(available):
    for i, tickets in enumerate(available):
        print(f"Train {i+1}: {tickets} tickets available")

# Function to set up the screen display for the start of the day
def start_of_day():
    print("Welcome to the Electric Mountain Railway!")
    print("Initial Train Schedule:")
    print("Up Journeys:")
    display_schedule(available_tickets['up'])
    print("\nDown Journeys:")
    display_schedule(available_tickets['down'])

# Testing the start of the day setup
start_of_day()
