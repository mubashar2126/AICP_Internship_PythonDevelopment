import datetime
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
BOAT_COUNT = 10
boat_data = [{'available': True, 'total_hours': 0, 'return_time': None} for _ in range(BOAT_COUNT)]
def task_1(boat_number, start_time, end_time):
    if not (10 <= start_time <= 17 and 10 <= end_time <= 17):
        print("Error: Boats can only be hired between 10:00 and 17:00.")
        return

    duration = end_time - start_time
    if duration in [0.5, 1, 2, 3, 4, 5]:
        cost = HOURLY_RATE * duration if duration >= 1 else HALF_HOUR_RATE * duration
    else:
        print("Error: Invalid duration. Please enter 0.5, 1, 2, 3, 4, or 5 hours.")
        return
    boat_data[boat_number - 1]['total_hours'] += duration
    boat_data[boat_number - 1]['return_time'] = end_time
    return cost


def task_2(current_time):
    available_boats = [i + 1 for i, data in enumerate(boat_data) if data['available']]

    if not available_boats:
        earliest_return_time = min(boat['return_time'] for boat in boat_data)
        print(f"No boats available. The earliest available time is {earliest_return_time}:00.")
    else:
        print(f"Available boats: {', '.join(map(str, available_boats))}")
def task_3():
    total_money = sum(data['total_hours'] * HOURLY_RATE for data in boat_data)
    total_hours = sum(data['total_hours'] for data in boat_data)
    unused_boats = sum(1 for data in boat_data if data['total_hours'] == 0)
    most_used_boat = max(range(BOAT_COUNT), key=lambda i: boat_data[i]['total_hours'] or 0) + 1

    print(f"\nTotal money taken: ${total_money}")
    print(f"Total hours boats were hired: {total_hours}")
    print(f"Number of boats not used: {unused_boats}")
    print(f"Boat {most_used_boat} was used the most with {boat_data[most_used_boat - 1]['total_hours']} hours.")
def main():
    print("Welcome to Boat Management System!")

    while True:
        print("\nChoose a task:")
        print("1. Calculate money taken for one boat")
        print("2. Find the next boat available")
        print("3. Calculate money taken for all boats at the end of the day")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            boat_number = int(input("Enter boat number (1-10): "))
            start_time = int(input("Enter start time (10-17): "))
            end_time = int(input("Enter end time (10-17): "))

            cost = task_1(boat_number, start_time, end_time)
            if cost is not None:
                print(f"\nBoat {boat_number} hired for {end_time - start_time} hours. Cost: ${cost}")

        elif choice == '2':
            current_time = int(input("\nEnter current time: "))
            task_2(current_time)

        elif choice == '3':
            task_3()

        elif choice == '4':
            print("Exiting Boat Management System. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
