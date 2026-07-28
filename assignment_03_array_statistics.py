# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================




# Function to calculate the sum
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# Function to calculate the average
def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


# Function to find the maximum value
def find_max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


# Function to find the minimum value
def find_min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


# Main function
def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: Number of values must be greater than 0.")
        return

    numbers = []

    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    print("\nResults:")
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))
    print("Minimum:", find_min(numbers))


# Run the program
main()
