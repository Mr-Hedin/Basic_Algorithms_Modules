"""
Welcome to the Great Algorithm Race! 🏎️
Let's see which search algorithm is faster!
"""

import time
import random

def linear_search(numbers, target):
    """Linear search implementation."""
    steps = 0
    for i in range(len(numbers)):
        steps += 1
        if numbers[i] == target:
            return True, steps
    return False, steps

def binary_search(numbers, target):
    """Binary search implementation."""
    steps = 0
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if numbers[mid] == target:
            return True, steps
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, steps

def race_preparation():
    """Prepare the race track (data) for our algorithms."""
    print("🏁 Welcome to the Great Algorithm Race! 🏁")
    print("We'll race Linear Search vs Binary Search!")
    
    # Let the user choose the track size (list size)
    while True:
        try:
            size = int(input("\nHow many numbers should we race with? (10-1000): "))
            if 10 <= size <= 1000:
                break
            print("Please choose a number between 10 and 1000!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Create our sorted racetrack (list of numbers)
    numbers = list(range(1, size + 1))
    return numbers

def display_race_results(linear_time, linear_steps, binary_time, binary_steps, found):
    """Display the race results in a fun way."""
    print("\n🏆 Race Results 🏆")
    print("=" * 40)
    
    # Convert times to milliseconds for easier reading
    linear_ms = linear_time * 1000
    binary_ms = binary_time * 1000
    
    print(f"Linear Search:")
    print(f"⏱️  Time: {linear_ms:.2f} milliseconds")
    print(f"👣 Steps: {linear_steps}")
    
    print(f"\nBinary Search:")
    print(f"⏱️  Time: {binary_ms:.2f} milliseconds")
    print(f"👣 Steps: {binary_steps}")
    
    # Determine the winner
    print("\n🎯 And the winner is...")
    if binary_time < linear_time:
        print("🥇 BINARY SEARCH! 🥇")
        print(f"Binary Search was {(linear_time/binary_time):.1f}x faster!")
    elif linear_time < binary_time:
        print("🥇 LINEAR SEARCH! 🥇")
        print(f"Linear Search was {(binary_time/linear_time):.1f}x faster!")
    else:
        print("🤝 It's a tie!")
    
    # Show if the number was found
    if found:
        print("\n✨ The number was successfully found by both algorithms!")
    else:
        print("\n😅 The number wasn't in the list, but both algorithms figured that out!")

def run_race():
    """Run the algorithm race."""
    numbers = race_preparation()
    
    # Let's make it interesting by sometimes searching for a number that doesn't exist
    if random.random() < 0.2:  # 20% chance of searching for a missing number
        target = len(numbers) + 1
        print(f"\nWe'll search for {target} (Spoiler: It's not in the list! 😉)")
    else:
        target = random.choice(numbers)
        print(f"\nWe'll search for {target}")
    
    input("\nPress Enter to start the race! 🏁")
    
    # Race the algorithms!
    print("\n🏃 Linear Search is running...")
    linear_start = time.time()
    linear_found, linear_steps = linear_search(numbers, target)
    linear_time = time.time() - linear_start
    
    print("🏃 Binary Search is running...")
    binary_start = time.time()
    binary_found, binary_steps = binary_search(numbers, target)
    binary_time = time.time() - binary_start
    
    # Show the results
    display_race_results(linear_time, linear_steps, binary_time, binary_steps, linear_found)
    
    # Educational insights
    print("\n📚 What did we learn?")
    print("- Binary Search is usually faster for large lists")
    print("- Linear Search checks every number one by one")
    print("- Binary Search cuts the search area in half each time")
    print(f"- With {len(numbers)} numbers:")
    print(f"  * Linear Search might need up to {len(numbers)} steps")
    print(f"  * Binary Search never needs more than {int(len(numbers).bit_length())} steps!")

if __name__ == "__main__":
    print("Welcome to the Algorithm Racing Championship!")
    print("We'll race different search algorithms to see which is faster.")
    
    while True:
        run_race()
        
        play_again = input("\nWant to race again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for racing with algorithms! Keep exploring! 🏎️")
            break 