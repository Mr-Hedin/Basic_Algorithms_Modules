"""
Lesson 3: Calculating Averages
Learn how to find the average (mean) of a group of numbers.
"""

def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def practice_averages():
    print("Let's practice calculating averages.")
    numbers = []
    
    while True:
        try:
            print("\nCurrent numbers:", numbers)
            if numbers:
                print("Current average:", calculate_average(numbers))
            
            number = float(input("\nEnter a number (or 0 to finish): "))
            
            if number == 0:
                break
                
            numbers.append(number)
            
        except ValueError:
            print("Please enter a valid number.")
    
    if numbers:
        print("\nFinal Results:")
        print("Numbers entered:", numbers)
        print("Average:", calculate_average(numbers))
        print("Number of values:", len(numbers))
        print("Sum of values:", sum(numbers))

if __name__ == "__main__":
    print("Lesson 3: Calculating Averages")
    print("An average tells us the typical value in a group of numbers.")
    print("To calculate an average:")
    print("1. Add all the numbers together")
    print("2. Divide by how many numbers there are")
    print("\nExample: For numbers [10, 20, 30]")
    print("1. Sum = 10 + 20 + 30 = 60")
    print("2. Count = 3 numbers")
    print("3. Average = 60 ÷ 3 = 20")
    
    while True:
        practice_averages()
        again = input("\nWould you like to practice more averages? (yes/no): ")
        if again.lower() != 'yes':
            break 