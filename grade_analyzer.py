# Grade Analyzer program that uses conditionals and loops to process student data

# Pre_loaded student scores
scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
# Define dictionary of grades and variables for counts
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
passing = 0
failing = 0

# Categorize each score and tally passing/failing
for score in scores:
    if score >= 90:
        grade_counts["A"] += 1
        passing += 1
    elif score >= 80:
        grade_counts["B"] += 1
        passing += 1
    elif score >= 70:
        grade_counts["C"] += 1
        passing += 1
    elif score >= 60:
        grade_counts["D"] += 1
        passing += 1
    else:
        grade_counts["F"] += 1
        failing += 1

# Calculations
tot_scores = len(scores)
score_sum = sum(scores)
average = score_sum / tot_scores
highest = max(scores)
lowest = min(scores)
passing_percentage = (passing / tot_scores) * 100
failing_percentage = (failing / tot_scores) * 100

# Display summary of calculations
print("=== Grade Analyzer ===")
print(f"Total scores: {tot_scores}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")
print(f"Passing: {passing} ({passing_percentage:.1f}%)")
print(f"Failing: {failing} ({failing_percentage:.1f}%)")

# Display grade distribution
print("\nGrade Distribution:")
for grade, count in grade_counts.items():
    print(f"{grade}: {count} students")

# Let user add new scores until 'done' is typed 
print(f"\n=== Add More Scores ===")
while True:
    add_scores = input("Enter a score (or 'done' to finish): ")
    try:
        if add_scores.lower() == "done":
            # Exit loop and show final average
            updated_average = sum(scores) / len(scores)
            print(f"\nFinal Average: {updated_average:.1f}")
            break
        else:
            # Add valid score and recalculate average
            new_score = int(add_scores)
            scores.append(new_score)
            updated_average = sum(scores) / len(scores)
            print(f"Updated Average: {updated_average:.1f}")
            
    except ValueError:
        print(f"Invalid score number")
       
