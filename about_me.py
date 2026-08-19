#Python Practice Exercise 
"""
Python Practice Exercise
Small program that displays Student Information, in which we are praticing python variable naming conventions, formatted string, and string multiplication.

"""

# Variables for student information
first_name = "Erika"
last_name = "Hurtado"
age = 42
city = "Gulf Breeze"
career = "Child Program Assistant Director"
goals = "I want to persue a carreer in software development."
fun_fact = "I can speak 3 languages, and I have an accent when I speak each one."

# Display the Student Profile

print("*" * 40)
print("\tStudent Profile")
print("*" * 40)
print(f"Name:\t{first_name} {last_name}")
print("Age:\t", age)
print("City:\t", city)
print("Previous Career:", career)
print("\nWhy I'm learning to code:\n", goals)
print("\nFun fact:", fun_fact)
print("*" * 40)