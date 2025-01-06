"""
Lesson 2: Adding Numbers and Finding Sums
Learn how to add multiple numbers together.
"""

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def practice_sums():
    print("Let's practice adding numbers together.")
    numbers = []
    
    while True:
        try:
            print("\nCurrent numbers:", numbers)
            if numbers:
                print("Current sum:", calculate_sum(numbers))
            
            number = int(input("\nEnter a number (or 0 to finish): "))
            
            if number == 0:
                break
                
            numbers.append(number)
            
        except ValueError:
            print("Please enter a valid whole number.")
    
    if numbers:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Total sum:", calculate_sum(numbers))
        print("Number of values added:", len(numbers))

if __name__ == "__main__":
    print("Lesson 2: Adding Numbers")
    print("Adding numbers helps us find the total of multiple values.")
    print("Example: 5 + 3 + 2 = 10")
    print("Example: 10 + 20 + 30 = 60")
    
    while True:
        practice_sums()
        again = input("\nWould you like to practice more sums? (yes/no): ")
        if again.lower() != 'yes':
            break 