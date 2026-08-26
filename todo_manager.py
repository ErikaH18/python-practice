# Interactive to-do-list

# To-do list with 3 task (pre-populated)
todo_list = ["Finish homework", "Call the doctor", "Go to the dentist"]

print("=" * 35)
print("     My To-Do List")
print("=" * 35)

for i in range(len(todo_list)):
    print(f"{i + 1}. {todo_list[i]}")

total_tasks = len(todo_list)

print(f"\nTotal tasks: {total_tasks}")

# Add or remove from list based on choice input
print(f"\nWould you like to Add(1) or Remove(2) a task?")

print(f"1. Add a task")
print(f"2. Remove a task")

try:
    choice = int(input("\nChoice: "))
    if choice == 1:
        new_task = input("Enter new Task: ")
        todo_list.append(new_task)
    elif choice == 2:
        remove_task = int(input("Enter the number of the task to remove: "))
        todo_list.pop(remove_task - 1)
    else:
        # Handle choice outside 1 or 2
         print(f"\n({choice}) is not a valid choice. No changes made")    
# Handle invalid value and out of range index       
except (ValueError, IndexError):
    print("\nInvalid input. No changes made")
    
# Display updated list after changes
print(f"\nUpdated List:")
for i in range(len(todo_list)):
        print(f"{i + 1}. {todo_list[i]}")

total_tasks = len(todo_list)
print(f"\nTotal tasks: {total_tasks}")



