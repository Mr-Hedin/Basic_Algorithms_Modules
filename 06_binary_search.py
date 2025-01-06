"""
Lesson 6: Binary Search
Learn how to find a number in a sorted list by repeatedly dividing the search area in half.
"""

def binary_search(numbers, target):
    """
    Search for a number using binary search.
    Returns the position if found, or -1 if not found.
    """
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        middle = (left + right) // 2
        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

def practice_binary_search():
    # Create a sorted list of numbers
    numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    
    print("We will search through this sorted list:", numbers)
    
    while True:
        try:
            target = int(input("\nEnter a number to search for: "))
            
            # Show the search process
            print("\nSearching through the list...")
            left = 0
            right = len(numbers) - 1
            steps = 0
            
            while left <= right:
                steps += 1
                middle = (left + right) // 2
                print(f"\nStep {steps}:")
                print(f"Checking middle position {middle}: {numbers[middle]}")
                
                if numbers[middle] == target:
                    print(f"Found {target} at position {middle}")
                    break
                elif numbers[middle] < target:
                    print(f"{target} is larger, looking in right half")
                    left = middle + 1
                else:
                    print(f"{target} is smaller, looking in left half")
                    right = middle - 1
            else:
                print(f"\n{target} is not in the list")
                
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        break

if __name__ == "__main__":
    print("Lesson 6: Binary Search")
    print("Binary search finds a number in a sorted list by checking the middle")
    print("and eliminating half of the remaining numbers each time.")
    print("\nExample: To find 23 in [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]")
    print("1. Check middle (16) - 23 is larger, look in right half")
    print("2. Check middle (56) - 23 is smaller, look in left half")
    print("3. Check middle (23) - Found it!")
    
    while True:
        practice_binary_search()
        again = input("\nWould you like to try another search? (yes/no): ")
        if again.lower() != 'yes':
            break 