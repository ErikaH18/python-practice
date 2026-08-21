#Python Practice Exercise 
"""
Python Practice Exercise
Small program that displays Student Information, in which we are practicing python variable naming conventions, formatted string, and string multiplication.

"""

# Variables for student information
first_name = "Erika"
last_name = "Hurtado"
age = 42
city = "Gulf Breeze"
career = "Child Program Assistant Director"
reasonforlearning = "I want to pursue a career in software development."
fun_fact = "I can speak 3 languages, and I have an accent when I speak each one."

# Display the Student Profile

print("*" * 40)
print("Student Profile".center(40))
print("*" * 40)
print(f"{'Name:':<8} {first_name} {last_name}")
print(f"{'Age:':<8} {age}")
print(f"{'City:':<8} {city}")
print(f"Previous Career: {career}")
print(f"\nWhy I'm learning to code:\n {reasonforlearning}")
print("\nFun fact:", fun_fact)
print("*" * 40)