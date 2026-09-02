# Toolkit of reusable functions for common calculations

def calculate_average(numbers):
    """ Takes a list of numbers and returns its average.
    Returns 0 if list is empty."""   
    if not numbers:
        return 0
    average = sum(numbers) / len(numbers)
    return average

def find_max_and_min(numbers):
    """" Takes a list of numbers and returns a tuple (max, min) """
    # If the list is empty, return tuple(None, None)  
    if not numbers:
        return (None, None)
    
    max_number = numbers[0]
    min_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return (max_number, min_number)

def count_occurrences(items, target):
    """" Takes a list and a target value, returns how many times the target appears in the list """
    # don't use .count() 
    target_count = 0
    for item in items:
        if item == target:
            target_count += 1
    return target_count

def is_palindrome(text):
    """" Takes a string , returns True if it reads the same forward and backward (case-insensitive, ignoring spaces)"""
    text = text.lower().replace(" ", "")
    length = len(text)
    
    for index in range(length):
        if text[index] != text[length - (index + 1)]:
            return False
    return True

def create_report(title, scores):
    """" Takes a report title and a list of scores. """
    #uses calculate_average and find_max_and_min internally. Returns a formatted string report (NOT a print - a return).
    average = calculate_average(scores)
    
    max_min_score = find_max_and_min(scores)

    report = f"=== {title} ==="
    
    report += f"\nThe average: {average:.1f}\n"    
    report += f"Max score: {max_min_score[0]}\n"
    report += f"Min score: {max_min_score[1]}\n"

    return report

if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93, 85]
    
    print(f"Average: {calculate_average(test_scores):.1f}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print()
    print(create_report("Class Scores", test_scores))

    # passing a empty list to test the functions
    empty_scores = []
    print(f"Average: {calculate_average(empty_scores):.1f}")
    print(f"Max/Min: {find_max_and_min(empty_scores)}")
    print(f"Count of 85: {count_occurrences(empty_scores, 85)}")
    print(f"'r a c eCAR' palindrome: {is_palindrome('r a c eCAR')}")
    print(f"'HEL l o' palindrome: {is_palindrome('HEL l o')}")
    print(f"'P' palindrome: {is_palindrome('P')}")
    print()
    print(create_report("Empty Report", empty_scores))