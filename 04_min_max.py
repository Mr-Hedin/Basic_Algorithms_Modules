"""
Lesson 4: Finding Minimum and Maximum Values
Learn how to find the smallest and largest numbers in a group.
"""

def find_min(numbers):
    """Find the smallest number in a list."""
    if not numbers:
        return None
    return min(numbers)

def find_max(numbers):
    """Find the largest number in a list."""
    if not numbers:
        return None
    return max(numbers)

def practice_min_max():
    print("Let's practice finding minimum and maximum values.")
    numbers = []
    
    while True:
        try:
            print("\nCurrent numbers:", numbers)
            if numbers:
                print("Smallest number:", find_min(numbers))
                print("Largest number:", find_max(numbers))
            
            number = float(input("\nEnter a number (or 0 to finish): "))
            
            if number == 0:
                break
                
            numbers.append(number)
            
        except ValueError:
            print("Please enter a valid number.")
    
    if numbers:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Smallest number (minimum):", find_min(numbers))
        print("Largest number (maximum):", find_max(numbers))
        if len(numbers) >= 2:
            print("Difference between largest and smallest:", find_max(numbers) - find_min(numbers))

if __name__ == "__main__":
    print("Lesson 4: Finding Minimum and Maximum Values")
    print("The minimum (min) is the smallest number in a group.")
    print("The maximum (max) is the largest number in a group.")
    print("\nExample: In the numbers [5, 2, 8, 1, 9]")
    print("Minimum = 1 (smallest)")
    print("Maximum = 9 (largest)")
    
    while True:
        practice_min_max()
        again = input("\nWould you like to practice finding min/max? (yes/no): ")
        if again.lower() != 'yes':
            break 