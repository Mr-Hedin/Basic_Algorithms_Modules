"""
Lesson 5: Linear Search
Learn how to find an item in a list by checking each item one by one.
"""

def linear_search(items, target):
    """
    Search for an item in a list one by one.
    Returns the position (index) if found, or -1 if not found.
    """
    for index in range(len(items)):
        if items[index] == target:
            return index
    return -1

def practice_linear_search():
    # Simple list of numbers to search through
    numbers = [17, 3, 75, 42, 8, 21, 56, 93]
    
    print("We will search through this list:", numbers)
    
    while True:
        try:
            target = int(input("\nEnter a number to search for: "))
            
            # Show the search process
            print("\nSearching through the list...")
            for i, num in enumerate(numbers):
                print(f"Checking position {i}: {num}")
                if num == target:
                    print(f"Found {target} at position {i}")
                    break
                print("Not found, continuing search...")
            else:
                print(f"{target} is not in the list")
                
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        break

if __name__ == "__main__":
    print("Lesson 5: Linear Search")
    print("Linear search finds an item by checking each element one at a time.")
    print("It works on any list, even if it's not in order.")
    print("\nExample: To find 42 in [17, 3, 75, 42, 8]")
    print("1. Check 17 - not found")
    print("2. Check 3  - not found")
    print("3. Check 75 - not found")
    print("4. Check 42 - found!")
    
    while True:
        practice_linear_search()
        again = input("\nWould you like to try another search? (yes/no): ")
        if again.lower() != 'yes':
            break 