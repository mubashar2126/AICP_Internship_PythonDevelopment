
COST_CEMENT = 3
COST_GRAVEL = 2
COST_SAND = 2
DISCOUNT_PACK_CEMENT = 1
DISCOUNT_PACK_SAND = 2
DISCOUNT_PACK_GRAVEL = 2
DISCOUNT_PACK_PRICE = 10
# Task 1
def check_single_sack():
    content = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
    weight = float(input("Enter the weight of the sack in kilograms: "))

    if content not in ['C', 'G', 'S']:
        print("Error: Invalid content. Please enter C, G, or S.")
        return False

    if (content == 'C' and (weight < 24.9 or weight > 25.1)) or \
            ((content == 'G' or content == 'S') and (weight < 49.9 or weight > 50.1)):
        print("Error: Invalid weight for the sack. for cement enter weight 24.9-25.1 for gravel,sand enter between 49.9--50.1  ")
        return False

    print(f"Sack accepted - Contents: {content}, Weight: {weight} kg")
    return True

# Task 2
def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Welcome to the store! how may I help you?.Select your order .Enter the number of sacks of cement: "))
    num_gravel = int(input("Enter the number of sacks of gravel: "))
    num_sand = int(input("Enter the number of sacks of sand: "))

    for _ in range(num_cement):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 25

    for _ in range(num_gravel):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 50

    for _ in range(num_sand):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 50

    print(f"Total weight of the order: {total_weight} kg")
    print(f"Number of sacks rejected from the order: {sacks_rejected}")

    return num_cement, num_gravel, num_sand, total_weight

# Task 3
def calculate_order_price(num_cement, num_gravel, num_sand, total_weight):
    regular_price = (COST_CEMENT * 25) + (COST_GRAVEL * 50) + (COST_SAND * 50)

    num_discount_packs = min(
        total_weight // (25 + (2 * 2 * 50)),
        min(num_cement, num_gravel // 2, num_sand // 2)
    )

    discount_price = num_discount_packs * DISCOUNT_PACK_PRICE
    total_price = regular_price - discount_price

    print(f"Regular price for the order: ${regular_price}")
    print(f"Number of discount packs applied: {num_discount_packs}")
    print(f"New price for the order: ${total_price}")
    print(f"Amount saved with discount: ${discount_price}")

num_cement, num_gravel, num_sand, total_weight = check_customer_order()
calculate_order_price(num_cement, num_gravel, num_sand, total_weight)
