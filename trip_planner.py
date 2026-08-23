# Interactive program that collects user data, processes it, and displays meaningful output

# variables with user inputs
destination = input("What is your Destination? ")
distance = float(input("What is the distance in miles? "))
mpg = float(input("What is your car fuel efficiency (MPG)? "))
gas_price = float(input("What is the current price of gas per mile? $"))
nights = int(input("How many nights are you planning to stay in the hotel? "))
hotel_cost = float(input("What is the hotel overage cost per night? "))
food_budget = float(input("What is your daily food budget for this trip? "))

# Calculations 
gallons = distance / mpg
gas_cost = gallons * gas_price
tot_hotel_cost = nights * hotel_cost
food_cost = (nights + 1) * food_budget
estimate_total = gas_cost + tot_hotel_cost + food_cost

# Creating labels for better display
gas_label = f"Gas  ({gallons:.2f} gal @ ${gas_price:.2f}):"
hotel_label = f"Hotel  ({nights} nights @ ${hotel_cost:.2f}):"
food_label = f"Food  ({nights + 1} days @ ${food_budget:.2f}):"

# Display trip summary with formatted outputs
print("=" * 50)
print("Road Trip Budget Planner".center(50))
print("=" * 50)
print(f"{'Destination:':<15} {destination}")
print(f"{'Distance:':<15} {distance:.2f} miles\n")
print("--- Cost Breakdown ---".center(50))
print(f"{gas_label:<35} ${gas_cost:.2f}")
print(f"{hotel_label:<35} ${tot_hotel_cost:.2f}")
print(f"{food_label:<35} ${food_cost:.2f}")
print("-" * 50)
print(f"{'Estimated total:':<35} ${estimate_total:.2f}")


