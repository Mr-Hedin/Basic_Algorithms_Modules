"""
Lesson 2: Adding Numbers and Finding Sums
Learn how to add multiple numbers together.
"""


# Basic Algorithm
def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total








# Use our summing algorithm to create a small program
def practice_sums():
    numbers = []
    print("\nCurrent numbers:", numbers)
    if numbers:
        print("Current sum:", calculate_sum(numbers))
    
    number = int(input("\nEnter a number (or 0 to finish): "))

    # if the user enters a 0, exit the while True loop
    if number == 0:
        break
        
    numbers.append(number)
    
    if numbers:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Total sum:", calculate_sum(numbers))
        print("Number of values added:", len(numbers))

while True:
    practice_sums()
