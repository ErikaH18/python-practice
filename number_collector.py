"""
Crash-Proof Number Collector program. 
Handle Errors when user enters invalid input, 
prints helpful message, sets that value to 0 as a default
"""
print("Number Collector")
try:
    number1 = int(input("Enter number 1: "))        
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number1 = 0
       
try:
    number2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number2 = 0

try:
   number3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    number3 = 0

# Calculations
numbers_sum = number1 + number2 + number3
average = float(numbers_sum / 3)

# Display calculations with formatted outputs
print(f"Your numbers: {number1}, {number2}, {number3}")
print(f"Sum: {numbers_sum}")
print(f"Average: {average:.2f}")
